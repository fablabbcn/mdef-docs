from jinja2 import Environment, FileSystemLoader
import re
import os
import yaml

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
        result = template.render(vbls)

        return result

    def get_frontmatter(content):
        if '---\n' not in content:
            print ('No frontmatter in content')
            return None

        if '---\n' in content[1:]:
            frontmatter = yaml.load('\n'.join(content[1:content[1:].index('---\n')+1]), Loader=yaml.SafeLoader)
        else:
            frontmatter = None

        return frontmatter

    def create_faculty(faculty):
        environment = Environment(loader=FileSystemLoader("custom_theme/templates/"))
        template = environment.get_template("faculty.html")

        faculty_path = 'docs/faculty'

        if os.path.exists(f"docs/faculty/{faculty}.md"):
            with open(os.path.join(faculty_path, f'{faculty}.md')) as _file:
                content = _file.readlines()

            frontmatter = get_frontmatter(content)
            if frontmatter is not None:
                vbls = frontmatter
                vbls['body'] = '\n'.join(content[content[1:].index('---\n')+2:])
                result = template.render(vbls)
                # TODO add custom_theme as environment variable
                with open(os.path.join("custom_theme/includes", f'{faculty}.html'), 'w') as _file:
                    _file.write(result)
        else:
            print (f"{faculty}.md not found")

    @env.macro
    def insert_faculty():

        if 'faculty' in env.page.meta:
            print ('--------')
            print (env.page.meta['faculty'])
            print ('--------')
            result = ''

            for faculty in env.page.meta['faculty']:
                create_faculty(faculty)
                # TODO add custom_theme as environment variable
                if os.path.exists(f"custom_theme/includes/{faculty}.html"):
                    with open(f"custom_theme/includes/{faculty}.html") as file:
                        result += file.read()
                else:
                    print (f"{faculty}.html not found")

        return result

# def on_pre_page_macros(env):
#     if 'page_type' in env.page.meta:
#         if env.page.meta['page_type'] == 'course':
#             md = env.markdown
#             print (md)

            # p = re.compile("^(#{1,6}\s*[\S]+)")
            # p = re.compile("/(?:^|\n)##\s[^\n]*\n(.*?)(?=\n##?\s|$)/gs")
            # p = re.compile("^" + 'Schedule' + "$", re.MULTILINE)
            # start = p.search(md)
            # print (start)

            # if start is not None:
            #     print (start)

            # env.markdown = '{{ insert_banner() }}\n' + env.markdown