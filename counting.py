def counting_sort(nums) :
    output = [0 for i in range(len(nums))]

    count = [0 for i in range(256)]
  

    ans = ["" for _ in nums]
  

    for i in nums:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i-1]
  

    for i in range(len(nums)):
        output[count[ord(nums[i])]-1] = nums[i]
        count[ord(nums[i])] -= 1
  
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(nums)):
        ans[i] = output[i]
    return ans 