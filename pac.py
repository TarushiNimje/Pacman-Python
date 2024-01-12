import tkinter as tk
import random

# Constants
GRID_WIDTH = 20
GRID_HEIGHT = 20
CELL_SIZE = 30
PACMAN_SPEED = 1
GHOST_SPEED = 1
time_limit = 180  # 3 minutes


# Initialize tkinter
root = tk.Tk()
root.title("Pac-Man")

# Create a canvas to draw the game
canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE, bg="black")
canvas.pack()

# Define the maze as a grid (0 = empty, 1 = wall, 2 = dot, 3 = fruit, 4 = fruit/power-up)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 4, 2, 2, 1],
    [1, 2, 3, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 2, 2, 2, 2, 1, 2, 2, 3, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
    [1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1],
    [1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 4, 2, 1],
    [1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 3, 2, 2, 1, 1, 2, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Define Pac-Man's initial position
pacman_x = 1
pacman_y = 1
score = 0
high_score = 100

# Define the initial position of a ghost
ghost_x = random.randint(0, GRID_WIDTH - 1)
ghost_y = random.randint(0, GRID_HEIGHT - 1)

# Function for drawing the maze
def draw_maze():
    canvas.delete("maze")
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if maze[y][x] == 1:
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill="blue", tags="maze")
            elif maze[y][x] == 2:
                canvas.create_oval(x * CELL_SIZE + 10, y * CELL_SIZE + 10, (x + 1) * CELL_SIZE - 10, (y + 1) * CELL_SIZE - 10, fill="white", tags="maze")
            elif maze[y][x] == 3:
                canvas.create_oval(x * CELL_SIZE + 5, y * CELL_SIZE + 5, (x + 1) * CELL_SIZE - 5, (y + 1) * CELL_SIZE - 5, fill="orange", tags="maze")
            elif maze[y][x] == 4:
                canvas.create_oval(x * CELL_SIZE + 5, y * CELL_SIZE + 5, (x + 1) * CELL_SIZE - 5, (y + 1) * CELL_SIZE - 5, fill="green", tags="maze")

# Function for moving Pac-Man
def move_pacman(event):
    global pacman_x, pacman_y, score, high_score
    key = event.keysym
    new_x, new_y = pacman_x, pacman_y
    if key == "Up":
        new_y -= PACMAN_SPEED
    elif key == "Down":
        new_y += PACMAN_SPEED
    elif key == "Left":
        new_x -= PACMAN_SPEED
    elif key == "Right":
        new_x += PACMAN_SPEED

    # Check for collisions with walls
    if maze[new_y][new_x] != 1:
        pacman_x, pacman_y = new_x, new_y

    # Check for collisions with dots
    if maze[pacman_y][pacman_x] == 2:
        maze[pacman_y][pacman_x] = 0  # Remove the dot
        score += 10  # Increase the score
        canvas.delete("maze")  # Redraw the maze without the eaten dot
        draw_maze()
    elif maze[pacman_y][pacman_x] == 4:
        maze[pacman_y][pacman_x] = 0  # Remove the fruit/power-up
        score += 50  # Increase the score (adjust as needed)
        canvas.delete("maze")  # Redraw the maze without the collected item
        draw_maze()

    # Check for collisions with fruits
    if maze[pacman_y][pacman_x] == 3:
        maze[pacman_y][pacman_x] = 0  # Remove the fruit
        score += 50  # Increase the score
        canvas.delete("maze")  # Redraw the maze without the eaten fruit
        draw_maze()

    # Update the high score if the current score is higher
    if score > high_score:
        high_score = score

    canvas.delete("score")
    canvas.create_text(20, 20, text=f"Score: {score}", anchor="nw", fill="white", font=("Arial", 16), tags="score")
    canvas.create_text(20, 50, text=f"High Score: {high_score}", anchor="nw", fill="white", font=("Arial", 16), tags="score")
    draw_pacman()

# Function for drawing Pac-Man
def draw_pacman():
    canvas.delete("pacman")
    x0 = pacman_x * CELL_SIZE
    y0 = pacman_y * CELL_SIZE
    x1 = x0 + CELL_SIZE
    y1 = y0 + CELL_SIZE
    canvas.create_arc(x0, y0, x1, y1, start=30, extent=300, fill="yellow", outline="yellow", tags="pacman")

# Function for moving the ghost
def move_ghost():
    global ghost_x, ghost_y
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    dx, dy = random.choice(moves)
    new_x = ghost_x + dx
    new_y = ghost_y + dy
    if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
        ghost_x = new_x
        ghost_y = new_y

    # Check for collisions with Pac-Man
    if pacman_x == ghost_x and pacman_y == ghost_y:
        game_over()

    draw_ghost()
    root.after(250, move_ghost)  # Move the ghost every second

# Function for drawing the ghost
def draw_ghost():
    canvas.delete("ghost")
    x0 = ghost_x * CELL_SIZE
    y0 = ghost_y * CELL_SIZE
    x1 = x0 + CELL_SIZE
    y1 = y0 + CELL_SIZE
    canvas.create_oval(x0, y0, x1, y1, fill="red", outline="red", tags="ghost")

# Function for ending the game
# Function for ending the game
def game_over(message="Game Over"):
    canvas.create_text(GRID_WIDTH * CELL_SIZE // 2, GRID_HEIGHT * CELL_SIZE // 2, text=message, fill="red", font=("Arial", 24))
    canvas.update_idletasks()
    root.after(2000, root.destroy)  # Close the game window after 2 seconds

# Check for collisions with Pac-Man
if pacman_x == ghost_x and pacman_y == ghost_y:
    game_over("You were caught by a ghost! Game Over")  # Display a custom message


def update_timer():
    global time_limit
    canvas.delete("timer")
    if time_limit > 0:
        canvas.create_text(GRID_WIDTH * CELL_SIZE - 20, 20, text=f"Time Left: {time_limit} s", anchor="ne", fill="white", font=("Arial", 16), tags="timer")
        time_limit -= 1
        root.after(1000, update_timer)  # Update the timer every 1 second
    else:
        game_over()  # Call the game_over function when the time runs out

# Bind arrow key events to move Pac-Man
root.bind("<Up>", move_pacman)
root.bind("<Down>", move_pacman)
root.bind("<Left>", move_pacman)
root.bind("<Right>", move_pacman)

# Draw the initial maze and Pac-Man
# Draw the initial maze and Pac-Man
draw_maze()
draw_pacman()
move_ghost()

# Start the timer
update_timer()


root.mainloop()
