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
root.title("Balls")
 
# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()
 

# Перевменные вводимые в окошки
speed_1 = ""
speed_2 = ""

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
 

# Создаем окошки
speed1_entry = Entry(speed_1)
speed2_entry = Entry(speed_2)

speed1_entry.place(relx = .15, rely = .05, anchor = "e", height=30, width=130)
speed2_entry.place(relx = .85, rely = .05, anchor = "w", height=30, width=130)

# Записываем текст в окошках и переводим в число
sp1 = int(speed1_entry.get())
sp2 = int(speed2_entry.get())

enter(sp1)
enter(sp2)

# запускаем работу окна
root.mainloop()
