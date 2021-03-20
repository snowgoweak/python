def thesaurus(*name):
    name_list = list(name)
    d = {}
    # print(name_list)
    for i in name_list:
        i.split()
        d.setdefault(i[0], i)
    print(d)


thesaurus("Иван", "Мария", "Петр", "Илья", "Петруша")
