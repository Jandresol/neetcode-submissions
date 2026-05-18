class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # (index, temperature)
        stack = []

        for i, temp in enumerate(temperatures):
            # If temp is greater than the last element in the stack
            while stack and temp > stack[-1][1]:
                stack_index = stack[-1][0]
                result[stack_index] = i - stack_index
                stack.pop()
            stack.append((i, temp))
        return result
        