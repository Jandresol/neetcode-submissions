class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # index and block
        maxArea = 0
        for i, b in enumerate(heights):
            start = i
            # go through the stack 
            while stack and stack[-1][1] > b:
                # if the bar before the current is bigger
                # we want to pop the old one
                index, block = stack.pop()
                # compute the backwards area
                maxArea = max(maxArea, block * (i - index))
                #  the new block goes backwards
                start = index
            # add the position onto the stack 
            stack.append((start, b))

        # anything thats still in the stack,
        # they're able to be extended to the end
        for i, b in stack:
            maxArea = max(maxArea, b * (len(heights) - i))
        return maxArea
        