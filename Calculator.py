from tkinter import *


root = Tk()
root.title("Rahul's Calculator")

opr_no = 0
current_num_sum = 0
current_num_minus = 0
current_num_div = 0
current_num_mul = 0

e = Entry(root, width = 50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def button_click(number, entry):
        current_number = e.get()
        e.delete(0, END)
        e.insert(0, str(current_number) + str(number))


def sum_click():
    global current_num_sum, opr_no
    if opr_no == 0:
        new_current_number = 0
        current_num_sum = e.get()
        if current_num_sum != "":
            e.delete(0, END)
            opr_no = 1
        else:
            print("please input a number")
            pass
    elif opr_no == 1:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_num_sum):
            current_num_sum = float(current_num_sum) + float(new_current_number)
            e.insert(0, current_num_sum)
        else:
            current_num_sum = int(current_num_sum) + int(new_current_number)
            e.insert(0, str(current_num_sum))

def minus_click():
    global current_num_minus, opr_no
    if opr_no == 0:
        new_current_number = 0
        current_num_minus = e.get()
        if current_num_minus != "":
            e.delete(0, END)
            opr_no = 2
        else:
            print("please input a number")
            pass
    elif opr_no == 2:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_num_minus):
            current_num_minus = float(current_num_minus) - float(new_current_number)
            e.insert(0, current_num_minus)
        else:
            current_num_minus = int(current_num_minus) - int(new_current_number)
            e.insert(0, str(current_num_minus))

def multiply_click():
    global current_num_mul, opr_no
    if opr_no == 0:
        new_current_number = 0
        current_num_mul = e.get()
        if current_num_mul != "":
            e.delete(0, END)
            opr_no = 3
        else:
            print("please input a number")
            pass
    elif opr_no == 3:
        new_current_number = e.get()
        e.delete(0,END)
        if "." in str(current_num_mul):
            current_num_mul = float(current_num_mul) * float(new_current_number)
            e.insert(0, current_num_mul)
        else:
            current_num_mul = int(current_num_mul) * int(new_current_number)
            e.insert(0, str(current_num_mul))

def division_click():
    global current_num_div, opr_no
    if opr_no == 0:
        new_current_number = 0
        current_num_div = e.get()
        if current_num_div != "":
            e.delete(0, END)
            opr_no = 4
        else:
            print("please input a number")
            pass
    elif opr_no == 4:
        new_current_number = e.get()
        e.delete(0,END)

        try:
            if "." in str(current_num_div):
                current_num_div = float(current_num_div) / float(new_current_number)
                e.insert(0, current_num_div)
            else:
                current_num_div = int(current_num_div) / int(new_current_number)
                e.insert(0, str(current_num_div))
        except ZeroDivisionError:
            e.insert(0, 'Can not divide by zero.')

def toPowerof():
    global current_number_power, opr_no
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        opr_no = 5
    else:
        print("please input a number")
        pass

def positive_negative():
    try:
        current_number = e.get()
        e.delete(0, END)
        if "." in current_number:
            e.insert(0, -(float(current_number)))
        else:
            e.insert(0, -(int(current_number)))
    except:
        print("There is no number")
        pass

def delete():
    try:
        current_number = e.get()
        e.delete(0, END)
        current_number = current_number[:-1]
        e.insert(0, current_number)
    except:
        print("No number to delete")
        pass

def add_point():
    current_number = e.get()
    if "." in current_number:
        print("Number already has a point")
        pass
    else:
        if current_number != "":
            current_number = str(current_number) + str(".")
            e.delete(0,END)
            e.insert(0, current_number)
        else:
            current_number = "0."
            e.insert(0, current_number)

