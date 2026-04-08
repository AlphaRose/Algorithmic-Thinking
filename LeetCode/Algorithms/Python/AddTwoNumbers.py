########################################################################
# Source : <https://leetcode.com/problems/add-two-numbers/>            #
# Author : Rose Martin                                                 #
# Date   : 20260408                                                    #
#----------------------------------------------------------------------#
#           Challenge Description - [2. Add Two Numbers]               #
#----------------------------------------------------------------------#
# You are given two non-empty linked lists representing two            #
# non-negative integers. The digits are stored in reverse order,       #
# and each of their nodes contains a single digit. Add the two         #
# numbers and return the sum as a linked list.                         #
#                                                                      #
# You may assume the two numbers do not contain any leading zero,      #
# except the number 0 itself.                                          #
#                                                                      #
# Example:                                                             #
#   Input: l1 = [2,4,3], l2 = [5,6,4]                                  #
#   Output: [7,0,8]                                                    #
#   Explanation: 342 + 465 = 807.                                      #
#                                                                      #
#   Input: l1 = [0], l2 = [0]                                          #
#   Output: [0]                                                        #
#                                                                      #
#   Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]                        #
#   Output: [8,9,9,9,0,0,0,1]                                          #
#----------------------------------------------------------------------#
# Constraints:                                                         #
#   - The number of nodes in each list is in the range [1, 100].       #
#   - 0 <= Node.val <= 9                                               #
#   - It is guaranteed that the list represents a number that          #
#     does not have leading zeros.                                     #
########################################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x    # Store node value
        self.next = None  # Pointer to next node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)   # Placeholder head to simplify result building
        current = dummy       # Pointer to track current position in result
        carry = 0             # Carry value for sums >= 10

        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0  # Get l1 value or 0 if exhausted
            y = l2.val if l2 is not None else 0  # Get l2 value or 0 if exhausted
            sum = carry + x + y                  # Sum current digits and carry
            carry = sum // 10                    # Calculate new carry

            current.next = l1 if l1 is not None else l2  # Reuse existing node
            current.next.val = sum % 10                   # Store only the ones digit

            current = current.next                        # Advance result pointer
            if l1 is not None: l1 = l1.next              # Advance l1 if not exhausted
            if l2 is not None: l2 = l2.next              # Advance l2 if not exhausted

        if carry > 0:
            current.next = ListNode(carry)  # Append final carry as new node if needed

        return dummy.next  # Return result list, skipping dummy head
