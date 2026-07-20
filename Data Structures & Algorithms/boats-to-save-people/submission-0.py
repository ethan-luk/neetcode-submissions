class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # lower bound == len(people) / 2, two people in every boat
        # upper bound == len(people), everybody needs their own boat

        # the ordering doesn't matter

        # heaviest with the lightest, if that doesn't work, the heaviest needs their own boat

        people.sort()

        l = 0
        r = len(people) - 1

        min_boats = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                min_boats += 1
                l += 1
                r -= 1
            else:
                min_boats += 1
                r -= 1
        
        if l == r:
            min_boats += 1
        
        return min_boats

            