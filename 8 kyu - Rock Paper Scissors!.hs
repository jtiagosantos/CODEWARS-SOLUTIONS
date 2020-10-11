{-
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:
rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!

https://i.imgur.com/aimOQVX.png
-}

module Codewars.RockPaperScissors(rps) where

rps :: String -> String -> String
rps p1 p2 | (p1 == "scissors" && p2 == "paper") = "Player 1 won!"
          | (p1 == "paper" && p2 == "rock") = "Player 1 won!"
          | (p1 == "rock" && p2 == "scissors") = "Player 1 won!"
          | (p2 == "scissors" && p1 == "paper") = "Player 2 won!"
          | (p2 == "paper" && p1 == "rock") = "Player 2 won!"
          | (p2 == "rock" && p1 == "scissors") = "Player 2 won!"
          | otherwise = "Draw!"