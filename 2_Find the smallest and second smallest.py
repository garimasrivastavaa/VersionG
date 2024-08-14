#Find the smallest and second smallest element
#https://www.geeksforgeeks.org/problems/find-the-smallest-and-second-smallest-element-in-an-array3226/1

class Solution:
    def minAnd2ndMin(self, arr):
        if len(arr) < 2:
            return [-1]

        # Initialize the smallest and second smallest
        smallest = float('inf')
        second_smallest = float('inf')

        # Iterate through the array to find the smallest and second smallest
        for num in arr:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif smallest < num < second_smallest:
                second_smallest = num

        # Check if we have found a valid second smallest
        if second_smallest == float('inf'):
            return [-1]
        else:
            return [smallest, second_smallest]
        
