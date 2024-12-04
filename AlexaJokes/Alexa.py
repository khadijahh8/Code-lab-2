from tkinter import *
from PIL import Image, ImageTk  
import random

# Function to read jokes from the text file
def read_jokes():
    with open('AlexaJokes\jokes.txt', 'r') as file:
        setup_list = []
        punchline_list = []
        for line in file:
            setup, punchline = line.strip()[2:].split('?')
            setup += "?"
            setup_list.append(setup)
            punchline_list.append(punchline)
    return setup_list, punchline_list

# Load jokes into memory
setup_list, punchline_list = read_jokes()

# Function to get a random joke
def get_random_joke():
    random_choice = random.randint(0, len(setup_list) - 1)
    setup = setup_list[random_choice]
    punchline = punchline_list[random_choice]
    return setup, punchline

# Create a Tkinter window
window = Tk()
window.title("Alexa's Jokes")
window.geometry("382x683")

# Function to switch to the Jokes frame and display a joke
def show_Jokes_frame():
    main_page.place_forget()  # Hide the main_page frame
    Jokes_frame.place(relwidth=1, relheight=1)  # Show the Jokes_frame
    display_joke()  # Show the first joke

# Function to display a joke in the Jokes_frame
def display_joke():
    setup, punchline = get_random_joke()
    joke_label.config(text=setup)  # Update the setup text
    punchline_label.config(text="")  # Clear the punchline initially
    punchline_button.config(command=lambda: reveal_punchline(punchline))  # Update the button to reveal punchline

# Function to reveal the punchline
def reveal_punchline(punchline):
    punchline_label.config(text=punchline)  # Show the punchline

# Main Page Frame
main_page = Frame(window)
main_page.place(relwidth=1, relheight=1)

# Load and resize the image for the main page
img_main = Image.open("AlexaJokes\Images\Frame1.jpg")
resized_image_main = img_main.resize((382, 683))
new_image_main = ImageTk.PhotoImage(resized_image_main)

# Display the image in a Label on the main page
Label(main_page, image=new_image_main).pack()

# Create an Entry widget for user input
input_entry = Entry(
    main_page,
    font=('Bungee', 10),
    fg="Black",
    bg="#D9D9D9",
    bd=1,
    justify="center"
)
input_entry.place(x=52, y=240, width=300, height=50)
input_entry.insert(0, "Type here")  # Placeholder text

# Create and place the Start button
start_button = Button(
    main_page,
    text="Start",
    compound="center",
    font=('Bungee', 8),
    fg="black",
    bg="#F0CFFE",
    borderwidth=0,
    activebackground="#F0CFFE",
    command=show_Jokes_frame  # Bind the button to the function
)
start_button.place(x=148, y=390)

# Jokes Page Frame
Jokes_frame = Frame(window)

# Load and resize the image for the Jokes page
img_Jokes = Image.open("AlexaJokes\Images\Frame2.jpg")
resized_image_Jokes = img_Jokes.resize((382, 683))
new_image_Jokes = ImageTk.PhotoImage(resized_image_Jokes)

# Display the image in a Label on the Jokes page
Label(Jokes_frame, image=new_image_Jokes).pack()

# Add a label for the joke setup
joke_label = Label(
    Jokes_frame,
    text="",
    font=('Bungee', 10),
    bg="#F0CFFE",
    wraplength=300,
    justify="center"
)
joke_label.place(x=40, y=150)

# Add a label for the punchline
punchline_label = Label(
    Jokes_frame,
    text="",
    font=('Bungee', 10),
    bg="#F0CFFE",
    wraplength=300,
    justify="center"
)
punchline_label.place(x=40, y=230)

# Add a button to reveal the punchline
punchline_button = Button(
    Jokes_frame,
    text="Reveal Punchline",
    font=('Bungee', 8),
    fg="white",
    bg="#43284E",
    borderwidth=0,
    activebackground="#43284E",
)
punchline_button.place(x=125, y=320)

# Add a button to get more jokes
More_button = Button(
    Jokes_frame,
    text="More Jokes",
    font=('Bungee', 8),
    fg="black",
    bg="#F0CFFE",
    borderwidth=0,
    activebackground="#F0CFFE",
    command=display_joke  # Bind to display_joke
)
More_button.place(x=145, y=415)

# Add a button to exit the app
Exit_button = Button(
    Jokes_frame,
    text="Exit",
    font=('Bungee', 8),
    fg="black",
    bg="#F0CFFE",
    borderwidth=0,
    activebackground="#F0CFFE",
    command=window.destroy  # Properly bind to close the application
)
Exit_button.place(x=180, y=485)

# Run the Tkinter main loop
window.mainloop()
