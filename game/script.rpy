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
    show lector base at center
    jump neurons
    l "Прежде всего: если у тебя вдруг эпилепсия или какие-нибудь побочки, при которых нельзя смотреть на яркие вспышки - выключай это дело."
    l "Серьёзно, если так - выключай прямо сейчас. Я такими вещами не шучу."
    l "..."
    l "Окей, предположительно моя скромная лекция тебя не убьёт."
    l "Добро пожаловать."
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

label styg_lum:
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
    l "На лист бумаги нельзя нанести минус миллиграмм краски."
    l "В других цветовых моделях математика может меняться, но смысл остаётся прежним:"
    l "Чем темнее цвет, тем ближе он к чёрному. Чем светлее цвет, тем ближе он к белому."
    l "Никакой цвет не может быть таким же тёмным, как чёрный, не будучи собственно чёрным."
    l "Но, разумеется, я бы не стал пилить целый проект, чтобы рассказать тебе, что чёрный цвет самый тёмный."
    show lector talk
    l "Я запилил целый проект, чтобы показать, что это не так."
    l "Открыл эти штуки не я, а другие люди. Не претендую. В папке с этим проектом даже есть пара статей."
    l "Но тем не менее, это довольно крутая штука. Итак, цвет темнее чёрного."
    label stygian_blue:
        show lector base
        l "Сразу предупреждаю, лично у меня срабатывает примерно через раз. Так что если не получится — попробуй повторить через минуту."
        l "Вот как это работает: сейчас ты увидишь крестик в цветном круге на сером фоне."
        l "Смотри на него, не отрываясь, пока круг внезапно не станет синим. Он может начать двигаться."
        l "Внимание, вопрос: светлее ли этот синий, чем окружающий чёрный?"
        hide lector
        window hide
        # TODO: Ignore mouse and keypresses
        scene sb fatigue
        pause 20.0
        scene sb target
        pause
        scene bg black
        show lector base
        window show
        l "Получилось?"
        menu:
            "Да":
                l "Отлично."
                l "Возможно, ты уже догадалась, что синий цвет я на мониторе не показывал. Он существовал только в твоей голове."
            "Кажется, круг был {i}слегка{/i} светлей фона?":
                l "Какой чудесный вопрос."
                l "Лично мне кажется, что не должен был. Но тут вот какое дело:"
                l "Возможно, ты уже догадалась, что синий цвет я на мониторе не показывал. Он существовал только в твоей голове."
                l "А штуки в голове имеют одно забавное свойство - довольно легко убедить себя в их существовании или несуществовании."
                l "Что с определённой точки зрения и {i}делает{/i} их существующими или несуществующими, но мы на этой точке зрения не стоим."
                l "К тому же эта магия в принципе почему-то не всегда срабатывает. Чёрт её знает. Но мировая наука в целом в эти вещи верит."
                l "Хотя и чувствует себя несколько неловко при обсуждении заведомо неизмеримых квалиа."
                l "Если есть под рукой томограф и сто добровольцев - можно попробовать проверить. Статью в Nature напишем."
                l "А потом салют… в нашу честь. Салют в нашу честь. Сначала на парад, а потом в дом офицеров пойдём. Бал будет. Пиво. Салют. В мою честь салют. Я полковник и ты — на белом коне."
                l "Я с кортиком, на белом коне, командую парадом! Я полковник! Я командую парадом! Я в звёздах! На белом коне! Я полковник! Я командую парадом!"
                l "Кхм."
        l "Предполагаю, кстати, что ты нормально воспринимаешь цвета и вовсе не дальтоник."
        l "Я не уверен, но я спрашивал Руку с Владосом, и они говорят, что таки нет."
        l "И вообще, цитирую, \"Интересный вопрос для человека довольно давно знающего ее\""
        show lector harsh
        pause
        show lector base
        l "Так вот."
        jump neurons

label neurons:
    l "Тот синий цвет, который ты видела — это afterimage. Штука, которая плавает перед глазами, если посмотреть на лампочку, а потом отвести взгляд."
    l "И вот откуда он берётся: сам по себе цвет не более чем количество фотонов разных длин волн, но человеческая голова никогда ничего не представляет как оно есть."
    l "В мозгу есть участок, ответственный за то, чтоб сводить данные с глаз и передавать их в кору. Драйвер глаза, если угодно."
    l "Там какая-то довольно замороченная нейробиология, но по сути есть три типа нейронов:"
    l "Одни просто измеряют общий уровень сигнала и указывают на то, темный ли цвет или светлый. То есть ближе ли он к чёрному или белому."
    l "Другие измеряют, ближе ли он к красному или зелёному, и в процессе эволюции помогают тебе не жрать незрелые овощи."
    l "А третьи измеряют, ближе ли он к жёлтому или синему, и в процессе эволюции помогают тебе не вешать вверх ногами украинский флаг."
    l "Соответственно, для каждого участка сетчатки по одному нейрону каждого типа передают значения от 0\% до 100\% каждый, которые ты воспринимаешь как цвет."
    l "Так вот, если определённый класс нейронов для определённого участка долго передаёт один и тот же сигнал — то он начинает врать."
    l "То ли истощаются/переполняются ресурсы низкоуровневых нейронов, то ли это поправка, которую вносит кора, не важно."
    l "Важно, что если долго передавать одинаковый сигнал, то мозг начинает видеть не истинный цвет, а нечто, смещённое от него к центру цветового пространства."
    l "Жёлтый становится слегка синее, красный слегка зеленее, а чёрный светлее (и наоборот)."
    l "Если в этот момент резко подменить внешний стимул, в нашем случае картинку на экране, то вносимая поправка/ошибка откатывается не сразу."
    l "Грубо говоря, ты видела нечто более тёмное, чем фон. Фон резко стал чёрным, темнее которого вроде как нельзя, но до нейронов это ещё не дошло."
    l "Вуаля: они показывают тебе нечто более тёмное, чем чёрное. Точнее, столь же тёмное, но таки имеющее цвет."
    show lector talk at center
    l "Это называется \"Стигийский синий\". Никакой объект не может иметь этот цвет. Никакая цветовая модель для монитора или печати не может его описать. Невозможно создать краску такого цвета."
    l "И тем не менее, его можно увидеть, в самом буквальном смысле хакнув своё восприятие."
    l "Слово \"хакнуть\" изначально именно это и означает: понять, как что-то работает, и заставить это что-то делать нечто, для чего оно не предназначено."
    l "По-моему, довольно круто."
    show lector base
    l "Аналогичным образом можно увидеть нечто более светлое, чем белое."
    l "По-английски это называется Self-Luminous colours. Светоносные? Сиятельные? Мне нравится слово \"Сиятельные\""
    l "На мониторе не впечатляет, потому что выглядит так, будто объект светится. Мониторы по определению светятся, камон."
    l "На бумаге прикольнее. Кстати, как раз про них лучшая иллюстрация к научной статье в истории научных статей."
    show lector base at right
    show print at top
    l "Impossible to print, ага. Наука, сучечки."
