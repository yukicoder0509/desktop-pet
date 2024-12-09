import tkinter as tk

imgFolderPath = "D:\\desktop\\programming\\desktop-pet\\src\\catgif\\"
imageSize = "100x100"
curFrameIdx = 0
windowpos = [100, 100]

def windowPosStr():
    return "+" + str(windowpos[0]) + "+" + str(windowpos[1])

# create root window
window = tk.Tk()
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
    if curFrameIdx == len(walk_left):
        curFrameIdx = 0
    label.configure(image=walk_left[curFrameIdx])
    label.image = walk_left[curFrameIdx]
    curFrameIdx += 1
    window.after(100, update)

window.after(100, update)
window.mainloop()