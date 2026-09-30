class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        short, long = nums1, nums2
        if len(nums1) > len(nums2):
            short, long = nums2, nums1
        
        half = (len(short) + len(long) + 1) // 2
        left, right = 0, len(short)
        while True:
            # i is not index! -> # elements to pick from short
            # so j is # elements to pick from long
            i = (left + right) // 2
            j = half - i
            if i > 0 and short[i-1] > long[j]:
                right = i - 1
            elif i < len(short) and long[j-1] > short[i]:
                left = i + 1
            else:
                short_l = short[i-1] if i > 0 else float("-inf")
                short_r = short[i] if i < len(short) else float("inf")
                long_l = long[j-1] if j > 0 else float("-inf")
                long_r = long[j] if j < len(long) else float("inf")
                if (len(short) + len(long)) % 2:
                    return max(short_l, long_l)
                else:
                    return (max(short_l, long_l) + min(short_r, long_r)) / 2