def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3

nums = [19, 19, 5, 5, 15, 5, 5]

print ("Original List")
print (nums)

print ("Output:",test(nums))