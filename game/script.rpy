# У цьому файлі міститься сценарій гри.

define character.player = Character(
    None,
    window_xpos=0.49,
    window_xanchor=1.0,
    window_xsize=400,
)
define character.animal = Character(
    None,
    window_xpos=0.51,
    window_xanchor=0.0,
    window_xsize=400,
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
