#task_1

lst = [1, 2]
lst2 = [5, 1]


def comparison(msv, msv2):
    for x in msv:
        if x in msv2:
            print(True)
            break
        else:
            print(False)


comparison(msv=lst, msv2=lst2)

#task_2

num = [5, 4, 3, 2, 1]
num2 = []

for x in num:
    m = num.index(x)
    n = x + m
    num2.append(n)
print(num2)


#task_3

inp = int(input("Enter number: "))
lst = [5, 1, 8, 9]
lst2 = []


def percent(input, msv, msv2):
    m1 = len(msv)
    for num in msv:
        if num > input or num == input:
            lst2.append(num)
            m2 = len(msv2)
            result = (m2*100/m1)
            print(result)


percent(input=inp, msv=lst, msv2=lst2)



#task_4

num = [1, 2, 3, 4, 5, 6]
num2 = int(input("son kriting: "))

del num[0]
num.append(num2)
print(num)


#task_5

lugatlar = {
    'odam1': {'ism': 'John', 'byudjet': 5000},
    'odam2': {'ism': 'Jane', 'byudjet': 7000},
    'odam3': {'ism': 'Bob', 'byudjet': 6000}
}

yigindi = 0
for odam in lugatlar.values():
    yigindi += odam.get('byudjet', 0)

print(f"Odamlar byudjetlarining yig'indisi: {yigindi}")


#task_6


a = [1, 1]
b = []
clon = a.copy()
b.append(a)
b.append(clon)
print(b)


#task_7

list = [1, 2, "name", 3, "surname", "nickname", 4,5]
list2 = []


def find_int(lst, lst2):
    for x in lst:
        if type(x) == int:
            lst2.append(x)
    print(lst2)
find_int(list,list2)


#task_8



lst = ["sardor", "sarvar"]
ln = len(lst)

for name in lst:
    if ln == 0:
        print("no online")

    elif ln == 1:
        print(lst[0] + "online")

    elif ln == 2:
        print(f"{lst[0]} and {lst[1]}" + " online")


#task_9



lst = ["sardor", "sarvar"]
ln = len(lst)

for name in lst:
    if ln == 0:
        print("no online")

    elif ln == 1:
        print(lst[0] + "online")

    elif ln == 2:
        print(f"{lst[0]} and {lst[1]}" + " online")


#task_10

lst = [1, 2, 3, "a", "b", 4]
lst2 = []


def str(msv, msv2):
    for num in msv:
        if type(num) == int:
            lst2.append(num)
    print(msv2)

str(lst,lst2)

