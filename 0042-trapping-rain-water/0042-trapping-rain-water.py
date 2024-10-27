class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 # Initialize two pointers, one at the beginning and one at the end of the height list
        left_max, right_max = -1, -1 # Initialize variables to store the maximum height encountered so far from the left and right sides
        water = 0 # Initialize a variable to store the total trapped water

        # Traverse the height list from both ends towards each other until the pointers meet
        while l < r:
            left_max = max(left_max, height[l]) # Update the maximum height encountered from the left side
            right_max = max(right_max, height[r]) # Update the maximum height encountered from the right side

            # Calculate the trapped water based on the lower maximum height encountered so far (between left_max and right_max)
            # If left_max is less than right_max, the current height at index l can trap water, otherwise, the current height at index r can trap water
            if left_max < right_max:
                water += left_max - height[l]
                l += 1
            else:
                water += right_max - height[r]
                r -= 1

        return water # Return the total trapped water
