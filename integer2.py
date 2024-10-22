def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3

nums = [19,4,5,7,4,6,4,5]

print (nums)
print ("Output:",test(nums))