define character.zayec = Character(None)


label fourth_animal:

    # Frame - E1
    scene bg tale
    show folket at left_page
    with fade
    """
    Але недалеко зміг пройти Фолькет.
    Якась істота, наче блискавка, вистрибнула з кущів.
    """

    # Frame - E2
    show zayec at right_page
    zayec '''
    Це був заєць, який бігав туди-сюди, а коли побачив менестреля, швидко заступив йому дорогу.
    "У мене, е-е, у мене є для вас загадка. Якщо ви, е-е, зможете її розгадати, то я, е-е, пропущу вас."
    '''

    # Frame - E3
    player """
    І вам доброго дня, шановний сір Заєць.
    Я з радістю буду вам опонувати.
    """

    # Frame - E4
    zayec """
    Заєць Jittery жваво запитав менестреля: «Я швидко бігаю, я легкий, але я важкий. 
    Що я?»
    """


label frame_e5:
    player """
    Менестрель подумав і дещо нервово сказав: \n
    {a=jump:frame_e5_1}1) ти - вітер!{/a} \n
    {a=jump:frame_e5_2}2) ти - сокіл!{/a} \n
    {a=jump:frame_e5_3}3) ти - думка, швидка й невагома, але можеш обтяжувати розум!{/a} \n
    """ (advance=False)

    label frame_e5_1:
        zayec "О ні, ця відповідь абсолютно неправильна!"
        jump frame_e5

    label frame_e5_2:
        zayec "Боже, це навіть не близько. У вас не все добре, чи не так?"
        jump frame_e5

    label frame_e5_3:
        zayec "У зайця загорілися очі: «Ти справді правий, можеш проходити, менестрелю»."


label frame_e6:
    "І з цими словами заєць помчав у ліс, залишивши менестреля продовжувати свою подорож..."


return