# ---
# Difficulty: Easy
# Tags: [String, Two Pointers]
# Link: https://leetcode.com/problems/valid-palindrome/description/
# ---

'''
isme mera approach more or less same hi h but important theoretical concept se time complexity quadratic se linear ki ja skti h. when I do z+=i it creates a new string at 
a fresh new memory location because strings are immutable which causes O(n) inside of a for loop which makes it quadratic time.

Time complexity: O(n^2)
Space complexity: O(n)
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = ''
        for i in s:
            if i.isalnum():
                z+=i.lower()
        if z==z[::-1]:
            return True
        else:
            return False

'''
instead, agar ek list bnaoge aur usse end m join krdoge toh it'll be much more efficient because list ke liye new memory location allocate nhi ho rhi h toh time complexity 
remains linear

Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = []
        for i in s:
            if i.isalnum():
                z.append(i.lower())
        f = ''.join(z)
        return f == f[::-1]

'''
two pointer approach is the best because isse no extra datastructural space created/maintained only two pointers left and right toh space remains constant which is ideal
one thing to keep in mind jo do nested while loop h usme agar left<right wali condition nhi lgaoge toh they may go out of bounds, like for example the input is ".,/?.,."
toh technically, according to the rules of palindrome defined in the question, this input IS a palindrome but right pointer alnum dhoondne ke chakkar m skip past kr jayega
through all this. same is the thing with left pointer. so it is crucial to check at every step and maintain ki left remains less than right

Time complexity: O(n)
Space complexity: O(1) 🤩
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            while left<right and not s[right].isalnum():
                right-=1
            while left<right and not s[left].isalnum():
                left+=1
            if s[right].lower()!=s[left].lower():
                return False
            else:
                right-=1
                left+=1
        return True
