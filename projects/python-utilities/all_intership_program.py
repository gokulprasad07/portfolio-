import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image
from playsound import playsound
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
import names
import os # Added for path handling

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
        
        title = Label(self.master, text="Painting Software", font=('times new roman', 30, 'bold'), fg="Black", relief=GROOVE)
        title.pack(fill=X)
        
        self.paint_tools = Frame(self.master, width=100, height=300, relief=RIDGE, borderwidth=2)
        self.paint_tools.place(x=0, y=50)

        # NOTE: Using placeholders for images to make the code run without external files.
        try:
            # Attempt to load images if they exist
            self.pen_logo = ImageTk.PhotoImage(Image.open('pen.png'))
            self.brush_logo = ImageTk.PhotoImage(Image.open('brush.png'))
            self.color_logo = ImageTk.PhotoImage(Image.open('color.png'))
            self.eraser_logo = ImageTk.PhotoImage(Image.open('eraser.png'))
        except FileNotFoundError:
             # Create simple text placeholders if images are missing
             self.pen_logo = self._create_placeholder_image(16, 16, 'P')
             self.brush_logo = self._create_placeholder_image(16, 16, 'B')
             self.color_logo = self._create_placeholder_image(16, 16, 'C')
             self.eraser_logo = self._create_placeholder_image(16, 16, 'E')

        self.pen_button = Button(self.paint_tools, image=self.pen_logo, command=self.use_pen)
        self.pen_button.place(x=60, y=10)
        Label(self.paint_tools, text="Pen").place(x=5, y=11)

        self.brush_button = Button(self.paint_tools, image=self.brush_logo, command=self.use_brush) 
        self.brush_button.place(x=60, y=40)
        Label(self.paint_tools, text="Brush").place(x=5, y=40)

        self.color_button = Button(self.paint_tools, image=self.color_logo, command=self.choose_color)
        self.color_button.place(x=60, y=70)
        Label(self.paint_tools, text="Color").place(x=5, y=70)

        self.eraser_button = Button(self.paint_tools, image=self.eraser_logo, command=self.use_eraser)
        self.eraser_button.place(x=60, y=100)
        Label(self.paint_tools, text="Eraser").place(x=5, y=100)

        Label(self.paint_tools, text="Pen Size").place(x=15, y=250)
        self.choose_size_button = Scale(self.paint_tools, from_=1, to=10, orient=VERTICAL, length=80) 
        self.choose_size_button.place(x=20, y=150)
        self.choose_size_button.set(self.DEFAULT_PEN_SIZE)

        self.c = Canvas(self.master, bg='white', width=1250, height=700, relief=RIDGE, borderwidth=0)
        self.c.place(x=100, y=50)

        self.setup()

    def _create_placeholder_image(self, width, height, text):
        # Fallback function to create a small image if the file is missing
        from PIL import ImageDraw
        img = Image.new('RGB', (width, height), color = 'gray')
        d = ImageDraw.Draw(img)
        d.text((1,1), text, fill=(0,0,0)) 
        return ImageTk.PhotoImage(img)

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.pen_button.config(relief=SUNKEN)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self): self.activate_button(self.pen_button)
    def use_brush(self): self.activate_button(self.brush_button)
    def choose_color(self):
        self.eraser_on = False
        color_code = askcolor(color=self.color)[1]
        if color_code: self.color = color_code
    def use_eraser(self): self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

# --- Application 2: Piano Program Class ---

class PianoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Piano")
        self.master.geometry('700x300')
        self.master.maxsize(700,300)
        self.master.minsize(700,300)
        self.master['bg']="white"
        
        # NOTE: Placeholder for piano icon.
        Label(self.master, text="PIANO", font=('verdana', 15, 'bold'), bg='white').place(x=310,y=10)

        self.frame1 = Frame(self.master, width=700, height=198, bg="white")
        self.frame1.place(x=0,y=100)
        
        for i in range(1, 24):
            self.create_piano_key(i)

    def PianoSound(self, sound):
        # NOTE: This part requires 'playsound' and 'PianoX.mp3' files to work.
        # It's kept for structure but may not produce sound without the files.
        try:
            # playsound(f'Piano{sound}.mp3', block=False)
            print(f"Attempting to play Piano{sound}.mp3...")
        except Exception as e:
            # print(f"Could not play sound Piano{sound}.mp3: {e}")
            pass

    def create_piano_key(self, index):
        if index % 2 != 0:
            Button(self.frame1, padx=10, pady=100, bg="black", fg="white", relief=RAISED, 
                   borderwidth=3, command=lambda: self.PianoSound(index), cursor="hand2").grid(row=0, column=index)
        else:
            Button(self.frame1, padx=10, pady=100, bg="white", fg="black", relief=RAISED, 
                   borderwidth=2, command=lambda: self.PianoSound(index), cursor="hand2").grid(row=0, column=index)

