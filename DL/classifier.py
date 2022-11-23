from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import cv2

width = 600
height = 450

win = Tk()

win.grid_columnconfigure(0, weight=1)
# win.configure(background="gray")
win.title("BlackSwan")
win.geometry(f'{width}x{height}')
win.resizable(False, False)


Label(win, text="Fall Classifier", font=("맑은 고딕", 20, "bold")).grid(row=0, column=0, padx=5, pady=5)

def open_dialog():
    global img
    
    file = filedialog.askopenfilename(initialdir="/")    
    entered_file.delete(0, "end")
    entered_file.insert(0, file)

    
    if os.path.splitext(file)[1] =='.jpg':
        img = Image.open(file).convert("RGB")
        img = img.resize((224, 224))
        img.save("result.png", 'png')
        
    img = PhotoImage(file="result.png")
    label_img.config(image=img)
    
    os.remove('result.png')


entered_file = Entry(win, width=50)
entered_file.grid(row=1, column=0)

button = Button(win, text="Upload", command=open_dialog)
button.grid(row=2, column=0, pady=(0,10)) 

py_img = PhotoImage(file="./images/noimg.png", master=win)
label_img = Label(win, image=py_img)
label_img.grid(row=3, column=0)

classifier_btn = Button(win, text="Classifiy", width=15)
classifier_btn.grid(row=4, column=0)

font = ("맑은 고딕", 10, "bold")
result = Frame(win)
result.grid(row=5, column=0, pady=10)
Label(result, text="Prediction", font=font).grid(row=0, column=0, padx=10)
Label(result, text="Probability", font=font).grid(row=0, column=1, padx=10)

ans = Frame(win)
ans.grid(row=6, column=0)
pred = Label(ans, text="fall", font=font, fg="blue").grid(row=0, column=0, padx=10)
ans.columnconfigure(1, minsize=50)
prob = Label(ans, text="99", font=font, fg="blue").grid(row=0, column=2, padx=10)

win.mainloop()