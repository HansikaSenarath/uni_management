import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

# Function to connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='university_management'
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Functions for Student Table Operations
def fetch_student_data(student_id, entries):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT first_name, second_name, email, dob FROM student WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        if result:
            entries['first_name'].delete(0, tk.END)
            entries['first_name'].insert(0, result[0])
            entries['second_name'].delete(0, tk.END)
            entries['second_name'].insert(0, result[1])
            entries['email'].delete(0, tk.END)
            entries['email'].insert(0, result[2])
            entries['dob'].delete(0, tk.END)
            entries['dob'].insert(0, result[3])
        else:
            messagebox.showwarning("Fetch Error", "No student found with the provided ID.")
        cursor.close()
        connection.close()

def update_student_data(entries, student_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = """UPDATE student SET first_name = %s, second_name = %s, email = %s, dob = %s 
                   WHERE student_id = %s"""
        values = (entries['first_name'].get(), 
                  entries['second_name'].get(), 
                  entries['email'].get(), 
                  entries['dob'].get(), 
                  student_id)
        try:
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Update", "Student data updated successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

def delete_student_data(student_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM student WHERE student_id = %s"
        try:
            cursor.execute(query, (student_id,))
            connection.commit()
            messagebox.showinfo("Deletion", "Student data deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

def insert_student_data(entries):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = """INSERT INTO student (first_name, second_name, email, dob) 
                   VALUES (%s, %s, %s, %s)"""
        values = (entries['first_name'].get(), 
                  entries['second_name'].get(), 
                  entries['email'].get(), 
                  entries['dob'].get())
        try:
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Insert", "Student data inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

# Functions for Course Table Operations
def fetch_course_data(course_id, entries):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT course_name, course_code, credit, department FROM course WHERE course_id = %s"
        cursor.execute(query, (course_id,))
        result = cursor.fetchone()
        if result:
            entries['course_name'].delete(0, tk.END)
            entries['course_name'].insert(0, result[0])
            entries['course_code'].delete(0, tk.END)
            entries['course_code'].insert(0, result[1])
            entries['credit'].delete(0, tk.END)
            entries['credit'].insert(0, result[2])
            entries['department'].delete(0, tk.END)
            entries['department'].insert(0, result[3])
        else:
            messagebox.showwarning("Fetch Error", "No course found with the provided ID.")
        cursor.close()
        connection.close()

def update_course_data(entries, course_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = """UPDATE course SET course_name = %s, course_code = %s, credit = %s, department = %s
                   WHERE course_id = %s"""
        values = (entries['course_name'].get(), 
                  entries['course_code'].get(), 
                  entries['credit'].get(), 
                  entries['department'].get(), 
                  course_id)
        try:
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Update", "Course data updated successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

def delete_course_data(course_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM course WHERE course_id = %s"
        try:
            cursor.execute(query, (course_id,))
            connection.commit()
            messagebox.showinfo("Deletion", "Course data deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

def insert_course_data(entries):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = """INSERT INTO course (course_name, course_code, credit, department) 
                   VALUES (%s, %s, %s, %s)"""
        values = (entries['course_name'].get(), 
                  entries['course_code'].get(), 
                  entries['credit'].get(), 
                  entries['department'].get())
        try:
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Insert", "Course data inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

# Functions for Enrollment Table Operations
def fetch_enrollment_data(enrollment_id, entries):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT student_id, course_id FROM enrollment WHERE enrollment_id = %s"
        cursor.execute(query, (enrollment_id,))
        result = cursor.fetchone()
        if result:
            entries['student_id'].delete(0, tk.END)
            entries['student_id'].insert(0, result[0])
            entries['course_id'].delete(0, tk.END)
            entries['course_id'].insert(0, result[1])
        else:
            messagebox.showwarning("Fetch Error", "No enrollment found with the provided ID.")
        cursor.close()
        connection.close()

def update_enrollment_data(entries, enrollment_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = """UPDATE enrollment SET student_id = %s, course_id = %s 
                   WHERE enrollment_id = %s"""
        values = (entries['student_id'].get(), 
                  entries['course_id'].get(), 
                  enrollment_id)
        try:
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Update", "Enrollment data updated successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

def delete_enrollment_data(enrollment_id):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM enrollment WHERE enrollment_id = %s"
        try:
            cursor.execute(query, (enrollment_id,))
            connection.commit()
            messagebox.showinfo("Deletion", "Enrollment data deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

def insert_enrollment_data(entries):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = """INSERT INTO enrollment (student_id, course_id) 
                   VALUES (%s, %s)"""
        values = (entries['student_id'].get(), 
                  entries['course_id'].get())
        try:
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Insert", "Enrollment data inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

# Function to clear form fields
def clear_entries(entries):
    for entry in entries.values():
        entry.delete(0, tk.END)

# Function to handle form submission
def submit_form(entries, form_type, id_value=None):
    if form_type == "student":
        if id_value:
            update_student_data(entries, id_value)
        else:
            insert_student_data(entries)
    elif form_type == "course":
        if id_value:
            update_course_data(entries, id_value)
        else:
            insert_course_data(entries)
    elif form_type == "enrollment":
        if id_value:
            update_enrollment_data(entries, id_value)
        else:
            insert_enrollment_data(entries)

# Function to create and display the Student Form
def open_student_form():
    student_form = tk.Toplevel(root)
    student_form.title("Student Form")
    student_form.geometry("400x400")
    student_form.configure(bg="#f0f0f0")

    # Form Title
    title_label = tk.Label(student_form, text="Student Form", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
    title_label.pack(pady=10)

    # Form Fields
    fields = [("Student ID", "student_id"),
              ("First Name", "first_name"),
              ("Second Name", "second_name"),
              ("Email", "email"),
              ("Date of Birth", "dob")]

    entries = {}
    for field, var in fields:
        frame = tk.Frame(student_form, bg="#f0f0f0")
        frame.pack(pady=5, padx=10, fill="x")

        label = tk.Label(frame, text=field, font=("Helvetica", 12), bg="#f0f0f0")
        label.pack(side="left")

        entry = tk.Entry(frame, width=30)
        entry.pack(side="left")
        entries[var] = entry

    # Fetch, Submit, Delete, Clear Buttons
    fetch_button = ttk.Button(student_form, text="Fetch", command=lambda: fetch_student_data(entries['student_id'].get(), entries))
    fetch_button.pack(pady=5)

    submit_button = ttk.Button(student_form, text="Submit", command=lambda: submit_form(entries, "student", entries['student_id'].get()))
    submit_button.pack(pady=5)

    delete_button = ttk.Button(student_form, text="Delete", command=lambda: delete_student_data(entries['student_id'].get()))
    delete_button.pack(pady=5)

    clear_button = ttk.Button(student_form, text="Clear", command=lambda: clear_entries(entries))
    clear_button.pack(pady=5)

# Function to create and display the Course Form
def open_course_form():
    course_form = tk.Toplevel(root)
    course_form.title("Course Form")
    course_form.geometry("400x450")
    course_form.configure(bg="#f0f0f0")

    # Form Title
    title_label = tk.Label(course_form, text="Course Form", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
    title_label.pack(pady=10)

    # Form Fields
    fields = [("Course ID", "course_id"),
              ("Course Name", "course_name"),
              ("Course Code", "course_code"),
              ("Credit", "credit"),
              ("Department", "department")]

    entries = {}
    for field, var in fields:
        frame = tk.Frame(course_form, bg="#f0f0f0")
        frame.pack(pady=5, padx=10, fill="x")

        label = tk.Label(frame, text=field, font=("Helvetica", 12), bg="#f0f0f0")
        label.pack(side="left")

        entry = tk.Entry(frame, width=30)
        entry.pack(side="left")
        entries[var] = entry

    # Fetch, Submit, Delete, Clear Buttons
    fetch_button = ttk.Button(course_form, text="Fetch", command=lambda: fetch_course_data(entries['course_id'].get(), entries))
    fetch_button.pack(pady=5)

    submit_button = ttk.Button(course_form, text="Submit", command=lambda: submit_form(entries, "course", entries['course_id'].get()))
    submit_button.pack(pady=5)

    delete_button = ttk.Button(course_form, text="Delete", command=lambda: delete_course_data(entries['course_id'].get()))
    delete_button.pack(pady=5)

    clear_button = ttk.Button(course_form, text="Clear", command=lambda: clear_entries(entries))
    clear_button.pack(pady=5)

# Function to create and display the Enrollment Form
def open_enrollment_form():
    enrollment_form = tk.Toplevel(root)
    enrollment_form.title("Enrollment Form")
    enrollment_form.geometry("400x400")
    enrollment_form.configure(bg="#f0f0f0")

    # Form Title
    title_label = tk.Label(enrollment_form, text="Enrollment Form", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
    title_label.pack(pady=10)

    # Form Fields
    fields = [("Enrollment ID", "enrollment_id"),
              ("Student ID", "student_id"),
              ("Course ID", "course_id")]

    entries = {}
    for field, var in fields:
        frame = tk.Frame(enrollment_form, bg="#f0f0f0")
        frame.pack(pady=5, padx=10, fill="x")

        label = tk.Label(frame, text=field, font=("Helvetica", 12), bg="#f0f0f0")
        label.pack(side="left")

        entry = tk.Entry(frame, width=30)
        entry.pack(side="left")
        entries[var] = entry

    # Fetch, Submit, Delete, Clear Buttons
    fetch_button = ttk.Button(enrollment_form, text="Fetch", command=lambda: fetch_enrollment_data(entries['enrollment_id'].get(), entries))
    fetch_button.pack(pady=5)

    submit_button = ttk.Button(enrollment_form, text="Submit", command=lambda: submit_form(entries, "enrollment", entries['enrollment_id'].get()))
    submit_button.pack(pady=5)

    delete_button = ttk.Button(enrollment_form, text="Delete", command=lambda: delete_enrollment_data(entries['enrollment_id'].get()))
    delete_button.pack(pady=5)

    clear_button = ttk.Button(enrollment_form, text="Clear", command=lambda: clear_entries(entries))
    clear_button.pack(pady=5)

# Main window setup
root = tk.Tk()
root.title("OZON UNIVERSITY - Dashboard")
root.geometry("1100x500")
root.configure(bg="#f0f0f0")

# University Header
header_frame = tk.Frame(root, bg="#4CAF50", height=80)
header_frame.pack(side="top", fill="x")

header_label = tk.Label(header_frame, text="OZON UNIVERSITY", font=("Helvetica", 24, "bold"), fg="white", bg="#4CAF50")
header_label.place(relx=0.5, rely=0.5, anchor="center")

# Left Side Buttons (Navigation)
nav_frame = tk.Frame(root, bg="#d9d9d9", width=200)
nav_frame.pack(side="left", fill="y")

# Add Buttons
buttons = [("Student", open_student_form),
           ("Course", open_course_form),
           ("Enrollment", open_enrollment_form)]

for text, command in buttons:
    button = ttk.Button(nav_frame, text=text, command=command, style="TButton")
    button.pack(pady=20, padx=10, fill="x")

# Image Section
image_frame = tk.Frame(root, bg="white", width=400, height=250)
image_frame.place(relx=0.3, rely=0.55, anchor="center")

# Open and resize the image
image_path = "C:\\Users\\KS COMPUTERS\\Downloads\\uni management system\\image\\image.jpg"
image = Image.open(image_path)
image = image.resize((440, 325), Image.Resampling.LANCZOS)

# Convert to a format that Tkinter can use
photo = ImageTk.PhotoImage(image)

# Display the image in Tkinter
image_label = tk.Label(image_frame, image=photo)
image_label.image = photo
image_label.pack()

# About University Section (Text)
about_frame = tk.Frame(root, bg="#d9d9d9", width=400, height=250)
about_frame.place(relx=0.75, rely=0.55, anchor="center")

about_label = tk.Label(about_frame, text="About University", font=("Helvetica", 16, "bold"), bg="#d9d9d9")
about_label.pack(pady=10)

about_text = tk.Label(about_frame, text="Welcome to OZON University \n a leading institution for excellence in education.\n At OZON, we are dedicated to fostering academic excellence and\n developing future leaders.\n Our transformative learning environment empowers students\n to reach their highest potential.\n With world-class faculty, state-of-the-art facilities, and innovative programs,\n we inspire and challenge students in their quest for knowledge.\n Whether you're embarking on a journey of\n academic exploration, honing critical skills\n for your career, or engaging in groundbreaking research,\n OZON University is where your aspirations come to life.\n Join our vibrant community and become part of a tradition of\n excellence and innovation.", font=("Helvetica", 12), bg="#d9d9d9", justify="left")
about_text.pack(pady=10)

# Start the application
root.mainloop()
