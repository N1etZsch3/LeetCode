from typing import List


nums1_e = [1, 2, 3, 0, 0, 0]
m_e = 3
nums2_e = [2, 5, 6]
n_e = 3


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

        p -= 1


merge(nums1_e, m_e, nums2_e, n_e)
print(nums1_e)
