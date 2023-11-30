import pickle
from tkinter import LEFT, Frame, Label, OptionMenu, StringVar, Tk, Entry, Button, PhotoImage, Toplevel
import tkinter.messagebox
import math
import numpy as np
import datetime
from pathlib import Path


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

try:
    f = open("log.txt")
    f.close()
except:
    f = open("log.txt","w")
    f.close()

try:
    f = open("history.dat")
    f.close()
except:
    f = open("history.dat","wb")
    f.close()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("338x599")
window.configure(bg = "#2A2437")
window.title("Poggers Calculator")
window.call('wm', 'iconphoto', window,PhotoImage(file=relative_to_assets('icons8-calculator-62.png')))

equation = StringVar()
expression = ""

historyvar = StringVar()

entrybg = Label(bg="#352E42")
entrybg.place(x=0.0,y=0.0,width=338.0,height=189.0)

entry_1 = Entry(bd=0,bg="#352E42",highlightthickness=0,textvariable=equation,font="Open_Sans 22",justify=LEFT,fg="white")
entry_1.place(x=10,y=123,width=319,h=41)


entry_2 = Entry(bd=0,bg="#352E42",highlightthickness=0,textvariable=historyvar,font="Open_Sans 15",justify=LEFT,fg="white")
entry_2.place(x=10,y=55,width=319,h=41)


sin_image= PhotoImage(file=relative_to_assets("button_1.png"))
power_image = PhotoImage(file=relative_to_assets("button_2.png"))
sqrt_image= PhotoImage(file=relative_to_assets("button_3.png"))
lcm_image= PhotoImage(file=relative_to_assets("button_4.png"))
log_image= PhotoImage(file=relative_to_assets("button_5.png"))
hcf_image= PhotoImage(file=relative_to_assets("button_6.png"))
tan_image= PhotoImage(file=relative_to_assets("button_7.png"))
cos_image= PhotoImage(file=relative_to_assets("button_8.png"))
return1_image = PhotoImage(file=relative_to_assets("button_9.png"))
button_image_1 = PhotoImage(file=relative_to_assets("plus.png"))
button_image_2 = PhotoImage(file=relative_to_assets("options.png"))
button_image_3 = PhotoImage(file=relative_to_assets("divide.png"))
button_image_4 = PhotoImage(file=relative_to_assets("equals.png"))
button_image_5 = PhotoImage(file=relative_to_assets("multiply.png"))
button_image_6 = PhotoImage(file=relative_to_assets("minus.png"))
button_image_7 = PhotoImage(file=relative_to_assets("9.png"))
button_image_8 = PhotoImage(file=relative_to_assets("8.png"))
button_image_9 = PhotoImage(file=relative_to_assets("dot.png"))
button_image_10 = PhotoImage(file=relative_to_assets("0.png"))
button_image_11 = PhotoImage(file=relative_to_assets("7.png"))
button_image_12 = PhotoImage(file=relative_to_assets("6.png"))
button_image_13 = PhotoImage(file=relative_to_assets("5.png"))
button_image_14 = PhotoImage(file=relative_to_assets("4.png"))
button_image_15 = PhotoImage(file=relative_to_assets("2.png"))
button_image_16 = PhotoImage(file=relative_to_assets("1.png"))
button_image_17 = PhotoImage(file=relative_to_assets("back.png"))
button_image_18 = PhotoImage(file=relative_to_assets("open.png"))
button_image_19 = PhotoImage(file=relative_to_assets("close.png"))
button_image_20 = PhotoImage(file=relative_to_assets("3.png"))

