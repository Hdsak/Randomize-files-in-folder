import os
import random
from tkinter import *
from tkinter.filedialog import *

def FoldChoose():
    try:
        global vvd
        vvd = askdirectory()
        pth.config(text = vvd)
        global msv
        msv = os.listdir(path = vvd)
        random.shuffle(msv)
        if len(vvd) > 20:
            s = (len(vvd) - 20) * 10 + 200
            root.geometry(str(s) + 'x100')
    except Exception:
        return

def Shuf():
    if (os.path.exists(vvd + "/DelThisFold") == True) and (vvd != ''):
        pth.config(text = 'Пожалуйста, удалите\nпапку DelThisFold')
        return
    
    try:
        os.mkdir(vvd + "/DelThisFold")
    except Exception:
        return
    
    for i in range(len(msv)):
        frmt = msv[i].split('.')
        g = len(frmt) - 1
        if g != 0:
            os.rename(vvd + "/" + str(msv[i]),
                      vvd + "/DelThisFold/" + str(i) + '.' + frmt[g])
        elif os.path.exists(vvd + "/" + str(msv[i])) == True:
            pass
        else:
            os.rename(vvd + "/" + str(msv[i]),
                      vvd + "/DelThisFold/" + str(i))
    
    lst = os.listdir(path= vvd + "/DelThisFold")
    
    for j in range(len(lst)):
        os.rename(vvd + "/DelThisFold/" + str(lst[j]),
                  vvd + "/" + str(lst[j]))
    
    os.rmdir(vvd + "/DelThisFold")

    root.destroy()
    qt = Tk()
    qt.geometry('200x120')
    qt.title('Готово!')
    qt_txt = Label(qt, text = "Перемешивание\nзавершено",font = ('Times', 15))
    knpk = Button(qt, text = 'OK', command = qt.destroy, width = 15)
    
    qt_txt.pack()
    knpk.pack()

root = Tk()
root.geometry('200x100')
root.title('Mix')
pth = Label(root, text = '"Выбранный путь"', font = ('Times', 15))
bt = Button(root, text = "Выбрать папку", command = FoldChoose)
bt2 = Button(root, text = "Перемешать", command = Shuf)

pth.pack()
bt.pack()
bt2.pack()
root.mainloop()