def linear_search(arr, target):
    iterations = 0
    for i in range(len(arr)):
        iterations += 1

        if arr[i] == target:
            print(f" --> Found {target} at index {i} in {iterations} iteration(s)\n")
            return i
    print(f"--> {target} not found after {iterations} iteration(s)\n")
    return -1

data = [10, 20, 30, 40, 50]
print("Array:", data)

best_target= 10
best_index = linear_search(data, best_target)
print(f"Best Case -> Searching {best_target}: Found at index {best_index}")

avg_target=30
avg_index = linear_search(data, avg_target)
print(f"Average Case -> Searching {avg_target}: Found at index {avg_index}")

worst_target=50
worst_index = linear_search(data, worst_target)
print(f"Worst Case -> Searching {worst_target}: Found at index {worst_index}")

missing_target = 67
missing_index = linear_search(data, missing_target)
print(f"Missing Case -> Searching {missing_target}: Found at index {missing_index}")