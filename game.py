# imported items
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk

root = tk


# create Dog class, inherits from tkinter Frame
class Dog(tk.Frame):
    # intialise the class
    def __init__(self, parent):
        # intialise the frame
        tk.Frame.__init__(self, parent)
        # top frame created
        self.frameTop = tk.Frame(parent, width=400, height=400)
        self.frameTop.pack(side='top', fill='x')
        # middle frame created
        self.frameMiddle = tk.Frame(parent, width=400, height=400)
        self.frameMiddle.pack(side='top', fill='x')
        # bottom frame created
        self.frameBottom = tk.Frame(parent, width=400, height=40)
        self.frameBottom.pack(side='bottom', fill='x')

        # define variables
        # set actions to false
        self.active = False
        self.roll = False
        self.tiredNod = False
        self.waggling = False
        self.licking = False
        self.contentment = False
        # set planned events to None
        self.restore1 = None

        # set action counts to 0
        self.wagCount = 0
        self.lickCount = 0
        self.sitCount = 0

        # Create a canvas
        self.C = tk.Canvas(self.frameTop, height=350, width=300, background='white', cursor="hand2")
        self.gif = ImageTk.PhotoImage(file='stand.png')
        self.imgDefine = self.C.create_image(0, 0, image=self.gif, anchor='nw')
        self.C.pack()

        # image area canvas items, nose, eye, other eye configurations, ball, sleeping text
        self.nose = self.C.create_oval(28, 131, 43, 145, fill="black")
        self.eye = self.C.create_oval(58, 108, 83, 133, fill="white")
        self.eye2 = self.C.create_oval(63, 113, 77, 127, fill="black")
        self.eye3 = self.C.create_oval(63, 113, 71, 121, fill="white")
        self.st = self.C.create_line(80, 118, 60, 114, 60, 122, width=1, fill="black", state="hidden", smooth='true')
        self.ball = self.C.create_oval(30, 185, 56, 211, fill="red", state="hidden")
        self.eyelid = self.C.create_arc(56, 100, 87, 135, start=-20, extent=180, fill="#e6cb9c", outline="",
                                        state="hidden")
        self.eyelid2 = self.C.create_arc(61, 100, 84, 125, start=10, extent=180, fill="#e6cb9c", outline="",
                                         state="hidden")
        self.zz = self.C.create_text(15, 90, anchor="nw", fill='snow3', font=('Arial', -18))
        self.C.itemconfig(self.zz, text="Zz", state="hidden")

        # set energy variable
        self.energy = 100
        # sets label for energy
        self.label = tk.Label(self.frameTop, text="100 energy", font="Arial 10", width=10)
        self.label.pack(anchor="s")

        # set attention variable
        self.attention = 100
        # sets label for attention
        self.label2 = tk.Label(self.frameTop, text="100 attention", font="Arial 10", width=10)
        # packs attention label
        self.label2.pack(anchor="s")

        # set happiness variable
        self.happiness = 100
        # sets label for happiness
        self.label3 = tk.Label(self.frameTop, text="100 happiness", font="Arial 10", width=10)
        self.label3.pack(anchor="s")

        # refreshLabel is called 
        self.label.after(2000, self.refreshLabel)
        # blank line
        self.blank = tk.Label(self.frameTop)
        self.blank.pack(anchor="s")

        # create feed Button in top frame
        self.feed_button = ttk.Button(self.frameTop, text="Feed", command=self.feed)
        # packs so appears to the left
        self.feed_button.pack(side='left')

        # create sleep Button to the left
        self.sleep_button = ttk.Button(self.frameTop, text="Sleep", command=self.sleep)
        self.sleep_button.pack(side='left')
        # create play Button to the left
        self.play_button = ttk.Button(self.frameTop, text="Play", command=self.play)
        self.play_button.pack(side='left')
        # create pat Button to the left
        self.pat_button = ttk.Button(self.frameTop, text="Pat", command=self.pat)
        self.pat_button.pack(side='left')
        # create end game Button to the right
        self.close_button = ttk.Button(self.frameTop, text="End game", command=self.endGame)
        self.close_button.pack(side='right')

        # how to information displayed on click
        self.howto_button = tk.Button(self.frameMiddle, text="?", font="Arial 10", bg="GAINSBORO", relief="ridge", bd=1,
                                      command=self.message)
        self.howto_button.pack(side="left")

        self.name = tk.StringVar()

        self.name_button = ttk.Button(self.frameMiddle, text="Name", command=self.rename)
        self.name_button.pack(side='left')

        # set var for namestore
        self.nameStore = tk.StringVar()
        # default name is set
        self.nameStore.set("  Name: Fido")
        self.nameLabel = tk.Label(self.frameMiddle, textvariable=self.nameStore, font="Arial 10", width=10)
        self.nameLabel.pack(side="left")

        # status bar to show important information
        self.status = tk.Label(self.frameBottom, text="Welcome!", font="Arial 10", width=10, bd=1, relief='sunken',
                               anchor='w')
        self.status.pack(side="bottom", fill='x')
        root.geometry("400x510")  # defines the size of the application
        root.resizable(0, 0)  # makes application non resizable

        self.C.bind('<Button-1>', self.pat)  # binds button click to pat function
        root.wm_iconbitmap(default='paw.ico')  # sets icon
        root.title("  Virtual Dog")  # sets title

    # function called by end game button, will prompt user to quit
    def message(self):
        messagebox.showinfo("How to Play",
                            "Use the buttons or click the interface to interact with the dog. Keep the dog from getting too low on energy, attention or happiness.Your dog will express to you how it is feeling and the status bar below will display this. \n\nRename the dog using the name button to make the pop up menu appear, to input and set a new name.")

    def endGame(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()  # destroys the window

    def rename(self):
        toplevel = tk.Toplevel()
        dog_name_entry = tk.Entry(toplevel, width=7, textvariable=self.name)
        # sets the hurricane entry widget
        dog_name_entry.pack(side='left')
        self.changeName_button = ttk.Button(toplevel, text="Rename", command=self.naming)
        self.changeName_button.pack(side='left')

    def naming(self):
        if self.name.get().isalnum():
            self.nameStore.set('  Name: ' + self.name.get())

    def refreshLabel(self):
        # increments the variables
        # refreshes the content of the labels
        # sets the pet state upon checking that no action is being performed

        if self.energy >= 5:
            self.energy -= 5
        # configures label energy  
        self.label.configure(text="%i energy" % self.energy)

        if self.attention >= 5:
            self.attention -= 5
        # configures label attention
        self.label2.configure(text="%i attention" % self.attention)

        if self.happiness >= 5:
            self.happiness -= 5
        # configures label happiness
        self.label3.configure(text="%i happiness" % self.happiness)

        # set the dog state
        if (self.happiness <= 0) and (not self.active):
            self.status.configure(text="dog is unhappy")
            self.sad()
        elif (self.energy <= 0) and (not self.active):
            self.tired()
        elif (self.attention <= 0) and (not self.active):
            self.lonely()
            self.status.configure(text="dog needs attention")
        elif (self.happiness >= 80) and (not self.active):
            self.status.configure(text="feeling happy")
            if not self.waggling:
                self.restore1 = self.C.after(100, self.waggle())
        elif (self.energy >= 80) and (not self.active):
            self.status.configure(text="satisified")
            if not self.licking:
                self.lick()
        elif (self.attention >= 80) and (not self.active):
            self.status.configure(text="feeling good")
            if not self.contentment:
                self.contented()

        # call refreshLabel after given delay
        self.label.after(5000, self.refreshLabel)

    # function called when dog meets the criteria for contented 
    def contented(self):
        self.contentment = True
        self.gif = ImageTk.PhotoImage(file='content1.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        if self.attention >= 80:
            self.restore1 = self.C.after(3000, lambda: self.contented2())
        else:
            self.restore1 = self.C.after(200, lambda: self.stand())

    # contented 2 called after contented 
    def contented2(self):
        self.gif = ImageTk.PhotoImage(file='content2.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        self.sitCount += 1
        if self.sitCount % 3 == 0:  # check if the count is a multiple of three
            wait = 7000  # if so wait is a longer time period of 7000
        else:
            wait = 3000  # otherwise wait is 3000
        if self.attention >= 80:
            self.restore1 = self.C.after(wait, lambda: self.contented())
        else:
            self.restore1 = self.C.after(wait, lambda: self.stand())

    # lick function called when dog meets criteria for excited
    # will set the canvas image for excited
    def lick(self):
        self.licking = True
        self.gif = ImageTk.PhotoImage(file='excited.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        if self.energy >= 80:
            self.restore1 = self.C.after(200, lambda: self.lick2())
        else:
            self.restore1 = self.C.after(200, lambda: self.stand())

    # called by lick function
    # will wait and then call lick function unless condition is not met
    # length of wait determined by calculation
    def lick2(self):
        self.gif = ImageTk.PhotoImage(file='excited2.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        self.lickCount += 1
        if self.lickCount % 3 == 0:
            wait = 2000
        else:
            wait = 500
        if self.energy >= 80:
            self.restore1 = self.C.after(wait, lambda: self.lick())
        else:
            self.restore1 = self.C.after(wait, lambda: self.stand())

    # called when dog is tired
    def tired(self):
        self.tiredNod = True
        self.status.configure(text="dog lacks energy")
        self.C.itemconfig(self.eyelid, state="normal")
        self.gif = ImageTk.PhotoImage(file='nod.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        self.C.move(self.nose, -2, 4)
        self.C.move(self.eye, -2, 0)
        self.C.move(self.eye2, -2, 0)
        self.C.move(self.eye3, -2, 0)
        self.restore1 = self.C.after(1000, self.stand)

    # called when dog is sad
    def sad(self):
        self.status.configure(text="dog is unhappy")
        self.gif = ImageTk.PhotoImage(file='sad1.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        self.restore1 = self.C.after(1500, lambda: self.down())

    def down(self):
        self.gif = ImageTk.PhotoImage(file='sad2.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        self.status.configure(text="dog is unhappy")

    # called when dog is happy
    def waggle(self):
        self.waggling = True
        self.gif = ImageTk.PhotoImage(file='wag.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        if self.happiness >= 80:
            self.restore1 = self.C.after(350, lambda: self.waggle2())
        else:
            self.restore1 = self.C.after(350, lambda: self.stand())

    def waggle2(self):
        if self.active:
            pass
        else:
            self.gif = ImageTk.PhotoImage(file='wag2.png')
            self.C.itemconfig(self.imgDefine, image=self.gif)
            self.wagCount += 1
            if self.wagCount % 3 == 0:
                wait = 7000
            else:
                wait = 500

            if self.happiness >= 80:
                self.restore1 = self.C.after(wait, lambda: self.waggle())
            else:
                self.restore1 = self.C.after(wait, lambda: self.stand())
    # called when dog needs attention
    def lonely(self):
        self.status.configure(text="dog needs attention")
        self.gif = ImageTk.PhotoImage(file='attention.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        self.C.itemconfig(self.eyelid2, state="normal")
        self.attenNose = True
        self.C.move(self.nose, 0, -10)
        self.restore1 = self.C.after(500, self.stand)

    # ------------------------------------------------------------#
    # stand function is called to set the default standing state of the dog
    def stand(self):
        self.gif = ImageTk.PhotoImage(file='stand.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        # is ref right
        self.waggling = False
        self.licking = False
        self.contentment = False
        self.active = False
        self.status.configure(text="")
        self.coord()  # set coordinates
        if self.roll:
            self.roll = False
            self.C.itemconfig(self.ball, state="hidden")
            self.C.coords(self.ball, 30, 185, 56, 211)

    # cancel function cancels pending actions relating to states
    def cancel(self):
        if self.restore1 is not None:
            self.C.after_cancel(self.restore1)
            self.restore1 = None

        # set conditions to false regardless of whether there is a pending action
        self.waggling = False
        self.licking = False
        self.contentment = False

    # sets the coordinate of eyes
    def coord(self):
        self.C.coords(self.nose, 28, 131, 43, 145)
        self.C.coords(self.eye, 58, 108, 83, 133)
        self.C.coords(self.eye2, 63, 113, 77, 127)
        self.C.coords(self.eye3, 63, 113, 71, 121)
        self.C.itemconfig(self.eyelid, state="hidden")
        self.C.itemconfig(self.eyelid2, state="hidden")

    # function called when feed button is clicked
    def feed(self):
        if self.active:
            self.status.configure(text="sorry an action is already in progress")
        else:
            self.coord()  # set coordinates
            self.cancel()  # cancel any pending actions
            self.active = True
            if self.energy <= 70:
                self.energy += 30
            elif self.energy > 70:
                self.energy = 100
            self.label.configure(text="%i energy" % self.energy)
            self.gif = ImageTk.PhotoImage(file='feed.png')
            self.C.itemconfig(self.imgDefine, image=self.gif)
            feedCount = 0
            
            def eating():
                # image changed
                self.gif = ImageTk.PhotoImage(file='eating7.png')
                self.C.itemconfig(self.imgDefine, image=self.gif)
                # nose and eyes reconfigured
                self.C.coords(self.nose, 6, 241, 21, 255)
                self.C.coords(self.eye, 28, 200, 53, 225)
                self.C.coords(self.eye2, 33, 205, 47, 219)
                self.C.coords(self.eye3, 33, 205, 41, 213)

            def eating2():
                # image changed
                self.gif = ImageTk.PhotoImage(file='eatingclose.png')
                self.C.itemconfig(self.imgDefine, image=self.gif)
                # nose and eyes reconfigured
                self.C.coords(self.nose, 14, 234, 29, 248)
                self.C.coords(self.eye, 30, 195, 55, 220)
                self.C.coords(self.eye2, 35, 200, 49, 214)
                self.C.coords(self.eye3, 35, 200, 43, 208)

            def eaten():
                # image changed
                self.gif = ImageTk.PhotoImage(file='eaten.png')
                self.C.itemconfig(self.imgDefine, image=self.gif)
                # nose and eyes reconfigured
                self.C.coords(self.nose, 21, 234, 36, 248)
                self.C.coords(self.eye, 28, 190, 53, 215)
                self.C.coords(self.eye2, 33, 195, 47, 209)
                self.C.coords(self.eye3, 33, 195, 41, 203)

            # cycle through actions
            self.C.after(1000, lambda: eating())
            self.C.after(1500, lambda: eating2())
            self.C.after(1600, lambda: eating())
            self.C.after(1700, lambda: eaten())
            self.C.after(2700, self.stand)

    # function called when sleep button is pressed
    def sleep(self):
        if self.active:
            self.status.configure(text="sorry an action is already in progress")
        else:
            self.active = True
            self.coord()  # set coordinates
            self.cancel()  # cancel any pending actions
            self.C.itemconfig(self.st, state="normal")
            self.C.itemconfig(self.eye, state="hidden")
            self.C.itemconfig(self.eye2, state="hidden")
            self.C.itemconfig(self.eye3, state="hidden")
            self.C.itemconfig(self.zz, text="Zz", state="normal")

            self.C.configure(background='black')
            self.gif = ImageTk.PhotoImage(file='liedown.png')
            self.C.itemconfig(self.imgDefine, image=self.gif)
            if self.energy < 100:
                self.energy += 5
                self.label.configure(text="%i energy" % self.energy)
            if self.happiness < 100:
                self.happiness += 5
                self.label3.configure(text="%i happiness" % self.happiness)
            self.C.after(5000, self.reset)

    # reset function restores items to default state
    def reset(self):
        self.C.itemconfig(self.st, state="hidden")
        self.C.itemconfig(self.eye, state="normal")
        self.C.itemconfig(self.eye2, state="normal")
        self.C.itemconfig(self.eye3, state="normal")
        self.C.configure(background='white')
        self.C.itemconfig(self.zz, text="Zz", state="hidden")
        self.gif = ImageTk.PhotoImage(file='stand.png')
        self.C.itemconfig(self.imgDefine, image=self.gif)
        self.status.configure(text="")
        self.active = False

    # pat function called when you press pat button or you mouse click on the canvas
    # sets canvas image
    def pat(self, *args):
        if self.active:
            pass
        else:
            self.coord()  # set coordinates
            self.cancel()  # cancel any pending actions
            self.active = True
            self.gif = ImageTk.PhotoImage(file='pat.png')
            self.C.itemconfig(self.imgDefine, image=self.gif)
            if self.attention < 95:
                self.attention += 10
            elif self.attention == 95:
                self.attention += 5
            self.label2.configure(text="%i attention" % self.attention)

            self.C.after(500, self.stand)

    # play function called when you click the play button
    def play(self):
        if self.active:
            self.status.configure(text="sorry an action is already in progress")
        else:
            self.coord()  # set coordinates
            self.cancel()  # cancel any pending actions
            if self.happiness < 95:
                self.happiness += 10
            elif self.happiness == 95:
                self.happiness += 5
            if self.energy > 5:
                self.energy -= 5
            self.label3.configure(text="%i happiness" % self.happiness)
            self.label.configure(text="%i energy" % self.energy)
            self.active = True
            self.roll = True
            self.C.itemconfig(self.ball, state="normal")
            self.gif = ImageTk.PhotoImage(file='pounce.png')
            self.C.itemconfig(self.imgDefine, image=self.gif)
            # configure eye position and nose
            self.C.move(self.eye, 15, -25)
            self.C.move(self.eye2, 14, -24)
            self.C.move(self.eye3, 14, -24)
            self.C.move(self.nose, 15, -25)
            self.C.after(200, lambda: bounceDown())

            # called through the play function
            # moves ball position and changes the pose of the dog
            def bounceDown():
                self.C.move(self.ball, -5, 30)
                self.C.move(self.eye, -15, 25)
                self.C.move(self.eye2, -15, 25)
                self.C.move(self.eye3, -15, 25)
                self.C.move(self.nose, -15, 25)
                self.gif = ImageTk.PhotoImage(file='playpose.png')
                self.C.itemconfig(self.imgDefine, image=self.gif)
                self.C.after(150, lambda: bounceUp())

            # bounce down calls this function
            def bounceUp():
                # ball moves
                self.C.move(self.ball, -5, -30)
                # eyes and nose move
                self.C.move(self.eye, -7, 8)
                self.C.move(self.eye2, -7, 8)
                self.C.move(self.eye3, -7, 8)
                self.C.move(self.nose, -7, 8)
                self.gif = ImageTk.PhotoImage(file='playpose2.png')
                self.C.itemconfig(self.imgDefine, image=self.gif)
                # bouncecatch function is called
                self.C.after(200, bounceCatch)

            def bounceCatch():
                # ball moves
                self.C.move(self.ball, -5, 30)
                # eyes and nose move
                self.C.move(self.eye, -20, 22)
                self.C.move(self.eye2, -20, 22)
                self.C.move(self.eye3, -20, 22)
                self.C.move(self.nose, -10, 45)
                self.gif = ImageTk.PhotoImage(file='playposefix.png')
                self.C.itemconfig(self.imgDefine, image=self.gif)
                # mouth function is called
                self.C.after(200, mouth)

            def mouth():
                # ball moves
                self.C.move(self.ball, -5, -25)
                # eyes and nose move
                self.C.move(self.eye, -12, 10)
                self.C.move(self.eye2, -12, 10)
                self.C.move(self.eye3, -12, 10)
                self.C.move(self.nose, -17, -10)
                self.gif = ImageTk.PhotoImage(file='dogcatchytest9999.png')
                self.C.itemconfig(self.imgDefine, image=self.gif)
                # mouth2 function is called
                self.C.after(400, mouth2)

            def mouth2():
                # ball moves
                self.C.move(self.ball, 0, -20)
                # eyes and nose move
                self.C.move(self.eye, 5, -18)
                self.C.move(self.eye2, 5, -18)
                self.C.move(self.eye3, 5, -18)
                self.C.move(self.nose, 0, -20)
                self.gif = ImageTk.PhotoImage(file='dogcatchytest89.png')
                self.C.itemconfig(self.imgDefine, image=self.gif)
                # stand function is called
                self.C.after(600, self.stand)


# called when you try to quit through "X" button in the top right corner
def closure():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()  # close window on exit


if __name__ == "__main__":
    root = tk.Tk()
    dog = Dog(root)
    root.protocol("WM_DELETE_WINDOW", closure)  # set protocol for closure of window
    root.mainloop()  # run main loop
