Max = float(input())
N = int(input())

Maxel = 0
maxN = -100000000000`
errorN = 0
sum = 0

for i in range(N):
    Str = input()

    if str(Str) == 'error':
        errorN += 1
    else:
        sum += float(Str)
        if float(Str) > float(Maxel):
            Maxel = float(Str)
        if float(Str) > float(Max):
            maxN += 1

print(f"Элементов - {N}")
print(f"Ошибки - {errorN}")
print(f"Превышений - {maxN}")
print(f"Максимальный элемент - {Maxel:.1f}")
print(f"Средний элемент - {(sum / (N - errorN)):.1f}")
