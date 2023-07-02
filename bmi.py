from tkinter import *
from functools import *
import tkinter as tk

window=tk.Tk()
window.title("BMI-Calculator")

def bmi(label_result, ht, wt):  
    ht = float((ht.get()))  
    wt = float((wt.get()))
    ht=ht/100
    bmi=float(wt / (ht*ht))
    bmi=round(bmi,1)

    conclusion=""

    if bmi<18.5: 
      conclusion="Under Weight" 
    elif bmi>18.4 and bmi<=24.9: 
      conclusion="Normal" 
    elif bmi>24.9 and bmi<=29.9:
      conclusion="Over Weight"
    else:
      conclusion="Obesity"

    output= "BMI = "+str(bmi)+"\n" +conclusion

    label_result.config(text=output)
    return

ht = tk.StringVar()  
wt = tk.StringVar()  

heightText=Label(window,text="Height (CM)").grid(row=0, padx=10,pady=10)
height=Entry(window, textvariable = ht ).grid(row=0, column=1, padx=10,pady=10)

weightText=Label(window,text="Weight (KG)").grid(row=1, padx=10,pady=5)
weight=Entry(window, textvariable = wt ).grid(row=1, column=1, padx=10,pady=5)

labelResult = tk.Label(window) 
labelResult.grid(row=4, column=0)

bmi = partial(bmi, labelResult, ht, wt)  
btn=Button(window,text="Calculate",command = bmi).grid(row=2, column=1, padx=20,pady=5)

window.geometry("350x300+12+10")
window.mainloop()