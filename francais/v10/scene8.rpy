# SCENE 8: Fight Results
# Locations: Abandoned Warehouse
# Characters: Ryan (Outfit 2), Josh (Outfit 2),MC (Outfit 7), Grayson (Outfit 3),Imre (Outfit 4), Sebastian (Outfit 1),Cameron (Outfit 3),Chris (Outfit 2)
# Time: Saturday Night
label v10_fight_result:
    $ renpy.end_replay()
    scene v10fr1 # FPP. Show close up of Josh pointing down towards the floor, slight smile, mouth open
    with dissolve
    jo "*Rires* Dans les mots de Smokey, \"vous avez été assommé !\""

    play music "music/v10/Scene 8/Track 8.mp3" fadein 3

    if joinwolves:
    # -If MC wins the fight against Ryan-

        if v10_ryan_win:

            scene v10fr1
            with dissolve

            jo "Je pense que comme nous nous y attendions tous, [nom] a dominé ! Alors mesdames, si vous avez envie d'un gagnant ce soir, j'en ai trouvé un."

            jo "Quelque chose de l'homme lui-même ?"

            scene v10fr2 # TPP. Show close up of MC hands in the air above head, excited face, mouth closed
            with dissolve

            if reaction == 0.5:
                $ grant_achievement("lights_out")

            u "Ce n'était pas seulement un combat pour moi, c'était un combat pour moi et mes frères."

            u "C'est notre victoire !"

            scene v10fr3 # TPP. Show MC and Josh standing in ring, ryan on the floor in the ring, Josh mouth open
            with dissolve

            jo "Heureux de voir l'excitation ! Félicitations pour une victoire bien méritée."

            scene v10fr5 # FPP. Show close up of MC exiting the ring, mouth closed
            with dissolve

            pause 0.5

            scene v10fr4 # FPP. Show chris and sebastian, chris one hand up in the air, excited face, chris mouth open, sebatian mouth closed
            with dissolve

            ch "*Le Loup hurle* Tu nous as rendu fier, putain de super boulot !"

            u "(putain je l'ai fait!)"
            
            u "(Ouf, je suis tellement épuisé maintenant... Je veux juste aller me coucher.)"

            
            stop music fadeout 3
            jump v10_leave_fight

        else:

            scene v10fr3b # TPP. Show imre and Josh standing in ring, MC on the floor in the ring, Josh mouth open, imre mouth closed
            with dissolve
            jo "Je n'ai certainement pas vu cela se produire, je pense que personne ne l'a fait. Des mots de l'homme lui-même ?"

            scene v10fr3a # TPP. Show Ryan and Josh standing in ring, MC on the floor in the ring, Josh mouth closed, Ryan mouth open
            with dissolve

            ry "J'ai travaillé dur pour ça et je l'ai eu ! Putain de Wolves, ces nuls !"

            scene v10fr3b # TPP. Show Ryan and Josh standing in ring, MC on the floor in the ring, Josh mouth open, Ryan mouth closed
            with dissolve

            jo "Heureux de voir l'excitation ! Félicitations pour une victoire bien méritée."

            scene v10fr6 # TPP. Show Ryan helping MC get up, Ryan mouth open, Mc mouth closed
            with dissolve

            ry "J'espère que tu vas bien, mec. Je ne peux pas me permettre d'être un ami dans un combat. Tu vas bien ?"

            scene v10fr7 # FPP. Show ryan in ring, neutral look, mouth closed
            with dissolve

            u "Ouais, je vais bien. Félicitations."

            scene v10fr5
            with dissolve

            pause 0.5

            scene v10fr4a # FPP. Show chris and sebastian, both slight frown, chris mouth open, sebastian mouth open
            with dissolve
            ch "Perdre est toujours difficile, mais tu te bats bien."

            scene v10fr4b # FPP. Show chris and sebastian, both slight frown, chris mouth closed, sebastian mouth closed
            with dissolve

            u "Désolé, Chris. Je voulais vraiment faire mieux."

            scene v10fr4a # FPP. Show chris and sebastian, both slight frown, chris mouth open, sebastian mouth open
            with dissolve
            ch "C'est bon, mec. Tu l'auras la prochaine fois."

            scene v10fr4b # FPP. Show chris and sebastian, both slight frown, chris mouth closed, sebastian mouth closed
            with dissolve

            u "(Putain, j'ai laissé tomber toute ma fraternité...)"
            u "(Dieu, je veux juste aller au lit.)"

            stop music fadeout 3

            jump v10_leave_fight
    else:

        if v10_imre_win:
            scene v10fr1
            with dissolve
            jo "Je pense que comme nous nous y attendions tous, [nom] a dominé ! Alors mesdames, si vous avez envie d'un gagnant ce soir, j'en ai trouvé un."

            jo "Quelque chose de l'homme lui-même ?"

            scene v10fr2
            with dissolve

            if reaction == 0.5:
                $ grant_achievement("golden_boy")

            u "Ce n'était pas seulement un combat pour moi, c'était un combat pour moi et mes frères."

            u "C'est notre victoire!"

            scene v10fr3c # TPP. Show MC and Josh standing in ring, Imre on the floor in the ring, Josh mouth open
            with dissolve

            jo "Heureux de voir l'excitation ! Félicitations pour une victoire bien méritée."

            scene v10fr4c # FPP. Show Grayson and cameron, both slight smile, grayson mouth open, cameron mouth closed
            with dissolve
            gr "*Chantant* Apes! Apes! Apes!"
            gr "Putain ouais, mec!"

            u "(putain je l'ai fait!)"
            
            u "(Ouf, je suis tellement épuisé maintenant... Je veux juste aller me coucher.)"
            stop music fadeout 3

            jump v10_leave_fight
        
        else:
            scene v10fr3d # TPP. Show imre and Josh standing in ring, MC on the floor in the ring, Josh mouth open, imre mouth closed
            with dissolve
            jo "Je n'ai certainement pas vu cela se produire, je pense que personne ne l'a fait. Des mots de l'homme lui-même ?"

            scene v10fr3e # TPP. Show imre and Josh standing in ring, MC on the floor in the ring, Josh mouth closed, imre mouth open
            with dissolve

            imre "WOLVES POUR LA VIE ! Aussi, les dames m'ont frappées."

            scene v10fr3d
            with dissolve

            jo "Heureux de voir l'excitation ! Félicitations pour une victoire bien méritée."

            scene v10fr5 # FPP. Show close up of MC exiting the ring, mouth closed
            with dissolve

            pause 0.5

            scene v10fr4d # FPP. Show grayson and cameron, both slight frown, grayson mouth open, cameron mouth closed
            with dissolve
            gr "C'était de la merde, mec ! Tu dois faire mieux si tu veux représenter APES !"

            scene v10fr4e # FPP. Show grayson and cameron, both slight frown, grayson mouth closed, cameron mouth closed
            with dissolve

            u "D'accord, je suis désolé..."

            scene v10fr4d # FPP. Show grayson and cameron, both slight frown, grayson mouth open, cameron mouth closed
            with dissolve
            gr "Désolé, ce n'est pas assez bon. J'ai vu quelque chose en toi, ne me le fais pas regretter."

            u "(Putain, j'ai laissé tomber toute ma fraternité...)"
            
            u "(Dieu, je veux juste aller au lit.)"
            stop music fadeout 3
            
            jump v10_leave_fight



