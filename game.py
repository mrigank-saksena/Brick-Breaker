from tkinter import *
from intersect import *

root = Tk()


class MyCanvas(Canvas):
    score = 0

    def __init__(this, *args, **kwargs):
        Canvas.__init__(this, *args, **kwargs)
        this.score = 0
        this.rectangle = this.makeRectangle(225, 475)
        this.balls = []

	#THIS IS THE STARTING POSITION OF THE BALL, YOU CAN CHANGE IT IF YOU WANT
        this.balls.append(this.makeBall ( 225, 300 ))

	#THESE ARE THE BLOCKS YOU CAN CHANGE THEIR POSITIONS AND DELETE THEM IF YOU WANT
        this.makeStrongBlock(0, 100)
        this.makeStrongBlock(50, 100)
        this.makeStrongBlock(100, 100)
        this.makeStrongBlock(150, 100)
        this.makeStrongBlock(200, 100)
        this.makeStrongBlock(250, 100)
        this.makeStrongBlock(300, 100)
        this.makeStrongBlock(350, 100)
        this.makeStrongBlock(400, 100)
        this.makeStrongBlock(450, 100)
        this.makeBlock(0, 125)
        this.makeBlock(50, 125)
        this.makeBlock(100, 125)
        this.makeBlock(150, 125)
        this.makeBlock(200, 125)
        this.makeBlock(250, 125)
        this.makeBlock(300, 125)
        this.makeBlock(350, 125)
        this.makeBlock(400, 125)
        this.makeBlock(450, 125)
        this.makeStrongBlock(0, 150)
        this.makeStrongBlock(100, 150)
        this.makeStrongBlock(200, 150)
        this.makeStrongBlock(300, 150)
        this.makeStrongBlock(400, 150)
        this.makeBlock(50, 175)
        this.makeBlock(150, 175)
        this.makeBlock(250, 175)
        this.makeBlock(350, 175)
        this.makeBlock(450, 175)
        this.makeExtraBlock(225, 225)

        this.ballv = []

	#THIS IS THE VELOCITY OF THE BALL (X,Y) YOU CAN INCREASE/DECREASE THE SPEED OF THE BALL
        this.ballv.append([1, 2])

        this.bind("<Motion>", this.mouseHasMoved)
        this.focus_set()

    def mouseHasMoved(this, event):
        rsx, rsy, rex, rey = this.coords(this.rectangle)
        this.move(this.rectangle, (event.x - (rsx + rex) / 2), 0)
        # print( event.x, event.y )

    # Making the rectangle
    def makeRectangle(this, x, y, color="orange"):
        return this.create_rectangle(x, y, x + 50, y + 10, fill=color)

    # Making the ball
    def makeBall(this, x, y, color="blue"):
        return this.create_oval(x, y, x + 5, y + 5, fill=color)

    # Moving the ball
    def moveBall(this):
        for i in range(len(this.balls)):
            this.move(this.balls[i], this.ballv[i][0], this.ballv[i][1])
            rsx, rsy, rex, rey = this.coords(this.rectangle)
            sx, sy, ex, ey = this.coords(this.balls[i])
            # Creating tags for different types of blocks
            allblocks = this.find_withtag("block")
            allstrong = this.find_withtag("strong")
            allextra = this.find_withtag("extra")
            for block in allblocks:
                bsx, bsy, bex, bey = this.coords(block)
                if hits(bsx, bsy, bex, bey, sx, sy, ex, ey):
                    if block not in allstrong and block not in allextra:
                        this.delete(block)
                        MyCanvas.score += 1
                    elif block not in allextra:
                        this.makeBlock(bsx, bsy)
                        this.delete(block)
                    else:
                        this.balls.append(this.makeBall(100, 260, color="red"))
                        this.ballv.append([2, 1])
                        this.delete(block)
                if "N" in hits(bsx, bsy, bex, bey, sx, sy, ex, ey):
                    this.ballv[i][1] = -abs(this.ballv[i][1])
                if "S" in hits(bsx, bsy, bex, bey, sx, sy, ex, ey):
                    this.ballv[i][1] = abs(this.ballv[i][1])
                if "W" in hits(bsx, bsy, bex, bey, sx, sy, ex, ey):
                    this.ballv[i][0] = -abs(this.ballv[i][0])
                if "E" in hits(bsx, bsy, bex, bey, sx, sy, ex, ey):
                    this.ballv[i][0] = abs(this.ballv[i][0])
            if len(allblocks) == 0:
                this.create_text(240, 240, fill="#f33", text="You Win")
                raise ValueError("You Win")
            if ex >= 500 or sx <= 0:
                this.ballv[i][0] = -this.ballv[i][0]
            if sy >= 500 or sy <= 0:
                this.ballv[i][1] = -this.ballv[i][1]
            if rsx <= ex <= (rsx + ((rex - rsx) / 3)) and ey >= rsy:
                this.ballv[i][0] = (this.ballv[i][0] - .5)
                this.ballv[i][1] = -this.ballv[i][1]
            if (rsx + ((rex - rsx) / 3)) <= ex <= (rex - ((rex - rsx) / 3)) and ey >= rsy:
                this.ballv[i][0] = this.ballv[i][0]
                this.ballv[i][1] = -this.ballv[i][1]
            if rex >= ex >= (rex - ((rex - rsx) / 3)) and ey >= rsy:
                this.ballv[i][0] = (this.ballv[0][0] + .5)
                this.ballv[i][1] = -this.ballv[i][1]
            # Game ends when ball falls below a certain y coordinate
            if ey >= 500:
                this.create_text(240, 240, fill="#f33", text="GAME OVER")
                raise ValueError("game over")

    def makeBlock(this, x, y, color="green"):
        return this.create_rectangle(x, y, x + 50, y + 10, fill=color, tags="block")

    def makeStrongBlock(this, x, y, color="red"):
        # print(this.create_rectangle( x, y, x+50, y+10, fill = color, tags= ("strong", "block")))
        return this.create_rectangle(x, y, x + 50, y + 10, fill=color, tags=("strong", "block"))

    def makeExtraBlock(this, x, y, color="yellow"):
        # print(this.create_rectangle( x, y, x+50, y+10, fill = color, tags= ("extra", "block") ))
        return this.create_rectangle(x, y, x + 50, y + 10, fill=color, tags=("extra", "block"))


canvas = MyCanvas(root, width=500, height=500)
canvas.pack()

try:
    while (True):
        # raise(Exception("error"))
        canvas.moveBall()
        import time

        time.sleep(0.001)
        root.update()
except:
    print("program closed")
    import traceback, sys

    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback)

root.destroy()