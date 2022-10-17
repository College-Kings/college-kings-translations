screen kct_home():
    tag phone_tag

    default image_path = "images/phone/kct/app-assets/"

    default kct_info = [
        {
            "title": "popular",
            "text": "Les personnes populaires sont aimées par la foule et sont souvent prises en compte pour les décisions importantes. Elles donnent la priorité à leur image et à leur statut plutôt qu'à aider les autres.",
            "text_color": "#1C69B9"
        },
        {
            "title": "Loyal",
            "text": "Les personnes loyales se soucient des autres personnes et gagnent leur confiance facilement. Elles sont connues pour être responsables, mais peuvent être un peu rabat-joie dès qu'il s'agit de faire des folies.",
            "text_color": "DC9D05"
        },
        {
            "title": "Confiant",
            "text": "Les personnes confiantes ne comptent pas sur les autres pour se joindre à elles dans leurs actions. Elles n'ont pas besoin de l'approbation de leurs amis, mais elles peuvent être perçues comme égoïstes.",
            "text_color": "#be66a8"
        }
    ]
    default kct_info_index = 0

    use base_phone:
        add image_path + "kct-background.webp"

        vbox:
            xalign 0.5
            ypos 300
            spacing 20

            for count, kct in enumerate(sortedKCT, start=1):
                frame:
                    background image_path + "kct-{}.webp".format(kct.lower() if count == 1 else "disabled")
                    xysize (320, 79)

                    text "{}. {}".format(count, kct.upper()):
                        align (0.5, 0.5)
                        if count == 1:
                            color "#fff"
                        elif kct.lower() == "confident":
                            color "#be66a8"
                        elif kct.lower() == "loyal":
                            color "#DC9D05"
                        elif kct.lower() == "popular":
                            color "#1C69B9"

    add image_path + "kct-diagram.webp" xpos 150 yalign 0.5

    frame:
        background image_path + "kct-box-background.webp"
        xpos 1200
        yalign 0.5
        xysize (535, 330)

        fixed:
            ysize 28
            ypos 6

            text kct_info[kct_info_index]["title"].upper():
                style "kct_info_title"
                align (0.5, 0.5)

        fixed:
            ysize 281
            ypos 42

            imagebutton:
                idle image_path + "left-button-idle.webp"
                hover image_path + "left-button-hover.webp"
                action SetScreenVariable("kct_info_index", max(0, kct_info_index - 1))
                yalign 0.5

            text kct_info[kct_info_index]["text"]:
                style "kct_info_text"
                xsize 415
                align (0.5, 0.5)

            imagebutton:
                idle image_path + "right-button-idle.webp"
                hover image_path + "right-button-hover.webp"
                action SetScreenVariable("kct_info_index", min(kct_info_index + 1, len(kct_info) - 1))
                align (1.0, 0.5)


style kct_info_title is text:
    font "fonts/Syne-ExtraBold.ttf"
    size 19
    color "#ffffff"

style kct_info_text is text:
    font "fonts/Effra-Regular.ttf"
    size 23
    color "#fff"
    text_align 0.5
