from Tkinter import *
from PIL import Image, ImageTk
import tkFileDialog
import cv2
import numpy as np
global path
size = 300,300
size1 = 750,225
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
    img.place(x=20,y=50)

def Encode():
    global path
    data = txt.get(1.0, "end-1c")
    img = cv2.imread(path)
    data = [format(ord(i), '08b') for i in data]
    h,w,_ = img.shape
    PixReq = len(data) * 3
    RowReq = PixReq/w
    count = 0
    charCount = 0
    for i in range(RowReq + 1):
        while(count < w and charCount <len(data)):
            char = data[charCount]
            charCount += 1
            for ck,k in enumerate(char):
                if((k == '1' and img[i][count][ck%3]%2 == 0) or (k == '0' and img[i][count][ck%3]%2 == 1)):
                    img[i][count][ck%3] -=1
                if(ck%3 == 2):
                    count +=1
                if(ck == 7):
                    if(charCount*3 < PixReq and img[i][count][2]%2 == 1):
                        img[i][count][2] -= 1
                    if(charCount*3 >= PixReq and img[i][count][2]%2 == 0):
                        img[i][count][2] -=1
                    count +=1
        count = 0
    cv2.imwrite("encrypted.png",img)

    encrypt = Image.open("encrypted.png")
    encrypt.thumbnail(size1, Image.ANTIALIAS)
    encrypt = np.asarray(encrypt)
    encrypt = Image.fromarray(np.uint8(encrypt))
    render = ImageTk.PhotoImage(encrypt)
    img1 = Label(root, image = render)
    img1.image = render
    img1.place(x=125,y=350)

    lbl = Label(root, text = "Encrypted Image", bg='lavender',font = ("Times New Roman",20))
    lbl.place(x = 60, y = 300)
    
root = Tk()
root.configure(background='lavender')
root.title("Encoder")
root.geometry('600x600')
btn = Button(root, text = "choose Image", bg='grey',fg='black',command = click)
btn.place(x = 250, y = 10)

txt = Text(root, wrap = WORD, width = 30)
txt.place(x = 340, y = 55, height = 165)

btn1 = Button(root, text = "Encode", bg='gray', fg='black', command = Encode)
btn1.place(x = 435, y = 230)
root.mainloop()



