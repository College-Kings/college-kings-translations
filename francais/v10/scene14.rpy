# SCENE 14: Samantha At The Apes
# Locations: MC - Apes Living Room
# Characters: Sam (Outfit 2), MC (Outfit 1), Cameron (Outfit 3)
# Time: Sunday Morning
label v10_apes_samantha:

    scene v10ssap1 # TPP. Show MC in the Ape's living room. He's sitting on the couch, appearing exhausted, mouth closed.
    with fade

    play music "music/v10/Scene 14/Track Scene 14.mp3" fadein 3

    u "(Merde, je suis fatigué.)"

    scene v10ssap1a # TPP. Same camera as v10ssap1. MC's sitting on the couch, appearing exhausted, mouth closed. He reaches forward to grab the remote.
    with dissolve
    
    pause 0.5

    scene v10ssap1b # TPP. Same camera as v10ssap1. MC's sitting on the couch, appearing exhausted, mouth closed. He's holding the remote. Show Samantha come into the living room.
    with dissolve
    
    pause 0.5

    scene v10ssap1c # TPP. Same camera as v10ssap1. MC's sitting on the couch, appearing exhausted, mouth closed. He's holding the remote. Samantha sits down on the couch next to him, smiling, mouth open.
    with dissolve

    sa "Hé hé!"

    scene v10ssap2 # FPP. Perspective is from MC, who is sitting on the couch in Ape's living room. Show Sam (who is sitting beside him), normal/slightly curious expresison, mouth closed.
    with dissolve

    u "Hé..."

    scene v10ssap2a # FPP. Same camera as v10ssap2. Show Sam, normal/slightly curious expresison, mouth open.
    with dissolve

    sa "Quelque chose ne va pas ?"

    scene v10ssap2
    with dissolve

    u "Uhm... non, je vais bien. Je suis juste fatiguée."

    scene v10ssap2a
    with dissolve

    sa "Oh ok. J'ai une question pour toi."

    scene v10ssap2
    with dissolve

    u "Qu'est-ce qu'il y a ?"

    scene v10ssap2a
    with dissolve

    sa "J'ai beaucoup pensé aux fraternités et aux bagarres. Mon frère a été une tête brûlée toute sa vie."

    scene v10ssap2
    with dissolve

    u "*Gloussements* Vraiment ? Je n'ai pas remarqué."

    scene v10ssap2b # FPP. Same camera as v10ssap2. Show Sam, smiling, mouth open.
    with dissolve

    sa "*Rires* Oui, c'est très subtil. Mais oui, il a toujours été une tête brûlée donc ça me semble logique qu'un gars comme lui se batte et soit dans une fraternité comme celle-ci, mais tu n'es pas comme lui et pourtant tu es dans cette fraternité aussi."

    scene v10ssap2c # FPP. Same camera as v10ssap2. Show Sam, smiling, mouth closed.
    with dissolve

    u "Et ta question est..."

    scene v10ssap2a
    with dissolve

    sa "Eh bien, je suppose que je veux juste savoir pourquoi. C'est un peu bizarre, tu ne trouves pas ? Tu ne t'adaptes pas vraiment à tout le monde ici."

    scene v10ssap2
    with dissolve
    menu:
        "Je suis peux être une tête brûlée":
            $ addPoint("tm", 1)

            scene v10ssap2c
            with dissolve

            u "Je suis peux être une tête brûlée au moins quand j'ai besoin de l'être, *gloussements* parfois quand je veux l'être."

            scene v10ssap2b
            with dissolve

            sa "Donc tu as un côté dangereux... Je ne le savais pas."

            scene v10ssap2c
            with dissolve

            u "Je ne me suis peut-être pas battu avant l'université, mais je n'ai jamais laissé les gens me manquer de respect et je n'avais certainement pas peur de dire ce que je pensais."

            scene v10ssap2b
            with dissolve

            sa "Ce que nous avons en commun."

            scene v10ssap2
            with dissolve

            u "Je pense juste que parfois il y a de meilleurs moyens que la violence pour faire payer quelqu'un."

            scene v10ssap2a
            with dissolve

            sa "Qu'est-ce que tu veux dire ?"

            scene v10ssap2a
            with dissolve

            u "Au lycée, j'avais un professeur qui voulait toujours m'avoir."
            u "Les gens faisaient toutes sortes de choses, ils lui lançaient des avions en papier pendant le cours, trichaient sur ses tests et se moquaient de lui même s'il était dans la salle."
            u "Mais ils n'ont jamais eu de problèmes. Si je faisais quoi que ce soit de douteux, j'allais directement en retenue."
            u "Eh bien, à un moment donné, j'en ai eu vraiment marre et j'ai voulu l'énerver, tu sais, le rendre vraiment bon..."

            scene v10ssap2b
            with dissolve

            sa "Dis-moi que ça mène à quelque chose de vraiment juteux comme une farce de terminale ou du sucre dans un réservoir d'essence ?"

            scene v10ssap2c
            with dissolve

            u "Pas tout à fait. Il a annoncé qu'il allait être l'un des chaperons pour notre bal de fin d'année et je savais que sa fille allait à notre école et serait diplômée avec moi."
            u "Donc... pour faire court, j'ai invité sa fille au bal de fin d'année et après des allers-retours très douloureux, elle a dit oui."
            u "Nous avons dansé toute la nuit et j'ai essayé de le regarder autant que possible, c'était tellement drôle."
            u "Pour être honnête, la fille n'était pas vraiment enthousiaste quand elle a découvert pourquoi je lui avais demandé, mais... ça valait vraiment le coup. *Rires*"

            scene v10ssap2b
            with dissolve

            sa "*Rires* Rappelle-moi de ne jamais faire partie de tes plans de vengeance.."

            scene v10ssap2c
            with dissolve

            u "Haha, je m'en souviendrai."
       
        "Qu'est-ce que ça veut dire ??":
            $ addPoint("bro", 1)
            
            scene v10ssap2c
            with dissolve

            u "*Gloussements* Qu'est-ce que ça veut dire ?"

            scene v10ssap2b
            with dissolve

            sa "Tu sais... C'est juste que tu n'es pas vraiment du genre macho et fort.."

            scene v10ssap2c
            with dissolve

            u "Je te ferais savoir que je peux être un dangereux lutteur de pouce. Aussi, j'aime toujours faire des conneries, j'essaye juste d'être intelligent à propos des conneries que je fais."

            scene v10ssap2b
            with dissolve

            sa "*Rires* C'était ta citation de fin d'études ou quelque chose comme ça ?"

            scene v10ssap2c
            with dissolve

            u "Non, mais ça aurait pu l'être. Ma citation de terminale était bien meilleure. C'était quelque chose comme *glousse* \"Les tricheurs ne gagnent jamais, mais je viens de le faire.\""

            scene v10ssap2b
            with dissolve

            sa "*Rires* Donc tu étais le \"Je peux copier sur toi\" type de gars ?"

            scene v10ssap2c
            with dissolve

            u "Hé, qui est le plus intelligent, celui qui étudie toute la nuit pour avoir les bonnes réponses ou celui qui n'étudie pas et obtient les réponses de celui qui étudie le lendemain matin."

            scene v10ssap2b
            with dissolve

            sa "Comment dit-on ? \"Ne détestez pas le joueur, détestez le jeu.\""

            scene v10ssap2c
            with dissolve

            u "Exactement."

    scene v10ssap1d # TPP. Same camera as v10ssap1. MC and Samantha are sitting on the couch, smiling, mouths closed. Camera walks into the living room with an aggressive look on his face, mouth closed.
    with fade
    
    pause 0.5

    scene v10ssap3 # FPP. Perspective is from MC, who is sitting on the couch in Ape's living room. He is looking up at Cameron who is standing nearby. Show Cameron with an angry expression, mouth open.
    with dissolve
    
    ca "Qu'est-ce que vous faites ? [name] tu essaies de draguer ma soeur ?!"

    scene v10ssap3a # FPP. Same camera as v10ssap3. Show Cameron with an angry expression, mouth closed.
    with dissolve
    menu:
        "Peut-être":
            $ addPoint("tm", 1)
            
            scene v10ssap3a
            with dissolve

            u "Peut-être, peut-être pas. Qu'est-ce que ça peut te faire ?"

            scene v10ssap2d # FPP. Same camera as v10ssap2. Show Sam, with a smile that displays a bit of interest, mouth closed.
            with dissolve
            
            pause 0.5

            scene v10ssap3
            with dissolve

            ca "Je n'ai pas besoin de raison, mais ne drague pas ma soeur !"

            scene v10ssap3a
            with dissolve

            u "C'est ma faute, je n'avais pas réalisé que tu avais déjà appelé Prem's."

            scene v10ssap3
            with dissolve

            ca "Putain, non ! J'ai juste..."

            scene v10ssap1e # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Camera is standing nearby, angry expression, mouth closed. Sam is smiling, mouth open. MC is smiling, mouth closed.
            with dissolve

            sa "*Rires*"

            scene v10ssap1f # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Camera is standing nearby, angry expression, mouth open. Sam looks pissed, mouth closed. MC has a normal expression, mouth closed.
            with dissolve

            ca "Je ne vois pas ce qu'il y a de drôle, tu ne devrais pas être..."

            scene v10ssap1g # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Camera is standing nearby, angry expression, mouth closed. Sam looks pissed, mouth open. MC has a normal expression, mouth closed.
            with dissolve

            sa "TU NE DEVRAIS PAS ME DIRE CE QUE JE DEVRAIS OU NE DEVRAIS PAS FAIRE ! Laisse-nous seuls, Cameron."

            scene v10ssap1f 
            with dissolve

            ca "*Grognements*"

            scene v10ssap1h # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Camera is walking away, angry expression, mouth closed. Sam looks annoyed, mouth closed. MC has a normal expression, mouth closed.
            with dissolve
            
            pause 0.5

            scene v10ssap2c
            with fade

            u "C'était amusant.."

            scene v10ssap2b
            with dissolve

            sa "*Gloussements* Oh, la ferme. Et juste pour que ce soit clair, personne n'a dit Preums sur moi. Je ne suis pas un reste de lasagne.."

            scene v10ssap2c
            with dissolve

            u "Oh, je suppose que je dois dire aux gars d'oublier que j'ai appelé Prem's."

            scene v10ssap2d
            with dissolve

            sa "Alors tu as dit prem's, hein ?"

            scene v10ssap2c
            with dissolve

            u "Euh... il y a peut-être eu un appel au Prem's à un moment donné dans le passé."

            scene v10ssap2b
            with dissolve

            sa "*Rires*"

            scene v10ssap1i # TPP. Same camera as v10ssap1. Show MC and Sam sitting on the couch. Sam starts to stand up from the couch. Mouths closed, normal expressions.
            with dissolve
            
            pause 0.5

            scene v10ssap3b # FPP. Same camera as v10ssap3. Show Sam standing nearby, normal expression, mouth open.
            with dissolve

            sa "D'accord, j'ai des choses à faire, à plus tard."

            scene v10ssap3c # FPP. Same camera as v10ssap3. Show Sam standing nearby, normal expression, mouth closed.
            with dissolve

            u "Quel genre de trucs ?"

            scene v10ssap3b
            with dissolve

            sa "Uhm... tu sais ? Des trucs."

            scene v10ssap1j # TPP. Same camera as v10ssap1. Show MC sitting on the couch. Sam is walking away. Mouths closed, normal expressions.
            with dissolve

            u "(Ahh, elle est quelque chose de différent. Je devrais monter dans ma chambre.)"

            scene v10ssap1k # TPP. Same camera as v10ssap1. Show MC standing up from the couch. Mouth closed, normal expression.
            with dissolve
            
            pause 0.5
 
        "Je ne sais pas.":
            scene v10ssap3a
            with dissolve

            u "Je ne sais pas de quoi tu parles, on ne fait que parler. En tant qu'amis."

            scene v10ssap2e # FPP. Same camera as v10ssap2. Show Sam, with an expression of awkward disappointment, mouth closed.
            with dissolve
            
            pause 0.5

            scene v10ssap4 # TPP. Show MC and Sam sitting on the couch. Cameron is standing nearby, angry expression, mouth closed. Sam has an awkward, disappointed expression, mouth closed, and is standing up from the couch. MC has a normal expression, mouth closed.
            with dissolve
            
            pause 0.5

            scene v10ssap3
            with fade

            ca "Ça ressemblait à plus qu'une simple conversation amicale pour moi. Ne tentez rien et nous n'aurons pas de problème."

            scene v10ssap3a
            with dissolve

            u "D'accord..."

            scene v10ssap3
            with dissolve

            ca "Samantha a déjà assez souffert et n'a pas besoin de subir tes conneries. Tu fais quoi que ce soit qui la contrarie et tu es mort."

            scene v10ssap3a
            with dissolve

            u "Bien, peu importe."

            scene v10ssap1k
            with fade

            u "(Il peut vraiment être un connard parfois. Ce bon vieux Cameron. Je devrais aller dans ma chambre.)"
    stop music fadeout 3

    jump v10_call_with_lauren1 # jump to scene 15