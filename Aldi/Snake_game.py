import random
import msvcrt
import os
import time

# Fungsi untuk mendapatkan input tanpa perlu menekan tombol Enter
def get_key():
    return msvcrt.getch()

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inisialisasi variabel-variabel permainan
sh, sw = 20, 60
snk_x = sw // 4
snk_y = sh // 2
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
food = [sh // 2, sw // 2]
score = 0

# Fungsi untuk menggambar papan permainan
def draw_board():
    clear_screen()
    for i in range(sh):
        for j in range(sw):
            if i == 0 or i == sh - 1 or j == 0 or j == sw - 1:
                print("#", end="")
            elif [i, j] in snake:
                print("*", end="")
            elif [i, j] == food:
                print("@", end="")
            else:
                print(" ", end="")
        print()

# Fungsi untuk menggerakkan ular
def move_snake(direction):
    head = list(snake[0])
    if direction == "UP":
        head[0] -= 1
    elif direction == "DOWN":
        head[0] += 1
    elif direction == "LEFT":
        head[1] -= 1
    elif direction == "RIGHT":
        head[1] += 1
    return head

# Fungsi untuk memeriksa apakah ular menabrak dinding atau dirinya sendiri
def check_collision():
    if snake[0][0] in [0, sh - 1] or snake[0][1] in [0, sw - 1] or snake[0] in snake[1:]:
        return True
    return False

# Fungsi untuk memperbarui posisi makanan
def update_food():
    global food
    food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]

# Fungsi utama permainan
def main():
    global score
    direction = "RIGHT"
    while True:
        draw_board()
        key = get_key()
        if key == b"w":
            direction = "UP"
        elif key == b"s":
            direction = "DOWN"
        elif key == b"a":
            direction = "LEFT"
        elif key == b"d":
            direction = "RIGHT"
        new_head = move_snake(direction)
        snake.insert(0, new_head)
        if snake[0] == food:
            score += 1
            update_food()
        else:
            snake.pop()
        if check_collision():
            print("Game Over! Score:", score)
            break
        time.sleep(0.1)

# Jalankan permainan
if __name__ == "__main__":
    main()
