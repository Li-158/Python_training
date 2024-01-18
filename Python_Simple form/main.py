import tkinter as tk

import tkinter.font as tkF


def submit_form():
    # Use a breakpoint in the code line below to debug your script.
    name = name_entry.get()
    address = address_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    line = line_entry.get()
    if not (name and address and age and gender):
        tk.Label(window, text="Please fill the basic information",bg= 'red').place(x=200, y=550)
    else:
        #Create a new row with the user input
        new_row = [name, address, age, gender, email, line]
        file_path = "user_data.txt"

        # 開啟文件並寫入新行數據
        with open(file_path, 'a') as file:
            file.write(','.join(new_row) + '\n')

window = tk.Tk()
window.title('test')
window.geometry('500x700')

# 姓名
name_label = tk.Label(window, text="Name")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

#地址
address_label = tk.Label(window, text="Address")
address_label.pack()
address_entry = tk.Entry(window)
address_entry.pack()

# Gender
gender_label = tk.Label(window, text="Gender")
gender_label.pack()

gender_var = tk.StringVar()
gender_btn_male = tk.Radiobutton(window, text = "男", variable=gender_var, value='Male')
gender_btn_male.pack()
gender_btn_male.select()
gender_btn_female = tk.Radiobutton(window, text = "女", variable=gender_var, value= 'Female')
gender_btn_female.pack()

#Age
age_label = tk.Label(window, text ="Age")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

#Email or line


def checkbox_change():
    if var_btn1.get() == "Email":
        email_label.pack()
        email_entry.pack()
    else:
        email_label.pack_forget()
        email_entry.pack_forget()

    if var_btn2.get() == "Line":
        line_label.pack()
        line_entry.pack()
    else:
        line_label.pack_forget()
        line_entry.pack_forget()

contect_label = tk.Label(window, text="Contect information(Email or Line)")
contect_label.pack()
var_btn1 = tk.StringVar()
check_btn1 = tk.Checkbutton(window, text= "Email", onvalue= "Email", offvalue= "1", variable=var_btn1,
                            command = checkbox_change)
check_btn1.pack()
check_btn1.deselect()

var_btn2 = tk.StringVar()
check_btn2 = tk.Checkbutton(window, text= "Line", onvalue= "Line", offvalue= "1", variable=var_btn2,
                           command = checkbox_change)
check_btn2.pack()
check_btn2.deselect()
# Input the line and email information
email_label = tk.Label(window, text="Email")
email_entry = tk.Entry(window)

line_label = tk.Label(window, text="Line")
line_entry = tk.Entry(window)

submit_btn = tk.Button(window, text= "Submit", command= submit_form)
submit_btn.place(x=220,y=600)

window.mainloop()

