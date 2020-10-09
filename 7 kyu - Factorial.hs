{-
Yor task is to write function factorial.
-}

module Factorial where

factorial :: Int -> Int
factorial n = product([i | i <- [1..n]])