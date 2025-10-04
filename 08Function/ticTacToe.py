import json
import os

FILENAME = 'TicTacToe.json'

if os.path.exists(FILENAME):
    with open(FILENAME, 'r', encoding="utf-8") as f:
        TicTacToe = json.load(f)

# 0.0 0.1 0.2
# 1.0 1.1 1.2
# 2.0 2.1 2.2


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
        ]

currentPlayer = 1
winner = None
moveCount = 0

def printBoard():
    print('\nПоточний статус:')
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print('-' * 13)
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print('-' * 13)
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print()

while True:
    row, col = None, None
    printBoard()

    validMode = False
    while not validMode:
        moveInput = input(f'Гравець {currentPlayer} (рядок.стовпчик): ')
        parts = moveInput.split(".")
        row = int(parts[0])
        col = int(parts[1])

        # перевірка на помилку
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Неправильна позиція")
            continue

        if board[row][col] != ' ':
            print('Клітинка зайнята')
        validMode = True

    moveCount += 1

    if currentPlayer == 1:
        board[row][col] = 'X'
    else:
        board[row][col] = 'O'

    # перевіряємо усі рядки
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][1] != ' ':
            winner = currentPlayer
            break

    # перевіряємо усі стовпчики
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            winner = currentPlayer
            break

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = currentPlayer
        break

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = currentPlayer
        break

    if moveCount >= 9 and winner is None:
        winner = 0 #Нічия
        break

    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1



    printBoard()

print('='*20)
if winner:
    print(f"Гравець {currentPlayer} переміг")
    with open('boardJson', 'w', encoding="utf-8") as f:
        json.dump(board, f, ensure_ascii=False, indent=4)
else:
    print('Нічия')
    with open('boardJson', 'w', encoding="utf-8") as f:
        json.dump(board, f, ensure_ascii=False, indent=4)










