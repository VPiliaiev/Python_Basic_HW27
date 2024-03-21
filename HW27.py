# Створити генератор геометричної прогресії.
# При заданні початку прогресії -2 та кроку прогресії -5,
# генератор видає таку послідовність:
# -2
# 10
# -50
# 250
# -1250
# 6250
# ...
# При заданні початку прогресії 10 і кроку прогресії 3, генератор видає таку послідовність:
#  10
# 30
# 90
# 270
# 810
# 2430
# ...
# def generator(min_1=0, max_1=100):
#     while max_1 >= min_1:
#         yield min_1 ** 2 - 2 * min_1
#         min_1 += 1
#         for item in [1, 2, 5, 8, 0, -11]:
#             print(item)


def generator(start, step):
    value = start
    while True:
        yield value
        value *= step


for item in generator(-2, -5):
    print(item)
    if -1000 <= item >= 1000:
        break

print('-' * 50)

for item in generator(10, 3):
    print(item)
    if -1000 <= item >= 1000:
        break
