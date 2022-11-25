class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int: 
        '''
        ###Algorithm(DP)###
        Solution(target)
        1.construct table and count(initial=0) to record the sub-result and result,respectively
        2.check if the result of target is in the table
        3.for number in nums:
        4.  subTarget = target - number(if >= 0)
        5.  if subTarget == 0:
        6.      count++
        7.  else:
        8.      count += Solution(subTarget)
        9.      save sub-result in table
        10. return count
        '''
        table = {}
        def Count(target):
            print("123456789")
            count = 0
            subCount = 0
            if target in table:
                return table[target]
            for n in nums:
                if n<=target:
                    subTarget = target - n
                    if subTarget == 0:
                        count += 1
                    else:
                        subCount =Count(subTarget)
                        count += subCount
                        table[subTarget] = subCount
            return count
        return Count(target)
