D = {'张三':123456,'李四':111111,'王五':888888}
def new():
    INnewtry = tkinter.Tk()
    if str(Newname.get()) in D:
        INnewtry.geometry("200x100")
        INnewtry.title("出错啦")
        tkinter.Label(INnewtry,text="该名字已经被占用了呢").place(x=40,y=30)
    else:
        INnewtry.geometry("200x100")
        INnewtry.title("成功")
        tkinter.Label(INnewtry,text="注册成功\n").place(x=40,y=30)
def try1():#登录窗口
    INtry1 = tkinter.Tk()
    if str(Name.get()) in D:
        if int(Number.get()) == D[str(Name.get())]:
            INtry1.geometry("200x100")
            INtry1.title("欢迎")
            tkinter.Label(INtry1 ,text="登陆成功，欢迎您").place(x=40,y=30)
        else:
            INtry1.geometry("200x100")
            INtry1.title("错误")
            tkinter.Label(INtry1 ,text="密码错误").place(x=40,y=30)
    else:
        INtry1.geometry("200x100")
        INtry1.title("错误")
        tkinter.Label(INtry1 ,text="账号不存在，请先注册").place(x=40,y=30)
def try2():#注册窗口
    INtry2 = tkinter.Tk()
    INtry2.geometry("300x260")
    INtry2.title("用户注册")
    tkinter.Label(INtry2 ,text="密码：").place(x=30,y=100)
    tkinter.Entry(INtry2,textvariable=Newnumber,show='*').place(x=85,y=100)
    tkinter.Label(INtry2 ,text="注册名：").place(x=30,y=70)
    past=tkinter.Entry(INtry2,textvariable=Newname).place(x=85,y=70)
    tkinter.Button(INtry2, text ="确认",command = new).place(x=120,y=150)
def try3():#退出
    return
from tkinter import *
import tkinter.messagebox
from tkinter import Tk
IN = tkinter.Tk()
Number = StringVar()
Name = StringVar()
Newnumber = StringVar()
Newname = StringVar()
IN.geometry("300x300") #设置窗口尺寸
IN.title("王者荣耀2.0") #设置窗口标题
tkinter.Label(IN ,text="欢迎使用“王者荣耀").place(x=70,y=10) #标签
tkinter.Label(IN ,text="密码：").place(x=30,y=100)
tkinter.Entry(IN,textvariable=Number,show='*').place(x=85,y=100)
tkinter.Label(IN ,text="账号：").place(x=30,y=70)
copy=tkinter.Entry(IN,textvariable=Name).place(x=85,y=70)
tkinter.Button(IN, text ="登录",command = try1).place(x=70,y=150)
tkinter.Button(IN, text ="注册",command = try2).place(x=120,y=150)
tkinter.Button(IN, text ="退出").place(x=170,y=150)
IN.mainloop()


