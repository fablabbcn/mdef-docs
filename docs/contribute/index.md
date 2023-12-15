---
title: Contribute
hide:
    - navigation
---

## Overview

Welcome! This is a general guide for contributing to this website.

This website is created using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) which is an open source static site generator particularly useful for documentation. **Content in MkDocs Material is written in Markdown**, a markup language which is easier to understand and edit than HTML, making content formatting more accessible.

!!! note "MkDocs Material References"
    
    [Mkdocs Material](https://squidfunk.github.io/mkdocs-material/reference) has extensive documentation, so if you get stuck, it is a good idea to check there to see if the issue you are dealing with is explained in their documentation.

**It is okay for contributors to make small changes to the MDEF website via GitHub using a [`pull request`](#branches-and-pull-requests) without testing locally.** Some small changes might include updating a faculty bio, changing a photo, or fixing a detail on a module page. **However, larger changes are a bit more complex and should be done in a more systematic way**, which will be [covered in detail below](#testing-locally).

This document will first look at some basics (Markdown guidelines, `git` development workflows, and local development). This foundational knowledge will allow us to move onto the specifics of major changes to this website.

After laying the groundwork, the bulk of this guide will consider three major changes that might need to be made to the MDEF website and specific guidelines on how to make these changes:

1. [Adding new module pages](#adding-new-module-pages)
2. [Adding a new faculty profile](#adding-new-faculty)
3. [Updating the menu to reflect these changes](#updating-adding-to-the-menu)

**First though, we need to start with the basics before we can start editing. Let's get started!**

## Markdown

Since the content of Mkdocs Materials websites is written using Markdown files, **it is important that you are familiar with some Markdown basics.** If you already know Markdown, you can skip to to the [next section](#branches-and-pull-requests).

Using Markdown to format documents is simple, and using Markdown within MkDocs Material allows you to add all the elements that are used on this website (including more complex formatting like [content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/) which we use to show schedules).

The following sub-sections will cover the Markdown basics most frequently used on this website. However, we've included some [additional resources](#additional-resources-for-markdown) as well which offer more detailed explanations and might help with troubleshooting if you can't find an answer in this document. The [tutorial](https://www.markdowntutorial.com/) suggested in the additional resources section does not take very long to complete, and it is **highly recommended** if you are new to Markdown.

### Headings

Headings on websites create a heirarchy, both for human readers as well as robot readers (like web crawlers, bots that systematically index the internet for search engines).

Headings are created using the number sign (#) with the corresponding amount of symbols equating to the heading number it will create:

| Heading     | Markdown                       |
| ----------- | -------------------------------|
| H1          | `# Your H1 Title`              |
| H2          | `## Your H2 Title`             |
| H3          | `### Your H3 Title`            |
| H4          | `#### Your H4 Title`           |
| H5          | `##### Your H5 Title`          |
| H6          | `###### Your H6 Title`         |

!!! important "Important notes"

    1. Note that above **there is always a space after the number signs**, if you don't include this space before the header title, your text **will not** appear as a header.
    2. There should only be one H1 on each page, this is considered a best practice and it is also logical for human readers. Importantly, using only one H1 also helps web crawlers to understand the structure of website content and can affect SEO ranking (negatively if more than one H1 is used on a page).
    3. H1 titles of most pages on this website are included in the Front Matter of the Markdown files ([see below](#front-matter-for-module-pages)).

### Paragraphs

Paragraphs should be separated by a blank line. If you do not include this blank line, the content will run together. Also, there should not be tabs or spaces at the beginning of a paragraph.

### Bold and italics

Add emphasis with bold or italics using asterisks or underscores before and after the text to be emphasized (one for _italics_, two for **bold**, and three for **_bold and italics_**).

| Example               | Markdown                                     |
| --------------------- | ---------------------------------------------|
| **A bold text**       | `**A bold text**`                            |
| __A bold text__       | `__A bold text__`                            |
| *An italicized text*  | `*An italicized text*`                       |
| _An italicized text_  | `_An italicized text_`                       |
| ***An italicized bold text***  | `***An italicized bold text***`     |
| ___An italicized bold text___  | `___An italicized bold text___`     |

!!! note "Keep it consistent"

    **Consistency in your formatting is important.** This website has been built largely using two asterisks for bold and one underscore for italics. Choose your preference, but be consistent. It makes reading your Markdown documents easier for others.

### Lists

#### Unordered lists

**Unordered lists** (with bullet points) can be created with a number of symbols. The typical symbol is a dash (-), though other symbols like asterisks (\*) or plus signs (+) can be used. You should follow the symbol by a space and then the content.

!!! note "Keep it consistent"
    
    It is best to be consistent with which symbols you use, both in individual lists as well as between documents.

#### Ordered lists

**Ordered lists** (with numbers) are created with numbers followed by periods, a space, and then your content.

#### More complex lists

You can create nested lists within both types of lists using a new line followed by a tab, and then whichever structure you desire for the nested list.

``` text title="List examples in Markdown"

**Examples of lists**

_Unordered list with nested unordered list_

- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item

_Ordered list with nested ordered list_

1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item

_Ordered list with nested unordered list_

1. First item
2. Second item
3. Third item
    - Indented item
    - Indented item
4. Fourth item
```

!!! note ""

    **Examples of lists**

    _Unordered list with nested unordered list_

    - First item
    - Second item
    - Third item
        - Indented item
        - Indented item
    - Fourth item

    _Ordered list with nested ordered list_

    1. First item
    2. Second item
    3. Third item
        1. Indented item
        2. Indented item
    4. Fourth item

    _Ordered list with nested unordered list_

    1. First item
    2. Second item
    3. Third item
        - Indented item
        - Indented item
    4. Fourth item

!!! warning "Don't break the list"

    **Lists can be broken if the formatting is not done correctly.** It is possible to add images, admonitions, and block quotes within lists, but all of these must be indented within the list so that the heirarchy is not broken (which would reset numbering in the case of ordered lists.)

    _Ordered list with admonitions_

    1. First item

        !!! note ""
            Admonition that doesn't breaks the list
    2. Second item
    3. Third item
    !!! note ""
        Admonition that breaks the list
    4. Fourth item

### Links

Adding links is as simple as including the text you want to appear as a link within square brackets like `[this]` followed by the URL within parenthesis like `(this)`.

**A complete example of a link would be:**

> `[A simple link](https://fablabbcn.org/)`

**The result would look like this:**

> [A simple link](https://fablabbcn.org/)

!!! bug "Troubleshooting"

    Notice that there is no space between the square brackets and the parentesis.
    
    **This is important, if there is a space your link will not work!**

Relative links are also possible, and should be formatted with an absolute path. An example of this would be the following:

> `[A link to the faculty page](/faculty)`

> [A link to the faculty page](/faculty)

### Images

Images are added starting with an exclamation point (!), followed by square brackets [] with an `alt text`. Then a set of parentheses with the path to the image, either with a URL or a relative link (we keep our images in the `/assets` folder). 

!!! info "What is an `alt text` and why should I include one?"

    The `alt text` is not mandatory, and the square brackets can be left blank. However, including an `alt text` is a best pratice for a number of reasons. 
    
    1. The `alt text` functions as a description in case something goes wrong with loading the image.
    2. It is indexed by search engine bots to better understand image and page content.
    3. The `alt text` can be read aloud by programs called screen readers which are used by people with visual impairments and low vision. 

    **Takeaway: Including an `alt text` is important for accessiblity and general best practices.**

**Here is an example followed by the expected output:**

```
![Banner image for Agriculture Zero module](/assets/images/2023-24/year-1/t-1/agriculture-zero.jpg)
```

![Banner image for Agriculture Zero module](/assets/images/2023-24/year-1/t-1/agriculture-zero.jpg)

**Images can also be links!** All you have to do to make an image a link to include the entire line within a set of square brackets followed by the URL within parenthesis, just like we saw within the link examples above.

```
[![Banner image for Agriculture Zero module](/assets/images/2023-24/year-1/t-1/agriculture-zero.jpg)](/2023-24/year-1/t1/agriculture-zero/)
```

[![Banner image for Agriculture Zero module](/assets/images/2023-24/year-1/t-1/agriculture-zero.jpg)](/2023-24/year-1/t1/agriculture-zero/)

### Additional resources for markdown

- [Markdown tutorial](https://www.markdowntutorial.com/)
- [Basic syntax markdown guide](https://www.markdownguide.org/basic-syntax/)

### Additional formatting with MkDocs Material

Other MkDocs specific formatting options that are used throughout this website include:

- [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
- [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/)
- [Data tables](https://squidfunk.github.io/mkdocs-material/reference/data-tables/)

Each of these three formatting options has a specific use case on the MDEF website. All three are described in detail [below](#mdef-website-specifics).

[MkDocs Material](https://squidfunk.github.io/mkdocs-material/reference/) has an overall reference page which provides very thorough documentation to help users format their documents easily. On the MDEF website, some of the visual elements have been edited for stylistic reasons, but their functionality should not change.

## Branches and pull requests

All contributions should be made with a `pull request` which requires the creation of a new `branch`.

!!! info "What is a `branch`?"

    git-scm explains a `branch` like this:

    > Branching means you diverge from the main line of development and continue to do work without messing with that main line.

    > [Read more on about `branches` on git-scm book](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

!!! info "What is a `pull request`?"

    GitHub explains a `pull request` like this:

    > A pull request is a proposal to merge a set of changes from one branch into another. In a pull request, collaborators can review and discuss the proposed set of changes before they integrate the changes into the main codebase. Pull requests display the differences, or diffs, between the content in the source branch and the content in the target branch.

    > [Read more on about `pull requests` on GitHub.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

By using `pull requests`, we can assure that the live version of the website does not crash, have broken links, or material that is not ready to be published. Large changes can be grouped together and changed can be lauched at the same time, for example, releasing the module pages for a new term.

### Contribution requirements

In general, only maintainers and admins have the permission to make direct changes to the `main` branch. The general process is to open a `pull request` on the git repository. If you are not part of the repository, you can always create a fork and do the `pull request` from there.

!!! danger "Big changes can create big problems"

    For small changes, it is fine to edit on the GitHub interface. However, we do not recommend this for bigger changes as **they could break the site**.

If you are editing on the GitHub interface, anyone can contribute to files through a `pull request`, either as a `fork` or on the repository itself. When you edit an existing file and commit changes, you will be prompted to create a `branch` for your changes, and you will be redirected to an open `pull request` page. You can do as many commits as you want on this `branch` and they will be automatically added to your `pull request`. If you are still making changes, you can convert your `pull request` to a draft and then mark it as "ready for review" when you are ready.

!!! warning "Keep it simple"

    You don't need to create a new `branch` for each change. Once you create the `branch` and have the related `pull request`, make sure that additional **related** changes are done within the same `branch`. As mentioned above, additional commits on the same branch will be added to your pull request.

## Testing locally

Testing locally is recommended for big changes, for example, adding new features, or large amounts of new material. This will require some basic knowledge of command line, python, and git.

### Setting up your work environment

1. Clone the repository:
    ```
    git clone git@github.com:fablabbcn/mdef-docs.git
    ```
2. Install Python 3:

    Python newies! Read the following [guide](https://realpython.com/installing-python/).

3. Install requirements:
    ```
    pip install -r requirements.txt
    ```
    _In Windows if it fails use `pip install -r requirements.txt --user` instead._

4. Serve the mkdocs site and make your edits:
    ```
    mkdocs serve
    ```

    When mkdocs is serving, a line with the local host address will appear in the commandline. Typically, `http://127.0.0.1:8000`

!!! info "Contribute to the main repository"

    Once you are doing making your changes, you can push to a `branch`:

    ```
    git checkout -b <Your branch name>
    ```
    This will create a new branch where you can add, commit, and then push your changes to be reviewed.


## MDEF website specifics

### Adding new module pages

For new module pages, you will need to create a new Markdown file. This file should be named `index.md` and it will be saved within a folder named to reflect the module, for instance `design-studio-01` and `design-with-others` are both folders with a single markdown file both named `index.md`. This structure allows the pages to be loaded without a `.md` extension in the browser window.

!!! warning "Folder structures and changes"
    The structure of these folders is important to maintain.  If folders or files are moved, their corresponding locations have to be correctly updated in the `mkdocs.yml` file to ensure that there are not broken links in the menu.

**Pages for MDEF modules follow a specific structure.** The headings should be used consistently since all **H2 headers appear in the “Table of contents”** or secondary menu (in the lower right corner of the screen).

Likewise, the **Front Matter** of these pages provides the structure that creates the banners with course details. First, we will look at the Front Matter, as it is always at the top of a new Markdown file. Then we will look at the content and what it includes.

#### Front Matter for module pages

Front Matter is a list of _keys_ or fields at the top of a document that don't necessarily show up automatically on the page. Some are native to MkDocs and others have been created based on the needs of the MDEF website. The Front Matter of the page goes at the very top of a Markdown document. Here are the keys used in MDEF module pages followed by a description of each of them and then an example filled out correctly.

``` text linenums="1" title="Front Matter for module pages"
---
title:
page_type:
track:
course_type:
feature_img:
img_caption:
faculty:
    - 
ects:
---
```

!!! info "Understanding the Front Matter keys used on module pages"

    _**Keys in Front Matter are the different fields** that need to be filled in, for example: `title:`, `page_type:` or `faculty:`_

    **title:** This is your **H1, the title of the course** in the case of the MDEF modules. This title will appear on top of your banner image. _It should not be excessively long._

    **page_type:** For MDEF modules this will always be `course`, written in lowercase.

    **track:** Track types include: **`Application`, `Reflection`, `Exploration`, and `Instrumentation`**. When written in the Front Matter, make sure the track names are written correctly and with the first letter capitalized. If this is not done correctly, the corresponding icon will not appear properly in your intro banner and the course will not be included in module lists, like [this one](https://mdef.fablabbcn.org/2023-24/year-1/#modules-by-track).

    **course_type:** The course types are less rigid in their formatting than the tracks. They will appear at the top of the banner image next to the track type written just as they are input into this field (respecting capitalization, etc.). The original course types agreed upon are: **workshop, seminar, short course, and long course**, with only one course type being selected under ideal conditions. These should be written with the first letter capitalized to respect formatting guidelines, but on a technical level not doing so will not produce an error.
    
    **feature_img:** The featured image will appear as the banner image on a module page. The image will automatically be cropped to a 16/9 aspect ratio cropping evenly, thus prioritizing the center of the image and standardizing the sizes of the images without additional work. Likewise, the image has a color overlay for stylistic purposes, this cannot be changed. To define a featured image, you need to define a relative path as described in the [image](#images) section of this guide.
    
    !!! danger "Saving images"
    
        All images should be saved in the `assets` folder under `images` to maintain order. For module courses, these images are saved in the corresponding year, and then term. An example of the location of featured image can be seen below in the example of Front Matter with the content filled out. **Image files should be reduced to be less than 1000KB (1MB) to ensure fast loading of the page. The naming convention for these images is the name of the course in lowercase with dashes between words.**
    
    **img_caption:** The image caption will be added just as it is written below the module banner image. **If this is left blank or simply not included, no caption will appear.**

    **faculty:** Since there can be multiple faculty on a single module, this `key` allows for a list of `values`, so it has a slightly different format. In this case, even if there is a single faculty member to list, a line break is needed, followed by a tab, dash (-), a space, and then the faculty name. The format of the faculty name should be firstname-lastname. (See the example below). Naming conventions correspond to the faculty files, so these should match exactly. This will be covered later in the section on [adding a new faculty member](#adding-new-faculty).

    **ects:** This is the amount of credits that this course is accredited for.

!!! bug "Troubleshooting Front Matter on module pages"

    1. Front Matter must **start and end** with three dashes (---) on their own lines.
    2. Following each `key`, there must be a colon (:) followed by a space. **If you do not include this space, it will produce an error.**
    3. Some `keys` can have multiple `values`, like in the case of faculty. `Keys` like this have a slightly different formatting. The `values` should be written each on a new line, tabbed in once, followed dash (-) and a space then the value as described above.

``` text linenums="1" title="Example with content:"
---
title: Extended Intelligences
page_type: course
track: Exploration
course_type: Course
feature_img: /assets/images/2023-24/year-1/t-1/extended-intelligences.jpeg
img_caption: Martian Species, Estampa, 2021
faculty:
    - ramon-sanguesa
    - lucas-pena
    - pau-artigas
ects: 3
---
```

#### Expected sections within module pages

**`{{ '{{ insert_banner() }}' }}`**

Make sure you include the line `{{ '{{ insert_banner() }}' }}` following the Front Matter or the banner image will not appear even if all the details are correctly filled out.

**`## Syllabus`**

**Includes:** Syllabus content and keywords.

> **EXAMPLE:**

> The first term Design Studio aims to create a solid ground for the students to start developing their projects. Weekly activities will be set to interlink results from the courses like their mappings, cartographies, experiments, 1st person design activities, prototypes, with their personal development plan. In order to propose an area of intervention at the end of the trimester. The Design Studio activities will consist of presentations, group activities, short exercises and personal coaching.

> **Keywords: Prototyping, 1st Person Research through Design, Design Space, Documentation and Communication, Design Interventions**

**`### Learning Objectives`**

**Includes:** Learning objectives provided by faculty. If not included, this can be left blank.

**`### Methodological Strategies`**

**Includes:** Methodological strategies provided by faculty. If not included, this can be left blank.

**`## Schedule`**

The schedule is written in a particular format so that it appears as [content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/). In the full model markdown code listed below this formatting is modeled.

**`## Grading Methods`**

This section often makes use of a [data table](https://squidfunk.github.io/mkdocs-material/reference/data-tables/) to show percentages and the corresponding description of how the final grade will be determined. In the full model markdown code listed below this formatting is modeled.

If no table is provided, you can include an [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) explaining that "Grading criteria will be defined by faculty during the module."

```
!!! info ""

    :fontawesome-solid-circle-info:{ .icon-padding-right } **Grading criteria will be defined by faculty during the module.**
```

Finally, the MDEF website has a [custom admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#custom-admonitions) that displays the ECTS of the module. The code should be written as follows:

```
!!! ects "European Credit Transfer and Accumulation System (ECTS)"

    {{ '{{ ects }}' }} ECTS
```
!!! info "This is generated automatically"

    If if the Front Matter is filled out correctly, the ECTS will appear with the corresponding number of credits.

**`### Evaluation strategies`**

**Includes:** Evaluation strategies provided by faculty. If not included, this can be left blank.

**`## Additional Resources`**

**Includes:** Additional resources provided by faculty. If not included, this can be left blank. Often these resources are provided as lists with links, see the Markdown section above for guidance if necessary.

**`## Faculty`**

To call the faculty listed in the Front Matter, all you need to do is include the line:

```
{{ '{{ insert_faculty() }}' }}
```

As long as the Front Matter has been filled out correctly and the faculty file exists, the faculty should be automatically added to the module page.

#### Module skeleton file

``` text linenums="1"
---
title:
page_type:
track:
course_type:
feature_img:
img_caption:
faculty:
    - 
ects:
---

{{ '{{ insert_banner() }}' }}

## Syllabus

**Keywords:**

### Learning Objectives

### Methodological Strategies

## Schedule

=== "DATE 1"

    CONTENT OF TAB

=== "DATE 2"

    CONTENT OF TAB

=== "DATE 3"

    CONTENT OF TAB

=== "DATE 4"

    CONTENT OF TAB

## Deliverables

## Grading Method

| Percentage  | Description                         |
| ----------- | ------------------------------------|
| XX%         | Description                         |
| XX%         | Description                         |

!!! ects "European Credit Transfer and Accumulation System (ECTS)"

    {{ '{{ ects }}' }} ECTS

## Additional Resources

## Faculty

{{ '{{ insert_faculty() }}' }}
```

!!! info "Check an existing file"

    It is always a good idea to check an existing file if you need to model content. You can see the source code of any page of this website by clicking the view source button at the top of the page.

    Here is an example of a source code page for the module [Atlas of Weak Signals](https://raw.githubusercontent.com/fablabbcn/mdef-docs/main/docs/2023-24/year-1/t1/atlas-of-weak-signals/index.md).


### Adding new faculty

1. **Create the new faculty Markdown document** with the first and last name of the new faculty member (please only use one first name, and one last name)

    > docs/faculty/first-last.md

2. **Add the content using the format below.**

    ```text title="Template for faculty biographies"
    ---
    name: 
    role:
    feature_img: /assets/images/faculty/first-last.jpeg
    socials:
        email:
        website:
        linkedin:
        twitter:
        facebook:
        instagram:
        github:
    ---
    Biography text provided by the faculty member.
    ```

    1. Unlike the file name, the name listed in the _key_ `name:` can be the complete name of the faculty member as they prefer it to be written.
    2. Socials are not required, and can be left blank.
    3. Only one social profile per platform is possible.
    4. Email format is just the email address (i.e. `bob@burgers.net`)
    5. Social media links need a complete URL (i.e. `https://twitter.com/tomasdiez`)
    
3. **Add the `feature_img` to the correct folder** with the same naming structure as the Markdown file and make sure that the file name is correctly reflected in the Mardown file. For instance, for the faculty `first-last` example from above, `feature_img` should read:

    > feature_img: /assets/images/faculty/first-last.jpeg

    Next, make sure that `first-last.jpeg` exists in the `/assets/images/faculty/` directory.

4. **Add the faculty to specific courses and to the faculty page if applicable** using their name in the Front Matter as we saw when creating a new module page.

### Updating & adding to the menu

The menu of a website built with the MkDocs Material template is defined within the `mkdocs.yml` file which can be found in the `root` folder of the repository.

The navigation structure is defined in the `nav` section of the document.

The first level of the navigation is defined with a single tab, dash (-), space, title, and then the path. These first level navigation items appear in the top navigation bar and currently include: Welcome!, Faculty, Students, Year 1, Year 2, and Glossary.

Here is an example of how a first level navigation item is written if it does not have a secondary menu within it: 

``` yaml
nav:
  ...
  - Students: 2023-24/students/index.md
```

However, pages which have sub-menus are written with the path on a separate line. Then, other pages within the sub-menu are listed below it with the previously explained format.

``` yaml
nav:
  ...
  - Year 1:
    - 2023-24/year-1/index.md
    - Calendar: 2023-24/year-1/calendar/index.md
    - Term 1:
      - 2023-24/year-1/t1/index.md
      - Design Studio 01: 2023-24/year-1/t1/design-studio-01/index.md
```

!!! danger "Pay attention to detail"

    As you can see, these nested lists need to follow a strict indentation format or **the structure of the menu can be broken**.
