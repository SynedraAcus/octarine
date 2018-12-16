# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define l = Character('Лектор', color='#ffffff')
# Images
image bg black = '#000'
image lector base = 'base.png'
image lector harsh = 'harsh.png'
image lector talk = 'talk.png'
# Flags
default fs = False

# Игра начинается здесь:
label start:
    scene bg black
    show lector base at right
    l "Добро пожаловать на нашу скромную лекцию."
    l "Как можно было догадаться из названия, она посвящена цветам."
    l "Не тем, которые на растениях, а тем, которые... эм..."
    l "Цвета. Colours. Не цветы. Важно не путать."
    $ fs = preferences.fullscreen
    if not fs:
        l "Лучше всего смотреть эту лекцию в темноте в полноэкранном режиме."
        l "В наушниках или нет — неважно. Звука всё равно не будет."
        l "Но если вокруг будет слишком яркий свет, то фокус не получится"
        menu:
            "Сейчас переключу":
                menu:
                    "Готово":
                        $ fs = preferences.fullscreen
                        if not fs:
                            show lector harsh
                            l "..."
                            l "   ..."
                            l "      ..."
                            $ preferences.fullscreen = True
                            l "Так-то лучше"
                            show lector base
                        else:
                            "Спасибо."
                    "А как его переключить?":
                        l "Секунду."
                        $ preferences.fullscreen = True
                        l "Alt+Enter на винде и линуксе, а насчёт мака не уверен."
                        l "Кажется, Cmd+Shift+F?"
                        l "В настройках точно есть кнопка"
            "Мне в окне удобнее":
                show lector harsh
                l "Только не говори потом, что тебе фокус бракованный подсунули."
    else:
        l "Отлично, полноэкранный режим. Лучше не переключать в окно."
        l "Мир от этого, конечно, не рухнет, но фокус может не получиться"
    show lector talk
    l "Отлично, можно начинать"
    show lector harsh
    l "Определённо крипотно"
    show lector base
    return
