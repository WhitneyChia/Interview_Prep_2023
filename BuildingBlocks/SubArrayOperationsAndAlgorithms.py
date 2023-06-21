# Kadane's Algorithm
print("Maximum Subarray - Kadane's Algorithm")
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(nums)
current_subarray_max = overall_maximum = nums[0]

for i in range(1, len(nums)):
    if current_subarray_max < 0:
        current_subarray_max = nums[i]
    else:
        current_subarray_max = nums[i] + current_subarray_max
    overall_maximum = max(current_subarray_max, overall_maximum)

print(overall_maximum)
print("\n")

# Cumulative Sum
print("Calculating a Cumulative Sum")
nums = [-1, 2, 1, -4, 2, 3, -1, 2]
cum_sum = [nums[0]]
print(nums)
for i in range(1, len(nums)):
    cum_sum.append(cum_sum[i - 1] + nums[i])

print(cum_sum)
print("\n")

# Find Subarray that sums to 0
print("Finding a subarray that sums to 0 - leverages cumulative sum")
nums = [-1, 2, 1, -4, 2, 3, -1, 2]
print(nums)
cum_sum = [nums[0]]
cumulative_sums = {nums[0]: 0}
for i in range(1, len(nums)):
    sum_here = cum_sum[i - 1] + nums[i]
    if sum_here in cumulative_sums:
        print(cumulative_sums[sum_here], i)
        break
    cumulative_sums[sum_here] = i
    cum_sum.append(sum_here)

print("\n")
