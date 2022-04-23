from ast import For, Return
from django.shortcuts import render
from . import util
from markdown2 import Markdown
import random
markdown = Markdown()


def entry(request):
    if request.method == "POST":
        title = request.POST['title']
        if title in util.list_entries():
            data = "Sorry this entry already exists"
        else:
            content = request.POST['content']
            f = open("./entries/"+title+".md", "w")
            f.write(content)
            f.close()
            data = markdown.convert(util.get_entry(title))
        return render(request, "encyclopedia/details.html", {
            "title": data
        })
    else:
        return render(request, "encyclopedia/entry.html", {
        })
    return render(request, "encyclopedia/entry.html", {})


def index(request):
    print(util.list_entries())
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "random": random.choice(util.list_entries())
    })


def title(request, pk):
    print(pk)
    data = markdown.convert(util.get_entry(pk))
    return render(request, "encyclopedia/details.html", {
        "content": data,
        "title": pk,
        "random": random.choice(util.list_entries())
    })


def search(request):
    if request.method == "POST":
        searched = request.POST['search']
        if searched in util.list_entries():
            return render(request, "encyclopedia/details.html", {
                "title": util.get_entry(searched),
                "random": random.choice(util.list_entries())

            })
        else:
            return render(request, "encyclopedia/search.html", {
                "title": searched,
                'list': util.list_entries(),
                "random": random.choice(util.list_entries())

            })
    else:
        return render(request, "encyclopedia/search.html", {
            "random": random.choice(util.list_entries())

        })


def edit(request, pk):
    if request.method == "POST":
        content = request.POST['content']
        f = open("./entries/"+pk+".md", "w")
        f.write(content)
        f.close()
        return title(request, pk)
    return render(request, "encyclopedia/edit.html", {
        "title": pk,
        "random": random.choice(util.list_entries())

    })
