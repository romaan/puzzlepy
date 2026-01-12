Given an array of integers, nums, find all possible subsets of nums, including the empty set. Note: The solution set must not contain duplicate subsets. You can return the solution in any order.

Constraints:

1≤ nums.length ≤ 10
−
−10 ≤ nums[i] ≤ 10

All the numbers of nums are unique.

-------------------------------------

Solution:

Start: []

                         []
              /---------------------------\
          exclude 1                    include 1
              []                          [1]
          /---------\                /-------------\
     exclude 2   include 2       exclude 2       include 2
         []         [2]              [1]           [1,2]
       /----\      /----\          /----\         /------\
   ex3   in3  ex3   in3         ex3   in3      ex3      in3
    []   [3]  [2]  [2,3]       [1]  [1,3]    [1,2]   [1,2,3]

