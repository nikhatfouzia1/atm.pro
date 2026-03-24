class Sort:
    def __init__(self, arr):
        self.arr = arr
    def display(self):
        print("Sorted array:", self.arr)
    def bubble_sort(self):
        arr = self.arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        self.arr = arr
    def selection_sort(self):
        arr = self.arr.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        self.arr = arr
    def insertion_sort(self):
        arr = self.arr.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        self.arr = arr
    def merge_sort(self):
        def merge_sort_recursive(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort_recursive(arr[:mid])
            right = merge_sort_recursive(arr[mid:])
            return merge(left, right)
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        self.arr = merge_sort_recursive(self.arr.copy())
    def quick_sort(self):
        def quick_sort_recursive(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort_recursive(left) + middle + quick_sort_recursive(right)
        self.arr = quick_sort_recursive(self.arr.copy())
def main():
    arr = list(map(int, input("Enter elements: ").split()))
    sorter = Sort(arr)
    while True:
        print("\n--- Sorting Menu ---")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            sorter = Sort(arr)
            sorter.bubble_sort()
            sorter.display()
        elif choice == 2:
            sorter = Sort(arr)
            sorter.selection_sort()
            sorter.display()
        elif choice == 3:
            sorter = Sort(arr)
            sorter.insertion_sort()
            sorter.display()
        elif choice == 4:
            sorter = Sort(arr)
            sorter.merge_sort()
            sorter.display()
        elif choice == 5:
            sorter = Sort(arr)
            sorter.quick_sort()
            sorter.display()
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")
if __name__ == "__main__":
    main()
