#167 - Two Sum II - Input array is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)# length of array
        j = length - 1# tail pointer points to the last element
        
        # move the head pointer backward to make the sum bigger and closer to the target value.
        for i in range(length):
            # move the tail pointer forward to make the sum smaller and closer to the target value.
            # stop when the sum <= target or the tail pointer is ahead of the head pointer.
            while numbers[i] + numbers[j]  > target and i < j:
                j -= 1
            
            #return positions of the pointers if reaches the target value.
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
        return [-1, -1]
