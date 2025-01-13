import turtle
import random
import time

turtle_screen = turtle.Screen()
turtle_screen.title("Catch The Turtle")
turtle_screen.setup(width=800, height=600)
turtle_screen.bgcolor("#0065c0")

kalem = turtle.Turtle()
kalem.hideturtle()
kalem.penup()

kalem1 = turtle.Turtle()
kalem1.hideturtle()
kalem1.penup()

skor = 0

kalem = turtle.Turtle()
kalem.hideturtle()
kalem.penup()
ekran_genislik = turtle_screen.window_width()
ekran_yukseklik = turtle_screen.window_height()

kalem.goto(0, ekran_yukseklik // 2 - 30)
kalem.write(f"Score: {skor}", align="center", font=("Arial", 16, "bold"))

def skor_guncelle():
    kalem.clear()  # Önceki skoru temizle
    kalem.write(f"Score: {skor}", align="center", font=("Arial", 16, "bold"))


def kaplumbaga_tikla(x, y):
    global skor
    skor += 1
    skor_guncelle()


turtle_screen.onclick(kaplumbaga_tikla)


turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.shapesize(1.5)
turtle_instance.penup()



kalem1.goto(0, ekran_yukseklik // 2 - 60)


def geri_sayim(sure):
    for saniye in range(sure, 0, -1):

        kalem1.clear()
        kalem1.write(f"Time: {saniye}", align="center", font=("Arial", 16, "bold"))


        turtle_instance.penup()
        x = random.randint(-turtle_screen.window_width() // 2 + 70, turtle_screen.window_width() // 2 - 70)
        y = random.randint(-turtle_screen.window_height() // 2 + 70, turtle_screen.window_height() // 2 - 70)
        turtle_instance.goto(x, y)

        time.sleep(1)


    kalem1.clear()
    kalem.clear()
    kalem1.write("Bitti!", align="center", font=("Arial", 16, "bold"))


geri_sayim(30)



turtle.done()