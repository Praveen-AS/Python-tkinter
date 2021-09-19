from tkinter import *
import math

base = Tk()
base.geometry("420x500")
base.title("BMI Calculator")
base.configure(borderwidth="1")

def validate():
    a=agee.get()
    h=heighte.get()
    w=weighte.get()
    if a.isdecimal():
       val1.config(text="")
    else:
       val1.config(text="It should be a number!", fg="red")
    if h.isdecimal():
       val2.config(text="")
    else:
       val2.config(text="It should be a number!", fg="red")
    if w.isdecimal():
       val3.config(text="")
    else:
       val3.config(text="It should be a number!", fg="red")

    calculateBMI(a,h,w)

def calculateBMI(age,height,weight):
    if age.isdecimal() and height.isdecimal() and weight.isdecimal():
       wei= int(weight)
       hei= int(height)
       heightmeter=hei/100
       bmi=wei/(heightmeter**2)
       truncate=math.trunc(bmi)
       status=BMIstatus(truncate)
       BMI.config(text=status)

def BMIstatus(BMI1):
    if int(BMI1)<20:
       return 'UnderWeight!'
    elif int(BMI1)>18 and int(BMI1)<=24:
       return 'Healthy!'
    elif int(BMI1)>25 and int(BMI1)<=29:
       return 'OverWeight!'
    else:
       return 'Obesity! You need a care!'

heading=Label(base,text="Hello!! Calculate BMI??",font=('Helvetica bold',20))
heading.pack(pady=10)
agel=Label(base,text="AGE")
agel.pack(pady=5)
agee=Entry(base,text="age",width=30,bg="green",justify="center")
agee.pack(ipady=5)
val1=Label(base,text="")
val1.pack(pady=3)

heightl=Label(base,text="HEIGHT (cm)")
heightl.pack(pady=5)
heighte=Entry(base,text="height",width=30,bg="orange",justify="center")
heighte.pack(ipady=5)
val2=Label(base,text="")
val2.pack(pady=3)

weightl=Label(base,text="WEIGHT (kgs)")
weightl.pack(pady=5)
weighte=Entry(base,text="weight",width=30,bg="blue",justify="center")
weighte.pack(ipady=5)
val3=Label(base,text="")
val3.pack(pady=3)

calculate= Button(base,text="Calculate BMI",width=10,height=1,command=validate)
calculate.pack(pady=20)

BMIlabel=Label(base,text="RESULT here!",width=30,fg="green")
BMIlabel.pack(pady=3)
BMI=Label(base,text="",relief="sunken",width=30,bg="yellow")
BMI.pack(pady=3,ipady=5)

base.mainloop()
