#Largest number in an array
#https://www.naukri.com/code360/problems/largest-element-in-the-array-largest-element-in-the-array_5026279?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse

def largestElement(arr: [], n: int) -> int:

    max = arr[0]
    for i in range(0, n):
        if (max < arr[i]):
            max = arr[i]
    return max