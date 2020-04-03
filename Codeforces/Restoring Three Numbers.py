nums = list(map(int, input().split()))
s = max(nums)
nums.remove(s)
print(s - nums[2], s - nums[1], s - nums[0])