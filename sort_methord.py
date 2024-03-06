fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruit_counts = {}

for fruit in fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

sorted_fruits = sorted(fruit_counts.keys())

for fruit in sorted_fruits:
    print(f"{fruit}: {fruit_counts[fruit]}")