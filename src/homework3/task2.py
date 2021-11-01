""" Условие задачи 2, List practice

1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке
этого элемента не было."""

list1 = [i + j for i in "ab" for j in "bcd"]
list2 = list1[::2]
list3 = [str(i) + "a" for i in range(1, 5)]
print(list3.pop(1))
list4 = list3.copy()
list4.append("2a")
