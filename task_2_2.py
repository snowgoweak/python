home_work_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# home_work_list = ' 0'.join(home_work_list)

# for i in range(len(home_work_list)):
#     try:
#
#         home_work_list[i] = int(home_work_list[i])
#
#
#
#
#
#     except ValueError:
#         continue


for j in range(len(home_work_list)):
    if home_work_list[j].isdigit():
        home_work_list = ' 0'.join(map(str, home_work_list[j]))
        print('hello')



# home_work_list = ' 0'.join(map(str, home_work_list))
print(home_work_list)
# print(dir(home_work_list))
# print(home_work_list)


