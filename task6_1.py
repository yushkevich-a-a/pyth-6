n = int(input())


cnt = 0

for i in range(n):
    a = int(input())
    if a == 0:
        cnt += 1

print(f"колличество переданных 0: {cnt}")
