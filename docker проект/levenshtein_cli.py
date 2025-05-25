#!/usr/bin/env python3
import sys

def levenshtein(s1: str, s2: str) -> int:
    """
    Вычисляет расстояние Левенштейна между строками s1 и s2.
    Время O(len(s1)*len(s2)), память O(len(s2)).
    """
    if len(s1) < len(s2):
        # чтобы использовать меньше памяти, пусть s2 будет длиннее
        return levenshtein(s2, s1)

    # предыдущий и текущий ряд для динамики
    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1, start=1):
        current_row = [i]
        for j, c2 in enumerate(s2, start=1):
            ins_cost = previous_row[j] + 1      # вставка
            del_cost = current_row[j-1] + 1     # удаление
            sub_cost = previous_row[j-1] + (c1 != c2)  # замена
            current_row.append(min(ins_cost, del_cost, sub_cost))
        previous_row = current_row

    return previous_row[-1]

def main():
    try:
        s1 = input("Первая строка: ")
        s2 = input("Вторая строка: ")
    except EOFError:
        print("Ошибка ввода.", file=sys.stderr)
        sys.exit(1)

    dist = levenshtein(s1, s2)
    print(f"Расстояние Левенштейна: {dist}")

if __name__ == "__main__":
    main()
