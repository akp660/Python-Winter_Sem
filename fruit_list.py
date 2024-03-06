fruits = ['orange', 'apple', 'pear','banana', 'kiwi', 'apple', 'banana']

# Count number of fruits

fruit_counts = {}

for fruit in fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

for fruit, count in fruit_counts.items():
    print(f"{fruit}: {count}")