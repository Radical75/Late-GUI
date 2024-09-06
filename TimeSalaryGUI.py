from tkinter import *
from tkinter import messagebox
root = Tk()
root.config(background="black",borderwidth=12)
root.title("Late No More")
root.geometry("400x400")
#Entry for employee name
n = Entry(root, width=15)
n.grid(column=1,row=0)

#Entry for employee ID
i = Entry(root, width=15)
i.grid(column=1,row=3)

n_lbl = Label(root,text="Enter your name",fg="white",bg="black")
n_lbl.grid(column=0,row=0)

i_lbl = Label(root,text="Enter your employee ID",fg="white",bg="black")
i_lbl.grid(column=0,row=3)

from datetime import datetime

def Login(employeeName, employeeLvl):
    f = open("employee.txt", "r")
    for d in f:
        pos = d.rfind("/")
        employeeName.append(d[:pos])
        employeeLvl.append(int(d[pos+1]))


def employee():
    EmployeeList = []
    employee_lvl = []
    salary =[]

    Login(EmployeeList, employee_lvl)
    for d in range(len(employee_lvl)):
        salary.append(employee_lvl[d] * 20000)

    def isValid(employee_name, EmployeeList):
        if employee_name in EmployeeList:
            return True
        else:
            return False    
    
    name = n.get()
    if name == "" and i.get() == "":
        messagebox.showerror("Invalid input","Please enter your name and employee ID")
    elif not(i.get().isnumeric()):
        messagebox.showerror("Invalid input", "Please enter a number!")
    else:
        id = int(i.get()) 
        check_in_time = datetime.now().strftime("%H:%M:%S")
        if not isValid(name, EmployeeList):
            messagebox.showerror("Invalid User", "User does not exist")
        else:
            for d in range(len(EmployeeList)):
                if name == EmployeeList[d]:
                    j = d

            messagebox.showinfo("result",f"Employee {name},employee id number {id} accepted. You arrived at {check_in_time} ")
            
            hours = int(check_in_time[:2])
            minutes = int(check_in_time[3:5])
            if hours ==8 and minutes == 0:
                messagebox.showinfo("result",f"Just on time!")
            elif hours >= 8:
                messagebox.showinfo("result",f"{name}, {id} you are late! You arrived at {check_in_time} as a result your salary will be deducted.")
                if hours == 8 and minutes >0:
                    salary[j] -= 30
                    messagebox.showinfo("result",f"Your new deducted salary is R{salary[j]}")
                elif hours == 9:
                    salary[j] -= 50
                    messagebox.showinfo("result",f"Your new deducted salary is R{salary[j]}")
                else:
                    messagebox.showinfo("result","Report to the office!")

            elif hours < 8:
                messagebox.showinfo("result",f"You arrived at {check_in_time},You are early! No money will be deducted from your salary")

        
        
def help():
    h = Label(root,borderwidth=12)
    messagebox.showinfo("Help","Enter your employee name and employee ID")

btn = Button(root,text="Enter",fg="white",bg="green" ,borderwidth=12,command=employee)
btn.grid(column=1,row=6)
hbtn = Button(root,text="HELP",borderwidth=12,fg="black",bg="red",command=help)
hbtn.grid(column=0,row=1000)
root.mainloop()