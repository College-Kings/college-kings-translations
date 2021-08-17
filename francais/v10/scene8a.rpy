# SCENE 8a: Fight Results
# Locations: Abandoned Warehouse
# Characters:MC (Outfit 7), Grayson (Outfit 3),Chris (Outfit 2)
# Time: Saturday Night
label v10_avoid_fight:
    $ renpy.end_replay()
    if not v10_ryan_fight and not v10_imre_fight:   

        scene v10frr1 # TPP. Show MC leaving the warehouse.(camera from inside wearhouse positioned behind mc)
        with dissolve

        play music "music/v10/Scene 8/Track Scene 8a.mp3" fadein 3

        pause 0.75

        scene v10frr2 # TPP. Show MC having just left the warehouse (camera from outside, mc facing camera)        
        with dissolve

        if joinwolves:
            scene v10frr2a # TPP. same camera as v10frr2, Show MC having just left the warehouse (camera from outside, mc facing camera), Show chris just exiting the warehouse. MC mouth closed, Chris mouth open
            with dissolve
            ch "Hé!"

            u "(Je ne veux vraiment pas parler maintenant.)"

            scene v10frr2c # TPP. same camera as v10frr2, Show chriss now right behind MC, Chris hand on MC shoulder, chris mouth open, MC mouth closed
            with dissolve

            ch "Hé! Mec qu'est-ce que c'était ? Pourquoi tu t'es enfuis comme ça ?"

            scene v10frr3 # FPP. Show Chris, mouth closed, worried look.
            with dissolve

            u "*Soupirs* Ecoute, je ne sais pas d'accord."

            scene v10frr3a # FPP. same camera as v10frr3, Show Chris, mouth open, serious look.
            with dissolve

            ch "Je vais essayer d'être compréhensif, mais c'est vraiment difficile pour moi de rester calme après avoir pensé à tout ce qui a mené à ce moment."

            scene s764 # Ignore this render, old image from 0.4
            with dissolve

            pause 0.4

            scene v10frr3a
            with dissolve

            ch "Tu étais l'un des trois engagements qui ont été reçus même si beaucoup d'autres se sont battus pour ta place."

            ch "Et même maintenant, je me concentre ici sur le gars qui a couru alors que tout le monde, y compris Imre qui a fait un travail spectaculaire, est à l'intérieur."

            ch "Se casser le cul pour leur montrer qu'ils appartiennent aux Wolves. Ce soir était censé être une nuit d'accomplissement et de célébration."

            ch "Si c'est comme ça que tu vas agir quand les choses se présentent, alors réfléchis bien à savoir si cela est bien pour ton cas."

            menu:
                "Apologize":
                    $ addPoint("bro", 1)
                    scene v10frr3b # FPP. same camera as v10frr3, Show Chris, mouth closed, serious look.
                    with dissolve
                    u "*Soupirs* A quoi pensais-je ? Je n'aurais pas dû vous laisser tomber juste parce que.."

                    scene v10frr3a
                    with dissolve

                    ch "Juste parce que c'est ton ami ?"

                    scene v10frr3b
                    with dissolve

                    u "Ouais... MERDE ! Je vais le faire."

                    scene v10frr3a
                    with dissolve

                    ch "Heureux que vous compreniez et que vous ayez raison, mais ce navire a navigué."

                    scene v10frr3b
                    with dissolve

                    u "Je.."

                    scene v10frr3a
                    with dissolve

                    ch "C'est probablement mieux si tu rentres chez toi. Je ne pense pas que tu veuilles affronter les autres WOLVES maintenant."

                    scene v10frr3b
                    with dissolve

                    u "Chris, je.."

                    scene v10frr3a
                    with dissolve

                    ch "Rentre juste à la maison."
                "Défends ton territoire":
                    scene v10frr3b
                    with dissolve

                    u "Je respecte les Wolves, vous êtes comme une famille pour moi. Mais mes amis sont comme une famille aussi."

                    scene v10frr3a
                    with dissolve

                    ch "Laisses moi te demander ceci, Ryan aurait-il hésité à te battre?"

                    scene v10frr3b
                    with dissolve

                    u "C'est mon ami alors.."

                    scene v10frr3a
                    with dissolve

                    ch "Sois honnête avec toi-même, aurait-il hésité ?"

                    scene v10frr3b
                    with dissolve

                    u "*Soupirs* Non."

                    scene v10frr3a
                    with dissolve

                    ch "C'est probablement mieux si tu rentres chez toi. Je ne pense pas que tu veuilles affronter les autres Wolves maintenant."

                    scene v10frr3b
                    with dissolve
                    u "Chris, je.."

                    scene v10frr3a
                    with dissolve

                    ch "Rentre juste à la maison."
                    
        else:
            scene v10frr4 # TPP. Show MC stood near the side of the warehouse outside, Show Grayson approaching, grayson mouth open, MC mouth closed.
            with dissolve

            gr "Hé [name]!"

            u "(Je ne veux vraiment pas parler maintenant.)"

            scene v10frr5 # FPP. Show Grayson, worried look, mouth open
            with dissolve

            gr "Tu vas bien, mon pote ? On avait l'impression que tu étais un peu dépassé là-bas ?"

            scene v10frr5a # FPP. Same camera as v10frr5, Show Grayson, worried look, mouth closed
            with dissolve

            u "Je suis désolé, c'était juste. Aurais-tu combattu ton ami comme ça ?"

            scene v10frr5
            with dissolve

            gr "Ahhh, c'est donc ça le problème. Tu sais, tu me rappelles en fait un engagement que nous avions l'année dernière... Lui et moi étions très proches."

            scene v10frr5a
            with dissolve

            u "Où est-il maintenant ?"

            scene v10frr6 # TPP. Show MC and Grayson now stood by the corner of the building, both mouths closed.
            with dissolve

            pause 0.75

            scene v10frr6a # TPP. Same camera as v10frr6, Show MC and Grayson now stood around to corner with the door no exit no longer visable from where they're stood, both mouths closed.
            with dissolve

            scene v10frr7 # FPP. Show Grayson (now stood round the corner from v10frr5), worried look, mouth open
            with dissolve

            gr "Oh, il a abandonné SVC. Je pense qu'il a fini par avoir des problèmes."

            scene v10frr7a # FPP. Show Grayson (now stood round the corner from v10frr5), worried look, mouth closed
            with dissolve

            u "Quel genre de problèmes ?"

            u "Grayson ?"

            u "Quel genre de problèmes?"

            scene v10frr8 # TPP. Show Grayson arm pulled back ready to punch MC.
            with dissolve

            pause 0.5

            scene v10frr8a # TPP. same camera as v10frr8, Show Grayson Punching MC in the stomach.
            with dissolve
            gr "Il."

            scene v10frr8
            with dissolve

            pause 0.5

            scene v10frr8a
            with dissolve
            gr "A été."

            scene v10frr8
            with dissolve

            pause 0.5

            scene v10frr8a
            with dissolve
            gr "Une."

            scene v10frr8
            with dissolve

            pause 0.5

            scene v10frr8a
            with dissolve
            gr "Putain."

            scene v10frr8
            with dissolve

            pause 0.5

            scene v10frr8a
            with dissolve
            gr "De chatte !"

            scene v10frr7b # FPP. Same camera as v10frr7, Show Grayson angry look, mouth closed
            with dissolve

            u "Merde ! Pourquoi as-tu fait ça ?!"

            scene v10frr7c # FPP. Same camera as v10frr7, Show Grayson angry look, mouth open
            with dissolve

            gr "Je m'en fiche si nous partageons le même sang, un combat est un combat ! Tu as déjà refait des conneries de chatte comme ça et tu es sorti ! Tu as ça ?"

            scene v10frr7b
            with dissolve

            u "*Tousse* Ouais..."

            scene v10frr7c
            with dissolve

            gr "Maintenant, fous le camp d'ici, je ne veux pas voir ton visage !"

            scene v10frr7b
            with dissolve

            u "(Putain ce coup, je rentre à la maison.)"
    stop music fadeout 3
    jump v10_leave_fight