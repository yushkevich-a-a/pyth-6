num = int(input())

cnt = 0
a = 1

while (a <= num): 
    if num % a == 0:
        cnt +=1
        print(a)
    a +=1

print(cnt)