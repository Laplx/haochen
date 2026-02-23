"""
Original from https://www.jb51.net/article/258025.htm
Modified by Laplace(laplx) on Sun Sep  3 16:41:55 2023
"""

from tkinter import messagebox as msgbox
import tkinter as tk
import webbrowser
import random
  
class Lifes:
    def __init__(self, rows=38, cols=38):
        self.row = rows
        self.col = cols
        self.items = [[0]*self.col for _ in range(self.row)]
        self.histroy = []
        self.histroySize = 30
        self.running = False
        self.runningSpeed = 100
         
    def rndinit(self, rate=0.3):
        self.histroy = []
        for i in range(self.row):
            for j in range(self.col):
                rnd = random.random()
                if rnd > 1-rate:
                    self.items[i][j]=1
                elif rnd < rate:
                    self.items[i][j]=-1
  
    def reproduce(self):
        new = [[0]*self.col for _ in range(self.row)]
        self.add_histroy()
        if len(self.histroy) > self.histroySize:
            self.histroy.pop(0)
        for i in range(self.row):
            for j in range(self.col):
                if i*j==0 or i==self.row-1 or j==self.col-1:
                    new[i][j]=0
                else:
                    lifes=0
                    for m in range(i-1,i+2):
                        for n in range(j-1,j+2):
                            if m==i and n==j:
                                continue
                            lifes += self.items[m][n]
                    if self.items[i][j]>0:
                        if lifes==2 or lifes==3:
                            new[i][j]=1
                        elif lifes==-2 or lifes==-3:
                            new[i][j]=-1
                        else:
                            new[i][j]=0
                    elif self.items[i][j]<0:
                        if lifes==-2 or lifes==-3:
                            new[i][j]=-1
                        elif lifes==2 or lifes==3:
                            new[i][j]=1
                        else:
                            new[i][j]=0
                    else:
                        if lifes==3:
                            new[i][j]=1
                        elif lifes==-3:
                            new[i][j]=-1
        for idx,narray in enumerate(new):
            self.items[idx] = narray
  
    def is_stable(self):
        if len(self.histroy)<self.histroySize:
            return False
        arr = []
        for i in self.histroy:
            if i not in arr:
                arr.append(i)
        if len(arr)<20: # cannot find long loops
            return True
  
    def add_histroy(self, Items=None):
        arr = []
        if Items==None:
            Items=self.items[:]
        for item in Items:
            b = 0
            for i,n in enumerate(item[::-1]):
                b += n*2**i # isn't rigorous
            arr.append(b)
        self.histroy.append(arr)

    
def check(it):
    res = False
    for i in it:
        for j in i:
            if j!=0:
                res = True
    return res
  
def drawCanvas():
    global tv,rect
    tv = tk.Canvas(win, width=win.winfo_width(), height=win.winfo_height())
    tv.pack(side = "top")
    for i in range(36):
        coord = 40, 40, 760, i*20 + 40
        tv.create_rectangle(coord)
        coord = 40, 40, i*20 + 40, 760
        tv.create_rectangle(coord)
    coord = 38, 38, 760, 760
    tv.create_rectangle(coord,width=2)
    coord = 39, 39, 760, 760
    tv.create_rectangle(coord,width=2)
    coord = 38, 38, 762, 762
    tv.create_rectangle(coord,width=2)
    R,XY = 8,[50+i*20 for i in range(36)]
    rect = [[0]*36 for _ in range(36)]
    for i,x in enumerate(XY):
        for j,y in enumerate(XY):
            rect[i][j] = tv.create_rectangle(x-R,y-R,x+R,y+R,tags=('imgButton1'))
            tv.itemconfig(rect[i][j],fill='lightgray',outline='lightgray')
    tv.tag_bind('imgButton1','<Button-1>',on_Click)
  
def drawLifes():
    XY = [50+i*20 for i in range(36)]
    if Life.running:
        for i,x in enumerate(XY):
            for j,y in enumerate(XY):
                if Life.items[i+1][j+1]==1:
                    tv.itemconfig(rect[i][j],fill='red',outline='red')
                elif Life.items[i+1][j+1]==-1:
                    tv.itemconfig(rect[i][j],fill='blue',outline='blue')
                else:
                    tv.itemconfig(rect[i][j],fill='lightgray',outline='lightgray')
        tv.update()
        Life.reproduce()
        if Life.is_stable():
            Life.running = False
            if check(Life.items):
                msgbox.showinfo('Message','Stable or cyclic.')
            else:
                msgbox.showinfo('Message','Dead.')
    win.after(Life.runningSpeed, drawLifes)
  
