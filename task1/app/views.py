import csv

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'

    inf_rus_list = []
    inf_rus_dict = {}

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
    # print(inf_rus_list)
    #
    # for i in inf_rus_list:
    #     for key, value in i.items():
    #         if key in inf_rus_dict.keys():
    #             inf_rus_dict[key].append(value)
    #         else:
    #             inf_rus_dict[key] = [value]

    # чтение csv-файла и заполнение контекста
    context = {
        #'info_dict': inf_rus_dict,
        'head': list(inf_rus_list[0].keys()),
        'info_list': inf_rus_list
    }

    return render(request, template_name,
                  context)