def sin():
    sin_window = Toplevel(window)   
    sin_window.title("sin")
    sin_window.resizable(False, False)
    sin_window.grab_set()

    def sin_calculate_method(event=None):
        global expression, equation
        if str(deg_rad.get()) == "deg":
            try:
                sin_answer = math.sin(math.radians(eval(sin_expression.get())))
                sin_answer = round(sin_answer, 11)
                expression += str(sin_answer)
                equation.set(expression)
                with open("log.txt","a") as f:
                    f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"sin("+sin_expression.get()+")"))
                sin_window.grab_release()
                sin_window.destroy()
            except:
                tkinter.messagebox.showerror("sin()", "Invalid expression")
        else:
            try:
                sin_answer = math.sin(eval(sin_expression.get()))
                expression += str(sin_answer)
                equation.set(expression)
                with open("log.txt","a") as f:
                    f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"sin("+sin_expression.get()+")"))
                sin_window.grab_release()
                sin_window.destroy()
            except:
                tkinter.messagebox.showerror("sin()", "Invalid expression")

    options = ["deg", "rad"]
    deg_rad = StringVar()
    deg_rad.set("deg")

    sin_expression = StringVar()

    sin_format = Frame(sin_window)
    sin_format.pack()

    sin_label = Label(sin_format, text="sin(", font="Roboto 10 bold")
    sin_label.pack(side="left")
    sin_entry = Entry(sin_format, textvariable=sin_expression, bd=5)
    sin_entry.pack(side="left")
    sin_options = OptionMenu(sin_format, deg_rad, *options)
    sin_options.pack(side="left")
    sin_label = Label(sin_format, text=")", font="Roboto 10 bold")
    sin_label.pack(side="left")

    sin_calculate = Button(sin_window, text="=", fg='black', bg="#33cc00", command=sin_calculate_method, height=1,
                           width=8)
    sin_calculate.pack()
    sin_window.bind("<Return>",sin_calculate_method)

def cos():
    cos_window = Toplevel(window)
    cos_window.title("cos")
    cos_window.resizable(False, False)
    cos_window.grab_set()

    def cos_calculate_method(event = None):
        global expression, equation
        if str(deg_rad.get()) == "deg":
            try:
                cos_answer = math.cos(math.radians(eval(cos_expression.get())))
                cos_answer = round(cos_answer, 11)
                expression += str(cos_answer)
                equation.set(expression)
                with open("log.txt","a") as f:
                    f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"cos("+cos_expression.get()+")"))
                cos_window.grab_release()
                cos_window.destroy()
            except:
                tkinter.messagebox.showerror("cos()", "Invalid expression")
        else:
            try:
                cos_answer = math.cos(eval(cos_expression.get()))
                expression += str(cos_answer)
                equation.set(expression)
                with open("log.txt","a") as f:
                    f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"cos("+cos_expression.get()+")"))
                cos_window.grab_release()
                cos_window.destroy()
            except:
                tkinter.messagebox.showerror("cos()", "Invalid expression")

    options = ["deg", "rad"]
    deg_rad = StringVar()
    deg_rad.set("deg")

    cos_expression = StringVar()

    cos_format = Frame(cos_window)
    cos_format.pack()

    cos_label = Label(cos_format, text="cos(", font="Roboto 10 bold")
    cos_label.pack(side="left")
    cos_entry = Entry(cos_format, textvariable=cos_expression, bd=5)
    cos_entry.pack(side="left")
    cos_options = OptionMenu(cos_format, deg_rad, *options)
    cos_options.pack(side="left")
    cos_label = Label(cos_format, text=")", font="Roboto 10 bold")
    cos_label.pack(side="left")

    cos_calculate = Button(cos_window, text="=", fg='black', bg="#33cc00", command=cos_calculate_method, height=1,
                           width=8)
    cos_calculate.pack()
    cos_window.bind("<Return>",cos_calculate_method)

def tan():
    tan_window = Toplevel(window)
    tan_window.title("tan")
    tan_window.resizable(False, False)
    tan_window.grab_set()

    def tan_calculate_method(event=None):
        global expression, equation
        if str(deg_rad.get()) == "deg":
            try:
                tan_answer = math.tan(math.radians(eval(tan_expression.get())))
                tan_answer = round(tan_answer, 11)
                expression += str(tan_answer)
                equation.set(expression)
                with open("log.txt","a") as f:
                    f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"tan("+tan_expression.get()+")"))
                tan_window.grab_release()
                tan_window.destroy()
            except:
                tkinter.messagebox.showerror("tan()", "Invalid expression")
        else:
            try:
                tan_answer = math.tan(eval(tan_expression.get()))
                expression += str(tan_answer)
                equation.set(expression)
                with open("log.txt","a") as f:
                    f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"tan("+tan_expression.get()+")"))
                tan_window.grab_release()
                tan_window.destroy()
            except:
                tkinter.messagebox.showerror("tan()", "Invalid expression")

    options = ["deg", "rad"]
    deg_rad = StringVar()
    deg_rad.set("deg")

    tan_expression = StringVar()

    tan_format = Frame(tan_window)
    tan_format.pack()

    tan_label = Label(tan_format, text="tan(", font="Roboto 10 bold")
    tan_label.pack(side="left")
    tan_entry = Entry(tan_format, textvariable=tan_expression, bd=5)
    tan_entry.pack(side="left")
    tan_options = OptionMenu(tan_format, deg_rad, *options)
    tan_options.pack(side="left")
    tan_label = Label(tan_format, text=")", font="Roboto 10 bold")
    tan_label.pack(side="left")

    tan_calculate = Button(tan_window, text="=", fg='black', bg="#33cc00", command=tan_calculate_method, height=1,
                           width=8)
    tan_calculate.pack()
    tan_window.bind("<Return>",tan_calculate_method)


