########################################################################
# Source : <https://leetcode.com/problems/word-frequency/>             #
# Author : Rose Martin                                                 #
# Date   : 20260407                                                    #
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

# Check if the input file exists. 
# Exit with an error message if it does not. 
if [ ! -f "words.txt" ]; then
  echo "Error: words.txt not found."
  exit 1
fi

# Use mawk with C locale for consistent character handling and performance.
# mawk over awk should speed things up, look into that more later.
# Process each line: split into lowercase words, count occurrences.
LC_ALL=C mawk '{
  n = split(tolower($0), arr, /[^a-zA-Z]+/)

  for (i = 1; i <= n; i++)
    if (arr[i] != "") count[arr[i]]++
}
END {
  for (word in count)
