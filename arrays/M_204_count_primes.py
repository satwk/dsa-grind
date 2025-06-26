# ---
# Difficulty: Medium
# Tags: [Array, Math, Number Theory]
# Link: https://leetcode.com/problems/count-primes/description/
# ---

'''
Ye solution mera ek leetcode contest m bhi work kiya h, isme basically check krte individual numbers ka in isPrime function.
<=1, 2,3, their multiples tk ka toh straightforward h. uske baad ek new variable define krte (i) =5 aur fir usko aur i+2
ko check krte taki saare odd numbers check ho jaye. ye check wala loop runs √n times [dekho i*i wali line] aur loop m 
i+=6 krte because every number can be represented as 6k+1,2,3,4,5,6. 6k+2,4,6 wale 2 ke multiples h toh checked already
same with 6k+3,6 with 3. bache 6k+1 and 6k+5 (aka 6M-1) toh bs inhe check krte hi sab computer ho jata h. Mere given testcases
saare pass ho gye with this code but time limit exceeded with a testcase where n = 5000000 💀 toh next approach is better/best

Time complexity: O(n*√n) or O(n^3/2) which isnt bad per se but when inputs > 10^6 = TLE
Space complexity: O(1)
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrime(n):
            if n<=1:
                return False
            if n==2 or n==3:
                return True
            if n%2==0 or n%3==0:
                return False
            i = 5
            while i*i<=n:
                if n%i==0 or n%(i+2)==0:
                    return False
                i+=6
            return True
        count = 0
        for i in range(n):
            if isPrime(i):
                count+=1
        return count

'''
this approach is called Sieve of Eratosthenes. isme n+1 length ki list bnti h (iss question m 'n' ki hi bnai because upto n
bola h questino m mtlb 'n' wala number check nhi krna h) aur fir aur har element ke position ko '1' set krdete list m. fir
0 aur 1 ko manually '0' set krte (obviously). then check krte from 2 to √n (same logic as before) aur fir if that position is
'1' then from that position uss position element ke saare multiples ko '0' set krdena hota h. isse kya hota ki after complete
traversal only prime positions = '1' rest = '0' toh fir end m manipulations kr skte iss list m. jaise iss question m count 
poocha tha toh direct sum(primelist) return krdiya but individual elements maangte toh
elements = [i for i in range(len(primelist) if primelist[i]==1 ] kr skte the

Time complexity: O(n log(log n))
Space complexity: O(n)
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        primelist = [1]*n
        primelist[0] = 0
        primelist[1] = 0
        for i in range(2, int(n**(1/2)+1)):
            if primelist[i]==1:
                for j in range(i*i, n, i):
                    primelist[j] = 0
        return sum(primelist)
