from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import webbrowser

root = Tk()
root.title("Flappy Plane Launcher")
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
root.configure(bd=5,relief="raised")

def launchgame():
    webbrowser.open("http://71.19.146.161/")
    print("DEBUG")
    messagebox.showinfo("Launched", "Game should be launched. Check your browser!")


# header
txt1 = Label(text="\nPlay Flappy Plane - September Edition\nVersion: 9/11\n", font="liberationserif 15 bold")
txt1.pack()

# img
img1 = Image.open("img1.jpg")
imtk = ImageTk.PhotoImage(img1)
imglbl = Label(image=imtk)
imglbl.pack()

# launch button
lncbutton = Button(text="Launch", bg="green", fg="white", font="liberationmono 12 bold", bd=5,relief="raised", command=launchgame)
lncbutton.pack(pady=12)

# warn
lncwarn = Label(text="An active internet connection is\nrequired to play the game.", fg="red",font="liberationmono 8")
lncwarn.pack()

# footer
txt2 = Label(text="Launcher developed by bedanta.tech.\nAll power to the developer u/flappyplanedev on Reddit.")
txt2.pack(side="bottom")

root.mainloop()