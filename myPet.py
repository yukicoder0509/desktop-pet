import tkinter as tk

imgFolderPath = "D:\\desktop\\programming\\desktop-pet\\src\\catgif\\"
imageSize = "100x100"
curFrameIdx = 0
xSpeed = -5
ySpeed = 5

# create root window
window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
windowpos = [screen_width-100, 0]

def windowPosStr():
    return "+" + str(windowpos[0]) + "+" + str(windowpos[1])

# config the window
window.title("My Pet")
window.geometry(imageSize+windowPosStr())
window.resizable(False, False)
window.configure(highlightbackground="black")
window.wm_attributes("-transparentcolor", "black")

# create a label
label = tk.Label(window, bd=0, bg="black")
label.pack()

# create frames
walk_left = [tk.PhotoImage(file=imgFolderPath+'walkleft.gif',format = 'gif -index %i' %(i)) for i in range(8)]
#===========================================
def update():
    global walk_left
    global curFrameIdx
    global windowpos
    global xSpeed

    if curFrameIdx == len(walk_left):
        curFrameIdx = 0

    label.configure(image=walk_left[curFrameIdx])
    label.image = walk_left[curFrameIdx]

    if windowpos[0] < 0:
        xSpeed = 5
    elif windowpos[0] > screen_width-100:
        xSpeed = -5
    windowpos[0] += xSpeed
    window.geometry(imageSize+windowPosStr())

    curFrameIdx += 1
    window.after(100, update)

window.after(100, update)
window.mainloop()