import tkinter
import customtkinter
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

def draw():
    global player_score
    global enemy_score
    win_label.configure(text=" ")
    randint = random.randint(0, len(cards) - 1)
    player_cards.append(cards[randint])
    player_score += int(cards[randint])

    if enemy_score <= 16:
        randint = random.randint(0, len(cards) - 1)
        enemy_cards.append(cards[randint])
        enemy_score += int(cards[randint])

    if player_score > 21 or enemy_score > 21:
        end_game()

    player_score_text = "Your score: " + str(player_score)
    enemy_score_text = "Enemy score: " + str(enemy_score)

    player_card_label.configure(text=player_score_text)
    enemy_card_label.configure(text=enemy_score_text)

def end_game():
    global player_score
    global enemy_score
    global player_cards
    global enemy_cards

    if player_score > 21:
        win_label.configure(text="You Lose!")
    elif player_score < enemy_score:
        win_label.configure(text="You Lose!")
    elif enemy_score > 21:
        win_label.configure(text="You Win!")
    elif player_score > enemy_score:
        win_label.configure(text="You Win!")
    else:
        win_label.configure(text="Tie!")

    player_score = 0
    enemy_score = 0
    player_cards = []
    enemy_cards = []



if __name__ == '__main__':
    player_score = 0
    player_cards = []
    enemy_score = 0
    enemy_cards = []

    root_tk = customtkinter.CTk()
    root_tk.geometry("400x300")
    root_tk.title("Blackjack")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    draw_button = customtkinter.CTkButton(master=root_tk, text="Draw Card", command=draw)
    draw_button.place(relx=0.3, rely=0.8, anchor=tkinter.CENTER)

    stand_button = customtkinter.CTkButton(master=root_tk, text="Stand", command=end_game)
    stand_button.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)

    player_card_label = customtkinter.CTkLabel(master=root_tk, text="Blank")
    player_card_label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    enemy_card_label = customtkinter.CTkLabel(master=root_tk, text="Blank")
    enemy_card_label.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

    win_label = customtkinter.CTkLabel(master=root_tk, text=" ")
    win_label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    root_tk.mainloop()
