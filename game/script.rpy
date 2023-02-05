# У цьому файлі міститься сценарій гри.

define character.side = Character(
    None,
    window_ypos=0.2,
    window_yalign=0.0,
    window_xsize=420,
    window_ysize=300,
)
define character.player = Character(
    None, kind=character.side,
    window_xpos=0.499,
    window_xanchor=1.0,
)
define character.animal = Character(
    None, kind=character.side,
    window_xpos=0.501,
    window_xanchor=0.0,
)

# Гра починається тут.
label start:

    call intro

    call first_animal

    call second_animal

    call third_animal

    call fourth_animal

    call boss

    call ending

    return
