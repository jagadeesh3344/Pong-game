import tkinter as tk
from GameBoard import PongGame

def show_end_game_message(winner_name):
    end_game_win = tk.Toplevel()
    end_game_win.title("Final Result")
    end_game_win.geometry("500x250")
    end_game_win.resizable(width=False, height=False)
    end_game_win.configure(bg="black")
    print(winner_name)

    if winner_name == "player":
        message = f"Congratulations, {winner_name}!"
    else:
        message = "Game Over"

    end_label = tk.Label(end_game_win, text=message, fg="yellow", bg="black", font=("Arial", 16))
    end_label.pack(pady=20)

    play_again_button = tk.Button(end_game_win, text="Play Again", command=main_window)
    play_again_button.pack(pady=5)

    exit_button = tk.Button(end_game_win, text="Exit", command=exit_all_windows)
    exit_button.pack(pady=5)
    
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
    global final_score
    final_score = int(final_score_entry.get()) 

    if invalid:
        invalid = False

    welcome_win.destroy()
    show_end_game_message(PongGame().run(final_score))

def Alert(): # Invalid input
     global alert
     alert = tk.Label(welcome_win, text="Enter a valid input")
     alert.pack()

     global invalid
     invalid = True
     

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

