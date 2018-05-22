################################
#Hashing
################################
#Q-1
"""
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]
"""
from collections import defaultdict

def anagrams(self, A):
    res = []
    d = defaultdict(list)

    for i in range(len(A)):
        key = ''.join(sorted(A[i]))
        d[key].append(i + 1)

    for key, indices in d.iteritems():
        res.append(indices)

    return res


#################################
# Linked Lists - solutions
#################################

# Q- 1

def lPalin(self, A):
    """
    Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

    Notes:

    Expected solution is linear in time and constant in space.
    For example,

    List 1-->2-->1 is a palindrome.
    List 1-->2-->3 is not a palindrome.
    """
    end, mid = A, A
    while end and end.next:
        end = end.next.next
        mid = mid.next

    pNode = None
    while mid:
        tmp = mid.next
        mid.next = pNode
        pNode = mid
        mid = tmp

    while pNode:
        if pNode.val != A.val:
            return 0
        pNode = pNode.next
        A = A.next
    return 1

#  Q- 2

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def addTwoNumbers(self, A, B):
    """
    You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8

        342 + 465 = 807
    Make sure there are no trailing zeros in the output list
    So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
    """

    sum, carry = 0, 0
    root = res = ListNode(0)

    while A or B or carry:
        n1, n2 = 0, 0
        if A:
            n1 = A.val
            A = A.next
        if B:
            n2 = B.val
            B = B.next
        carry, sum = divmod(n1 + n2 + carry, 10)

        res.next = ListNode(sum)
        res = res.next

    return root.next