def root_calculation():
    global expression, equation
    screen1 = Toplevel(window)
    screen1.title("Roots")
    screen1.geometry("250x150")
    screen1.grab_set()
    screen1.config(bg="#313975")
    screen1.resizable(0,0)

    def clear():
        screen1.grab_release()
        screen1.destroy()

    def answer1():
        global answer, expression, equation
        expression += str(answer)
        equation.set(expression)
        clear()

    def answer2():
        global answer, expression, equation
        answer = "-" + str(answer)
        expression += str(answer)
        equation.set(expression)
        clear()

    def answer_method():
        global expression, equation, answer
        value_of_n = eval(ntext.get())
        value_of_x = eval(xtext.get())
        answer = value_of_n ** (1 / value_of_x)
        with open("log.txt","a") as f:
            f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+ntext.get()+" root "+xtext.get()))
        if value_of_x % 2 == 1:
            expression += str(answer)
            equation.set(expression)
            clear()
        elif value_of_x % 2 == 0:
            choice1.pack()
            choice2.pack()

    topiclabel = Label(screen1, text="Roots x√n", font="Roboto 16 bold",bg="#313975",fg='white')
    topiclabel.pack(pady=5)

    label1 = Label(screen1, text="Enter the value for x",bg="#535A92",fg='white')
    label1.place(x=15,y=40) 

    xtext = StringVar()
    xtextbox = Entry(screen1, textvariable=xtext, bd=5, width=14)
    xtextbox.place(x=135,y=38)

    label2 = Label(screen1, text="Enter the value for n",bg="#535A92",fg='white')
    label2.place(x=15,y=70)
    ntext = StringVar()
    ntextbox = Entry(screen1, textvariable=ntext, bd=5, width=14)
    ntextbox.place(x=135,y=68)

    calculate_root = Button(screen1, text='=',fg='white', bg="#181F58", command=answer_method, height=2, width=26)
    calculate_root.place(x=33,y=100)
    screen1.bind("<Return>",answer_method)

    choice1 = Button(screen1, text='+', fg='black', bg="#33cc00", command=answer1, height=1, width=7)
    choice2 = Button(screen1, text='-', fg='black', bg="#33cc00", command=answer2, height=1, width=7)


def hcf_method():
    screen3 = Toplevel(window)
    screen3.title("HCF")
    screen3.geometry("250x150")
    screen3.config(bg="#313975")
    screen3.grab_set()

    def method(event = None):
        global expression, equation
        try:
            value1 = int(xtext.get())
            value2 = int(ntext.get())
            answer = math.gcd(value1, value2)
            expression += str(answer)
            equation.set(expression)
            with open("log.txt","a") as f:
                f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+"HCF("+ntext.get()+","+xtext.get()+")"))
            screen3.grab_release()
            screen3.destroy()
        except:
            tkinter.messagebox.showerror("HCF", "Please enter correct values")

    topiclabel = Label(screen3, text="HCF", font="Roboto 16 bold",bg="#313975",fg='white')
    topiclabel.pack(pady=5)

    label1 = Label(screen3, text="Enter num1: ",bg="#535A92",fg='white')
    label1.place(x=15,y=40)

    xtext = StringVar()
    xtextbox = Entry(screen3, textvariable=xtext, bd=5, width=14)
    xtextbox.place(x=135,y=38)

    label2 = Label(screen3, text="Enter num2: ",bg="#535A92",fg='white')
    label2.place(x=15,y=70)
    ntext = StringVar()
    ntextbox = Entry(screen3, textvariable=ntext, bd=5, width=14)
    ntextbox.place(x=135,y=68)

    calculate_root = Button(screen3, text='=',fg='white', bg="#181F58", command=method, height=2, width=26)
    screen3.bind('<Return>',method)
    calculate_root.place(x=33,y=100)


