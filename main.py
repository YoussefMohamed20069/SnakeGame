# Import the important packages
import curses
import random
import time
import os

# Import the draw_snake function
from draw_snake import draw_snake

# Initialize curses package
stdscr = curses.initscr()

# Define the height and the width of the game screen
SIZE = (HEIGTH, WIDTH) = (20, 60)

# Try to start the game window
try:
  # Start the game screen
  WIN = curses.newwin(SIZE[0], SIZE[1], 0, 0)
  
  # enable the keypad mode
  WIN.keypad(True)
  
  # use noecho function to be able to use keys as input
  curses.noecho()
  
  # Ignore the curser
  curses.curs_set(False)
  
  # Define the border of the screen
  WIN.border(0)
  
  # Make no delay
  WIN.nodelay(True)

# Close the game if the window didn't work
except:
  curses.endwin()

def main():
  # Define the Score variable
  score = 0

  # Define the snake and the food variables
  snake = [(4, 10), (4, 11), (4, 12)]
  food = (random.randint(1, 18), random.randint(1, 58))

  # Define the ESCAPE Key
  ESC = 27

  # Define the key variable
  key = curses.KEY_RIGHT
  
  while key != ESC:
    # Write the score on the screen
    WIN.addstr(0, 2, f"Score: {score}")

    # Draw the food on the screen
    WIN.addch(food[0], food[1], "#")

    # Draw the snake on the screen
    draw_snake(snake, WIN)
    
    # Get the user input from the keyboard
    event = WIN.getch()

    # Define a previous key variable
    prev_key = key

    # Define the key for move
    if event != -1:
      key = event
    else:
      key = prev_key

    # Get the location of the snake
    x = snake[0][1]
    y = snake[0][0]
      
    # Move the snake
    if key == curses.KEY_UP:
      y -= 1
    if key == curses.KEY_DOWN:
      y += 1
    if key == curses.KEY_LEFT:
      x -= 1
    if key == curses.KEY_RIGHT:
      x += 1

    pos = (y, x)
    # Add the new location to the snake
    snake.insert(0, pos)

    # Add score when the snake eat the food
    if snake[0] == food:
      # Add one to the snake variable
      score += 1

      # Empty the food variable
      food = ()

      # Add new food
      while food == ():
        food = (random.randint(1, 18), random.randint(1, 58))
        WIN.addch(food[0], food[1], "#")

    # Remove the snake tail to save the snake length
    elif snake[0] != food:
      snake.pop()

    # Stop the game if the snake touch itself
    if snake[0] in snake[1:-1]:
      break

    # Stop the game if the snake touch the window left and right border
    if (snake[0][0] >= 0 and snake[0][0] <= 20) and (snake[0][1] == 0 or snake[0][1] == 60):
      break
    
    # Stop the game if the snake touch the window top or bottom borderf
    if (snake[0][1] >= 0 and snake[0][1] <= 60) and (snake[0][0] == 0 or snake[0][0] == 20):
      break

    # Set time delay
    time.sleep(0.2)

    # erase the window
    WIN.erase()

    # Draw a box around the window
    WIN.box()

  # Return the final score of the game
  return score

# Start the game
if __name__ == "__main__":
  # Try to start the game and draw the final score of the user
  try:
    # Get the player final score
    final_score = main()

    # Clear the terminal window
    os.system("clear")

    # Print the player's final score
    print("Final score: {}".format(final_score))

  # Print good bye for the user if he or she exit the game
  except KeyboardInterrupt:
    print("Good Bye")
