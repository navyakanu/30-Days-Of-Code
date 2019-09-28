n = int(input())
phone_book = {}
for i in range(0,n):
    print("Enter the name and number to add to phone book in the format name number")
    name, id = input().split()
    phone_book[name] = id
while 1:
    temp = ''
    print("Enter the name to search number for")
    name = input()
    if name == temp:
        break
    if name in phone_book:
        print("Found" + name + "=" + phone_book[name])
    else:
        print("Not found")