def lcm_method():
    screen4 = Toplevel(window)
    screen4.title("LCM")
    screen4.geometry("250x150")
    screen4.config(bg="#313975")
    screen4.grab_set()

    def method(event = None):
        global expression, equation
        try:
            value1 = int(xtext.get())
            value2 = int(ntext.get())
            answer = np.lcm(value1, value2)
            expression += str(answer)
            equation.set(expression)
            screen4.grab_release()
            screen4.destroy()
        except:
            tkinter.messagebox.showerror("LCM", "Both values need to be an integer")

    topiclabel = Label(screen4, text="LCM(x, n)", font="Roboto 16 bold",bg="#313975",fg='white')
    topiclabel.pack(pady=5)

    label1 = Label(screen4, text="Enter num1: ",bg="#535A92",fg='white')
    label1.place(x=15,y=40)

    xtext = StringVar()
    xtextbox = Entry(screen4, textvariable=xtext,bd=5, width=14)
    xtextbox.place(x=135,y=38)

    label2 = Label(screen4, text="Enter num2: ",bg="#535A92",fg='white')
    label2.place(x=15,y=70)
    
    ntext = StringVar()
    ntextbox = Entry(screen4, textvariable=ntext,bd=5, width=14)
    ntextbox.place(x=135,y=68)

    calculate_root = Button(screen4, text='=',fg='white', bg="#181F58", command=method, height=2, width=26)
    screen4.bind('<Return>',method)
    calculate_root.place(x=33,y=100)

def log():
    log_window = Toplevel(window)
    log_window.title("log()")
    log_window.resizable(False, False)
    log_window.grab_set()

    def log_calculate_method():
        global expression, equation
        try:
            log_answer = math.log(eval(log_expression.get()), eval(log_base.get()))
            expression += str(log_answer)
            equation.set(expression)
            with open("log.txt","a") as f:
                    f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+log_expression.get()+"log"+log_base.get()))
            log_window.grab_release()
            log_window.destroy()
        except:
            tkinter.messagebox.showerror("log()", "Invalid values")

    log_expression = StringVar()
    log_base = StringVar()

    log_label = Label(log_window, text="log(x, base)", font="Roboto 10 bold")
    log_label.pack()

    log_format = Frame(log_window)
    log_format.pack()

    log_label = Label(log_format, text="log(", font="Roboto 10 bold")
    log_label.pack(side="left")
    log_entry = Entry(log_format, textvariable=log_expression, bd=5)
    log_entry.pack(side="left")
    log_entry = Entry(log_format, textvariable=log_base, bd=5)
    log_entry.pack(side="left")
    log_label = Label(log_format, text=")", font="Roboto 10 bold")
    log_label.pack(side="left")

    log_calculate = Button(log_window, text="=", fg='black', bg="#33cc00", command=log_calculate_method, height=1,
                           width=8)
    log_calculate.pack()
    log_window.bind("<Return>",log_calculate_method)

def exponential_calculation():
    global expression
    expression = expression.replace("^", "**")
    with open("log.txt","a") as f:
        f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression))


def modulus_calculation():
    global expression
    expression = expression.replace("MOD", "%")
    with open("log.txt","a") as f:
            f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression))


def div_calculation():
    global expression
    expression = expression.replace("DIV", "//")
    with open("log.txt","a") as f:
            f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression))

def press(num):
    global expression

    if expression == "Please enter a value":
        expression = ""

    expression = expression + str(num)
    equation.set(expression)


def equals(event=None):
    global expression, equation

    try:
        global equation
        if "^" in expression:
            exponential_calculation()
        elif "MOD" in expression:
            modulus_calculation()
        elif "DIV" in expression:
            div_calculation()

        with open("log.txt","a") as f:
            f.write("\n"+str(datetime.datetime.now().strftime( "%m/%d/%Y\t\t\t%H:%M:%S ")+'\t\t'+expression))

        answer = str(round(eval(expression), 10))
        equation.set(answer)
        historyvar.set(answer)
        with open("history.dat","ab") as f:
            pickle.dump(str(answer),f)

    except:
        if expression == "":
            equation.set("Please enter a value")
        else:
            equation.set("Error")
            expression = ""