# --- Application 3: Name Generator Program Class ---

class NameGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x200')
        self.master.title("Name Generator")
        
        Label(self.master, text="Name Generator", font=('verdana', 15, 'bold'), bg="black", fg="white").place(x=110, y=10)

        Label(self.master, text="Gender", font=('verdana', 10, 'bold')).place(x=10, y=60)
        self.g = tk.StringVar(value='Male') 
        self.gender_combobox = Combobox(self.master, width=13, textvariable=self.g, state='readonly', font=('verdana', 10, 'bold')) 
        self.gender_combobox['values'] = ('Male', 'Female')
        self.gender_combobox.place(x=10, y=90)

        Label(self.master, text="Type", font=('verdana', 10, 'bold')).place(x=170, y=60)
        self.t = tk.StringVar(value='Full Name') 
        self.types_combobox = Combobox(self.master, width=13, textvariable=self.t, state='readonly', font=('verdana', 10, 'bold')) 
        self.types_combobox['values'] = ('Full Name', 'First Name','Last Name')
        self.types_combobox.place(x=170, y=90)

        Button(self.master, text="Search", font=('verdana', '10', 'bold'), command=self.search).place(x=320, y=85)

        self.text = ScrolledText(self.master, width=40, height=3)
        self.text['font'] = ("verdana", 10, 'bold')
        self.text.place(x=10, y=130)

    def search(self):
        Gender = self.g.get()
        Type = self.t.get()
        name = ""
        
        try:
            gender_param = Gender.lower()
            if Type == "Full Name":
                name = names.get_full_name(gender=gender_param)
            elif Type == "First Name":
                name = names.get_first_name(gender=gender_param)
            elif Type == "Last Name":
                name = names.get_last_name()
            
            self.text.delete('1.0', END)
            self.text.insert(END, name)

        except Exception as e:
            self.text.delete('1.0', END)
            self.text.insert(END, f"Error: {e}. Check if 'names' library is installed.")


# --- Placeholder Applications (4, 5, 6) ---

class PlaceholderApp:
    """Base class for placeholder applications."""
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.master.geometry('350x150')
        Label(self.master, text=f"{title} Application", font=('verdana', 15, 'bold')).pack(pady=20)
        Label(self.master, text="This is a placeholder. Add your code here.").pack()

class TranslatorApp(PlaceholderApp):
    def __init__(self, master):
        super().__init__(master, "Translator")

class CalculatorApp(PlaceholderApp):
    def __init__(self, master):
        super().__init__(master, "Calculator")

class BillGeneratorApp(PlaceholderApp):
    def __init__(self, master):
        super().__init__(master, "Bill Generator")


# --- Main Controller Application (Launcher) ---

class AppLauncher:
    def __init__(self, master):
        self.master = master
        self.master.title("Six-in-One Program Launcher (Title Selection)")
        self.master.geometry("450x300")
        
        Label(master, text="Select an Application Title to Launch", 
              font=('Helvetica', 14, 'bold'), bg='lightgreen').pack(pady=15, fill=X)
        
        # Dictionary of options
        self.app_options = {
            "1. Painting Software": Paint,
            "2. Piano Application": PianoApp,
            "3. Name Generator": NameGeneratorApp,
            "4. Translator (Placeholder)": TranslatorApp,
            "5. Calculator (Placeholder)": CalculatorApp,
            "6. Bill Generator (Placeholder)": BillGeneratorApp,
        }
        
        # Create a dropdown (Combobox) for selection
        Label(master, text="Application Title:", font=('Helvetica', 10)).pack(pady=5)
        
        self.selected_app = tk.StringVar(value=list(self.app_options.keys())[0])
        self.app_combobox = Combobox(master, width=45, textvariable=self.selected_app, state='readonly', font=('Helvetica', 10))
        self.app_combobox['values'] = list(self.app_options.keys())
        self.app_combobox.pack(pady=5)
        self.app_combobox.current(0) # Select the first item by default

        # Launch Button
        Button(master, text="Launch Selected Program", 
               command=self.launch_selected_app, width=40, height=2, bg='blue', fg='white', font=('Helvetica', 10, 'bold')).pack(pady=15)
    
    def launch_selected_app(self):
        # Get the selected title (key) from the Combobox
        selected_title = self.selected_app.get()
        # Get the corresponding Class (value) from the dictionary
        AppClass = self.app_options[selected_title]
        
        # Create a new Toplevel window for the application
        new_window = tk.Toplevel(self.master)
        # Pass the new Toplevel window as the master to the application class
        app = AppClass(new_window)

if __name__ == '__main__':
    main_root = tk.Tk()
    launcher = AppLauncher(main_root)
    main_root.mainloop()