# capacity to ship packages within 'D' days usin Binary search

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            current_load = 0
            required_days = 1
            
            for weight in weights:
                if weight > capacity:
                    return False
                if current_load + weight > capacity:
                    required_days += 1
                    current_load = weight
                else:
                    current_load += weight
            
            return required_days <= days
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

def main():
    weights = list(map(int, input("Enter the weights of the packages separated by space: ").strip().split()))
    days = int(input("Enter the number of days to ship the packages: ").strip())
    
    solution = Solution()
    min_capacity = solution.shipWithinDays(weights, days)
    
    print(f"Minimum capacity required to ship the packages within {days} days: {min_capacity}")

if __name__ == "__main__":
    main()  

