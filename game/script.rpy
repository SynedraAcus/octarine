﻿# Вы можете расположить сценарий своей игры в этом файле.

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
    l "Цвета. Colours. Не цветы. Важно не путать. Совершенно разные вещи."
    $ fs = preferences.fullscreen
    if not fs:
        l "Лучше всего смотреть эту лекцию в полноэкранном режиме."
        l "В наушниках или нет — неважно. Звука всё равно не будет."
        l "Но если на мониторе будет слишком много всяких ярких штук, то фокус может не получиться."
        menu:
            "Сейчас переключу":
                menu:
                    "Готово":
                        $ fs = preferences.fullscreen
                        if not fs:
                            show lector harsh
                            l "..."
                            l "   ..."
                            $ preferences.fullscreen = True
                            l "Так-то лучше."
                            show lector base
                        else:
                            show lector talk
                            "Спасибо."
                    "А как его переключить?":
                        l "Секунду."
                        $ preferences.fullscreen = True
                        l "Alt+Enter на винде и линуксе, а насчёт мака не уверен."
                        l "Кажется, Cmd+Shift+F?"
                        l "В настройках точно есть такой пункт."
            "Мне в окне удобнее":
                show lector harsh
                l "..."
    else:
        show lector talk
        l "Отлично, полноэкранный режим. В оконный лучше не переключаться."
        l "Мир от этого, конечно, не рухнет, но фокус может не получиться"
    jump bw
    return

label bw:
    l "Итак, цвета. Для их описания существует целая куча всяких способов."
    l "RGB ты скорее всего знаешь: каждый цвет описывается как смесь красного, зелёного и синего."
    l "Цвет будет тем светлее, чем выше все значения, и тем темнее, чем они ниже."
    l "Соответственно, если задрать все значения до потолка, то получится белый цвет, #ffffff."
    l "И наоборот, если выставить их все в нули, то получится самый тёмный цвет, чёрный #000000"
    l "Эти два цвета ты как раз перед собой наблюдаешь - в буквах и фоне соответственно."
    l "Вот к чему я про это заговорил: {i}чёрный — самый тёмный цвет{/i}."
    l "(неизбежную шуточку про комикс вставишь сама)"
    l "По определению, ничего не может быть темнее, чем чёрный (кроме одноимённого аниме)."
    l "Чтобы любой цвет сделать темнее, нужно уменьшать все три значения, а меньше нуля их не уменьшишь."
    l "На пиксель монитора нельзя подать минус сколько-то вольт, чтобы он испустил минус сколько-то фотонов."
    l "В других цветовых моделях математика может меняться, но смысл остаётся прежним:"
    l "Чем темнее цвет, тем ближе он к чёрному. Чем светлее цвет, тем ближе он к белому."
    l "Никакой цвет не может быть таким же тёмным, как чёрный, не будучи собственно чёрным."
    l "Но, разумеется, я бы не стал пилить целый проект, чтобы рассказать тебе, что чёрный цвет самый тёмный."
    show lector talk
    l "Я запилил целый проект, чтобы показать, что это не так."
    l "Открыл эти штуки не я, а другие люди. Не претендую. Но штуки крутые"
    l "Но тем не менее, это довольно крутая штука. Итак, цвет темнее чёрного."
    label stygian_blue:
        show lector base
        l "Сразу предупреждаю, лично у меня срабатывает примерно через раз. Так что если не получится — попробуй повторить через минуту."
        l "Вот как это работает: сейчас ты увидишь крестик в цветном круге на сером фоне."
        l "Смотри на него, не отрываясь, пока круг внезапно не станет синим. Он может также начать двигаться"
        l "Внимание, вопрос: светлее ли этот синий, чем окружающий чёрный?"
        
    
