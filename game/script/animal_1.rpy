define character.piven = Character(None, kind=character.animal)


label first_animal:

    call scene_tale
    show folket at left_page
    with fade
    """
    Прийшовши до тями, Фолькет, опинився в дивному місці.

    Сонце світило якось приглушено, птахів не було чутно. Вдалені він побачив старовинний замок.

    Наближаючись до нього, його зустрів лютий на вигляд півень, на ім'я Шантеклер.
    """

    show piven at right_page with moveinright
    piven "Півень був захисником замку і погрожував напасти, якщо він негайно не піде."

    piven "Шантеклер подивився на Фолкета гострим поглядом. — Стій, менестрелю, — сказав Шантеклер. — Чому ви прагнете до замку?"

    player "Я...я всього лише мандрівний менестрель, який шукає притулку на ніч. Я не хочу зла."

    piven """
    Дорога до замку небезпечна, і тільки розумні можуть пройти. Докажи свою кмітливість, менестрелю.

    Дай відповідь на цю загадку:
    я кажу без рота і чую без вух. Я не маю тіла, але я оживаю з вітром.
    Що я таке?
    """

label frame_b4:
    player """
    Хм, це складно. Дай подумати:\n
    {a=jump:frame_b4_1}1)Це барабан?{/a} \n
    {a=jump:frame_b4_2}2)Це дзвіночок?{/a} \n
    {a=jump:frame_b4_3}3)Це труба?{/a} \n
    """ (advance=False)

    label frame_b4_1:
        piven "Неправильно! Ти не кмітливий, менестреле, бо ти неправильно здогадався. Можеш спробувати ще раз."
        jump frame_b4

    label frame_b4_2:
        piven "Ха!  Твої пісні можуть чарувати слух, але твій розум нудний, як струни арфи. Але я дам тобі ще один шанс."
        jump frame_b4

    label frame_b4_3:
        piven "Правильно! Ти зробив це, Фолькет. Ти можеш пройти."

label frame_b5:
    player "Уф, це було складно. Дякую за виклик, Півень Шантеклер."

    piven """
    Не такий вже ти і розумний...

    Задоволення було тільки моїм, менестрель. До наступного разу!
    """

    scene cover 1 piven with fade
    pause game.transition_pause 

return