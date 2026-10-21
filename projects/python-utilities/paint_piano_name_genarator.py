import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image
from playsound import playsound
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
import names
import sys # For playsound dependency fix on some systems

# --- Application 1: Paint Program Class ---

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self, master):
        self.master = master
        self.master.title('Paint')
        self.master.geometry('1350x750')
        self.master.maxsize(1350,750)
        self.master.minsize(1350,750)
        
        title = Label(self.master, text="Painting software", font=('times new roman', 30, 'bold'), fg="Black", relief=GROOVE)
        title.pack(fill=X)
        
        self.paint_tools = Frame(self.master, width=100, height=300, relief=RIDGE, borderwidth=2)
        self.paint_tools.place(x=0, y=50) # Adjusted y position to avoid overlapping title

        # NOTE: This code assumes 'pen.png', 'brush.png', 'color.png', 'eraser.png' image files are present.
        try:
            self.pen_logo = ImageTk.PhotoImage(Image.open('pen.png'))
            self.brush_logo = ImageTk.PhotoImage(Image.open('brush.png'))
            self.color_logo = ImageTk.PhotoImage(Image.open('color.png'))
            self.eraser_logo = ImageTk.PhotoImage(Image.open('eraser.png'))
        except FileNotFoundError:
             print("Warning: Image files (pen.png, brush.png, color.png, eraser.png) not found.")
             # Create small placeholder images if files are missing
             self.pen_logo = self._create_placeholder_image(16, 16, 'Pen')
             self.brush_logo = self._create_placeholder_image(16, 16, 'Brush')
             self.color_logo = self._create_placeholder_image(16, 16, 'Color')
             self.eraser_logo = self._create_placeholder_image(16, 16, 'Eraser')


        self.p = Label(self.paint_tools, text="pen", borderwidth=0, font=('verdana', 10, 'bold'))
        self.p.place(x=5, y=11)
        self.pen_button = Button(self.paint_tools, padx=6, image=self.pen_logo, borderwidth=2, command=self.use_pen)
        self.pen_button.place(x=60, y=10)

        self.b = Label(self.paint_tools, borderwidth=0, text='brush', font=('verdana', 10, 'bold'))
        self.b.place(x=5, y=40)
        self.brush_button = Button(self.paint_tools, image=self.brush_logo, borderwidth=2, command=self.use_brush) 
        self.brush_button.place(x=60, y=40)

        self.cl = Label(self.paint_tools, text='color', font=('verdana', 10, 'bold'))
        self.cl.place(x=5, y=70)
        self.color_button = Button(self.paint_tools, image=self.color_logo, borderwidth=2, command=self.choose_color)
        self.color_button.place(x=60, y=70)

        self.e = Label(self.paint_tools, text='eraser', font=('verdana', 10, 'bold'))
        self.e.place(x=5, y=100)
        self.eraser_button = Button(self.paint_tools, image=self.eraser_logo, borderwidth=2, command=self.use_eraser)
        self.eraser_button.place(x=60, y=100)

        self.pen_size = Label(self.paint_tools, text="Pen Size", font=('verdana', 10, 'bold'))
        self.pen_size.place(x=15, y=250)
        self.choose_size_button = Scale(self.paint_tools, from_=1, to=10, orient=VERTICAL, length=80) # Added length
        self.choose_size_button.place(x=20, y=150)
        self.choose_size_button.set(self.DEFAULT_PEN_SIZE) # Set initial value

        self.c = Canvas(self.master, bg='white', width=1250, height=700, relief=RIDGE, borderwidth=0) # Adjusted size for better fit
        self.c.place(x=100, y=50)

        self.setup()

    def _create_placeholder_image(self, width, height, text):
        # Fallback function to create a small image if the file is missing
        img = Image.new('RGB', (width, height), color = 'gray')
        # Placeholder text drawing requires a more complex setup with PIL, 
        # but for simplicity, we just create a gray box.
        return ImageTk.PhotoImage(img)

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.pen_button.config(relief=SUNKEN) # Activate pen by default
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        color_code = askcolor(color=self.color)[1]
        if color_code: # Check if a color was selected (not cancelled)
            self.color = color_code

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

# --- Application 2: Piano Program Class (Integrated) ---

class PianoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Piano")
        self.master.geometry('700x300')
        self.master.maxsize(700,300)
        self.master.minsize(700,300)
        self.master['bg']="white"
        
        # NOTE: Assumes 'piano.png' image file is present.
        try:
            self.icon = ImageTk.PhotoImage(Image.open('piano.png'))
            icon_label = Label(self.master, image=self.icon, bg='white')
            icon_label.place(x=295,y=10)
        except FileNotFoundError:
            print("Warning: Image file (piano.png) not found.")

        self.frame1 = Frame(self.master, width=700, height=198, bg="white")
        self.frame1.place(x=0,y=100)
        
        for i in range(1, 24):
            self.create_piano_key(i)

    def PianoSound(self, sound):
        # NOTE: This requires 'playsound' module and 'PianoX.mp3' files to work.
        # Use an absolute path or ensure the MP3 files are in the same directory.
        try:
            playsound(f'Piano{sound}.mp3', block=False)
        except Exception as e:
            # print(f"Could not play sound Piano{sound}.mp3: {e}")
            pass # Suppress sound-related errors if MP3 files are missing

    def create_piano_key(self, index):
        if index % 2 != 0:
            Button(self.frame1, padx=10, pady=100, bg="black", fg="white", relief=RAISED, 
                   borderwidth=3, command=lambda: self.PianoSound(index), cursor="hand2").grid(row=0, column=index)
        else:
            Button(self.frame1, padx=10, pady=100, bg="white", fg="black", relief=RAISED, 
                   borderwidth=2, command=lambda: self.PianoSound(index), cursor="hand2").grid(row=0, column=index)

# --- Application 3: Name Generator Program Class (Integrated) ---

class NameGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x200')
        self.master.title("Name Generators")
        
        l = Label(self.master, text="Name Generators", font=('verdana', 15, 'bold'), bg="black", fg="white")
        l.place(x=110, y=10)

        l1 = Label(self.master, text="Gender", font=('verdana', 10, 'bold'))
        l1.place(x=10, y=60)
        
        self.g = tk.StringVar() 
        self.gender_combobox = Combobox(self.master, width=13, textvariable=self.g, state='readonly', font=('verdana', 10, 'bold')) 
        self.gender_combobox['values'] = ('Male', 'Female')
        self.gender_combobox.place(x=10, y=90)
        self.gender_combobox.current(0) 

        l2 = Label(self.master, text="Type", font=('verdana', 10, 'bold'))
        l2.place(x=170, y=60)
        
        self.t = tk.StringVar() 
        self.types_combobox = Combobox(self.master, width=13, textvariable=self.t, state='readonly', font=('verdana', 10, 'bold')) 
        self.types_combobox['values'] = ('Full Name', 'First Name','Last Name')
        self.types_combobox.place(x=170, y=90)
        self.types_combobox.current(0) 

        button = Button(self.master, text="Search", font=('verdana', '10', 'bold'), command=self.search)
        button.place(x=320, y=85)

        self.text = ScrolledText(self.master, width=40, height=3)
        self.text['font'] = ("verdana", 10, 'bold')
        self.text.place(x=10, y=130)

    def search(self):
        Gender = self.g.get()
        Type = self.t.get()
        name = ""
        
        try:
            if Gender == 'Male' and Type == "Full Name":
                name = names.get_full_name(gender="male")
            elif Gender == 'Male' and Type == "First Name":
                name = names.get_first_name(gender="male") # Explicitly set gender for consistency
            elif Gender == 'Male' and Type == "Last Name":
                name = names.get_last_name() # names doesn't have a gendered last name function
            
            elif Gender == 'Female' and Type == "Full Name":
                name = names.get_full_name(gender="female")
            elif Gender == 'Female' and Type == "First Name":
                name = names.get_first_name(gender="female") # Explicitly set gender for consistency
            elif Gender == 'Female' and Type == "Last Name":
                name = names.get_last_name()
            
            self.text.delete('1.0', END)
            self.text.insert(END, name)

        except Exception as e:
            self.text.delete('1.0', END)
            self.text.insert(END, f"Error: {e}. Check if 'names' library is installed.")


# --- Main Controller Application ---

class AppLauncher:
    def __init__(self, master):
        self.master = master
        self.master.title("Multi-App Launcher")
        self.master.geometry("400x200")
        
        Label(master, text="Select an Application", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        # Launch buttons
        Button(master, text="1. Launch Paint Program", command=lambda: self.launch_app(Paint), width=30).pack(pady=5)
        Button(master, text="2. Launch Piano App", command=lambda: self.launch_app(PianoApp), width=30).pack(pady=5)
        Button(master, text="3. Launch Name Generator", command=lambda: self.launch_app(NameGeneratorApp), width=30).pack(pady=5)
    
    def launch_app(self, AppClass):
        # Create a new Toplevel window for each application
        new_window = tk.Toplevel(self.master)
        # Pass the new Toplevel window as the master to the application class
        app = AppClass(new_window)

if __name__ == '__main__':
    # Ensure playsound library is imported but suppress its stdout when imported
    # This is a common pattern when playsound is used in tkinter applications.
    
    main_root = tk.Tk()
    launcher = AppLauncher(main_root)
    main_root.mainloop()