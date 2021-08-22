# SCENE 9: MC and Frat leave. MC back in room
# Locations: MC Apes/Wolves Room
# Characters: Ryan (Outfit 2), Sam (Outfit 2),MC (Outfit 7), Grayson (Outfit 3),Imre (Outfit 4), Sebastian (Outfit 1),Cameron (Outfit 3),Chris (Outfit 2)
# Time: Sunday Morning
label v10_leave_fight:
    play music "music/v10/Scene 9/Track Scene 9.mp3" fadein 3
    if joinwolves:
        scene v10sraf1 # TPP. MC sits down on bed in his room.
        with fade
        pause 0.5

        if v10_ryan_win: # RCS - MC is a Wolf and won the fight.
            scene v10sraf1a # TPP. Same camera as v10swaf1. Show MC sitting on the bed in his room. MC looks proud, mouth closed.
            with dissolve

            u "(Quelle putain de journée ! Je ne m'attendais certainement pas à tout cela quand je suis arrivé à l'université. Tant de hauts, tant de bas. Merde folle.)"
        else:
            scene v10sraf1b # TPP. Same camera as v10swaf1. Show MC sitting on the bed in his room. MC looks disappointed, mouth closed.
            with dissolve

            u "(Aujourd'hui ça ne s'est vraiment pas passé comme prévu... C'est la pire des sensations.)"

        if v10_ryan_fight:
            scene v10sraf1c # TPP. Same camera as v10swaf1. Show MC sitting on bed in his room. MC reacts to someone knocking on his door.
            with dissolve
            play sound "sounds/knock.mp3"

            pause 0.5

            menu:
                "Fais comme si tu dormais":
                    scene v10sraf1c
                    with dissolve

                    u "(Assez pour aujourd'hui, je vais dormir.)"

                    scene v10sraf2 # TPP. Show MC sitting in bed. He gets in the bed, deciding to go to sleep.
                    with dissolve
                    pause 0.5
           
                "Répondre à la porte":
                    scene v10sraf3 # FPP. Show the door in MC's Wolves room. MC is sitting on the bed.
                    with dissolve

                    u "Oui ?"

                    if v10_ryan_win: # RCS - MC is a Wolf and won the fight.
                        scene v10sraf3a # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre entering MC's room. They are all smiling.
                        with dissolve

                        pause 0.5
                    
                        scene v10sraf3b # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre. All smiling, Chris mouth open.
                        with dissolve

                        ch "Si jamais j'ai un fils, je l'appelle [name] ! Je suis tellement fier de toi en ce moment."

                        scene v10sraf3c # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre. All smiling, Sebastian mouth open.
                        with dissolve

                        se "On dirait que les gars appartiennent vraiment aux Wolves. Bien fait."

                        scene v10sraf3d # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre. All smiling, all mouths closed.
                        with dissolve

                        u "Imre s'est soit transformé en bête là-bas, soit son adversaire n'était qu'un déchet."

                        scene v10sraf3e # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre. All smiling, Imre mouth open.
                        with dissolve

                        imre "*Rires* Ce type n'avait aucune putain de chance, classique d'un Apes. Tellement de bavardages et aucun support."

                        scene v10sraf3b
                        with dissolve

                        ch "Vraiment bien joué les gars, vous êtes absolument en train de l'écraser."

                        scene v10sraf3d
                        with dissolve

                        u "Merci."

                        scene v10sraf3b
                        with dissolve

                        ch "Essayez de dormir, je suis sûr que c'est la seule intimité que vous aurez après un combat comme ça. *Rires*"

                        scene v10sraf3f # FPP. Same camera as v10sraf3. Show Chris, Sebastian and Imre leaving MC's room.
                        with dissolve

                        u "(Merde, je suis vraiment CE gars maintenant !)"

                        scene v10sraf2
                        with dissolve

                        pause 0.5
                
                    else: # RCS - MC is a Wolf and lost the fight
                        scene v10sraf3g
                        with dissolve
                        pause 0.5
                    
                        scene v10sraf3h
                        with dissolve

                        ch "e ne sais pas si c'est vrai, mais l'un des gars a mentionné que tu es peut-être retenu parce que tu étais ami avec ton adversaire. Il n'y a pas d'amis sur le ring, [name]."

                        scene v10sraf3i
                        with dissolve

                        se "Ouais, cette merde ne va pas bien. Tu ne peux pas te faire botter le cul par un Apes."

                        scene v10sraf3j
                        with dissolve

                        u "Je suis désolé les gars. Il était juste meilleur ce jour-là."

                        scene v10sraf3h
                        with dissolve

                        ch "Essayes de dormir un peu maintenant, inutile de te battre pour ça."

                        scene v10sraf3f
                        with dissolve
                        pause 0.5

                        scene v10sraf3f
                        with dissolve

                        u "(Merde, j'ai vraiment laissé tomber la balle là...)"

                        scene v10sraf2
                        with fade

                        pause 0.5

    else: # RCS - MC is an Ape
        scene v10sraf4 # TPP. MC sits down on bed in his room. Apes.
        with fade
        
        pause 0.5

        if v10_imre_win: # RCS - MC is an Ape and won the fight
            scene v10sraf4a # TPP. Same camera as v10sraf4. Show MC sitting on the bed in his room. MC looks proud, mouth closed.
            with dissolve

            u "(Quelle putain de journée ! Je ne m'attendais certainement pas à tout cela quand je suis arrivé à l'université. Tant de hauts, tant de bas. Merde folle.)"
        else:
            scene v10sraf4b # TPP. Same camera as v10sraf4. Show MC sitting on the bed in his room. MC looks disappointed, mouth closed.
            with dissolve

            u "(Aujourd'hui ça ne s'est vraiment pas passé comme prévu... C'est la pire des sensations.)"

        if v10_imre_win: # RCS - MC is an Ape and won the fight
            scene v10sraf4c # TPP. Same camera as v10sraf4. Show MC sitting on bed in his room. MC reacts to someone knocking on his door.
            with dissolve

            play sound "sounds/knock.mp3"

            pause 0.5

            menu:
                "Fais comme si tu dormais":
                    scene v10sraf4c
                    with dissolve

                    u "(Assez pour aujourd'hui, je vais dormir.)"

                    scene v10sraf5 # TPP. Show MC sitting in bed. He gets in the bed, deciding to go to sleep.
                    with fade
                    pause 0.5

                "Répondre à la porte":
                    scene v10sraf6 # FPP. Show the door in MC's Apes room. MC is sitting on his bed.
                    with dissolve

                    u "Oui ?"
                    scene v10sraf6a # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan entering MC's room. They are all smiling.
                    with dissolve
                    pause 0.5

                    scene v10sraf6b # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan. All smiling, Grayson mouth open.
                    with dissolve

                    gr "Super boulot ce soir [name], je savais que tu allais le détruire."

                    scene v10sraf6c # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan. All smiling, Cameron mouth open.
                    with dissolve

                    ca "Se transformer en combattant... ce n'est pas une performance horrible aujourd'hui."

                    scene v10sraf6d # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan. All smiling, all mouths closed.
                    with dissolve

                    u "Merci les gars. Ryan l'a tué aussi."

                    scene v10sraf6e # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan. All smiling, Ryan mouth open.
                    with dissolve

                    ry "Nous l'avons fait tous les deux, mec. Apes jusqu'au bout !"

                    scene v10sraf6b
                    with dissolve

                    gr "Putain c'est vrai."

                    scene v10sraf6d
                    with dissolve

                    u "Haha, j'apprécie les compliments, mais je suis super épuisé, donc je pense que je vais juste aller me coucher si ça va."

                    scene v10sraf6b
                    with dissolve

                    gr "Tu l'as mérité."

                    scene v10sraf6f # FPP. Same camera as v10sraf6. Show Grayson, Cameron and Ryan leaving MC's room.
                    with dissolve

                    pause 0.5

        else:
            scene v10sraf5
            with fade

            pause 0.5

    stop music fadeout 3
    jump v10_sun_morn