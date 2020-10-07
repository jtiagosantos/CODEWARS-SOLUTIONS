{-
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
-}

module Codewars.Kata.XO where

read_x :: String -> Int
read_x str = length([i | i <- str, i == 'x' || i == 'X'])


read_o :: String -> Int
read_o str = length([i | i <- str, i == 'o' || i == 'O'])


xo :: String -> Bool
xo str | (read_x(str) == read_o(str)) = True
       | otherwise = False