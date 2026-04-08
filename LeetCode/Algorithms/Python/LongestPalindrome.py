#############################################################################
# Source : <https://leetcode.com/problems/longest-palindromic-substring/>   #
# Author : Rose Martin                                                      #
# Date   : 20260408                                                         #
#---------------------------------------------------------------------------#
#        Challenge Description - [5. Longest Palindromic Substring]         #
#---------------------------------------------------------------------------#
# Given a string s, return the longest palindromic substring in s.          #
#                                                                           #
# Example:                                                                  #
#   Input: s = "babad"                                                      #
#   Output: "bab"                                                           #
#   Explanation: "aba" is also a valid answer.                              #
#                                                                           #
#   Input: s = "cbbd"                                                       #
#   Output: "bb"                                                            #
#---------------------------------------------------------------------------#
# Constraints:                                                              #
#   - 1 <= s.length <= 1000                                                 #
#   - s consists of only digits and English letters.                        #
#############################################################################

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        pals = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        return sorted(pals, key = len)[-1] if pals else ''
