import tkinter as tk
from PIL import Image, ImageTk

imgpath = "D:\\desktop\\programming\\desktop-pet\\src\\cat.png"
icopath = "D:\\desktop\\programming\\desktop-pet\\src\\cat.ico"
updateTime = 500 # in ms

image = Image.open(imgpath)
resizedImageBig = image.resize((300, 300))
resizedImageSmall = image.resize((100, 100))

status = 1 #i=1 for big, i=0 for small

windowOffset = "+100+100"

#creat root window
window = tk.Tk()
window.title("Cat!")
window.geometry("500x500"+windowOffset)
window.resizable(False, False)
window.iconbitmap(icopath)
#window.overrideredirect(True) # remove the title bar
window.configure(highlightthickness="2", highlightbackground="black")
window.wm_attributes("-transparentcolor", "black") # set the transparent color

# create a label
catImageBig = ImageTk.PhotoImage(resizedImageBig) # make the image object
catImageSmall = ImageTk.PhotoImage(resizedImageSmall) # make the image object

label = tk.Label(window, bd=0, bg="black")
label.configure(image=catImageBig)
label.image = catImageBig  # Keep a reference
label.pack() # add the label to the window

def update():
    global status
    if status == 1:
        label.configure(image=catImageSmall)
        label.image = catImageSmall  # Update the reference
        status = 0
    else:
        label.configure(image=catImageBig)
        label.image = catImageBig  # Update the reference
        status = 1

    # Schedule the next update
    window.after(updateTime, update)

window.after(updateTime, update) # update the image every 500ms

window.mainloop() # at last line