class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
    
        low, high, n = min(nums), max(nums), len(nums)
        if low == high:
            return 0
    
        # Step 1: Initialize buckets
        # Each bucket stores [min_val, max_val] for its range
        bucket_min = [float('inf')] * n
        bucket_max = [float('-inf')] * n
    
        # Step 2: Determine bucket size and fill buckets
        bucket_size = max(1, (high - low) // (n - 1))
    
        for x in nums:
            idx = (x - low) // bucket_size
            # The last element (high) might fall into an n-th index;
            # we clamp it to n-1
            idx = min(idx, n - 1)
            bucket_min[idx] = min(bucket_min[idx], x)
            bucket_max[idx] = max(bucket_max[idx], x)
    
        # Step 3: Scan buckets to find the max gap
        max_gap = 0
        prev_max = low
    
        for i in range(n):
            # Skip empty buckets
            if bucket_min[i] == float('inf'):
                continue
        
            # Gap is the difference between current bucket's min and previous bucket's max
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        
        return max_gap
