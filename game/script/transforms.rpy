transform left_page:
    anchor (1.0, 1.0)
    xoffset 536
    yoffset 914


transform right_page:
    anchor (1.0, 1.0)
    xoffset 1863
    yoffset 922
    

image animal_name = ShowingSwitch(
    "piven", Text(_("Шантеклер{#label}")),
    "olen", Text(_("Брехмер{#label}")),
    "vovchycya", Text(_("Гризетта{#label}")),
    "zayec", Text(_("Jittery{#label}")),
    "hryfon", Text(_("Prudens{#label}")),
    None, Null(),
)


image player_name = ShowingSwitch(
    "folket", Text(_("Фолькет{#label}"), color="#090"),
    None, Null(),
)
    

label scene_tale:
    scene bg tale

    show label_left zorder 1:
        anchor (1.0, 1.0)
        xoffset 548
        yoffset 1013

    show player_name zorder 2:
        anchor (0.5, 0.5)
        xoffset 300
        yoffset 940

    show label_right zorder 1:
        anchor (1.0, 1.0)
        xoffset 1846
        yoffset 1013
    
    show animal_name zorder 2:
        anchor (0.5, 0.5)
        xoffset 1600
        yoffset 940

    return