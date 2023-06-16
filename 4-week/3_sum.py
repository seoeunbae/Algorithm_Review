class Solution(object):
    def return_list(self, start,nums):
        end = len(nums) - 1
        middle = start + 1

        # end는 내부 while문에서 관리(증가시킨다.)
        while start < end:
            # 1. 포인터가 겹칠때, return
            if start >= end or middle >= end:
                return
            # 2. 중복된 마지막 값 일때, return
            if end < len(nums)-1 and nums[end] == nums[end+1]:
                end -= 1
                continue
            # 3. 중복된 시작값 일때, return
            if start > 0 and nums[start] == nums[start-1]:
                return

            if nums[start] + nums[end] + nums[middle] < 0:
                middle += 1
            elif nums[start] + nums[end] + nums[middle] > 0:
                end -= 1
            else:
                result.append([nums[start], nums[middle], nums[end]])
                end -= 1
                continue

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        global result
        result = list()

        nums.sort()

        if nums[-1] == 0:
            zero_idx = nums.index(0)
            if zero_idx + 3 > len(nums):
                return []
            else :
                return [[0, 0, 0]]
        elif nums[-1] < 0:
            return []
        # start는 전체 for문에서 관리(증가시킨다)
        for i in range(len(nums)):
            self.return_list(i,nums)
        return result