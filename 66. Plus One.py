class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        str_digits = ''.join(str(i) for i in digits)
        int_digits = int(str_digits) + 1
        str_digits = str(int_digits)
        for i in str_digits:
            result.append(int(i))
        return result
