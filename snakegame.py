import os
import random
import time

# Define the dimensions of the game board
WIDTH = 40
HEIGHT = 20

# Define the symbols used in the game
SNAKE_HEAD = 'O'
SNAKE_BODY = 'o'
FOOD = '*'
WALL = '#'
EMPTY = ' '

# Define the initial position and direction of the snake
INITIAL_SNAKE_POSITION = [(WIDTH // 2, HEIGHT // 2)]
INITIAL_DIRECTION = (1, 0)

# Define the function to display the game board
def display_board(snake_positions, food_position):
    os.system('cls')
    board = [[EMPTY] * WIDTH for _ in range(HEIGHT)]
    for x, y in snake_positions:
        board[y][x] = SNAKE_BODY
    head_x, head_y = snake_positions[0]
    board[head_y][head_x] = SNAKE_HEAD
    food_x, food_y = food_position
    board[food_y][food_x] = FOOD
    for row in board:
        print(''.join(row))

# Define the function to move the snake
def move_snake(snake_positions, direction):
    head_x, head_y = snake_positions[0]
    delta_x, delta_y = direction
    new_head = (head_x + delta_x, head_y + delta_y)
    snake_positions.insert(0, new_head)
    snake_positions.pop()

# Define the function to generate a new food position
def generate_food(snake_positions):
    while True:
        food_x = random.randint(0, WIDTH - 1)
        food_y = random.randint(0, HEIGHT - 1)
        if (food_x, food_y) not in snake_positions:
            return (food_x, food_y)

# Define the main function to run the game
def play_game():
    snake_positions = INITIAL_SNAKE_POSITION.copy()
    direction = INITIAL_DIRECTION
    food_position = generate_food(snake_positions)
    while True:
        display_board(snake_positions, food_position)
        move_snake(snake_positions, direction)
        if snake_positions[0] == food_position:
            food_position = generate_food(snake_positions)
        head_x, head_y = snake_positions[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            print('Game over! You hit the wall.')
            return
        if len(set(snake_positions)) != len(snake_positions):
            print('Game over! You ran into yourself.')
            return
        time.sleep(0.1)

# Run the game
play_game()
