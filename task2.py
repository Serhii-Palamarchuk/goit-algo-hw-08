# Завдання 2: Злиття k відсортованих списків
# Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. 
# Тепер при виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків в один відсортований список. 
# Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків та повертає відсортований список.

import heapq

def merge_k_lists(lists):
    min_heap = []

    # Додаємо перші елементи всіх списків до купи
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    result = []

    while min_heap:
        # Вибираємо найменший елемент
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)

        # Додаємо наступний елемент з того ж списку до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))

    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)