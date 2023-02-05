define character.olen = Character(None, kind=character.animal)


label second_animal:

    # frame c1
    call scene_tale
    show folket at left_page
    with fade
    """
    Сповнений надії, Фолькет вирушив далі по дорозі до замку...

    Але несподівано дорогу йому заступив олень з велетенськими рогами.
    """

    # frame c2
    show olen at right_page with moveinright
    olen """
    Стій, менестрелю!  Ти повинен відповісти на мою загадку, якщо сподіваєшся продовжити свою подорож.
    """


    # frame c3
    player '''
    Менестрель був спантеличений викликом оленя, але він був сповнений рішучості дістатися до замку.

    Він зібрався з розумом і відповів: "чудово, я приймаю твій виклик. Давай свою загадку, прекрасний олень!"
    '''


    # frame c4
    olen """
    Олень прочистив горло й промовив глибоким голосом:
    \"Що таке легке, як пір'їнка, але навіть найсильніша людина не може його довго тримати?\"
    """


label frame_c5:
    player """
    Менестрель на мить задумався, а потім впевнено відповів:\n
    {a=jump:frame_c5_1}1)Меч!{/a}\n
    {a=jump:frame_c5_2}2)Перо!{/a}\n
    {a=jump:frame_c5_3}3)Подих?{/a}\n
    """ (advance=False)

    label frame_c5_1:
        olen "Але олень лише розчаровано похитав головою. Неправильно."
        jump frame_c5

    label frame_c5_2:
        olen "Відповідь оленя була рішучою: ні."
        jump frame_c5

    label frame_c5_3:
        olen "Очі оленя спалахнули, і він відійшов убік, дозволивши менестрелю продовжити свою подорож."
        jump frame_c6


label frame_c6:
    olen "Але будьте обережний, дорога попереду сповнена небезпек і інших загадок."

    scene cover 2 olen
    with fade
    pause game.transition_pause 

return