""" Условие задачи 5, Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
 Элементы нужно выводить в том порядке, в котором они встречаются в списке."""
str1 = input("Ведите список чисел: ")
list1 = str1.split()
for i in list1:
    if list1.count(i) == 1:
        print(i)