def StartLife():
    if check(Life.items):
        Life.histroy = []
        Life.running = True
    else:
        msgbox.showinfo('Message','Click grids to fill in lifes or randomize')
  
def BreakLife():
    Life.running = not Life.running
    if Life.running:
        Life.histroy.clear()
        Life.add_histroy()
  
def RandomLife():
    Life.rndinit()
    Life.running = True
  
def ClearLife():
    Life.running = False
    Life.histroy = []
    Life.items = [[0]*38 for _ in range(38)]
    for x in range(36):
        for y in range(36):
            tv.itemconfig(rect[x][y],fill='lightgray',outline='lightgray')
  
def on_Enter(event):
    tCanvas.itemconfig(tVisit, fill='magenta')
  
def on_Leave(event):
    tCanvas.itemconfig(tVisit, fill='blue')
  
def on_Release(event):
    url = 'https://laplx.cc'
    webbrowser.open(url, new=0, autoraise=True)
  
def on_Click(event):
    x,y = (event.x-40)//20,(event.y-40)//20
    if not Life.running:
        if Life.items[x+1][y+1]==1:
            tv.itemconfig(rect[x][y],fill='blue',outline='blue')
            Life.items[x+1][y+1] = -1
        elif Life.items[x+1][y+1]==-1:
            tv.itemconfig(rect[x][y],fill='lightgray',outline='lightgray')
            Life.items[x+1][y+1] = 0
        else:
            tv.itemconfig(rect[x][y],fill='red',outline='red')
            Life.items[x+1][y+1] = 1
  
def on_Close():
    if msgbox.askokcancel("Quit","Do you want to quit?"):
        Life.running = False
        print(Copyright())
        win.destroy()
  
def Introduce():
    txt = '''【New Game of Life】\n\nEvolution rules：
    (1)When the cell is dead and has 3 red/blue cells living around it, it will become alive. (propagation)
    (2)When the cell is alive and has 2/3 net same-color living cells around it, it will keep alive. (living)
    (3)When the cell is alive and has 2/3 net different-color living cells around it, it will change color. (invasion)
    (4)When the cell is alive and has less than 2 or more than 3 net living cells of a color aroud it, it will become dead. (scramble or congestion)
    '''
    return txt
  
def Copyright():
    return "New Conway's Life Game Ver1.0\nOriginal Written by HannYang, Modified by Laplx, 2023/09/03."
  
  
if __name__ == '__main__':
  
    win = tk.Tk()
    X,Y = win.maxsize()
    W,H = 1024,800
    winPos = f'{W}x{H}+{(X-W)//2}+{(Y-H)//2}'
    win.geometry(winPos)
    win.resizable(False, False)
    win.title('New Game of Life')
    win.update()
    drawCanvas()
    Life = Lifes()
    drawLifes()
  
    tLabel = tk.Label(win, width=30, height=22, background='lightgray')
    tLabel.place(x=780, y=38)
    tLabel.config(text='\n'.join((Introduce(),Copyright())))
    tLabel.config(justify=tk.LEFT,anchor="nw",borderwidth=10,wraplength=210)
  
    bX,bY,dY = 835, 458, 50
    tButton0 = tk.Button(win, text=u'Start', command=StartLife)
    tButton0.place(x=bX, y=bY+dY*0 ,width=120,height=40)     
    tButton1 = tk.Button(win, text=u'Pause', command=BreakLife)
    tButton1.place(x=bX, y=bY+dY*1 ,width=120,height=40) 
    tButton2 = tk.Button(win, text=u'Random', command=RandomLife)
    tButton2.place(x=bX, y=bY+dY*2 ,width=120,height=40)
    tButton3 = tk.Button(win, text=u'Clear', command=ClearLife)
    tButton3.place(x=bX, y=bY+dY*3 ,width=120,height=40)
  
    tCanvas = tk.Canvas(win, width=200, height=45)
    tCanvas.place(x=800,y=680)
    tVisit = tCanvas.create_text((88, 22), text=u"Laplx's Blog")
    tCanvas.itemconfig(tVisit, fill='blue', tags=('btnText'))
    tCanvas.tag_bind('btnText','<Enter>',on_Enter)
    tCanvas.tag_bind('btnText','<Leave>',on_Leave)
    tCanvas.tag_bind('btnText','<ButtonRelease-1>',on_Release)
    win.protocol("WM_DELETE_WINDOW", on_Close)
    win.mainloop()