# Define a function to draw the snake on the screen
def draw_snake(snake, WIN):
  # Draw each pixel of the snake
  for i in range(len(snake)):
    WIN.addstr(snake[i][0], snake[i][1], "*")
