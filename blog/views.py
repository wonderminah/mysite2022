from bs4 import BeautifulSoup
from django.shortcuts import render
import markdown
import os
import time

path = 'static/post/md'
extensions = ["extra", "abbr", "attr_list", "def_list", "fenced_code", "footnotes", "md_in_html", "tables",
              "admonition", "codehilite", "legacy_attrs", "legacy_em", "meta", "nl2br", "sane_lists", "smarty",
              "toc", "wikilinks"]


def index(request):
    # File list
    file_list = []

    for root, directories, files in os.walk(path):
        for filename in files:
            if '.md' in filename:
                # Open markdown file
                full_path = path + filename
                stream = open(full_path, 'r', encoding='UTF-8')

                # Convert markdown string > html string > plain text
                raw_str = stream.read(300)
                html_str = markdown.markdown(raw_str, extensions=extensions)
                plain_text = ''.join(BeautifulSoup(html_str, 'html.parser').findAll(text=True))

                # Extract just first 300 string as summary
                summary = plain_text[:300]

                # Add to dict
                item = {
                    'title': filename[0:-3],
                    'last_modified_time': time.strftime('%B %d, %Y', time.localtime(os.path.getmtime(os.path.join(root, filename)))),
                    'summary': summary
                }
                file_list.append(item)

    # Context
    context = {'file_list': file_list}

    return render(request, 'blog/index.html', context)


def post(request, filename):
    # Read markdown file
    full_path = path + filename + '.md'
    with open(full_path, 'r', encoding='UTF-8') as file:
        text = file.read()

    # Convert to html
    html_str = markdown.markdown(text, extensions=extensions)
    file_contents = '{}'.format(html_str)

    # Context
    context = {'file_contents': file_contents}

    return render(request, 'blog/post.html', context)
