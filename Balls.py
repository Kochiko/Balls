from tkinter import *
 
# глобальные переменные
# настройки окна
WIDTH = 900
HEIGHT = 300
 
 
# настройки мяча
 
# радиус мяча
_1BALL_RADIUS = 10
_2BALL_RADIUS = 10
# устанавливаем окно
root = Tk()
root.title("PythonicWay Pong")
 
# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()
 

# установка объектов
 
# создаем мячи
_1BALL = c.create_oval(WIDTH/4 - _1BALL_RADIUS/2,
                     HEIGHT/2 - _1BALL_RADIUS/2,
                     WIDTH/4 + _1BALL_RADIUS/2,
                     HEIGHT/2 + _1BALL_RADIUS/2, fill="white")
 

_2BALL = c.create_oval(WIDTH*0.75 - _1BALL_RADIUS/2,
                     HEIGHT/2 - _1BALL_RADIUS/2,
                     WIDTH*0.75 + _1BALL_RADIUS/2,
                     HEIGHT/2 + _1BALL_RADIUS/2, fill="white")
 
 
# запускаем работу окна
root.mainloop()