def backspace(event=None):
    global expression, equation
    try:
        if expression[-1] != "D" and expression[-1] != "V":
            expression = expression[:-1]
            equation.set(expression)
        elif expression[-1] == "D":
            expression = expression.replace("MOD", "")
            equation.set(expression)
        elif expression[-1] == "V":
            expression = expression.replace("DIV", "")
            equation.set(expression)
        else:
            equation.set()
    except:
        pass


def clear(event=None):
    global expression
    expression = ""
    equation.set("")


#######################################################################################

def other_calcs(event=None):
    buttonbg = Label(bg="#2B2537")
    buttonbg.place(x=0,y=191,width=338,height=408)

    sin_button= Button(bg = "#2A2437",image=sin_image,borderwidth=0,highlightthickness=0,command=sin,relief="flat")
    sin_button.place(x=24.0,y=235.0,width=85.0,height=43.0)

    power = Button(bg = "#2A2437",image=power_image,borderwidth=0,highlightthickness=0,command=lambda: press("^"),relief="flat")
    power.place(x=230.0,y=383.0,width=85.0,height=43.0)
    window.bind("^",lambda event:press("^"))

    sqrt = Button(bg = "#2A2437",image=sqrt_image,borderwidth=0,highlightthickness=0,command=root_calculation,relief="flat")
    sqrt.place(x=24.0,y=383.0,width=80.0,height=43.0)

    lcm = Button(bg = "#2A2437",image=lcm_image,borderwidth=0,highlightthickness=0,command=lcm_method,relief="flat")
    lcm.place(x=230.0,y=309.0,width=85.0,height=43.0)

    logbutton = Button(bg = "#2A2437",image=log_image,borderwidth=0,highlightthickness=0,command=log,relief="flat")
    logbutton.place(x=27.0,y=309.0,width=85.0,height=43.0)

    hcf = Button(bg = "#2A2437",image=hcf_image,borderwidth=0,highlightthickness=0,command=hcf_method,relief="flat")
    hcf.place(x=127.0,y=309.0,width=85.0,height=43.0)

    tanbutton = Button(bg = "#2A2437",image=tan_image,borderwidth=0,highlightthickness=0,command=tan,relief="flat")
    tanbutton.place(x=230.0,y=235.0,width=85.0,height=43.0)

    cos_button = Button(bg = "#2A2437",image=cos_image,borderwidth=0,highlightthickness=0,command=cos,relief="flat")
    cos_button.place(x=127.0,y=235.0,width=85.0,height=43.0)

    return1 = Button(bg = "#2A2437",image=return1_image,borderwidth=0,highlightthickness=0,command=normal,relief="flat")
    return1.place(x=27.0,y=521.0,width=53.0,height=53.0)
    window.bind("<Tab>",normal)

    window.bind("<Escape>",clear)

