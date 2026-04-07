########################################################################
# Source : <https://leetcode.com/problems/valid-phone-numbers/>        #
# Author : Rose Martin                                                 #
# Date   : 20260407                                                    #
#----------------------------------------------------------------------#
#   Challenge Description - [193. Valid Phone Numbers]                 #
#----------------------------------------------------------------------#
# Given a text file file.txt that contains a list of phone numbers     #
# (one per line), write a one-liner bash script to print all valid     #
# phone numbers.                                                       #
#                                                                      #
# You may assume that a valid phone number must appear in one of the   #
# following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx.               #
# (x means a digit)                                                    #
#                                                                      #
# You may also assume each line in the text file must not contain      #
# leading or trailing white spaces.                                    #
#                                                                      #
# Example:                                                             #
# Assume that file.txt has the following content:                      #
#   987-123-4567                                                       #
#   123 456 7890                                                       #
#   (123) 456-7890                                                     #
# Your script should output the following valid phone numbers:         #
#   987-123-4567                                                       #
#   (123) 456-7890                                                     #
#----------------------------------------------------------------------#
# Note:                                                                #
#   - Could you write it in one-line using Unix pipes?                 #
########################################################################

p=\([0-9][0-9][0-9]\)\ [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] # Pattern for format: (xxx) xxx-xxxx
p1=[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] # Pattern for format: xxx-xxx-xxxx

while read -r line # Read file line by line
 do
  case "$line" in # Check if line matches either valid phone format
  $p)
  echo $line # Print if matches (xxx) xxx-xxxx
  ;;
  $p1)
  echo $line # Print if matches xxx-xxx-xxxx
  ;;
  esac
 done < file.txt # Feed file.txt as input to the while loop
