# SCENE 7: MC vs Imre (Apes)
# Locations: Warehouse
# Characters: MC (Outfit 7),Josh (Outfit 2),Imre (Outfit 2),Imre (Outfit 4),Grayson (Outfit 3)
# Time: Saturday Night
label v10_mc_vs_imre_fight:
    play music "music/v10/Scene 6 & 7/Track Scene 6 & 7.mp3" fadein 3
    scene v10mvi1 # FPP. Show imre and grayson near ring, Imre Mouth open Grayson mouth closed
    with dissolve
    ry "Hé mec vite fais. Je ne dis pas que je pense que tu le ferais, mais je sais que toi et Imre êtes amis et êtes proches depuis que vous avez commencé l'université..."

    ry "Ne laisses pas cela entrer au milieu de ce combat."

    scene v10mvi1a # FPP. Same camera as v10mvi1, Show Imre and Grayson near ring,imre mouth closed Grayson mouth closed
    with dissolve

    u "Juste parce que nous sommes..."

    scene v10mvi1b # FPP. Same camera as v10mvr1, Show imre and Grayson near ring, imre mouth closed Grayson mouth open
    with dissolve

    gr "Ne commence même pas avec toutes ces conneries ! Tu ferais mieux de lui détruire le cul !"

    scene v10mvr2 # Ignore this render, reused from scene 6
    with dissolve

    jo "*Murmure fort* Hé, j'ai des projets ce soir. Combien de temps encore..."

    scene v10mvi1b
    with dissolve

    gr "Bro calme-toi, on est prêt !"

    scene v10mvi1
    with dissolve

    ry "Faites-le pour Apes."

    scene v10mvi1a
    with dissolve

    u "Tu l'as eu."

    scene v10mvr3 #Ignore this render, reused from scene 6
    with dissolve

    jo "On dirait que nos combattants sont prêts !"

    scene v10mvi2 # TPP. Show josh in the centre of the ring MC and Imre next to josh either side, Josh mouth closed, mc mouth closed, imre mouth open
    with dissolve

    imre "Prêt à te faire botter le cul ?"

    menu:
        "Combattre Imre":
            $ v10_imre_fight = True
            scene v10mvi3 # FPP. Show Imre infront of camera in ring, mouth closed, hands raised ready to fight.
            with dissolve

            u "Tu descends ce soir."

            jo "Mêmes règles qu'avant, comprenez-le les gars !"

            # Imre Fight
            call screen fight_tutorialPopup

            scene v10mvi3

            call screen fight_typeMenu

            if fight_type == "normal":
                $ simImreFight = False
                $ imreStance = renpy.random.choice([1, 2, 3, 4])
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])

                call screen fight_selectDifficulty

                call screen fight_keybindOptions

            elif fight_type == "simReal" or fight_type == "simWin":
                $ simImreFight = True
                $ stance = 1

                $ imreStance = renpy.random.choice([1, 2, 3, 4])
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if fight_type == "simWin":
                $ youHealth = 100000
            else:
                $ youHealth = 3

            $ enemyhealth = 6
            $ youDamage = 0
            $ imreDamage = 0

            # Imre attacks MC
            label imre_McAttack:
                $ stance = 2 # Defence

                show screen fight_overlay(stance="defend")

                # Imre hook
                if imreAttack == 1:

                    scene imrehook
                    pause 0.6 # Trial Error

                    scene imrehookend
                    $ imreStance = renpy.random.choice([1, 2, 3, 4]) # Imre next defensive stance
                    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6]) # What attack you're gonna pick next

                    if simImreFight:
                        if imreSimulation in [1, 2, 3]: # simimre is imre random attack
                            jump imre_McKickHit # REMEMBER switch attacks!
                        else:
                            jump imre_McKickBlock

                    else:
                        call screen imreFight_MCDefend(attack="Hook")

                # Imre jab
                if imreAttack == 2:

                    scene imrejab
                    $ renpy.pause(0.5)

                    scene imrejabend
                    $ imreStance = renpy.random.choice([1, 2, 3, 4])
                    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

                    if simImreFight:
                        if imreSimulation in [1, 2, 3]:
                            jump imre_McJabHit
                        else:
                            jump imre_McJabBlock

                    else:
                        call screen imreFight_MCDefend(attack="Jab")

                # Imre body hook
                if imreAttack == 3:

                    scene imrebody
                    $ renpy.pause(0.7)

                    scene imrebodyend
                    $ imreStance = renpy.random.choice([1, 2, 3, 4])
                    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

                    if simImreFight:
                        if imreSimulation in [1, 2, 3]:
                            jump imre_McHookHit
                        else:
                            jump imre_McHookBlock

                    else:
                        call screen imreFight_MCDefend(attack="BodyHook")

                # Imre kick
                if imreAttack == 4:

                    scene imrekick
                    $ renpy.pause(0.6)

                    scene imrekickend
                    $ imreStance = renpy.random.choice([1, 2, 3, 4])
                    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

                    if simImreFight:
                        if imreSimulation in [1, 2, 3]:
                            jump imre_McBodyhookHit
                        else:
                            jump imre_McBodyhookBlock

                    else:
                        call screen imreFight_MCDefend(attack="Kick")


            # label Attacker_TargetAction
            label mc_imreKickHit: # MC Kicks Imre (Hits/No Block)

                $ imreDamage += 1
                scene mc_imre_Kick_hit
                pause 1 # Trial/Error
                if imreDamage >= enemyhealth:
                    jump mc_imreFightEnd
                jump imre_McAttack

            label mc_imreKickBlock: # MC Kicks Imre (Blocks)

                    scene mc_imre_Kick_block
                    pause 0.7 # Trial/Error
                    jump imre_McAttack


            label mc_imreJabsHit: # MC Jabs Imre (Hits/No Block)


                $ imreDamage += 1
                scene mc_imre_Jab_hit
                pause 0.7 # Trial/Error
                if imreDamage >= enemyhealth:
                    jump mc_imreFightEnd
                jump imre_McAttack

            label mc_imreJabsBlock: # MC Jabs Imre (Blocks)

                    scene mc_imre_Jab_block
                    pause 0.7 # Trial/Error
                    jump imre_McAttack


            label mc_imreHooksHit: # MC Hooks Imre (Hits/No Block)

                $ imreDamage += 1
                scene mc_imre_Hook_hit
                pause 0.7 # Trial/Error
                if imreDamage >= enemyhealth:
                    jump mc_imreFightEnd
                jump imre_McAttack

            label mc_imreHooksBlock: # MC Hooks Imre (Blocks)

                    scene mc_imre_Hook_block
                    pause 0.7 # Trial/Error
                    jump imre_McAttack


            label mc_imreBodyhookHit: # MC Body Hooks Imre (Hits/No Block)


                $ imreDamage += 1
                scene mc_imre_BodyJab_hit
                pause 0.7 # Trial/Error
                if imreDamage >= enemyhealth:
                    jump mc_imreFightEnd
                jump imre_McAttack

            label mc_imreBodyhookBlock: # MC Body Hooks Imre (Blocks)

                    scene mc_imre_BodyJab_block
                    pause 0.7 # Trial/Error
                    jump imre_McAttack


            label imre_McKickHit: # Imre Kicks MC (Hits/No Block)

                play sound "sounds/ks.mp3"
                $ youDamage += 1
                scene Imre_Kick_hit
                with hpunch

                pause 0.5
                $ stance = 1
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4, 5, 6])
                jump mc_imreAttack

            label imre_McKickBlock: # Imre Kicks MC (Blocked)

                play sound "sounds/ks.mp3"
                scene Imre_Kick_block
                with hpunch

                pause 0.5
                $ stance = 1
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_imreAttack

            label imre_McJabHit: # Imre Kicks MC (Hits/No Block)

                play sound "sounds/js.mp3"
                $ youDamage += 1
                scene Imre_Jab_hit
                with hpunch

                pause 0.5
                $ stance = 1
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4])
                if youDamage >= youHealth:
                        jump imre_McFightEnd
                jump mc_imreAttack

            label imre_McJabBlock: # Imre Kicks MC (Hits/No Block)

                play sound "sounds/bs.mp3"
                scene Imre_Hook_block
                with hpunch

                pause 0.5
                $ stance = 1
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_imreAttack

            label imre_McHookHit: # Imre Kicks MC (Hits/No Block)

                play sound "sounds/hs.mp3"
                $ youDamage += 1
                scene Imre_Hook_hit
                with hpunch

                pause 0.5
                $ stance = 1
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4])
                if youDamage >= youHealth:
                        jump imre_McFightEnd
                jump mc_imreAttack

            label imre_McHookBlock: # Imre Kicks MC (Hits/No Block)

                play sound "sounds/bs.mp3"
                scene Imre_Hook_block
                with hpunch

                pause 0.5
                $ stance = 1
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_imreAttack

            label imre_McBodyhookHit: # Imre Kicks MC (Hits/No Block)

                play sound "sounds/hs.mp3"
                $ youDamage += 1
                scene Imre_BodyJab_hit
                with hpunch

                pause 0.5
                $ stance = 1
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_imreAttack

            label imre_McBodyhookBlock: # Imre Kicks MC (Hits/No Block)

                play sound "sounds/bs.mp3"
                scene Imre_BodyJab_block
                with hpunch

                pause 0.5
                $ stance = 1
                $ imreAttack = renpy.random.choice([1, 2, 3, 4])
                $ imreSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_imreAttack


            label mc_imreAttack:
                if simImreFight:
                    if imreStance == 1: # Jab Weakness
                        if simyou == 1:
                            jump mc_imreBodyhookBlock
                        if simyou == 2:
                            jump mc_imreHooksBlock
                        if simyou == 3:
                            jump mc_imreKickBlock
                        if simyou == 4 or simyou == 5 or simyou == 6:
                            jump mc_imreJabsHit
                    if imreStance == 2: # Hook Weakness
                        if simyou == 1:
                            jump mc_imreHooksBlock
                        if simyou == 2:
                            jump mc_imreJabsBlock
                        if simyou == 3:
                            jump mc_imreKickBlock
                        if simyou == 4 or simyou == 5 or simyou == 6:
                            jump mc_imreBodyhookHit
                    if imreStance == 3: # Body Hook Weakness
                        if simyou == 1:
                            jump mc_imreJabsBlock
                        if simyou == 2:
                            jump mc_imreHooksBlock
                        if simyou == 3:
                            jump mc_imreKickBlock
                        if simyou == 4 or simyou == 5 or simyou == 6:
                            jump mc_imreBodyhookBlock
                    if imreStance == 4: # Kick Weakness
                        if simyou == 1:
                            jump mc_imreBodyhookBlock
                        if simyou == 2:
                            jump mc_imreHooksBlock
                        if simyou == 3:
                            jump mc_imreJabsBlock
                        if simyou == 4 or simyou == 5 or simyou == 6:
                            jump mc_imreKickHit
                else:
                    call screen imreFight_MCAttack


            label mc_imreFightEnd: # MC wins fight against Imre
                $ v10_imre_win = True

                jump imre_fightEnd

            label imre_McFightEnd: # MC loses fight against Imre
                $ v10_imre_win = False
                jump imre_fightEnd

            label imre_fightEnd:
                hide screen imreFight_MCAttack
                hide screen imreFight_MCDefend
                hide screen fight_overlay
                $ youDamage = 0
                $ stance = 0
                stop music fadeout 3

            jump v10_fight_result

        "Ne pas combattre":
            scene v10mvi3 # FPP. Show Imre infront of camera in ring, mouth closed, hands raised ready to fight.
            with dissolve

            $ grant_achievement("bros_before_blows")
            u "Je ne pense pas pouvoir faire ça. Je, je... Je suis désolé les gars."

            scene v10mvi4 # FPP. Show Close up from ring of Imre and grayson stood watching, Imre mouth open, Grayson mouth closed
            with dissolve
            ry "Qu'est-ce que je viens de dire, bordel ?! Je viens littéralement..."

            scene v10mvi4a # FPP. Show Close up from ring of Imre and grayson stood watching, Imre mouth closed, Grayson mouth open
            with dissolve

            gr "Putain de chatte, va te battre avec cette salope ou tu dors dehors ce soir !"

            scene v10mvi3a # FPP. Same Camera as v10mvi3, Show Imre infront of camera in ring, mouth open, hands raised ready to fight.
            with dissolve

            imre "Hahaha, chatte."

            scene v10mvi3
            with dissolve

            u "Je ne peux pas, je ne peux pas."
            
            stop music fadeout 3

            jump v10_avoid_fight

    # -Transition to Scene 8-
