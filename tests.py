from collections import Counter
from time import sleep, time

a = 'Ala ma kota'
b = 'alA am atok'


def rev_str(text: str):
    return ' '.join(x[::-1] for x in text.split())


print(rev_str(a))

x = [1, 2, 3, 4, 4, 4, 4, 5, 326, 26, 6, 4, 6, 4]


def duplicates(x):
    # c = Counter(x)
    # result = []
    # for k, v in c.items():
    #     if v > 1:
    #         result.append(k)
    # return result

    return [k for k, v in Counter(x).items() if v > 1]


print(duplicates(x))

i = [('Tom', 19, 80),
     ('John', 20, 90),
     ('Jony', 17, 91),
     ('Jony', 17, 93),
     ('Json', 21, 85)]
j = [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


def reorder(tuple_: tuple) -> tuple:
    return tuple_[0], tuple_[2], tuple_[1]


def sorted_list(lst: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]:
    return sorted(lst, key=reorder, reverse=True)


print(sorted_list(i))


def time_it(fun):
    def inner(*args, **kwargs):
        start = time()
        result = fun(*args, **kwargs)
        end = time()
        print(f'time taken {end - start}')
        return result

    return inner


@time_it
def sleep1():
    sleep(2)


@time_it
def dupa_2(value: int) -> int:
    print(value)
    return value * 2


print(dupa_2(42))
print(sleep1())
