home_work_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = []
new_names = []
# print(home_work_list[1].split()) # делает из отдельного эдемента из списка список



for i in range(len(home_work_list)):

    a = home_work_list[i].split()


    for j in range(len(a)): #не очень понимаю, каким образом тут выводит последний элемент(полуилось методом тыка)

        b = a[j].split()

    names.extend(b)



# print(names)

new_names = " ".join(names).title().split()
# print(new_names)
count = 0
while count < len(new_names):
    print("Привет,", new_names[count] + "!")
    count += 1







