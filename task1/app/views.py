import csv

from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'

    inf_rus_list = []

    with open('inflation_russia.csv') as file:
        info = csv.DictReader(file, delimiter=';')
        for line in info:
            for key, value in line.items():
                if key != 'Год':
                    if value:
                        line[key] = float(value)
                    else:
                        line[key] = 0.0
                else:
                    line[key] = int(value)
            inf_rus_list.append(line)

    # чтение csv-файла и заполнение контекста
    context = {
        'head': list(inf_rus_list[0].keys()),
        'info_list': inf_rus_list
    }

    return render(request, template_name,
                  context)
