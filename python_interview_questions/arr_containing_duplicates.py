'''
Given an integer array, return true if
any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: True

Example 2:
Input: nums = [1,2,3,4]
Output: False

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''
def arr_contains_duplicates(arr):
    arr_uniq = list(set(arr))
    if len(arr_uniq) == len(arr):
        return False
    else:
        return True
