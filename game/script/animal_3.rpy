define character.vovchycya = Character(None)


label third_animal:

    # Frame - D1
    call scene_tale
    show folket at left_page
    with fade
    """
    Недалеко зміг пройти менестрель Фолькет.
    Дорогу йому заступила вовчиця, на ім'я Гризетта.
    """


    # Frame - D2
    show vovchycya at right_page
    with dissolve
    vovchycya "Хто ти та куди так поспішаєшь, йдучі через мій ліс?"
    player """
    Я Фолькет з Марселю, відомий менестрель.
    Шукаю кращої долі та пригод.
    """


    # Frame - D3
    vovchycya "Ну пригоди ти вже знайшов, мій любчику!"
    player """
    Я сповнений рішучісті пройти далі, шановна леді Гризетта!
    Слухаю вас уважно.
    """


    # Frame - D4
    vovchycya '''
    Тримайся, менестрелю! У мене є для вас загадка.
    "Я завжди голодна, мене завжди треба нагодувати. Палець, якого я торкнуся, скоро почервоніє. Що я?"
    '''


label frame_d5:
    player """
    Зажди, дай спробувати: \n
    {a=jump:frame_d5_1}1)Це маленький вовк?{/a} \n
    {a=jump:frame_d5_2}2)Це великий вовк?{/a} \n
    {a=jump:frame_d5_3}3)Це вогонь?{/a} \n
    """ (advance=False)

    label frame_d5_1:
        vovchycya "Ти такий кумедний! Звісно-о-у ні!"
        jump frame_d5

    label frame_d5_2:
        vovchycya "Ти такий передбачуваний. Ні!"
        jump frame_d5

    label frame_d5_3:
        vovchycya "Бравоууу! Тобі це вдалося, Фолькет."
        jump frame_d6


label frame_d6:
    vovchycya "І з цими словами вовчиця відступила вбік, дозволяючи менестрелю продовжити свою подорож до замку вдалині."

    scene cover 3 vovchycya
    with fade
    pause game.transition_pause 


return