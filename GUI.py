import tkinter as tk

def show_end_game_message(winner_name):
    end_game_win = tk.Toplevel()
    end_game_win.title("Final Result")
    end_game_win.geometry("500x250")
    end_game_win.resizable(width=False, height=False)
    end_game_win.configure(bg="black")

    if winner_name == "Player":
        message = f"Congratulations, {winner_name}!"
    else:
        message = "Game Over"

    end_label = tk.Label(end_game_win, text=message, fg="yellow", bg="black", font=("Arial", 16))
    end_label.pack(pady=20)

    play_again_button = tk.Button(end_game_win, text="Play Again", command=main_window)
    play_again_button.pack(pady=5)

    exit_button = tk.Button(end_game_win, text="Exit", command=exit_all_windows)
    exit_button.pack(pady=5)

def show_main_window(final_score):
    # Function to show the main window with the provided final score
    win = tk.Toplevel()
    win.title("Pong Game")
    win.geometry("1200x700")
    win.resizable(width=False, height=False)
    mycolor = '#48C9B0'
    win.configure(bg=mycolor)

    # Label for Player
    player_label = tk.Label(win, text="Player", fg="yellow", bg="black", width=30, height=3 , font=("Arial", 12))
    player_label.place(x=200, y=30)

    # Score label for Player
    player_label = tk.Label(win, text=f"Score : 0", fg="yellow", bg="#4A235A", width=13, height=3 , font=("Arial", 10))
    player_label.place(x=280, y=100)

    # Label for Computer
    computer_label = tk.Label(win, text="Computer", fg="yellow", bg="black", width=30, height=3 , font=("Arial", 12))
    computer_label.place(x=800, y=30)

    # Score label for Computer
    computer_score_label = tk.Label(win, text="Score: 0", fg="yellow", bg="#4A235A", width=13, height=3 , font=("Arial", 10))
    computer_score_label.place(x=890, y=100)

    # Create left paddle
    left_paddle = tk.Canvas(win, width=10, height=100, bg="blue", highlightthickness=0)
    left_paddle.place(x=20, y=300)

    # Create right paddle
    right_paddle = tk.Canvas(win, width=10, height=100, bg="blue", highlightthickness=0)
    right_paddle.place(x=1170, y=300)

    # Create ball
    ball = tk.Canvas(win, width=20, height=20, bg="white", highlightthickness=0)
    ball.create_oval(0, 0, 20, 20, fill="white")  # to make the ball circle with border
    ball.place(x=610, y=330)

    # Simulate end of the game
    # Here we assume the player wins for demonstration purposes
    show_end_game_message("Player")

invalid = False # boolean for invalid input


def get_final_score():

    global invalid

    for ch in final_score_entry.get():
        if ord(ch)<48 or ord(ch)>57: # check char's ascii code
            if not invalid:
                Alert()
            return
        
    if final_score_entry.get()=='' or not int(final_score_entry.get()):  # empty string or equal 0
        if not invalid:
                Alert()
        return
    
    final_score = int(final_score_entry.get()) 

    if invalid:
        alert.destroy()
        invalid = 0

    welcome_win.destroy()
    show_main_window(final_score)

def Alert(): # Invalid input
     global alert
     alert = tk.Label(welcome_win, text="Enter a valid input")
     alert.pack()

     global invalid
     invalid = 1
     

def main_window():
     exit_all_windows()
     main()

    
def exit_all_windows():
    for window in start_window.winfo_children():
        window.destroy()
    start_window.destroy()

# Create a tkinter window

def main():
   global start_window
   start_window = tk.Tk()
   start_window.withdraw() 

   global welcome_win
   welcome_win = tk.Tk()
   welcome_win.title("Welcome to Pong Game")
   welcome_win.geometry("500x250")
   welcome_win.resizable(width=False, height=False)
   welcome_win.configure(bg="black")

   # Welcoming message
   welcome_label = tk.Label(welcome_win, text="Welcome to Pong Game!", fg="yellow", bg="black", font=("Arial", 18))
   welcome_label.pack(pady=20)

   # Prompt for final score
   final_score_label = tk.Label(welcome_win, text="Enter the final score:", fg="yellow", bg="black", font=("Arial", 14))
   final_score_label.pack()

   # Entry for final score
   global final_score_entry
   final_score_entry = tk.Entry(welcome_win, font=("Arial", 14))
   final_score_entry.pack(pady=10)

   # Next button
   next_button = tk.Button(welcome_win, text="Next", command=get_final_score)
   next_button.pack(pady=10)


   start_window.mainloop()

main()
