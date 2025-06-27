# ---
# Difficulty: Easy
# Tags: [String, Two Pointers, Greedy]
# Link: https://leetcode.com/problems/valid-palindrome-ii/description/
# ---

'''
isme maine sabse pehle l1 = list(s) kiya aur fir two pointers se check kiya when not equal aya toh try kiya pop krke manipulate
krne ka but popping se indices aage peeche ho jate aur incorrect indices pe pointers set hojate plus pop() method is O(n) so
ye maine starting me hi leave krdiya

neeche approach neetcode se kiya maine ki ek return (skipLeft or skipRight) kro taki agar left skip krke palindrome h toh
true ho jayega, right skip m hai tb bhi true but dono m nhi h toh false. isme bs list slicing aur list[::-1] ko equate krke bhi
kr skte the but fir extra space allot krni pd rhi thi toh ek alag function hi define krdiya and then again usme two pointer
approach lgaya

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return self.checkPalin(s,left+1,right) or self.checkPalin(s,left,right-1)
            left+=1
            right-=1
        return True
    def checkPalin(self, s: str, left: int, right: int) -> bool:
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

'''
small general note regarding manual function definition

jaise upar maine class ke andar but validPalindrome ke bahar new function define kiya h toh usme mereko line 30 m 
self parameter daalna pda. also line 26 m self.checkPalin(blah,blah) krna pda

agar mai validPalindrome ke andar hi NESTED FUNCTION define krta toh ye sb krne ki koi zrurat nhi hoti mereko
changes ko mai neeche mention kr rha hu

aise yaad kro, agar new function is not nester mtlb direct class ke under defined = self sufficient = aatmnirbhar
mtlb tab self self use krna hoga. agar nested h toh no need
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Nested checkPalin function
        def checkPalin(s: str, left: int, right: int) -> bool: # no self parameter
            ...
    # and under the loop while calling the function
    return checkPalin(s, left + 1, right) or checkPalin(s, left, right - 1) # again, no self  
