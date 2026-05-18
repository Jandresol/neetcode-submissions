class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency bucket where index represents the frequency
        freq = [[] for _ in range(len(nums) + 1)] 
        
        # Dictionary to count occurrences of each number
        count = {}
        for num in nums:
            # Increment the count for the number
            count[num] = count.get(num, 0) + 1 
        
        # Populate the frequency bucket
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Build the result list from the most frequent elements
        res = []
        for i in range(len(nums), 0, -1):  # Iterate from highest frequency to lowest
            for num in freq[i]:
                res.append(num)
                if len(res) == k:  # Stop when we've added k elements
                    return res
