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
    Label(text="Введите ваше уравнение", font=("Arial", 15)).place(x=250, y=50)

    def get_coefficient():
        a_c = a.get()
        print(a_c)

    a = Entry(width=5)
    a.place(x=100, y=100)

    Button(text="Решить", font=("Arial", 15), command=get_coefficient).place(x=250, y=120)


window = Tk()
window.geometry("700x600")
window.title("Square calc by Alex <3")
menu()
window.mainloop()

# one = Square(1, 2, 1)
# print(one.Discr())
# print(one.X())
