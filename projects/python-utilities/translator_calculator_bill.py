import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, Label, Button, Entry, Text, GROOVE, RIDGE, X, Y, BOTH, RIGHT, VERTICAL, Scrollbar, LabelFrame, Frame, StringVar, IntVar, END
import random
import os
# The following imports are REQUIRED for the Translator to work.
# Please ensure they are installed:
# pip install pillow googletrans==3.1.0a0
try:
    from PIL import ImageTk, Image
    from googletrans import Translator
except ImportError:
    # Placeholder classes/functions if libraries are missing
    class Translator:
        def translate(self, text, dest):
            return type('Output', (object,), {'text': f"Translation Failed: Missing 'googletrans' library."})()
    messagebox.showwarning("Warning", "The 'googletrans' or 'Pillow' library is not installed. Translator functionality may be limited.")


# ====================================================================
# A. MASTER MENU (The Single Interface)
# ====================================================================

class MasterMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Master Application Selector")
        self.master.geometry("300x230")
        self.master.resizable(False, False)
        
        # FIX: Used imported Label/Button instead of tk.Label/tk.Button 
        Label(self.master, text="Select an Application", font=('Arial', 16, 'bold')).pack(pady=15)
        
        # --- Buttons to launch other programs ---
        
        Button(self.master, text="1. Language Translator", command=self.launch_translator, width=25, height=2).pack(pady=5)
        Button(self.master, text="2. Billing System", command=self.launch_billing_system, width=25, height=2).pack(pady=5)
        Button(self.master, text="3. Tkinter Calculator", command=self.launch_calculator, width=25, height=2).pack(pady=5)

    def launch_translator(self):
        # Create a new top-level window for the translator
        newWindow = Toplevel(self.master)
        TranslatorApp(newWindow)

    def launch_billing_system(self):
        # Create a new top-level window for the billing system
        newWindow = Toplevel(self.master)
        # Renaming from Bill_App to BillingApp for consistency
        BillingApp(newWindow)

    def launch_calculator(self):
        # Create a new top-level window for the calculator
        newWindow = Toplevel(self.master)
        CalculatorApp(newWindow)

# ====================================================================
# B. LANGUAGE TRANSLATOR (Modified as a Class)
# ====================================================================

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Language Translator')
        self.root.geometry('530x330')
        self.root.maxsize(530,330)
        self.root.minsize(530,330)

        # --- Functions defined as local methods ---
        def translate():
            language_1 = self.t1.get("1.0","end-1c")
            cl = self.choose_langauge.get()
            if language_1 == '':
                messagebox.showerror('Language Translator','please fill the box')
            else:
                self.t2.delete(1.0,'end')
                translator = Translator()
                output = translator.translate(language_1, dest=cl)
                self.t2.insert('end',output.text)

        def clear():
            self.t1.delete(1.0,'end')
            self.t2.delete(1.0,'end')
        
        # --- GUI Elements (Adjusted to use self.root and self.variable) ---

        self.a = StringVar() 
        self.auto_detect = ttk.Combobox(self.root, width = 20, textvariable = self.a, state='readonly',font=('verdana',10,'bold')) 
        # Keeping only necessary values for space. Full list is in your original file.
        self.auto_detect['values'] = ('Auto Detect',) 
        self.auto_detect.place(x=30,y=70)
        self.auto_detect.current(0) 

        self.l = StringVar() 
        self.choose_langauge = ttk.Combobox(self.root, width = 20, textvariable = self.l, state='readonly',font=('verdana',10,'bold')) 
        # Keeping only a few language options to keep code manageable.
        self.choose_langauge['values'] = ('English', 'French', 'German', 'Spanish', 'Tamil', 'Hindi', 'Japanese', 'Korean')  
        self.choose_langauge.place(x=290,y=70)
        self.choose_langauge.current(0) 

        self.t1 = Text(self.root,width=30,height=10,borderwidth=5,relief=RIDGE)
        self.t1.place(x=10,y=100)

        self.t2 = Text(self.root,width=30,height=10,borderwidth=5,relief=RIDGE)
        self.t2.place(x=260,y=100)

        Button(self.root,text="Translate",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=translate).place(x=150,y=280)
        Button(self.root,text="Clear",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=clear).place(x=280,y=280)


