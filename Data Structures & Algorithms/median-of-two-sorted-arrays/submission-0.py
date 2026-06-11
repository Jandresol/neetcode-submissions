class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        half = n //2
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            # partition of A
            i = (l + r) // 2
            # partition of B
            j = half - (i + 1) - 1

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # if odd
                if n % 2 == 1: 
                    return(min(Aright, Bright))
                return(max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # move the partition down
                r = i - 1
            else:
                l = i + 1
        