def equals_click():
    global current_num_sum, current_num_minus, current_num_mul, opr_no
    current_number = e.get()
    e.delete(0, END)
    if opr_no == 0:
        e.insert(0,current_number)
        print("nothing to do")
    elif opr_no == 1:
        if "." in str(current_num_sum):
            e.insert(0, float(current_num_sum) + float(current_number))
            opr_no = 0
        else:
            e.insert(0, int(current_num_sum) + int(current_number))
            opr_no = 0
    elif opr_no == 2:
        if "." in current_num_minus:
            e.insert(0, float(current_num_minus) - float(current_number))
            opr_no = 0
        else:
            e.insert(0, int(current_num_minus) - int(current_number))
            opr_no = 0
    elif opr_no == 3:
        if "." in current_num_mul:
            e.insert(0, float(current_num_mul) * float(current_number))
            opr_no = 0
        else:
            e.insert(0, int(current_num_mul) * int(current_number))
            opr_no = 0
    elif opr_no == 4:

        try:
            if "." in current_num_div:
                e.insert(0, float(current_num_div) / float(current_number))
                opr_no = 0
            else:
                e.insert(0, int(current_num_div) / int(current_number))
                opr_no = 0
        except ZeroDivisionError:
            e.insert(0, 'Can not divide by zero.')

    elif opr_no == 5:
        if "." in current_number_power:
            e.insert(0, float(current_number_power) ** float(current_number))
            opr_no = 0
        else:
            e.insert(0, int(current_number_power) ** int(current_number))
            opr_no = 0

def clear_entry():
    global current_num_sum, current_num_minus, current_num_mul,current_num_div, opr_no
    opr_no = 0
    current_num_sum = 0
    current_num_mul = 0
    current_num_minus = 0
    current_num_div = 0
    e.delete(0, END)

button_powerto = Button(root, borderwidth=2, text="xY",padx=36, pady=20, command= lambda: toPowerof()).grid(row=5, column=2)
button_point = Button(root, borderwidth=2, text=".", padx=41, pady=20, command= lambda: add_point()).grid(row=5, column=1)

button_sum = Button(root, borderwidth=2, text="+", padx=37, pady=20, command= lambda: sum_click()).grid(row=3, column=3)
button_equals = Button(root, borderwidth=2, text="=", padx=36, pady=20, command= lambda: equals_click()).grid(row=5, column=3)
button_clear = Button(root, borderwidth=2, text="CE", padx=37, pady=20,command= lambda: clear_entry()).grid(row=4, column=0)

button_minus = Button(root, borderwidth=2, text="-", padx=38, pady=20, command= lambda: minus_click()).grid(row=2, column=3)
button_multiply = Button(root, borderwidth=2, text="X", padx=37, pady=20, command= lambda: multiply_click()).grid(row=1, column=3)
button_negative_positive = Button(root, borderwidth=2, text="+/-", padx=37, pady=20, command= lambda: positive_negative()).grid(row=4, column=2)

button_divide = Button(root, borderwidth=2, text="/", padx=38, pady=20, command= lambda: division_click()).grid(row=4, column=3)
button_del = Button(root, borderwidth=2, text="DEL",fg='red', padx=34, pady=20, command= lambda: delete()).grid(row=5, column=0)
button_0 = Button(root, borderwidth=2, text="0", padx=40, pady=20, command=lambda: button_click(0, e)).grid(row=4, column=1)

button_1 = Button(root, borderwidth=2, text="1", padx=40, pady=20, command=lambda: button_click(1, e)).grid(row=3, column=0)
button_2 = Button(root, borderwidth=2, text="2", padx=40, pady=20, command=lambda: button_click(2, e)).grid(row=3, column=1)
button_3 = Button(root, borderwidth=2, text="3", padx=40, pady=20, command=lambda: button_click(3, e)).grid(row=3, column=2)

button_4 = Button(root, borderwidth=2, text="4", padx=40, pady=20, command=lambda: button_click(4, e)).grid(row=2, column=0)
button_5 = Button(root, borderwidth=2, text="5", padx=40, pady=20, command=lambda: button_click(5, e)).grid(row=2, column=1)
button_6 = Button(root, borderwidth=2, text="6", padx=40, pady=20, command=lambda: button_click(6, e)).grid(row=2, column=2)

button_7 = Button(root, borderwidth=2, text="7", padx=40, pady=20, command=lambda: button_click(7, e)).grid(row=1, column=0)
button_8 = Button(root, borderwidth=2, text="8", padx=40, pady=20, command=lambda: button_click(8, e)).grid(row=1, column=1)
button_9 = Button(root, borderwidth=2, text="9", padx=40, pady=20, command=lambda: button_click(9, e)).grid(row=1,column=2)



root.mainloop()
