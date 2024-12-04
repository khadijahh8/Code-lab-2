#importing libiraries 
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Tkinter
root = Tk()
root.title("Students Manager")
root.geometry("700x500")
root.resizable(False, False)

#difining the file so that it is easier to access
file_path = "Studentmanger/StudentsMarks.txt"

# Function to calculate the grade
def calculating_grade(overall_percentage):
    if overall_percentage >= 70:
        return "A"
    elif overall_percentage >= 60:
        return "B"
    elif overall_percentage >= 50:
        return "C"
    elif overall_percentage >= 40:
        return "D"
    else:
        return "F"

# Function to get student informations
def get_student_info(file_path):
    students = []
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]  # skiping the first line in the file
        for line in lines:
            try:
                parts = line.strip().split(",")
                if len(parts) < 6:
                    continue
                coursework_marks = list(map(int, parts[2:5]))
                exam_mark = int(parts[5])
                total_coursework = sum(coursework_marks)
                overall_percentage = ((total_coursework + exam_mark) / 160) * 100
                grade = calculating_grade(overall_percentage)

                students.append({
                    "name": parts[1],
                    "number": parts[0],
                    "coursework": coursework_marks,
                    "exam_mark": exam_mark,
                    "total_coursework": total_coursework,
                    "overall_percentage": overall_percentage,
                    "grade": grade
                })
                #for handeling expected index and value eroors
            except (ValueError, IndexError):
                continue
    return students

# Function to display all student records
def display_all_students():
    # the end method is from this website
    # https://stackoverflow.com/questions/27966626/how-to-clear-delete-the-contents-of-a-tkinter-text-widget
    text_box.delete("1.0", END)
    students = get_student_info(file_path)
    for student in students:
        text_box.insert(END, f"Student Name: {student['name']}\n")
        text_box.insert(END, f"Student Number: {student['number']}\n")
        text_box.insert(END, f"Course Marks: {student['coursework']}\n")
        text_box.insert(END, f"Exam Mark: {student['exam_mark']}\n")
        text_box.insert(END, f"Total Coursework Mark: {student['total_coursework']}\n")
        text_box.insert(END, f"Overall Percentage: {student['overall_percentage']:.2f}%\n")
        text_box.insert(END, f"Grade: {student['grade']}\n")
        text_box.insert(END, "-" * 40 + "\n")

# Function to display the student with the highest score
def display_highest_score():
    text_box.delete("1.0", END)
    students = get_student_info(file_path)
    highest_student = max(students, key=lambda x: x["overall_percentage"])
    text_box.insert(END, f"Highest Scorer:\n")
    text_box.insert(END, f"Student Name: {highest_student['name']}\n")
    text_box.insert(END, f"Student Number: {highest_student['number']}\n")
    text_box.insert(END, f"Overall Percentage: {highest_student['overall_percentage']:.2f}%\n")
    text_box.insert(END, f"Grade: {highest_student['grade']}\n")

# Function to display the student with the lowest score
def display_lowest_score():
    text_box.delete("1.0", END)
    students = get_student_info(file_path)
    lowest_student = min(students, key=lambda x: x["overall_percentage"])
    text_box.insert(END, f"Lowest Scorer:\n")
    text_box.insert(END, f"Student Name: {lowest_student['name']}\n")
    text_box.insert(END, f"Student Number: {lowest_student['number']}\n")
    text_box.insert(END, f"Overall Percentage: {lowest_student['overall_percentage']:.2f}%\n")
    text_box.insert(END, f"Grade: {lowest_student['grade']}\n")

# Function to display individual student record
def display_individual_record():
    text_box.delete("1.0", END)
    students = get_student_info(file_path)
    selected_name = dropdown.get()
    for student in students:
        if student["name"] == selected_name:
            text_box.insert(END, f"Student Name: {student['name']}\n")
            text_box.insert(END, f"Student Number: {student['number']}\n")
            text_box.insert(END, f"Course Marks: {student['coursework']}\n")
            text_box.insert(END, f"Exam Mark: {student['exam_mark']}\n")
            text_box.insert(END, f"Total Coursework Mark: {student['total_coursework']}\n")
            text_box.insert(END, f"Overall Percentage: {student['overall_percentage']:.2f}%\n")
            text_box.insert(END, f"Grade: {student['grade']}\n")
            break

# Background Image
try:
    img_main = Image.open("Studentmanger/Main.jpg")
    resized_image_score = img_main.resize((700, 500))
    final_image = ImageTk.PhotoImage(resized_image_score)
    label = Label(root, image=final_image)
    label.pack()
except FileNotFoundError:
    pass

# Text box to display results
text_box = Text(root, width=80, height=12, bg="#1e3f66", fg="white", font=("Arial", 10), wrap=WORD)
text_box.place(x=50, y=260)

# Buttons
AllStudents_Records = Button(
    root,
    text="View All Students Records",
    font=("Bungee", 7),
    bg="#a3f2ea",
    fg="#004aad",
    borderwidth=0,
    activebackground="#a3f2ea",
    command=display_all_students 
)
AllStudents_Records.place(x=55, y=112)

High_Score = Button(
    root,
    text="Show Highest Score",
    font=("Bungee", 7),
    bg="#a3f2ea",
    fg="#004aad",
    borderwidth=0,
    activebackground="#a3f2ea",
    command=display_highest_score
)
High_Score.place(x=290, y=112)

Lowest_Score = Button(
    root,
    text="Show Lowest Score",
    font=("Bungee", 7),
    bg="#a3f2ea",
    fg="#004aad",
    borderwidth=0,
    activebackground="#a3f2ea",
    command=display_lowest_score
)
Lowest_Score.place(x=505, y=112)


# Dropdown and View Record button
students = get_student_info(file_path)
names_list = [student["name"] for student in students]
dropdown = ttk.Combobox(root, values=names_list, state="readonly")
if names_list:
    dropdown.set(names_list[0])
dropdown.place(x=400, y=215)

View_record= Button(
    text="View Record",
    font=("Bungee", 6),
    bg="#a3f2ea",
    fg="#004aad",
    borderwidth=0,
    activebackground="#a3f2ea",
    command=display_individual_record
)
View_record.place(x=575, y=205)

# Run the application
root.mainloop()