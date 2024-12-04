from tkinter import *
from PIL import Image, ImageTk  # For handling images
import random

# Functions
def composeProblem(difficulty_level):
    first_int = randomInt(difficulty_level)
    second_int = randomInt(difficulty_level)
    operation = decideOperation()
    return (first_int, operation, second_int)

def randomInt(difficulty_level):
    if difficulty_level == '1':
        return random.randint(-9, 9)
    elif difficulty_level == '2':
        return random.randint(-99, 99)
    elif difficulty_level == '3':
        return random.randint(-999, 999)

def decideOperation():
    return '+' if random.randint(0, 1) == 0 else '-'

def isCorrect(quiz, answer):
    first, operation, second = quiz
    correct_answer = first + second if operation == '+' else first - second
    return int(answer) == correct_answer

# Global variables
attempts_left = 2
current_quiz = None
difficulty_level = '1'
questions_asked = 0
correct_answers = 0

# Function to handle the Submit button click
def submit_answer():
    global attempts_left, current_quiz, questions_asked, correct_answers

    user_answer = answer_entry.get()  # Get user's input
    if not user_answer.isdigit() and not (user_answer.startswith('-') and user_answer[1:].isdigit()):
        feedback_label.config(text="Please enter a valid number.", fg="red")
        return

    if isCorrect(current_quiz, user_answer):
        feedback_label.config(text="Correct! Well done.", fg="green")
        correct_answers += 1
        load_next_question()
    else:
        attempts_left -= 1
        if attempts_left > 0:
            feedback_label.config(text=f"Incorrect. Try again. Attempts left: {attempts_left}", fg="orange")
        else:
            feedback_label.config(text="Incorrect. Moving to next question.", fg="red")
            load_next_question()

# Function to load the next question
def load_next_question():
    global attempts_left, current_quiz, questions_asked

    # Increment questions asked
    questions_asked += 1

    # Check if quiz is over (10 questions)
    if questions_asked > 10:
        show_score()
        return

    attempts_left = 2  # Reset attempts for the new question
    current_quiz = composeProblem(difficulty_level)
    question_label.config(text=f"{current_quiz[0]} {current_quiz[1]} {current_quiz[2]}")
    feedback_label.config(text="")  # Clear feedback
    answer_entry.delete(0, END)  # Clear answer input

# Function to display the score
def show_score():
    for widget in window.winfo_children():
        widget.destroy()  # Clears the window

    # Final Score Display
    score_frame = Frame(window, bg="#eac8ce")
    score_frame.place(relwidth=1, relheight=1)

    Label(
        score_frame,
        text=f"Quiz Over! You scored {correct_answers} out of 10.",
        font=('Bungee', 14),
        bg="#eac8ce",
        fg="#000000"
    ).pack(pady=50)

    # Displaing a final image 
    img_score = Image.open("MathQuiz\Images\score.jpg")  
    resized_image_score = img_score.resize((600, 400))
    final_image = ImageTk.PhotoImage(resized_image_score)

    Label(score_frame, image=final_image, bg="#eac8ce").pack(pady=20)

    # Exit Button
    Exit_button=Button(
        score_frame,
        text="Exit",
        command=window.quit,  # This closes the application
        font=('Bungee', 12),
        bg="#fdccd3",
        fg="black",
        borderwidth=0,
        activebackground="#fdccd3",
    )
    Exit_button.place(x=265, y=217)

    # to Prevent the image from being garbage-collected
    score_frame.image = final_image

# Tkinter Setup
window = Tk()
window.title("Math Quiz")
window.geometry("600x400")
window.resizable(False, False)

# Frames
main_page = Frame(window)
main_page.place(relwidth=1, relheight=1)

Levels_frame = Frame(window)
Instructions_frame = Frame(window)
Questions_frame = Frame(window)

# Main Page
img_main = Image.open("MathQuiz/images/1.jpg")  
resized_image_main = img_main.resize((600, 400))
new_image_main = ImageTk.PhotoImage(resized_image_main)

Label(main_page, image=new_image_main).pack()

start_button = Button(
    main_page,
    text="Start",
    font=('Bungee', 12),
    fg="black",
    bg="#ffffff",
    borderwidth=0,
    activebackground="#ffffff",
    command=lambda: show_frame(Levels_frame)
)
start_button.place(x=265, y=217)

# Levels Page
img_levels = Image.open("MathQuiz/images/2.jpg")
resized_image_levels = img_levels.resize((600, 400))
new_image_levels = ImageTk.PhotoImage(resized_image_levels)

Label(Levels_frame, image=new_image_levels).pack()

def set_difficulty(level):
    global difficulty_level
    difficulty_level = level
    show_frame(Instructions_frame)

easy_button = Button(Levels_frame, text="Easy", command=lambda: set_difficulty('1'), font=('Bungee', 6), bg="#eacdd2",borderwidth=0, activebackground="#eacdd2")
easy_button.place(x=50, y=150)
moderate_button = Button(Levels_frame, text="Moderate", command=lambda: set_difficulty('2'), font=('Bungee', 6), bg="#eacdd2",borderwidth=0, activebackground="#eacdd2")
moderate_button.place(x=50, y=190)
advanced_button = Button(Levels_frame, text="Advanced", command=lambda: set_difficulty('3'), font=('Bungee', 6), bg="#eacdd2",borderwidth=0, activebackground="#eacdd2")
advanced_button.place(x=50, y=230)

# Instructions Page
img_instruction = Image.open("MathQuiz/images/instructions.jpg")  # Replace with your instruction image
resized_image_instruction = img_instruction.resize((600, 400))  # Resize as needed
new_instruction_image = ImageTk.PhotoImage(resized_image_instruction)

Label(Instructions_frame, image=new_instruction_image).pack()

start_quiz_button = Button(
    Instructions_frame,
    text="Start Quiz",
    font=('Bungee', 12),
    bg="#ffffff",
    fg="#eacdd2",
    activebackground="white",
    borderwidth=0,
    command=lambda: [show_frame(Questions_frame), load_next_question()]
)
start_quiz_button.place(x=240, y=290)

# Questions Page
img_questions = Image.open("MathQuiz/images/4.jpg")
resized_image_questions = img_questions.resize((600, 400))
new_image_questions = ImageTk.PhotoImage(resized_image_questions)

Label(Questions_frame, image=new_image_questions).pack()

question_label = Label(Questions_frame, text="", font=('Bungee', 12), bg="#eac8ce", fg="#000000")
question_label.place(x=50, y=120)

answer_entry = Entry(Questions_frame, font=('Bungee', 10), bg="#f0f0f0", fg="#000000")
answer_entry.place(x=50, y=170, width=200)

feedback_label = Label(Questions_frame, text="", font=('Bungee', 10), bg="#eac8ce", fg="#000000")
feedback_label.place(x=50, y=220)

submit_button = Button(
    Questions_frame,
    text="Submit",
    command=submit_answer,
    font=('Bungee', 5),
    bg="#f9cbd6",
    activebackground="#f9cbd6",
    borderwidth=0,
)
submit_button.place(x=283, y=335)

# Frame Navigation
def show_frame(frame):
    main_page.place_forget()
    Levels_frame.place_forget()
    Instructions_frame.place_forget()
    Questions_frame.place_forget()
    frame.place(relwidth=1, relheight=1)

# Start App
window.mainloop()
