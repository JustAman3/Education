x = int(input())

if x < 0 or x > 36:
    print("ошибка ввода")
elif x == 0:
    print("зеленый")
elif 1 <= x <= 10:
    print("красный" if x % 2 != 0 else "черный")
elif 11 <= x <= 18:
    print("черный" if x % 2 != 0 else "красный")
elif 19 <= x <= 28:
    print("красный" if x % 2 != 0 else "черный")
elif 29 <= x <= 36:
    print("черный" if x % 2 != 0 else "красный")
