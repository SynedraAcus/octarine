# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define l = Character('Лектор', color='#ffffff')
# Images
image bg black = '#000'
image lector base = 'base.png'
image lector harsh = 'harsh.png'
image lector talk = 'talk.png'

# Игра начинается здесь:
label start:
    scene bg black
    show lector base at right
    l "Проект запускается"
    l "Сейчас я улыбнусь"
    show lector talk
    l "Так-то криповато"
    show lector harsh
    l "Определённо крипотно"
    show lector base
    return
