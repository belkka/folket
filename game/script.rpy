# У цьому файлі міститься сценарій гри.

define character.player = Character(None)

# Гра починається тут.
label start:

    call intro

    call first_animal

    call second_animal

    call third_animal

    # TODO

    call ending

    return
