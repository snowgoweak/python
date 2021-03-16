home_work_list = [57.8, 46.51, 97, 13.37, 48.97, 67, 113, 99.99, 38.07, 101.67, 45.65, 33.33, 69.99, 70.06, 322.22]
new_list = []

# count = 5
# a = int(home_work_list[count])
# b = round((home_work_list[count] - int(home_work_list[count])) * 100)
# print(a, b)

for i in range(len(home_work_list)):

    home_work_list.sort()
    a = int(home_work_list[i])
    b = round((home_work_list[i] - int(home_work_list[i])) * 100)

    print('Руб:', a, 'Коп:', f'{b:02}')


print(home_work_list)
