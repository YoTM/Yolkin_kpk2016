x = int(input())
n = 0
s = 0
p = 1
while x:
    digit = x%10
    n += 1
    s += digit
    p *= digit
    # print(digit, x)
    x //= 10
print('кол-во цифр:', n)
print('сумма цифр:', s)
print('произведение цифр:', n)
print('среднее арифметическое:', s/n)