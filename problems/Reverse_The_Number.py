t = int(input())
for i in range(t):
    num = input()
    num = num[::-1]
    count = 0
    while num[count] == "0":
        count += 1
    print(num[count:len(num) + 1])
