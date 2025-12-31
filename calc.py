
import tkinter as tk  #imports tkinter module as tk is an alias for easy acces

#button click handler
def press(v):  
    entry.insert(tk.END,v) 
    ''' called when a no/operator nutton clicked .
     inserts the pressed value at end of entry widget'''
    
#clear or delete functiom
def clear():
    entry.delete(0,tk.END)
    'it clear the calcu screen and delete all values from 0-End'
def back():
    curr=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,curr[:-1])

#Calculator Function
def calc():
    try:
        result=eval(entry.get()) #eval(): evaluates string as python expression
        'entry.get():retrives data e.g(2+4)'
        entry.delete(0,tk.END)  #claer the screen before displaying o/p
        entry.insert(0,result)  #display exception instead of crashing
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"INVALID EXPRESSION") #hanles invalid exp(e.g.5--)
        'Displays "Exception instead of crahsing"'

#Main window creation
root=tk.Tk() #crates amin window for our application
root.title("SIMPLE CALCULATOR APPLICATION")
root.configure(bg="#a8a3a3") #it gives background color 
root.resizable(False,False) #disable resizing window(static)

#entry widget to display screen
entry=tk.Entry(
    root,
    font=("Times new roman",20),
    bg="#5f5f5f",
    fg="white",
    bd=0,
    justify="right"
)
'''Text-i/p field.Acts as calcu display
   right aligned is done for better look'''
entry.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)

#button labels
buttons=[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]
'''represent calculator buttons
stored in lst to reduce repetative code'''

#dynamic button creation
r=1
c=0 
'''rows and col for grid layout'''

for b in buttons:
    cmd=calc if b=="=" else lambda x=b:press(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
       font=("Calibri",14),
        width=5,
        height=2,
        bg="#9B7D29" if b in "+-*/" else "#2d4460",
        fg="white",
        bd=0
    ).grid(row=r,column=c,padx=6,pady=6)
    c+=1
    if c==4:
        r+=1
        c=0 #moves to next row after 4 buttons
#back button
tk.Button(
    root,
    text="🔙",
    command=back,
    font=("Calibri",14),
    width=5,
    height=2,
    bg="#9B7D29",
    bd=0
    ).grid(row=r,column=0,columnspan=4,pady=4)

#clear button
tk.Button(
    root,
    text="clear",
    command=clear,
    font=("Calibri",14),
    width=5,
    height=2,
    bg="#9B7D29",
    bd=0

).grid(row=r,column=2,columnspan=4,pady=4)
'''clears the calculator display screen and
spans across all columns'''


#event loop
root.mainloop()
'''keeps the window running
listen for user interactions'''







 

















