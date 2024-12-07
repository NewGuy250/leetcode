class Solution:
    def permute(self, nums):
        n = len(nums)

        # Store the final permutations and the current solution
        ans = []
        sol = []  

        def backtrack():
            # Base Case: If the current solution has all `n` elements
            if len(sol) == n:
                ans.append(sol[:])  # Add a copy of the current solution to the results
                return  # Backtrack

            # Iterate through each number in the input list
            for x in nums:
                # Skip if the number is already in the current solution
                if x not in sol:
                    # Choose: Add the current number to the solution
                    sol.append(x)
                    
                    # Explore: Recursively call backtrack to continue building the permutation
                    backtrack()
                    
                    # Unchoose: Remove the last number to try the next possibility
                    sol.pop()

        backtrack()

        # Return the list of all permutations
        return ans
