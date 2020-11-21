
class Solution:
        
    def dominantIndex(self, nums: List[int]) -> int:   
        
        # self.explain_it_to_me()
        
        """
        Provided Solution
        """
        m = max(nums)
        if all(m  >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1
        
        """
        Method 1
        """
        # m1 = max(nums)
        # i = nums.index(m1)
        # x = m1//2
        # for n in nums:
        #     if x < n:
        #         return -1
        # return i
        
        """
        Method 2
        """
        # m1 = max(nums)
        # i = nums.index(m1)
        # nums[i] = -float("inf") # set max # to -infinity
        # m2 = max(nums)
        # return i if m1 >= m2*2 else -1
        
        
    def explain_it_to_me(self):
        """
        - [60 seconds read]
        - 
        - What the hell is `all(m  >= 2*x for x in nums if x != m)`?
        - 🤔
        ------------------------------------------------------------------------------------
        - Let's spread out
        -          all(m  >= 2*x for x in nums if x != m)
        ------------------------------------------------------------------------------------
        -      all(                  m >= 2*x      for x in nums           if x != m)
        ------------------------------------------------------------------------------------
        - Are `all`
        -          the values where `m >= 2*x` 
        -                                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        -                                     ~ WAIT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        -                                     ~ I know m = max(nums) from above ~
        -                                     ~ where did x come from? ~~~~~~~~~~
        -                                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        -                                          for x in nums           if x != m
        - Are `all` the values where `m >= 2*x` `for` all `x in nums` where `x != m` ?
        - Is it always(`all`) true that `m >= 2*x` `for` all `x in nums` where `x != m` ?
        -
        -
        ----------------------------------------------------------------------------------------
        |                      PYTHON COMMAND |                  OUTPUT | DESCRIPTION         
        ----------------------------------------------------------------------------------------
        |                                nums |        [10, 3, 3, 2, 1] | Prints nums         
        |                   (x for x in nums) | <generator object ... > | Prints reference to generator object
        |                   [x for x in nums] |        [10, 3, 3, 2, 1] | Added `[]` for better printing
        |            all(x < 5 for x in nums) |                   False | Are all x < 5 where x are all elements in nums? (10))
        |  all(x < 5 for x in nums if x != m) |                    True | [same] but the for loop only returns x where x != m

        - simply change `x < 5` to `m >= 2*x`
        - And we have `all(m >= 2*x for x in nums if x != m)`:  True
          - Are `all` the values where `m >= 2*x` `for` all `x in nums` where `x != m` ?
          - or: Is it always(`all`) true that `m >= 2*x` `for` all `x in nums` where `x != m` ?

        """
        
        
        # Helper code to generte some explanation details above
        nums = [10, 3, 3, 2, 1]
        m = max(nums)
        row_format = "| {:>35} | {:>23} | {:<20}"
        print("----------------------------------------------------------------------------------------")
        print(row_format.format(*["PYTHON COMMAND", "OUTPUT","DESCRIPTION"]))
        print("----------------------------------------------------------------------------------------")
        print(row_format.format(*["nums", str(nums),"Prints nums"]))
        print(row_format.format(*["(x for x in nums)", "<generator object ... >", "Prints reference to generator object"]))
        print(row_format.format(*["[x for x in nums]", str([x for x in nums]),    "Added `[]` for better printing"]))
        print(row_format.format(*["all(x < 5 for x in nums)", str(all(x < 5 for x in nums)),  "Are all x < 5 where x are all elements in nums? (10))"]))
        print(row_format.format(*["all(x < 5 for x in nums if x != m)", str(all(x < 5 for x in nums if x != m)),"[same] but the for loop only returns x where x != m"]))
        print("")
        print("- simply change `x < 5` to `m >= 2*x`")
        print("- And we have `all(m >= 2*x for x in nums if x != m)`: ", all(m >= 2*x for x in nums if x != m))
        print("  - Are `all` the values where `m >= 2*x` `for` all `x in nums` where `x != m` ?")
        print("  - or: Is it always(`all`) true that `m >= 2*x` `for` all `x in nums` where `x != m` ?")

