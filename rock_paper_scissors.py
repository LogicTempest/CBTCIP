from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint
from tkinter import messagebox
from PIL import Image, ImageTk

root =  Tk()

#working with images
rock_original = Image.open("rock.png").resize((100,100)).rotate(90)
scissors_original = Image.open("scissors.png").resize((100,100)).rotate(90)
paper_original = Image.open("paper.png").resize((100,100))

rock_computer = rock_original.transpose(Image.FLIP_LEFT_RIGHT)
scissors_computer = scissors_original.transpose(Image.FLIP_LEFT_RIGHT)
paper_computer = paper_original.transpose(Image.FLIP_LEFT_RIGHT)

rock_images = (rock_original, rock_computer)
scissors_images = (scissors_original, scissors_computer)
paper_images = (paper_original, paper_computer)

rock_image = ImageTk.PhotoImage(rock_original)
scissors_image = ImageTk.PhotoImage(scissors_original)
paper_image = ImageTk.PhotoImage(paper_original)

rock_image2 = ImageTk.PhotoImage(rock_computer)
scissors_image2 = ImageTk.PhotoImage(scissors_computer)
paper_image2 = ImageTk.PhotoImage(paper_computer)

choice_images = ({"rock": rock_image, "scissors": scissors_image, "paper": paper_image}, {"rock": rock_image2, "scissors": scissors_image2, "paper": paper_image2})

def image_selector(i, choice):
    if choice == "rock":
        return rock_images[i]
    elif choice == "paper":
        return paper_images[i]
    elif choice == "scissors":
        return scissors_images[i]
    
def choice_handler(choice):
    choices = ["rock", "paper", "scissors"]
    i = randint(0,2)
    computer_choice = choices[i]
    player_image = choice_images[0][choice]
    computer_image = choice_images[1][computer_choice]
    pscore = int(player_score.get())
    cscore = int(computer_score.get())
    if choice == computer_choice:
        result.configure(text = "It's a tie")
        cscore += 1
        pscore += 1
    elif choice == "rock":
        if computer_choice == "scissors":
            result.configure(text = "Rock crushes Scissors\nYou win!!")
            pscore+= 1
        elif computer_choice == "paper":
            result.configure(text = "Paper covers Rock\nComputer wins!!")
            cscore += 1
    elif choice == "paper":
        if computer_choice == "rock":
            result.configure(text="Paper covers Rock\nYou win!!")
            pscore += 1
        elif computer_choice == "scissors":
            result.configure(text = "Scissors cut Paper\nComputer wins!!")
            cscore += 1
    elif choice == "scissors":
        if computer_choice == "paper":
            result.configure(text="Scissors cut Paper\nYou win!!")
            pscore += 1
        elif computer_choice == "rock":
            result.configure(text="Rock crushes Scissors\nComputer wins!!")
            cscore += 1

    if pscore > int(player_score.get()) and cscore > int(computer_score.get()):
        result.configure(background="#ede021")
    elif pscore > int(player_score.get()):
        result.configure(background="#97f79c")
    else:
        result.configure(background="#f57d93")
    
    computer_image_label.configure(image = computer_image) 
    player_image_label.configure(image = player_image)

    computer_score.set(str(cscore))
    player_score.set(str(pscore))


score_frame = Frame(root)
score_frame.grid(row=0,column=0)
game_frame = Frame(root)
game_frame.grid(row=1,column=0)
choice_frame = Frame(root)
choice_frame.grid(row=2, column=0)
computer_score = StringVar()
player_score = StringVar()
computer_score.set("0")
player_score.set("0")

#score_frame
score_label_computer = Label(score_frame, textvariable=computer_score, background="#edad74")
score_label_computer.grid(row=0, column=1, sticky=E, padx=4)

score_label_player = Label(score_frame, textvariable=player_score, background="#75caff")
score_label_player.grid(row=0, column=2, sticky=W, padx=4)


#game_frame
Label(game_frame, text="Computer Chooses:", anchor="w", background="#edad74").grid(row=2, column=1, sticky=W, padx=10, pady=10)
Label(game_frame, text="Player Chooses:", background="#75caff").grid(row=2, column=4, sticky=E, padx=10, pady=10)
Label(game_frame, text="Result:").grid(row=2, column=2, columnspan=2)

result = Label(game_frame, width=30, height=2)
result.grid(row=3, column=3)




canvas_computer = Canvas(game_frame, width=100, height=100)
canvas_computer.grid(row=3, column=1)

canvas_player = Canvas(game_frame, width=100, height=100)
canvas_player.grid(row=3, column=4)

computer_image_label = Label(canvas_computer)
computer_image_label.grid()

player_image_label = Label(canvas_player)
player_image_label.grid()



#choice frame
Label(choice_frame, text = "Please select your choice:").grid(row=0, column=0, columnspan=3)


rock_button = Button(choice_frame, width= 15, text="Rock", command=lambda:choice_handler("rock"))
rock_button.grid(row=1, column=1)

paper_button = Button(choice_frame, width= 15, text="Paper", command=lambda:choice_handler("paper"))
paper_button.grid(row=1, column=2)

scissors_button = Button(choice_frame, width=15, text="Scissors", command=lambda:choice_handler("scissors"))
scissors_button.grid(row=1, column=3)

root.mainloop()