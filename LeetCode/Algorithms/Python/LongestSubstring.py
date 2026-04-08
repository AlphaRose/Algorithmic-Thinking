################################################################################################
# Source : <https://leetcode.com/problems/longest-substring-without-repeating-characters/>     #
# Author : Rose Martin                                                                         #
# Date   : 20260408                                                                            #
#----------------------------------------------------------------------------------------------#
#       Challenge Description - [3. Longest Substring Without Repeating Characters]            #
#----------------------------------------------------------------------------------------------#
# Given a string s, find the length of the longest substring without                           #
# repeating characters.                                                                        #
#                                                                                              #
# Example:                                                                                     #
#   Input: s = "abcabcbb"                                                                      #
#   Output: 3                                                                                  #
#   Explanation: The answer is "abc", with the length of 3.                                    #
#                                                                                              #
#   Input: s = "bbbbb"                                                                         #
#   Output: 1                                                                                  #
#   Explanation: The answer is "b", with the length of 1.                                      #
#                                                                                              #
#   Input: s = "pwwkew"                                                                        #
#   Output: 3                                                                                  #
#   Explanation: The answer is "wke", with the length of 3.                                    #
#----------------------------------------------------------------------------------------------#
# Constraints:                                                                                 #
#   - 0 <= s.length <= 5 * 10^4                                                                #
#   - s consists of English letters, digits, symbols and spaces.                               #
################################################################################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx, start, chars = 0, 0, {}
        for i in range(len(s)):
            if s[i] in chars and start <= chars[s[i]]: start = chars[s[i]] + 1
            else: mx = max(mx, i - start + 1)
            chars[s[i]] = i
        return mx