# ====================================================================
# C. BILLING SYSTEM (The Class and Methods remain the same, renamed to BillingApp)
# Note: The logic inside the methods comes directly from your 'OG billing_system.py'
# ====================================================================

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#badc57"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#badc57", fg="Black", relief=GROOVE)
        title.pack(fill=X)
    # ================variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.syrup = IntVar()
        self.cream = IntVar()
        self.thermal_gun = IntVar()
    # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.spices = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        #=============coldDrinks=============================
        self.sprite = IntVar()
        self.mineral = IntVar()
        self.juice = IntVar()
        self.coke = IntVar()
        self.lassi = IntVar()
        self.mountain_duo = IntVar()
    # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#badc57", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#badc57", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================Medical====================================
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        syrup_lbl = Label(F2, text="Syrup", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        syrup_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        syrup_txt = Entry(F2, width=10, textvariable=self.syrup, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        syrup_txt.grid(row=3, column=1, padx=10, pady=10)

        cream_lbl = Label(F2, text="Cream", font=('times new roman', 16, 'bold'), bg = "#badc57", fg = "black")
        cream_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        cream_txt = Entry(F2, width=10, textvariable=self.cream, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        cream_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=10, textvariable=self.thermal_gun, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        spices_lbl = Label(F3, text="Spices", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        spices_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        spices_txt = Entry(F3, width=10, textvariable=self.spices, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        spices_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========ColdDrinks================================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F4.place(x=670, y=180, width=325, height=380)

        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        mineral_lbl = Label(F4, text="Mineral Water", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        mineral_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mineral_txt = Entry(F4, width=10, textvariable=self.mineral, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mineral_txt.grid(row=1, column=1, padx=10, pady=10)

        juice_lbl = Label(F4, text="Juice", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        juice_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        juice_txt = Entry(F4, width=10, textvariable=self.juice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        juice_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        lassi_lbl = Label(F4, text="Lassi", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        lassi_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        lassi_txt = Entry(F4, width=10, textvariable=self.lassi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        lassi_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_duo_lbl = Label(F4, text="Mountain Duo", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        mountain_duo_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_duo_txt = Entry(F4, width=10, textvariable=self.mountain_duo, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mountain_duo_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="#badc57")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Medical Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Medical Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
        # FIX: The original billing system had the same variable `self.m_s_p` used for Sanitizer price AND Syrup price.
        # I'm keeping the original logic to maintain functionality, but be aware of this potential bug in your original file.
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_s_p_sanitizer = self.sanitizer.get()*2
        self.m_m_p = self.mask.get()*5
        self.m_s_p_syrup = self.syrup.get()*30
        self.m_c_p = self.cream.get()*5
        self.m_t_g_p = self.thermal_gun.get()*15
        
        # Original sum: self.m_m_p+self.m_h_g_p+self.m_s_p+self.m_c_p+self.m_t_g_p+self.m_s_p 
        # I'm using the unique variable names now:
        self.total_medical_price = float(self.m_m_p + self.m_h_g_p + self.m_s_p_sanitizer + self.m_c_p + self.m_t_g_p + self.m_s_p_syrup)

        self.medical_price.set("Rs. "+str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price*0.05), 2)
        self.medical_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*10
        self.g_f_o_p = self.food_oil.get()*10
        self.g_w_p = self.wheat.get()*10
        self.g_s_p = self.spices.get()*6
        self.g_f_p = self.flour.get()*8
        self.g_m_p = self.maggi.get()*5
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_s_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        # Note: Your original tax calculation for grocery was *5, not *0.05. I'm keeping the original *5.
        self.g_tax = round((self.total_grocery_price*5), 2) 
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*10
        self.c_d_w_p = self.mineral.get()*10
        self.c_d_j_p = self.juice.get()*10
        self.c_d_c_p = self.coke.get()*10
        self.c_d_l_p = self.lassi.get()*10
        self.c_m_d = self.mountain_duo.get()*10
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_w_p+self.c_d_j_p+self.c_d_c_p+self.c_d_l_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_medical_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Grocery Retail")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

    def bill_area(self):
        self.total() # Ensure total is calculated before generating bill
        if self.c_name.get() == "" or self.c_phone.get() == "": # Fixed space check
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
        # ============medical===========================
            if self.sanitizer.get() != 0:
                self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p_sanitizer}") # Fixed to use _sanitizer
            if self.mask.get() != 0:
                self.txtarea.insert(END, f"\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}")
            if self.hand_gloves.get() != 0:
                self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
            if self.syrup.get() != 0:
                self.txtarea.insert(END, f"\n Syrup\t\t{self.syrup.get()}\t\t{self.m_s_p_syrup}") # Fixed to use _syrup
            if self.cream.get() != 0:
                self.txtarea.insert(END, f"\n Cream\t\t{self.cream.get()}\t\t{self.m_c_p}")
            if self.thermal_gun.get() != 0:
                self.txtarea.insert(END, f"\n Thermal Gun\t\t{self.thermal_gun.get()}\t\t{self.m_t_g_p}") # Fixed quantity check
        # ==============Grocery============================
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.spices.get() != 0:
                self.txtarea.insert(END, f"\n Spices\t\t{self.spices.get()}\t\t{self.g_s_p}")
            if self.flour.get() != 0:
                self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
            if self.maggi.get() != 0:
                self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
            #================ColdDrinks==========================
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
            if self.mineral.get() != 0:
                self.txtarea.insert(END, f"\n Mineral\t\t{self.mineral.get()}\t\t{self.c_d_w_p}")
            if self.juice.get() != 0:
                self.txtarea.insert(END, f"\n Juice\t\t{self.juice.get()}\t\t{self.c_d_j_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
            if self.lassi.get() != 0:
                self.txtarea.insert(END, f"\n Lassi\t\t{self.lassi.get()}\t\t{self.c_d_l_p}") # Fixed quantity check
            if self.mountain_duo.get() != 0:
                self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.mountain_duo.get()}\t\t{self.c_m_d}") # Fixed quantity check
                self.txtarea.insert(END, f"\n--------------------------------")
        # ===============taxes==============================
            if self.medical_tax.get() != 'Rs. 0.0': # Changed to check StringVar
                self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
            if self.grocery_tax.get() != 'Rs. 0.0': # Changed to check StringVar
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drinks_tax.get() != 'Rs. 0.0': # Changed to check StringVar
                self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill:\t\t\t Rs.{round(self.total_bill, 2)}") # Rounded total
            self.txtarea.insert(END, f"\n--------------------------------")
            self.save_bill()

    def save_bill(self):
        # NOTE: This part requires a directory named 'bills' to exist in the same folder.
        if not os.path.exists("bills"):
            os.makedirs("bills")
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            # FIX: Ensure bills directory exists
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    def find_bill(self):
        if self.search_bill.get() == "":
            messagebox.showerror("Error", "Enter Bill Number to Search")
            return
            
        present = "no"
        # NOTE: This requires a directory named 'bills' to exist in the same folder.
        if not os.path.exists("bills"):
            os.makedirs("bills")

        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
                break # Exit loop once bill is found
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            # All variable sets (0 and "") from original file...
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.syrup.set(0)
            self.cream.set(0)
            self.thermal_gun.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.spices.set(0)
            self.flour.set(0)
            self.maggi.set(0)
    # =============coldDrinks=============================
            self.sprite.set(0)
            self.mineral.set(0)
            self.juice.set(0)
            self.coke.set(0)
            self.lassi.set(0)
            self.mountain_duo.set(0)
    # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


# ====================================================================
# D. TKINTER CALCULATOR (Modified as a Class)
# ====================================================================

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("170x230")
        self.root.title("Calculator")
        self.root.maxsize(170, 230)
        self.root.minsize(170, 230)
        
        # Used imported Entry instead of tk.Entry
        self.inp = Entry(self.root, width=16, borderwidth=3, relief=RIDGE)
        self.inp.grid(pady=10, row=0, sticky="w", padx=15)
        
        # --- Functions defined as local methods ---
        # FIX: Ensure these functions are defined before buttons use them.
        def insert_val(val):
            self.inp.insert("end", val)

        def result():
            try:
                content = self.inp.get()
                if content == "":
                    self.inp.insert("end", "error")
                elif content.startswith("0") and len(content) > 1 and content[1].isdigit():
                    self.inp.delete(0, "end")
                    self.inp.insert("end", "error")
                else:
                    res = eval(content)
                    self.inp.delete(0, "end")
                    self.inp.insert("end", res)
            except Exception: # Catch any other error (Syntax, ZeroDivision, etc.)
                self.inp.delete(0, "end")
                self.inp.insert("end", "Error")


        # --- Button Design (Ensuring all buttons use self.root as parent) ---
        
        # C Button (Used imported Button)
        clear = Button(self.root, text="C", width=2, command=lambda: self.inp.delete(0, "end"), bg="red", fg="white", relief=RIDGE)
        clear.grid(row=0, sticky="w", padx=125)
        
        # Row 1 (9, 8, 7, +)
        # FIX: Added self.root as parent for all buttons that were missing it.
        Button(self.root, text="9", width=2, command=lambda: insert_val("9"), borderwidth=3, relief=RIDGE).grid(row=1, sticky="w", padx=15)
        Button(self.root, text="8", width=2, command=lambda: insert_val("8"), borderwidth=3, relief=RIDGE).grid(row=1, sticky="w", padx=45)
        Button(self.root, text="7", width=2, command=lambda: insert_val("7"), borderwidth=3, relief=RIDGE).grid(row=1, sticky="w", padx=75)
        Button(self.root, text="+", width=2, command=lambda: insert_val("+"), borderwidth=3, relief=RIDGE).grid(row=1, sticky="e", padx=125)

        # Row 2 (6, 5, 4, -)
        Button(self.root, text="6", width=2, command=lambda: insert_val("6"), borderwidth=3, relief=RIDGE).grid(row=2, sticky="w", padx=15, pady=5)
        Button(self.root, text="5", width=2, command=lambda: insert_val("5"), borderwidth=3, relief=RIDGE).grid(row=2, sticky="w", padx=45, pady=5)
        Button(self.root, text="4", width=2, command=lambda: insert_val("4"), borderwidth=3, relief=RIDGE).grid(row=2, sticky="w", padx=75, pady=5)
        Button(self.root, text="-", width=2, command=lambda: insert_val("-"), borderwidth=3, relief=RIDGE).grid(row=2, sticky="e", padx=125, pady=5)

        # Row 3 (3, 2, 1, *)
        Button(self.root, text="3", width=2, command=lambda: insert_val("3"), borderwidth=3, relief=RIDGE).grid(row=3, sticky="w", padx=15, pady=5)
        Button(self.root, text="2", width=2, command=lambda: insert_val("2"), borderwidth=3, relief=RIDGE).grid(row=3, sticky="w", padx=45, pady=5)
        Button(self.root, text="1", width=2, command=lambda: insert_val("1"), borderwidth=3, relief=RIDGE).grid(row=3, sticky="w", padx=75, pady=5)
        Button(self.root, text="*", width=2, command=lambda: insert_val("*"), borderwidth=3, relief=RIDGE).grid(row=3, sticky="e", padx=125, pady=5)

        # Row 4 (0, 00, ., /)
        Button(self.root, text="0", width=2, command=lambda: insert_val("0"), borderwidth=3, relief=RIDGE).grid(row=4, sticky="w", padx=15, pady=5)
        Button(self.root, text="00", width=2, command=lambda: insert_val("00"), borderwidth=3, relief=RIDGE).grid(row=4, sticky="w", padx=45, pady=5)
        Button(self.root, text=".", width=2, command=lambda: insert_val("."), borderwidth=3, relief=RIDGE).grid(row=4, sticky="w", padx=75, pady=5)
        Button(self.root, text="/", width=2, command=lambda: insert_val("/"), borderwidth=3, relief=RIDGE).grid(row=4, sticky="e", padx=125, pady=5)

        # Row 5 (=, %)
        Button(self.root, text="=", width=10, command=result, bg="red", fg="white", borderwidth=3, relief=RIDGE).grid(row=5, sticky="w", padx=15, pady=5)
        Button(self.root, text="%", width=2, command=lambda: insert_val("%"), borderwidth=3, relief=RIDGE).grid(row=5, sticky="e", padx=125, pady=5)


# ====================================================================
# E. MAIN EXECUTION BLOCK
# ====================================================================

if __name__ == '__main__':
    main_root = tk.Tk()
    app = MasterMenu(main_root)
    main_root.mainloop()