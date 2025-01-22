import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != '':
            buttons[combo[0]].config(bg='green')
            buttons[combo[1]].config(bg='green')
            buttons[combo[2]].config(bg='green')
            messagebox.showinfo('Tic-Tac-Toe', f'{buttons[combo[0]]["text"]} wins!')
            root.after(3000, show_restart_button)  # Wait 3 seconds and then show the restart button
            return True  # Game is over
    return False

def check_draw():
    # Check if the board is full and there is no winner
    if all(button['text'] != '' for button in buttons) and not winner:
        messagebox.showinfo('Tic-Tac-Toe', 'It\'s a Draw!')
        root.after(3000, show_restart_button)  # Wait 3 seconds and then show the restart button

def button_click(index):
    global winner
    if buttons[index]['text'] == '' and not winner:
        buttons[index]['text'] = current_player
        winner = check_winner()
        if not winner:
            check_draw()  # Check for draw after each move
            toggle_player()

def toggle_player():
    global current_player
    current_player = 'X' if current_player == 'O' else 'O'
    label.config(text=f'Player {current_player}\'s turn')

def restart_game():
    global current_player, winner
    # Reset the buttons and game state
    for button in buttons:
        button.config(text='', bg='SystemButtonFace')
    winner = False
    current_player = 'X'
    label.config(text=f'Player {current_player}\'s turn')
    restart_button.grid_forget()  # Hide the restart button until the next game

def show_restart_button():
    restart_button.grid(row=4, column=0, columnspan=3)  # Show the restart button after 3 seconds

root = tk.Tk()
root.title('Tic-Tac-Toe')

# Create the buttons for the Tic-Tac-Toe board
buttons = [tk.Button(root, text='', font=('normal', 25), width=6, height=2, command=lambda index=index: button_click(index)) for index in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Label to show the current player's turn
current_player = 'X'
winner = False
label = tk.Label(root, text=f'Player {current_player}\'s turn', font=('normal', 25))
label.grid(row=3, column=0, columnspan=3)

# Restart button (initially hidden)
restart_button = tk.Button(root, text="Restart Game", font=('normal', 20), command=restart_game)

root.mainloop()
print("End of the game")