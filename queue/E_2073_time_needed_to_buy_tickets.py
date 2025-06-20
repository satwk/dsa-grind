# ---
# Difficulty: Easy
# Tags: [Queue, Simulation, Greedy]
# Link: https://leetcode.com/problems/time-needed-to-buy-tickets/
# ---

'''
Approach:
isme basically queue lgna tha but maine greedy maths se har step pe number of tickets bought nikalke maths ka savaal bnadiya ise

for i<=k agar tickets[i] is less than tickets[k] then people before k will buy all the tickets they want before exiting the queue but agar tickets[k] se more h toh vo 
max to max 'k' tickets hi khareed skte h because uske baad 'k' person ke saare tickets exhaust ho jayenge and he'll exit the queue

for i>k agar ticket[i] is less than tickets[k] toh same upar wala casee but if more than vo log max to max k-1 tickets khareed payenge. For example [1,2,3] h and k is 2
toh 3 wala banda max to max 1 (which is 2-1) tickets hi le payega because [0,2,3] - [1,3] - [2,1] - [0,2]

Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(len(tickets)):
            if i<=k:
                count += min(tickets[i], tickets[k])
            else:
                count += min(tickets[i], tickets[k]-1)
        return count
