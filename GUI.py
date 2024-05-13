from main import Square
from tkinter import *


# очистка гл. экрана(меню)
def clear():
    widgets = window.place_slaves()  # список виджетов
    for i in widgets:
        i.destroy()  # удаление виджетов
    b = Button(text="Домой", font=("Comic Sans", 15), command=menu)
    b.place(x=25, y=500, width=200)


def menu():
    clear()
    title = Label(text="Что вы выберете?", font=("Comic Sans", 24), fg="white", bg="orange")
    title.place(x=0, y=0, width=700)
    Button(text="Решить уравнение", font=("Arial", 15), command=calc).place(x=250, y=50)


def calc():
    clear()
    Label(text="Введите ваше уравнение", font=("Arial", 15)).place(x=100, y=50)

    def decide():
        a_c = int(a.get())
        b_c = int(b.get())
        c_c = int(c.get())
        sqr = Square(a_c, b_c, c_c)
        print(sqr.Discr())
        print(sqr.X())
        answer['text'] = sqr.X()
        dis['text'] = sqr.Discr()

    a = Entry(width=5)
    a.place(x=100, y=100)
    b = Entry(width=5)
    b.place(x=200, y=100)
    c = Entry(width=5)
    c.place(x=300, y=100)

    Button(text="Решить", font=("Arial", 15), command=decide).place(x=170, y=140)

    answer = Label(text="", font=("Arial", 15))
    answer.place(x=170, y=200)
    dis = Label(text="", font=("Arial", 15))
    dis.place(x=170, y=230)


window = Tk()
window.geometry("700x600")
window.title("Square calc by Alex <3")
menu()
window.mainloop()

# one = Square(1, 2, 1)
# print(one.Discr())
# print(one.X())
