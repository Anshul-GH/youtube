'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
'''
def add_one(arr):
    # routine scenario    
    if arr[-1] < 9:
        arr[-1] += 1
        return arr
    else:
        # reverse the array
        rev = arr[::-1]
        int_num = 0
        dec = 0

        for num in rev:
            int_num += num * (10**dec)
            dec += 1

        # perform the increment
        int_num += 1

        # convert number into a list
        new_arr = str(int_num)
        new_arr = [int(digit) for digit in new_arr]

        return new_arr
