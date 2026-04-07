########################################################################
# Source : <https://leetcode.com/problems/word-frequency/>             #
# Author : Rose Martin                                                 #
# Date   : 20260406                                                    #
#----------------------------------------------------------------------#
#          Challenge Description - [192. Word Freqency]                #
#----------------------------------------------------------------------#
# Write a bash script to calculate the of each word in a text file     #
# words.txt. For simplicity sake, you may assume:                      #
#   - words.txt contains only lowercase characters and space ' ' chars #
#   - Each word must consist of lowercase characters only.             #
#   - Words are separated by one or more whitespace characters.        #
#                                                                      #
# Example:                                                             #
# Assume that words.txt has the following content:                     #
#   the day is sunny the the                                           #
#   the sunny is is                                                    #
# Your script should output the following, sorted by descending freq:  #
#   the 4                                                              #
#   is 3                                                               #
#   sunny 2                                                            #
#   day 1                                                              #
#----------------------------------------------------------------------#
# Note:                                                                #
#   - Don't worry about handling ties, it is guaranteed that each      #
#     word's frequency count is unique.                                #
#   - Could you write it in one-line using Unix pipes?                 #
########################################################################
#!/bin/bash

# Read file | Flatten all words to one per line | sort alphabetically for uniq |
# count occurrences | sort by count descending | reformat to "word count"
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{ print $2, $1 }'