def normal(event=None):
    buttonbg = Label(bg="#2B2537")
    buttonbg.place(x=0,y=191,width=338,height=408)

    button_1 = Button(bg = "#2A2437",image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda:press("+"),    relief="flat")
    button_1.place(x=256.0,y=219.0,width=62.0,height=62.0)
    window.bind('+',lambda event: press("+"))

    button_2 = Button(bg = "#2A2437",image=button_image_2,borderwidth=0,highlightthickness=0,command=other_calcs,relief="flat")
    button_2.place(x=28.0,y=519.0,width=55.292877197265625,height=55.984344482421875)
    window.bind("<Tab>",other_calcs)

    button_3 = Button(bg = "#2A2437",image=button_image_3,borderwidth=0,highlightthickness=0,command=lambda:press("/"),    relief="flat")
    button_3.place(x=256.25,y=442.5,width=62.0,height=62.0)
    window.bind('/',lambda event: press("/"))

    button_4 = Button(bg = "#2A2437",image=button_image_4,borderwidth=0,highlightthickness=0,command=equals,relief="flat")
    button_4.place(x=260.0,y=520.0,width=58.0,height=57.0)
    window.bind("<Return>",equals)

    button_5 = Button(bg = "#2A2437",image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda:press("*"),    relief="flat")
    button_5.place(x=256.0,y=366.0,width=62.0,height=62.0)
    window.bind('*',lambda event: press("*"))

    button_6 = Button(bg = "#2A2437",image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda:press("-"),    relief="flat")
    button_6.place(x=256.0,y=291.0,width=62.0,height=62.0)
    window.bind('-',lambda event: press("-"))

    button_7 = Button(bg = "#2A2437",image=button_image_7,borderwidth=0,highlightthickness=0,command=lambda:press(9),    relief="flat")
    button_7.place(x=180.1477508544922,y=451.0,width=49.050132751464844,height=48.0)
    window.bind('9',lambda event: press(9))

    button_8 = Button(bg = "#2A2437",image=button_image_8,borderwidth=0,highlightthickness=0,command=lambda:press(8),relief="flat")
    button_8.place(x=104.0,y=451.0,width=49.050132751464844,height=47.52490234375)
    window.bind('8',lambda event: press(8))

    button_9 = Button(bg = "#2A2437",image=button_image_9,borderwidth=0,highlightthickness=0,command=lambda: press("."),    relief="flat")
    button_9.place(x=178.0,y=222.0,width=49.0,height=58.0)
    window.bind(".",lambda event: press("."))

    button_10 = Button(bg = "#2A2437",image=button_image_10,borderwidth=0 ,highlightthickness=0 ,command=lambda:press(0),relief="flat")
    button_10.place(x=103.0,y=521.0,width=50.0,height=48.0)
    window.bind('0',lambda event: press(0))

    button_11 = Button(bg = "#2A2437",image=button_image_11 ,borderwidth=0 ,highlightthickness=0 ,command=lambda:press(7),relief="flat")
    button_11.place(x=27.0,y=450.0,width=49.0,height=51.0)
    window.bind('7',lambda event: press(7))

    button_12 = Button(bg = "#2A2437",image=button_image_12 ,borderwidth=0 ,highlightthickness=0 ,command=lambda:press(6),relief="flat")
    button_12.place(x=181.0,y=371.0,width=49.0,height=48.0)
    window.bind('6',lambda event: press(6))

    button_13 = Button(bg = "#2A2437",image=button_image_13 ,borderwidth=0 ,highlightthickness=0 ,command=lambda:press(5),relief="flat")
    button_13.place(x=103.0,y=371.0,width=50.0,height=48.0)
    window.bind('5',lambda event: press(5))

    button_14 = Button(bg = "#2A2437",image=button_image_14 ,borderwidth=0 ,highlightthickness=0 ,command=lambda:press(4),relief="flat")
    button_14.place(x=24.0,y=370.0,width=49.0,height=48.0)
    window.bind('4',lambda event: press(4))

    button_15 = Button(bg = "#2A2437",image=button_image_15 ,borderwidth=0 ,highlightthickness=0, command=lambda:press(2),relief="flat")
    button_15.place(x=103.0,y=299.0,width=50.0,height=49.0)
    window.bind('2',lambda event: press(2))

    button_16 = Button(activebackground="#2A2437",image=button_image_16 ,borderwidth=0   ,highlightthickness=0 ,command=lambda:press(1),relief="flat")
    button_16.place(x=27.0,y=299.0,width=49.0,height=49.0)
    window.bind('1',lambda event: press(1))

    button_17 = Button(bg = "#2A2437",image=button_image_17 ,borderwidth=0 ,highlightthickness=0 ,command=backspace,relief="flat",repeatdelay=1000,repeatinterval=50)
    button_17.place(x=176.0,y=521.0,width=53.0,height=52.0)
    window.bind("<BackSpace>",backspace)

    button_18 = Button(bg = "#2A2437",image=button_image_18 ,borderwidth=0 ,highlightthickness=0 ,command=lambda:press("("),relief="flat")
    button_18.place(x=19.0,y=214.0,width=64.0,height=66.0)
    window.bind("(",lambda event: press("("))

    button_19 = Button(bg = "#2A2437",image=button_image_19 ,borderwidth=0,highlightthickness=0 ,command=lambda:press(")"),relief="flat")
    button_19.place(x=96.0,y=214.0,width=64.0,height=66.0)
    window.bind(")",lambda event: press(")"))

    button_20 = Button(bg = "#2A2437", image=button_image_20 ,borderwidth=0 ,highlightthickness=0 ,command=lambda:press(3),relief="flat")
    button_20.place(x=179.0,y=299.0,width=50.0,height=50.0)
    window.bind("3",lambda event:press(3))

    window.bind("<Escape>",clear)
normal()

window.resizable(False, False)
window.mainloop()