/*
Making Snake in JavaScript
                    
                               Rules:  
--------------------------------------------------------------------------

You control the snake.  Snake moves 1 square every 500 milliseconds
Change directions with arrow keys. 
An apple is randomly placed on the board
If you eat the apple, you grow longer and the apple is placed randomly on a new board tile
The  board is 100 x 100 tiles
The snake starts with a length of 3, grows 2 for every apple it eats

If the snake's "head" touches its body, game is over
If the snake's "head" touches a "wall" (the ends of the board), game is over
Every 5 apples eaten, the snake speeds up by 30 milliseconds
Every apple increases your score by 100 points + (.5 x NumOfApples)

To start the game, press any arrow game
After losing a game, press space to reset the board and snake, then any arrow key to start again


MileStones:
[] Build the board - 100x100 tiles, each tile is 5x5 pixels (?)
[] Build the apple - size=one tile, different color from board and snake. When snake eats it, it gets placed randomly somewhere else
[] Build the snake - size starts at 3, has event listeners for controls
[] Snake has a head that moves, and a trail that follow it. 
[] Snake gains length after eating an apple
[] Build board limits - if snake touches walls, game ends
[] 
[]
[]
*/