import tkinter as tk

calculation = ""
import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end  ")
    text_result.insert(1.0,calculation)


def evaluate_calculation():
    global calculation
    print(calculation)
    try:

         result = str(eval(calculation))
         calculation =""
         text_result.delete(1.0, "end")
         text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, result)


def clear_field():
    global calculation
    calculation =" "
    text_result.delete(1.0,"end")


root = tk.Tk()
root.geometry("315x275")

text_result =tk.Text(root, height=1,width=18 ,font=("lucid",23))
text_result.grid(columnspan=5)


btn_1 = tk.Button(root, text="1", command=lambda : add_to_calculation(1),padx= 4,pady=4, width=5 , bg="grey", font=("lucida 14 bold"))
btn_1.grid(row=2, column=1, pady=1,padx=1)
btn_2 = tk.Button(root, text="2", command=lambda : add_to_calculation(2),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda : add_to_calculation(3),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda : add_to_calculation(4),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_4.grid(row=3, column=1,pady=1,padx=1)
btn_5 = tk.Button(root, text="5", command=lambda : add_to_calculation(5),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda : add_to_calculation(6),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda : add_to_calculation(7),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_7.grid(row=4, column=1,pady=1,padx=1)
btn_8 = tk.Button(root, text="8", command=lambda : add_to_calculation(8),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda : add_to_calculation(9),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda : add_to_calculation(0),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_0.grid(row=5, column=2,pady=1,padx=1)
btn_plus = tk.Button(root, text="+", command=lambda : add_to_calculation("+"),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_plus.grid(row=2, column=4)
btn_mul = tk.Button(root, text="*", command=lambda : add_to_calculation("*"), padx= 4,pady=4,width=5 ,bg="grey", font=("lucida 14 bold"))
btn_mul.grid(row=3, column=4)
btn_minus = tk.Button(root, text="-", command=lambda : add_to_calculation("-"),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_minus.grid(row=4, column=4,pady=1,padx=1)
btn_div= tk.Button(root, text="/", command=lambda : add_to_calculation("/"),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_div.grid(row=5, column=4)
btn_open= tk.Button(root, text="(", command=lambda : add_to_calculation("("),padx= 4,pady=4, width=5 , bg="grey",font=("lucida 14 bold"))
btn_open.grid(row=5, column=1)
btn_close= tk.Button(root, text=")", command=lambda : add_to_calculation(")"),padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_close.grid(row=5, column=3,pady=1,padx=1)
btn_clear= tk.Button(root, text="c", command = clear_field(),width=5 ,padx= 4,pady=4,bg="grey", font=("lucida 14 bold"))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equals= tk.Button(root, text="=", command= evaluate_calculation,padx= 4,pady=4, width=5 ,bg="grey", font=("lucida 14 bold"))
btn_equals.grid(row=6, column=3, columnspan=2)
btn_dot= tk.Button(root, text=".", command= lambda :add_to_calculation("."),padx= 4,pady=4, width=5 , bg="grey",font=("lucida 14 bold"))
btn_dot.grid(row=6, column=2, columnspan=2)
root.mainloop()