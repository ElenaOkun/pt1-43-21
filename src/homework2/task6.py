def main():
    n = input("Введите целое не отрицательное число: ")
    try:
        n = int(n)
    except ValueError:
        print("Это не число!")
        return
    m = n
    if m < 0:
        print("Это отрицательное число")
        return
    if m % 10 == 0:
        print("Не палиндром")
        return
    new_number = 0
    while m > 0:
        new_number = new_number * 10 + m % 10
        m = m // 10
    if new_number == n:
        print("Палиндром")
    else:
        print("Не палиндром")


main()