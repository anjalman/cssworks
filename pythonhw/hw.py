def findClosestNumber(nums):
    
    closest = nums[0]
    min_distance = abs(nums[0])
    
    
    for num in nums:
        distance = abs(num)
        print(f"The distance from {num} to 0 is {distance}.")
        
        
        if distance < min_distance or (distance == min_distance and num > closest):
            closest = num
            min_distance = distance
            
    return closest

nums1 = [-1, 2, 9, 4, 6 ]
print("Input:", nums1)
print("Output:", findClosestNumber(nums1))
print()

nums2 = [3,-5,-2]
print("Input:", nums2)
print("Output:", findClosestNumber(nums2))