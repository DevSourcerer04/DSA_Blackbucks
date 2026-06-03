class solution:
    def leaders(self, arr):
        n = len(arr)
        result = []

        for i in range(n):
            flag = True
            for j in range(i + 1, n):
                if arr[i] <= arr[j]:
                    flag = False
                    break
            if flag:
                result.append(arr[i])
        return result
    
values = input("Enter array elements: ")
arr = [int(x) for x in values.replace("[", "").replace("]", "").replace(",", " ").split()]

print("Leaders:", solution().leaders(arr))

# time complexity: O(n^2)
# space complexity: O(n) for storing the leaders
# Hence brute force approach is not efficient for large arrays.
