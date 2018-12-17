# Scenes for viewing colors (excluding first appearances of stygian blue and
# self-luminous green).

label stygian_blue:
    l "Сейчас ты увидишь крестик в цветном круге."
    l "Смотри на него, не отрываясь, пока круг внезапно не изменит цвет. Он может начать двигаться."
    hide lector
    window hide
    scene sb fatigue
    $ renpy.pause(20.0, hard=True)
    scene sb target
    pause
    scene bg black
    show lector base
    window show
    l "asdasd"
    return

label stygian_red:
    l "Сейчас ты увидишь крестик в цветном круге."
    l "Смотри на него, не отрываясь, пока круг внезапно не изменит цвет. Он может начать двигаться."
    hide lector
    window hide
    scene sr fatigue
    $ renpy.pause(20.0, hard=True)
    scene sb target
    pause
    scene bg black
    show lector base
    window show
    return

label luminous_green:
    l "Сейчас ты увидишь крестик в цветном круге."
    l "Смотри на него, не отрываясь, пока круг внезапно не изменит цвет. Он может начать двигаться."
    hide lector
    window hide
    scene lg fatigue
    $ renpy.pause(20.0, hard=True)
    scene lg target
    pause
    scene bg black
    show lector base
    window show
    return

label luminous_yellow:
    l "Сейчас ты увидишь крестик в цветном круге."
    l "Смотри на него, не отрываясь, пока круг внезапно не изменит цвет. Он может начать двигаться."
    hide lector
    window hide
    scene ly fatigue
    $ renpy.pause(20.0, hard=True)
    scene lg target
    pause
    scene bg black
    show lector base
    window show
    return
