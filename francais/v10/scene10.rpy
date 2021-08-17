# SCENE 10: MC Wakes Up Room Scene
# Locations: MC Apes/Wolves Room
# Characters: MC (Underwear)
# Time: Sunday Morning

init python:
    def v10s10_reply1():
        setattr(store, "v10s10_hangWLinds", True)
        contact_Lindsey.newMessage("Vraiment ? Merci :*")
        contact_Lindsey.addReply("Je suis en route")

label v10_sun_morn:
    play music "music/v10/Scene 10/Track Scene 10.mp3" fadein 3
    if joinwolves:
        scene v10sum1 # TPP. Show MC in his Wolves bed looking up at the ceiling, MC looks tired.
        with fade
        play sound "sounds/vibrate.mp3"

        pause 1.25

        scene v10sum2 # TPP. Show MC reaching for his phone.
        with dissolve

        pause 0.75

        scene v10sum2a # TPP. Same as sum2, MC now on his phone in bed.
        with dissolve
        pause 0.75
    
        if v10_ryan_fight and not v10_ryan_win:
            $ contact_Riley.newMessage("Hé [name], ça va ?", queue=False)
            $ contact_Riley.addReply("On fait aller.")
            $ contact_Riley.newMessage("Comment tu te sens après le combat ?")
            $ contact_Riley.addReply("Bien.")
            $ contact_Riley.newMessage("Ecoute, je voulais juste te dire de ne pas le laisser t'atteindre.")
            $ contact_Riley.addReply("Tu penses que ça me dérange ? Le mec a juste eu de la chance, c'est tout.")
            $ contact_Riley.newMessage("Et bien je sais que ça me dérangerait ! Qui aime perdre, non ?")
            $ contact_Riley.addReply("C'est bon Riley, tu n'es vraiment pas obligé de faire ça.")
            $ contact_Riley.newMessage("Faire quoi ? Je voulais juste te faire savoir que je suis là pour toi si tu as besoin de moi.")
            $ contact_Riley.addReply("J'apprécie")
            $ contact_Riley.newMessage("Et je continuerai d'essayer d'attirer ton sourire.")
            $ contact_Riley.addReply("Peut-être une autre fois.")
            $ contact_Riley.newMessage("OK, je comprends. A plus")
            $ contact_Riley.addReply("A plus")

        elif v10_ryan_fight:
            $ contact_Riley.newMessage("Hé champion, tu nous as fait un show incroyable hier soir ! :)", queue=False)
            $ contact_Riley.addReply("Merci, Riley.")
            $ contact_Riley.newMessage("J'ai particulièrement aimé ce dernier coup de poing. Je veux dire, je ne suis pas dans la violence mais, tu sais.")
            $ contact_Riley.addReply("Haha je vais faire semblant et dire oui.")
            $ contact_Riley.newMessage("Quoi qu'il en soit, continues comme ça ! tu auras des supporters au coin de la rue. :)")
            $ contact_Riley.addReply("Que dire à part merci encore. Ce n'est qu'un début, je suppose.")
            $ contact_Riley.newMessage("Malgré le fait qu'il ne faut pas que tu te blesses !")
            $ contact_Riley.addReply("Hahah, je vais essayer.")
            $ contact_Riley.newMessage("Promis ?")
            $ contact_Riley.addReply("Promis.")
            $ contact_Riley.newMessage("Un petit doigt ?")
            $ contact_Riley.addReply("A plus, Riley. :)")

        else:
            $ contact_Josh.newMessage("Amis ou pas amis, mec wtf ?! C'était un bon spectacle gâché !", queue=False)
            $ contact_Josh.newMessage("Je dis juste que tu as manqué d'impressionner beaucoup de femmes aujourd'hui", queue=False)
            $ contact_Josh.addReply("Je sais... Mais bon, peut-être que certains apprécient la compassion ?")
            $ contact_Josh.newMessage("Haha, bien sûr mec")
            $ contact_Josh.addReply("Peu importe mec.")

        label v10s10_PhoneContinueJoshW1:
            if contact_Josh.replies or contact_Riley.replies:
                call screen phone
            if contact_Josh.replies or contact_Riley.replies:
                u "(Je devrais vérifier mon téléphone.)"
                jump v10s10_PhoneContinueJoshW1

        play sound "sounds/vibrate.mp3"

        if v10_ryan_win:
            $ contact_Lindsey.newMessage("Hé, [name]... félicitation pour la victoire.", queue=False)
            $ contact_Lindsey.newMessage("Je sais, c'est assez tôt, mais", queue=False)

        else:
            $ contact_Lindsey.newMessage("Hé, [name]... Je sais que tu as beaucoup de choses en tête en ce moment avec tout ce qui s'est passé hier...", queue=False)
            
        $ contact_Lindsey.newMessage("Je viens de gérer des trucs...", queue=False)
        $ contact_Lindsey.newMessage("Et j'ai besoin de quelqu'un à qui parler", queue=False)
        $ contact_Lindsey.newMessage("Désolé, nous ne nous connaissons même pas très bien", queue=False)
        $ contact_Lindsey.newMessage("C'est juste que je sens que je peux te parler...", queue=False)
        $ contact_Lindsey.newMessage("Je ne sais pas, je suis désolé, je ne veux pas te déranger", queue=False)
        $ contact_Lindsey.newMessage("Oublie juste ce que j'ai dit", queue=False)
        $ contact_Lindsey.addReply("Si tu as besoin de quelqu'un pour parler, je peux venir tout de suite !", v10s10_reply1)
        $ contact_Lindsey.addReply("Euh d'accord. Pas de soucis, dis-moi si tu as besoin de quelque chose")

        label v10s10_PhoneContinueLinW:
            if contact_Lindsey.replies:
                call screen phone
            if contact_Lindsey.replies:
                u "(Je devrais répondre à Lindsey.)"
                jump v10s10_PhoneContinueLinW

        scene v10sum3 # TPP. Show MC placing his phone back down and sitting on the edge of his bed.
        with dissolve

        u "(Faisons en sorte que cette journée soit meilleure qu'hier)"

        scene black
        with fade
        stop music fadeout 3
        if v10s10_hangWLinds:
            jump v10_linds_room

        else:
            jump v10_mc_clock_trans

    else:
        scene v10sum4 # TPP. Show MC in his Apes bed looking up at the ceiling, MC looks tired.
        with fade
        play sound "sounds/vibrate.mp3"

        pause 1.25

        scene v10sum5a # TPP. Same as sum2, MC now on his phone in bed.
        with dissolve

        pause 0.75
        
        if v10_imre_fight and not v10_imre_win:
            $ contact_Riley.newMessage("Hé [name], ça va ?", queue=False)
            $ contact_Riley.addReply("On fait aller.")
            $ contact_Riley.newMessage("Comment te sens-tu après le combat ?")
            $ contact_Riley.addReply("Bien.")
            $ contact_Riley.newMessage("Écoute, je voulais juste te dire de ne pas te laisser faire.")
            $ contact_Riley.addReply("Tu penses que ça me dérange ? Le mec a juste eu de la chance, c'est tout.")
            $ contact_Riley.newMessage("Et bien je sais que ça me dérangerait ! Qui aime perdre, non ?")
            $ contact_Riley.addReply("C'est bon Riley, tu n'es vraiment pas obligé de faire ça.")
            $ contact_Riley.newMessage("Faire quoi ? Je voulais juste te faire savoir que je suis là pour toi si tu as besoin de moi.")
            $ contact_Riley.addReply("J'apprécie.")
            $ contact_Riley.newMessage("Et je continuerai d'essayer d'attirer ton sourire.")
            $ contact_Riley.addReply("Peut-être une autre fois.")
            $ contact_Riley.newMessage("OK, je comprends. A plus")
            $ contact_Riley.addReply("A plus")

        elif v10_imre_fight:
            $ contact_Riley.newMessage("Hé champion, tu nous as fait un super show hier soir ! :)", queue=False)
            $ contact_Riley.addReply("Merci, Riley.")
            $ contact_Riley.newMessage("J'ai particulièrement aimé ce dernier coup de poing. Je veux dire, je ne suis pas dans la violence mais, tu sais.")
            $ contact_Riley.addReply("Haha je vais faire semblant et dire oui.")
            $ contact_Riley.newMessage("Quoi qu'il en soit, continues comme ça ! tu aurasdes supporters au coin de la rue. :)")
            $ contact_Riley.addReply("Que dire à part merci encore. Ce n'est qu'un début, je suppose.")
            $ contact_Riley.newMessage("Malgré le fait qu'il ne faut pas que tu te blesses !")
            $ contact_Riley.addReply("Haha, Je vais essayer.")
            $ contact_Riley.newMessage("Promis?")
            $ contact_Riley.addReply("Promis.")
            $ contact_Riley.newMessage("Un petit doigt ?")
            $ contact_Riley.addReply("A plus, Riley. :)")

        else:
            $ contact_Josh.newMessage("Amis ou pas amis, mec wtf ?! C'était un bon spectacle gâché !", queue=False)
            $ contact_Josh.newMessage("Je dis juste que tu as manqué d'impressionner beaucoup de femmes aujourd'hui", queue=False)
            $ contact_Josh.addReply("Je sais... Mais bon, peut-être que certains apprécient la compassion ?")
            $ contact_Josh.newMessage("Haha, bien sûr mec")
            $ contact_Josh.addReply("Peu importe mec.")

        label v10s10_PhoneContinueJoshW2:
            if contact_Josh.replies or contact_Riley.replies:
                call screen phone
            if contact_Josh.replies or contact_Riley.replies:
                u "(je devrais vérifier mon téléphone.)"
                jump v10s10_PhoneContinueJoshW2

        play sound "sounds/vibrate.mp3"

        if v10_imre_win:
            $ contact_Lindsey.newMessage("Hé, [name]... félicitation pour la victoire.", queue=False)
            $ contact_Lindsey.newMessage("Je sais, c'est un peu tôt, mais", queue=False)

        else:
            $ contact_Lindsey.newMessage("Hé, [name]... Je sais que tu as beaucoup de choses en tête en ce moment avec tout ce qui s'est passé hier...", queue=False)
            
        $ contact_Lindsey.newMessage("Je viens de gérer des trucs...", queue=False)
        $ contact_Lindsey.newMessage("Et j'ai besoin de quelqu'un à qui parler", queue=False)
        $ contact_Lindsey.newMessage("Désolé, nous ne nous connaissons même pas très bien", queue=False)
        $ contact_Lindsey.newMessage("C'est juste que je sens que je peux te parler...", queue=False)
        $ contact_Lindsey.newMessage("Je ne sais pas, je suis désolé, je ne veux pas te déranger", queue=False)
        $ contact_Lindsey.newMessage("Oublie juste ce que j'ai dit", queue=False)
        $ contact_Lindsey.addReply("Si tu as besoin de quelqu'un pour parler, je peux venir tout de suite !", v10s10_reply1)
        $ contact_Lindsey.addReply("Euh d'accord. Pas de soucis, dis-moi si tu as besoin de quelque chose")

        label v10s10_PhoneContinueLinA:
            if contact_Lindsey.replies:
                call screen phone
            if contact_Lindsey.replies:
                u "(Je devrais répondre à Lindsey.)"
                jump v10s10_PhoneContinueLinA

        scene v10sum6 # TPP. Show MC placing his phone back down and sitting on the edge of his bed.
        with dissolve

        u "(Faisons en sorte que cette journée soit meilleure qu'hier)"

        scene black
        with fade
        stop music fadeout 3
        if v10s10_hangWLinds:
            jump v10_linds_room

        else:
            jump v10_mc_clock_trans