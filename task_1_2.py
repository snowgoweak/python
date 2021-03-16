cubes = [i ** 3 for i in range(1, 1000) if i % 2 != 0]

print(cubes)


a = []

for element in cubes:

    suma = 0
    while element > 0:
        digit = element % 10
        suma = suma + digit
        element = element // 10

    # print(suma)
    for i in a:

        i.append(suma)
    print(a)


        # if suma % 7 == 0:
        #     a = suma // 7
        #     # print(a)
        #     print(cubes[element])










