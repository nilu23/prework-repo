

def is_palindrome(s):
    #strip spec charac
    s = ''.join(c for c in s if c.isalnum())
    rev = s[::-1]
    if s.lower() == rev.lower():
         return 1
    else:
        return 0


def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far



def reverseWords(self, A):
    A = A[::-1]
    l = []
    words = A.split(" ")
    for word in words:
        s = word[::-1]
        l.append(s)
    return ' '.join(l)


import collections
def repeatedNumber(self, a):
    for item, count in collections.Counter(a).items():
        if count > 1:
            return item