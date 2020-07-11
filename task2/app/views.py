from django.shortcuts import render
import os


def home_view(request):
    template_name = 'app/home.html'
    return render(request, template_name)


def about_view(request):
    template_name = 'app/about.html'
    return render(request, template_name)


def contacts_view(request):
    template_name = 'app/contacts.html'
    return render(request, template_name)


def examples_view(request):
    template_name = 'app/examples.html'
    path = '/home/dell-ubuntu/Рабочий стол/Disk D/dj/Динамическое формирование страниц/task2/app/templates/app/Comps'
    list_comp = os.listdir(path)
    list_html_comp = []
    for comp in list_comp:
        list_html_comp.append(f'app/Comps/{comp}')
    context = {
        'comps': list_html_comp
    }
    return render(request, template_name, context)
