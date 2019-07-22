from Tkinter import *
from PIL import Image, ImageTk
import tkFileDialog
import cv2
import numpy as np
global path

size = 1300, 250

def Decrypt():
    global path
    img = cv2.imread(path)
    h,w,_ = img.shape
    data = []
    stop = False
    for ci,i in enumerate(img):
        i.tolist()
        for cj,j in enumerate(i):
            if((cj)%3 == 2):
                data.append(bin(j[0])[-1])
                data.append(bin(j[1])[-1])
                if(bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                data.append(bin(j[0])[-1])
                data.append(bin(j[1])[-1])
                data.append(bin(j[2])[-1])
        if(stop):
            break
    msg = []
    for i in range((len(data)+1)/8):
        msg.append(data[i*8:(i*8+8)])

    msg = [chr(int(''.join(i),2)) for i in msg]
    msg = ''.join(msg)
    lbl = Label(root, text = msg, bg='lavender',font=("Times New Roman",10))
    lbl.place(x = 30, y = 400)
    

def click():
    global path
    path=tkFileDialog.askopenfilename()
    load = Image.open(path)
    load.thumbnail(size, Image.ANTIALIAS)
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    render = ImageTk.PhotoImage(load)
    img = Label(root, image = render)
    img.image = render
    img.place(x=100,y=50)

    btn1 = Button(root, text = "Decrypt", bg='grey', fg='black', command = Decrypt)
    btn1.place(x = 270, y = 320)



root = Tk()
root.configure(background='lavender')
root.title("Decoder")
root.geometry('600x600')
btn = Button(root, text = "choose Image", bg='grey',fg='black',command = click)
btn.place(x = 250, y = 10)



root.mainloop()
