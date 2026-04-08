########################################################################
# Source : <https://leetcode.com/problems/zigzag-conversion/>          #
# Author : Rose Martin                                                 #
# Date   : 20260408                                                    #
#----------------------------------------------------------------------#
#           Challenge Description - [6. Zigzag Conversion]             #
#----------------------------------------------------------------------#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a      #
# given number of rows like this:                                      #
#                                                                      #
#   P   A   H   N                                                      #
#   A P L S I I G                                                      #
#   Y   I   R                                                          #
#                                                                      #
# And then read line by line: "PAHNAPLSIIGYIR"                         #
# Write the code that will take a string and make this conversion      #
# given a number of rows.                                              #
#                                                                      #
# Example:                                                             #
#   Input: s = "PAYPALISHIRING", numRows = 3                           #
#   Output: "PAHNAPLSIIGYIR"                                           #
#                                                                      #
#   Input: s = "PAYPALISHIRING", numRows = 4                           #
#   Output: "PINALSIGYAHRPI"                                           #
#                                                                      #
#   Input: s = "A", numRows = 1                                        #
#   Output: "A"                                                        #
#----------------------------------------------------------------------#
# Constraints:                                                         #
#   - 1 <= s.length <= 1000                                            #
#   - s consists of English letters (lower-case and upper-case),       #
#     ',' and '.'.                                                     #
#   - 1 <= numRows <= 1000                                             #
########################################################################

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        row, direction, res = 0, -1, [""] * numRows
        for char in s:
            res[row] += char
            if row == 0 or row == numRows - 1: direction *= -1 
            row += direction
        return "".join(res) 
