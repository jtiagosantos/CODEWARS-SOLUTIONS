{-
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
-}

module Stray (stray) where
import Data.List

sort_list :: [Int] -> [Int]
sort_list list = sort(list)

stray :: [Int] -> Int
stray list = if head(sort_list(list)) == tail(sort_list(list)) !! 0 then last(sort_list(list)) else sort_list(list) !! 0