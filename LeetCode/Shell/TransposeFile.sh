########################################################################
# Source : <https://leetcode.com/problems/transpose-file/>             #
# Author : Rose Martin                                                 #
# Date   : 20260407                                                    #
#----------------------------------------------------------------------#
#   Challenge Description - [194. Transpose File]                      #
#----------------------------------------------------------------------#
# Given a text file file.txt, transpose its content.                   #
#                                                                      #
# You may assume that each row has the same number of columns, and     #
# each field is separated by the ' ' character.                        #
#                                                                      #
# Example:                                                             #
# Assume that file.txt has the following content:                      #
#   name age                                                           #
#   alice 21                                                           #
#   ryan 30                                                            #
# Your script should output the following:                             #
#   name alice ryan                                                    #
#   age 21 30                                                          #
########################################################################

# Read each line, store fields in a 2D matrix indexed by [column][row]
# Track the maximum number of columns seen across all lines
# Store field i of current row
# Update max column count
# Loop over each original column (now a row in transposed output)
# Print each value space-separated, no trailing space
# Newline after each transposed row

awk '
{
    for (i = 1; i <= NF; i++)
        matrix[i][NR] = $i
    if (NF > maxCols) maxCols = NF
}

END {
    for (i = 1; i <= maxCols; i++) {
        for (j = 1; j <= NR; j++)
            printf "%s%s", matrix[i][j], (j < NR ? " " : "")
        print ""
    } 
}' file.txt
