import tkinter as tk
from Physics.ProjectileMotion import routeByTop
from pynput.mouse import Controller

class Pet:
    def __init__(self, root:tk.Tk, startPos:list):
        self.root = root
        self.imgFolderPath = "D:\\desktop\\programming\\desktop-pet\\src\\catgif\\"
        self.curFrameIdx = 0
        self.windowpos = startPos
        self.xSpeed = 5
        self.imageSize = "100x100"
        self.mousePos = [0,0]
        
        # Get screen size
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        
        # Create label
        self.label = tk.Label(root, bd=0, bg="black")
        self.label.pack()
        self.label.bind("<Button-1>", self.pause)

        # create frames
        self.walk_left_frames = [tk.PhotoImage(file=self.imgFolderPath+'walkleft.gif',format = 'gif -index %i' %(i)) for i in range(8)]
        self.walk_right_frames = [tk.PhotoImage(file=self.imgFolderPath+'walkright.gif',format = 'gif -index %i' %(i)) for i in range(8)]

        #start the update
        self.update_id = self.walk_right()
    
    def get_mouse_pos(self):
        mouse = Controller()
        position = mouse.position
        self.mousePos = [position[0], position[1]]
        print("cat at" ,self.windowpos)
        print("mouse at" ,self.mousePos)

    def windowPosStr(self):
        return f"+{self.windowpos[0]}+{self.windowpos[1]}"
        
    def walk_left(self):
        if self.curFrameIdx == len(self.walk_left_frames):
            self.curFrameIdx = 0
        
        # update the image
        self.label.configure(image=self.walk_left_frames[self.curFrameIdx])
        self.label.image = self.walk_left_frames[self.curFrameIdx]
        self.curFrameIdx += 1

        # update the window position
        self.windowpos[0] += self.xSpeed
        self.root.geometry(self.imageSize + self.windowPosStr())

        if self.windowpos[0] > self.screen_width:
            self.xSpeed = -5
        elif self.windowpos[0] < 0:
            self.xSpeed = 5

        if self.xSpeed < 0:
            self.update_id = self.root.after(100, self.walk_left)
        else:
            self.update_id = self.root.after(100, self.walk_right)
    
    def walk_right(self):
        if self.curFrameIdx == len(self.walk_right_frames):
            self.curFrameIdx = 0
        
        # update the image
        self.label.configure(image=self.walk_right_frames[self.curFrameIdx])
        self.label.image = self.walk_left_frames[self.curFrameIdx]
        self.curFrameIdx += 1

        # update the window position
        self.windowpos[0] += self.xSpeed
        self.root.geometry(self.imageSize + self.windowPosStr())

        if self.windowpos[0] > self.screen_width:
            self.xSpeed = -5
        elif self.windowpos[0] < 0:
            self.xSpeed = 5

        if self.xSpeed > 0:
            self.update_id = self.root.after(100, self.walk_right)
        else:
            self.update_id = self.root.after(100, self.walk_left)
    
    def jumpByTop(self, positions):
        if positions == None:
            # get mouse position and generate a route by it
            self.get_mouse_pos()
            curPos = (self.windowpos[0], self.windowpos[1])
            topPos = (self.mousePos[0], self.mousePos[1])
            gravity = 5
            samplePoint = 10
            positions = routeByTop(curPos, topPos, gravity, samplePoint)
            self.update_id = self.root.after(100, lambda: self.jumpByTop(positions))
        
        else:
            if len(positions) == 0:
                self.update_id = self.root.after(1000, self.walk_right)
                return
            # update the window position
            self.windowpos = [int(positions[0][0]), int(positions[0][1])]
            self.root.geometry(self.imageSize + self.windowPosStr())
            positions = positions[1:]
            self.update_id = self.root.after(100, lambda: self.jumpByTop(positions))

    def pause(self, event):
        self.root.after_cancel(self.update_id)
        self.update_id = self.root.after(2000, lambda: self.jumpByTop(None))


# create root window
window = tk.Tk()

# config the window
window.title("My Pet")
window.resizable(False, False)
window.configure(highlightbackground="black")
window.overrideredirect(True)
window.wm_attributes("-transparentcolor", "black")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

app = Pet(window, [0, screen_height-150])
window.mainloop()