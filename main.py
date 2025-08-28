from jinja2 import Environment, FileSystemLoader
from mistune import html
import re
import os
import yaml
from pathlib import Path

def define_env(env):

    @env.macro
    def insert_banner():

        environment = Environment(loader=FileSystemLoader("custom_theme/templates/"))
        template = environment.get_template("banner.html")

        vbls = env.page.meta.copy()
        if 'page_type' in env.page.meta:
            if env.page.meta['page_type'] == 'course':
                try:
                    with open(f"custom_theme/templates/{env.page.meta['track'].lower()}_icon.html") as file:
                        icon = file.read()
                    vbls['banner_icon'] = icon
                except:
                    pass
        vbls['fallback_img'] = '/assets/images/grid.jpg'
        result = template.render(vbls)

        return result

    def recurse_dict(d):
        val = []

        for v in d.values():
            if isinstance(v, dict):
                val.extend(recurse_dict(v))

            elif isinstance(v, list):
                for i in v:
                    if isinstance(i, dict):
                        val.extend(recurse_dict(i))
                    else:
                        val.append(i)
            else:
                val.append(v)
        return val

    def get_frontmatter(content):
        if '---\n' not in content:
            print ('No frontmatter in content')
            return None

        if '---\n' in content[1:]:
            frontmatter = yaml.load('\n'.join(content[1:content[1:].index('---\n')+1]), Loader=yaml.SafeLoader)
        else:
            frontmatter = None

        return frontmatter

    def render_markdown(markdown):
        return html(markdown)

    def create_faculty(faculty, custom_dir, fallback_img):
        environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)
        template = environment.get_template("faculty_item.html")

        faculty_path = 'docs/faculty'

        if os.path.exists(f"docs/faculty/{faculty}.md"):
            with open(os.path.join(faculty_path, f'{faculty}.md')) as _file:
                content = _file.readlines()

            frontmatter = get_frontmatter(content)
            if frontmatter is not None:
                vbls = frontmatter
                vbls['body'] = render_markdown(''.join(content[content[1:].index('---\n')+2:]))
                vbls['fallback_img'] = fallback_img

                if vbls['feature_img'] is not None:
                    if not os.path.exists('docs' + vbls['feature_img']):
                        print (f'MACROS WARNING: Feature image for: {faculty} not found')
                        vbls['feature_img'] = None

                result = template.render(vbls)
                # TODO add custom_theme as environment variable
                with open(os.path.join(f"{custom_dir}/includes", f'{faculty}.html'), 'w') as _file:
                    _file.write(result)
        else:
            print (f"MACROS WARNING - {faculty}.md not found")

    @env.macro
    def insert_faculty():
        custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))
        fallback_img = '/assets/images/fall-back.jpg'

        if 'faculty' in env.page.meta:
            result = ''

            for faculty in env.page.meta['faculty']:
                create_faculty(faculty, custom_dir, fallback_img)

                if os.path.exists(f"{custom_dir}/includes/{faculty}.html"):
                    with open(f"{custom_dir}/includes/{faculty}.html") as file:
                        result += file.read()
                else:
                    print (f"{faculty}.html not found")

        return result

    @env.macro
    def insert_students(year=1):
        custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))

        environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)
        template = environment.get_template("students.html")

        if 'students' in env.page.meta:
            students = []
            for item in env.page.meta['students'].keys():
                # Default to year 1 if not there
                if 'year' in env.page.meta['students'][item]:
                    student_year = env.page.meta['students'][item]['year']
                else:
                    student_year = 1
                if student_year == year:
                    students.append({'name': item,
                                    'photo': env.page.meta['students'][item]['photo'],
                                    'website': env.page.meta['students'][item]['website']
                                    })

            result = template.render(students=students)
            return result
        else:
            print ('Incorrectly configured')
            return None

    @env.macro
    def insert_tracks():
        custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))

        environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)
        template = environment.get_template("track_cards.html")

        src_uri = env.page.file.src_uri
        parents = Path(src_uri).parents
        folder = str(parents[0])
        depth = len(parents)

        if depth == 3:
            uri_term = 'all'
            uri_year = os.path.split(parents[0])[1]
        if depth == 4:
            uri_term = os.path.split(parents[0])[1]
            uri_year = os.path.split(parents[1])[1]

        tracks = {}

        # get all paths in nav
        nav_paths = []
        for item in env.conf.nav:
            nav_paths += recurse_dict(item)

        for (root,dirs,files) in os.walk(os.path.join('docs',folder)):
            droot = len(Path(root).parents)
            if droot == 5:
                module = os.path.split(Path(root))[1]
                term = os.path.split(Path(root).parents[0])[1]
                year = os.path.split(Path(root).parents[1])[1]

                if os.path.join(root, 'index.md').replace('docs/', '') not in nav_paths:
                    print (root)
                    print ('Ignoring as its not in nav yet')
                    continue

                with open(os.path.join(root, 'index.md')) as _file:
                    content = _file.readlines()

                frontmatter = get_frontmatter(content)
                href = None

                if frontmatter is not None:
                    href = os.path.join(root).replace('docs', '')
                    track = frontmatter['track']

                    if track not in tracks:
                        tracks[track] = {}

                    tracks[track][module] = {
                        'title': frontmatter['title'],
                        'course_type': frontmatter['course_type'],
                        'year': year,
                        'term': term,
                        'term-expanded': f'Term {term[-1]}',
                        'href': href
                    }

        result = template.render(tracks=tracks, uri_year = uri_year, uri_term = uri_term)
        return result

    @env.macro
    def insert_projects():
        custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))

        environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)
        template = environment.get_template("highlighted-projects.html")

        src_uri = env.page.file.src_uri
        parents = Path(src_uri).parents
        folder = str(parents[0])
        depth = len(parents)

        if depth == 3:
            uri_term = 'all'
            uri_year = os.path.split(parents[0])[1]
        if depth == 4:
            uri_term = os.path.split(parents[0])[1]
            uri_year = os.path.split(parents[1])[1]

        tracks = {}

        # get all paths in nav
        nav_paths = []
        for item in env.conf.nav:
            nav_paths += recurse_dict(item)

        for (root,dirs,files) in os.walk(os.path.join('docs',folder)):
            droot = len(Path(root).parents)
            if droot == 5:
                module = os.path.split(Path(root))[1]
                term = os.path.split(Path(root).parents[0])[1]
                year = os.path.split(Path(root).parents[1])[1]

                if os.path.join(root, 'index.md').replace('docs/', '') not in nav_paths:
                    print (root)
                    print ('Ignoring as its not in nav yet')
                    continue

                with open(os.path.join(root, 'index.md')) as _file:
                    content = _file.readlines()

                frontmatter = get_frontmatter(content)
                href = None

                if frontmatter is not None:
                    href = os.path.join(root).replace('docs', '')
                    track = frontmatter['track']

                    if track not in tracks:
                        tracks[track] = {}

                    tracks[track][module] = {
                        'title': frontmatter['title'],
                        'course_type': frontmatter['course_type'],
                        'year': year,
                        'term': term,
                        'term-expanded': f'Term {term[-1]}',
                        'href': href
                    }

        result = template.render(tracks=tracks, uri_year = uri_year, uri_term = uri_term)
        return result
