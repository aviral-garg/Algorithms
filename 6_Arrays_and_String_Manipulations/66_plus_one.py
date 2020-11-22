class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        l = len(digits)
        for i, d in enumerate(reversed(digits)):
            i = l - i -1
            d += carry
            
            if d == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = d
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits
