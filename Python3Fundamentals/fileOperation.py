look = input("Enter the input to find: ")
found = False
with open('file.txt') as file:
#     # result = file.read()
#     # print(result)

#     # result = file.readlines()
#     # for line in result:
#     #     print(line)

    for line in file:
        if look in line:
            print(line)
            found = True
            break

if found==False:
    print("Accronym not Found")