from django.shortcuts import render
import markdown


def index(request):

    file_path = '/Users/minah.kim/Desktop/MinahKimTechBlog/'
    file_name = '1.md'
    target_file = file_path + file_name

    with open(target_file, 'r', encoding='UTF-8') as file:
        text = file.read()

    extensions = ["extra", "abbr", "attr_list", "def_list", "fenced_code", "footnotes", "md_in_html", "tables", "admonition", "codehilite", "legacy_attrs", "legacy_em", "meta", "nl2br", "sane_lists", "smarty", "toc", "wikilinks"]
    html = markdown.markdown(text, extensions=extensions)
    print(html)
    body = '{}'.format(html)
    context = {'title': 'this is title', 'body': body}

    return render(request, 'blog/index.html', context)
