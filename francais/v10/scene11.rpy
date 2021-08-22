# SCENE 11: 11) MC at Lindsey's Room
# Locations: Lindseys room
# Characters: MC (Outfit 1), Lindsey(Outfit 1)
# Time: Sunday Morning

label v10_linds_room:

    scene v10slds1 # TPP. Show MC arriving at the door to Lindsey's house and knocking. Normal expression, mouth closed.
    with fade

    play sound "sounds/knock.mp3"

    play music "music/v10/Scene 11/Track Scene 11.mp3" fadein 3

    pause 0.75
    
    scene v10slds1a # TPP. Same camera as v10slds1. Show MC and Lindsey. Lindsey answers the door. Sad expression, mouth closed.
    with dissolve

    pause 0.75

    scene v10slds2 # FPP. Lindsey just answered the door with MC standing outside. Show Lindsey, sad expression, mouth open.
    with dissolve

    li "Hé [name], *renifle* merci d'être venu."

    scene v10slds2a # FPP. Same camera as v10slds2. Show Lindsey, sad expression, mouth closed.
    with dissolve

    u "Bien sûr, tu semblais vraiment bouleversée et je voulais juste m'assurer que tout allait bien."

    scene v10slds2
    with dissolve

    li "Cela signifie vraiment beaucoup pour moi... J'avais juste besoin de parler à quelqu'un."

    scene v10slds2a # FPP. Same camera as v10slds2. Show Lindsey, sad expression, mouth closed.
    with dissolve

    u "Nous le faisons tous parfois."

    scene v10slds3 # FPP. MC and Lindsey are in Lindsey's room, sitting on her bed. Show Lindsey, sad expression, mouth open.
    with fade

    li "As-tu déjà l'impression que la vie ne ralentit jamais ? Comme dès que les choses commencent à s'adoucir, voici la prochaine grande chose ?"

    scene v10slds3a # FPP. Same camera as v10slds3. Show Lindsey, sad expression, mouth closed.
    with dissolve

    u "Ouais, surtout depuis que le collège a commencé. Même si cela peut être excitant, c'est quand même beaucoup parfois."

    scene v10slds3
    with dissolve

    li "Avant d'entrer à l'université, à quoi ressemblait ta vie ? Grande famille, petite famille, parents ?"

    scene v10slds3a
    with dissolve

    u "Euh... ma vie allait bien."

    u "Ma mère a toujours été une... euh... une personne froide. Quand j'étais enfant, elle voulait juste parcourir le monde, alors elle et mon père se sont séparés, je suis resté avec lui."
    
    u "Puis il a épousé ma belle-mère Julia. Mais on pouvait dire que ce n'était pas le genre de famille qu'il voulait. Il semblait qu'il considérait notre famille comme brisée."

    u "Donc, à un moment donné, il est devenu très distant, a trompé Julia et a fondé une nouvelle famille."
    u "Je l'aimais beaucoup et comme j'étais déjà assez vieux à ce moment-là, j'ai juste décidé de rester avec elle."

    u "Ce n'est pas comme si mon père voulait que j'aille avec lui de toute façon."

    scene v10slds3
    with dissolve

    li "Oh... Je suis désolé que tu es dû passer par là."

    scene v10slds3a
    with dissolve

    u "Ne m'éprenes pas, ce n'était pas si mal que ça."
    u "Vivre comme si vous étiez un enfant unique avec une belle-mère qui est déterminée à vous gâter."
    u "Beaucoup d'amour et d'attention pour compenser le manque de liens de sang n'est pas la pire vie au monde. *Rires*"

    scene v10slds3b # FPP. Same camera as v10slds3. Show Lindsey, uncomfortable expression, mouth closed.
    with dissolve
    
    pause 0.75

    scene v10slds3a
    with dissolve

    u "Je suis désolé, je ne devrais pas parler de moi, je suis venu ici pour toi. Ça te dérange de me dire ce qui te déprime ?"

    scene v10slds3
    with dissolve

    li "Eh bien, je ne sais pas si tu as entendu ou non, mais récemment, ma mère est décédée."

    li "Et ce matin... ça m'a un peu frappé. Je pensais que j'allais bien, j'étais distrait et je n'y pensais même pas beaucoup, tu vois ?"

    li "Mais quand je me suis réveillé... mon monde s'est juste effondré..."

    scene v10slds3a
    with dissolve

    menu:
        "Ouais, j'ai entendu":
            scene v10slds3a
            with dissolve

            u "Ouais, j'ai entendu. Je suis vraiment désolé pour ta perte."
            
            u "J'ai supposé que c'était pour ça que tu étais en colère, mais je ne voulais pas en parler, au cas où c'était autre chose."

            scene v10slds3
            with dissolve

            li "Si tu en as entendu parler, je suis sûr que d'autres soupirent aussi, nous savons tous que les mauvaises nouvelles voyagent plus vite que les bonnes."

        "Non, je n'avais aucune idée":
            scene v10slds3a
            with dissolve

            u "Oh mon Dieu, non, je n'avais pas entendu. Toutes mes condoléances."

            scene v10slds3
            with dissolve

            li "Je suis plutôt content que tu ne l'a pas entendu. Les gens qui ne savent pas le rendent plus facile à ignorer..."

    scene v10slds3a
    with dissolve
    
    u "Alors... vous étiez proches ? Toi et ta maman ?"

    scene v10slds3c # FPP. Same camera as v10slds3. Show Lindsey, with a sad (wistful) smile, mouth open.
    with dissolve

    li "Fermer serait un euphémisme. *Rires* Ma mère et moi avons tout fait ensemble et elle savait tout de moi. Elle était si belle aussi."

    li "Quand nous voyagions, les gens pensaient que nous étions sœurs. Parfois, quand nous partions en vacances, nous nous comportions comme si nous étions des sœurs et flirtions avec des gars."
    
    li "Nous avons beaucoup gaffé, mais c'était toujours tellement amusant avec elle."

    scene v10slds3d # FPP. Same camera as v10slds3. Show Lindsey, with a sad (wistful) smile, mouth closed.
    with dissolve

    u "Honnêtement, j'ai la chance de ne pas avoir eu à perdre quelqu'un dont je suis vraiment proche. Je ne peux même pas commencer à imaginer ce genre de douleur."

    scene v10slds3c
    with dissolve

    li "Ça fait mal, mais ma mère m'a élevé pour croire qu'un morceau de nos proches est toujours avec nous d'une manière ou d'une autre."

    li "Chaque fois que je me regarde dans le miroir ou que j'entends mon rire, je vois ma mère. Nous avions vraiment beaucoup de points communs. Elle tenait tellement à moi, parfois trop."

    scene v10slds3d
    with dissolve

    u "Wow... c'est une très belle pensée."

    scene v10slds3c
    with dissolve

    li "D'une certaine manière, elle était vraiment mon étoile polaire. Je n'ai jamais rien fait sans son intervention." 

    li "Elle a toujours su ce que j'avais besoin d'entendre et maintenant je suis là sans elle et je n'ai aucune idée de ce que je vais faire."

    li "Je n'ai pas la motivation de faire quoi que ce soit. L'école semble inutile, la maison semble inutile, tout semble inutile."

    li "Je sais que c'est normal d'être triste, mais parfois je ne suis pas seulement triste... Je suis vraiment en colère... Je... Je ne peux pas croire qu'elle soit vraiment partie. Et elle ne reviendra jamais."

    scene v10slds3d
    with dissolve
    menu:
       "Continuez à écouter":

            scene v10slds3c
            with dissolve
            
            li "Ce qui est triste, c'est que j'ai passé tellement de temps avec ma mère et nos personnalités se ressemblent tellement que même si elle n'est pas là, je sais EXACTEMENT ce qu'elle dirait."

            scene v10slds3d
            with dissolve

            u "Et qu'est-ce qu'elle dirait ?"

            scene v10slds3c
            with dissolve

            li "\"Arrête de te morfondre, commence à espérer !\" Haha, elle disait la même chose à chaque fois que j'étais triste depuis que je suis une petite fille."
            li "Être triste avec ma mère était un grand non non. Ma mère avait ça \"toujours être positif\" attitude envers elle."

            scene v10slds3d
            with dissolve
            menu:
                "Parler de sa mère":
                    scene v10slds3d
                    with dissolve
                   
                    u "Ta mère semble très sage."

                "Parle d'elle":
                    scene v10slds3d
                    with dissolve
                    u "Parfois, il est bon d'être triste."

                    scene v10slds3c
                    with dissolve

                    li "Tu es vraiment un bon auditeur. Je savais que te contacter était la meilleure chose que je pouvais faire."

                    li "Honnêtement, le simple fait de tout évacuer me fait déjà me sentir beaucoup mieux."


       "Faire une blague":
            
            if kct == "confident": # RCS - if MC chooses 'Faire une blague' with KCT confident

                scene v10slds3e # FPP. Same camera as v10slds3. Show Lindsey, with a somewhat amused smile, mouth closed.
                with dissolve

                u "Hé, au moins tu ne vas pas finir comme ce marin qui a suivi l'étoile polaire et qui a fini par mourir de froid dans une tempête de neige, non ?"

                call screen kctPopup
                
                scene v10slds3f # FPP. Same camera as v10slds3. Show Lindsey, with a somewhat amused smile, mouth open.
                with dissolve

                li "Haha, c'est vrai. Je suppose que ce n'était pas la meilleure référence."

                scene v10slds3e
                with dissolve

                u "Haha, juste pour te taquiner."

                scene v10slds3f
                with dissolve

                li "Haha, ouais je sais je sais. Ça craint parce que même si je souhaite que ma mère soit là pour me parler, je sais déjà exactement ce qu'elle dirait si elle l'était."

                scene v10slds3e
                with dissolve

                u "Et qu'est-ce qu'elle dirait ?"

                scene v10slds3f
                with dissolve

                li "\"Arrête de te morfondre, commence à espérer!\" Elle ne m'a jamais laissé me promener triste, même quand je le voulais."
                
                li "Ma mère était positive même quand être positif était difficile. Donc je suppose que je sais déjà ce que je dois faire."

                scene v10slds3e
                with dissolve
                menu:
                    "Parler de sa mère":
                        scene v10slds3e
                        with dissolve
                        
                        u "Ta mère semble très sage."

                        scene v10slds3c
                        with dissolve

                        li "Ouais... elle l'était."

                    "Parle sur elle":
                        scene v10slds3e
                        with dissolve

                        u "Parfois il est bon d'être triste."

            else: # RCS - kct is not confident
                $ sadlind_reaction = True # RCS - variable for MC getting bad reaction from Lindsey
                
                scene v10slds3d
                with dissolve
                
                u "Hé, au moins tu ne vas pas finir comme ce marin qui a suivi l'étoile polaire et qui a fini par mourir de froid dans une tempête de neige, non ?"

                scene v10slds3c
                with dissolve

                li "Quoi ?"

                scene v10slds3d
                with dissolve

                u "Oh, c'était juste une blague..."

                scene v10slds3c
                with dissolve

                li "Ouais... Je n'ai pas vraiment l'impression que je peux me mettre dans un esprit de plaisanterie en ce moment."

                scene v10slds3d
                with dissolve

                u "Oh euh ma faute, j'ai pensé que j'allais essayer d'alléger l'ambiance."

                scene v10slds3c
                with dissolve

                li "C'est bien, parce que j'aimerais que ma mère soit là... mais je sais aussi déjà exactement ce qu'elle dirait."

                scene v10slds3d
                with dissolve

                u "Et c'est ?"

                scene v10slds3f
                with dissolve

                li "\"Arrête de te morfondre, commence à espérer !\" Elle ne m'a jamais laissé me promener triste, même quand je le voulais."

                li "Ma mère était positive même quand être positif était difficile. Donc je suppose que je sais déjà ce que je dois faire."

                scene v10slds3e
                with dissolve

                menu:
                    "Parler de sa mère":
                        scene v10slds3e
                        with dissolve

                        u "Ta mère semble très sage."

                        scene v10slds3c
                        with dissolve

                        li "Ouais... elle l'était."

                    "Parle sur elle":
                        scene v10slds3e
                        with dissolve
                    
                        u "Parfois, il est bon d'être triste."


    scene v10slds3d 
    with dissolve

    u "Je suis juste content que tu te sentes un peu mieux."

    scene v10slds3c
    with dissolve

    li "Je ne me sentirais pas mieux sans toi. Je suis content de t'avoir appelé avant tout le monde."

    scene v10slds3g # FPP. Same camera as v10slds3. Show Lindsey, looking away from MC with her hand on her ear, a bit of a thoughtful/shy expression, mouth closed.
    with dissolve

    pause 0.75

    scene v10slds3f
    with dissolve

    li "Je suis désolé, je ne sais pas si j'aurais dû être aussi direct et dragueuse avant."

    scene v10slds3e
    with dissolve

    menu:
        "J'aime bien":
            
            if kct == "confident": # RCS - if MC chooses 'I like it' with KCT confident
                
                scene v10slds3e
                with dissolve
                u "Je ne dirais jamais non à l'attention que tu voulais donner."

                call screen kctPopup

                scene v10slds3f
                with dissolve

                li "Ah bon ? Je vais peut-être devoir t'en parler un de ces jours."

                scene v10slds3e
                with dissolve

                u "Dites simplement le mot."

            else: # RCS - MC is not KCT confident
                $ sadlind_reaction = True # RCS - variable for MC getting bad reaction from Lindsey

                scene v10slds3d
                with dissolve
                u "Je ne dirais jamais non à l'attention que tu voulais donner."

                scene v10slds3c
                with dissolve

                li "Je ne suis pas sûr que ce soit le meilleur moment..."

                scene v10slds3b
                with dissolve

                u "Euh ouais... non... Je comprends. Nous n'avons pas à le faire, tu sais... ahh tant pis."
   
        "je comprends":

            scene v10slds3e
            with dissolve

            u "Oh, ne t'en fais pas. Tu traverses des trucs, je comprends tout à fait."

            scene v10slds3f
            with dissolve

            li "Merci [name], cela signifie vraiment beaucoup pour moi."

            scene v10slds3e
            with dissolve

            u "N'importe quand."

    scene v10slds3c
    with dissolve

    li "Merci d'être venu [name]."

    scene v10slds3d
    with dissolve

    u "Ouais, bien sûr."

    if not sadlind_reaction: # -If no bad reaction (no flirting, no joke without KCT)-

        scene v10slds4 # TPP. Show Lindsey leaning over and hugging MC while they sit on the bed. MC facing away from camera. Lindsey has a little smile, mouth open.
        with dissolve

        li "Je suis sûr que j'ai pris assez de ta journée avec toutes mes paroles tristes, je vais arrêter de te prendre en otage. J'espère te revoir bientôt."

        scene v10slds4a # TPP. Same camera as v10slds4. Show Lindsey leaning over and hugging MC while they sit on the bed. MC facing away from camera. Lindsey has a little smile, mouth closed.
        with dissolve

        u "Je m'assurerai que tu le fasses."

        scene v10slds5 # TPP. Show MC leaving Lindsey's house. She is standing in the open doorway, watching him leave with a little smile, mouth closed.
        with fade

    else: # -If bad reactions-

        scene v10slds3c
        with dissolve
        
        li "Alors euh, je suppose que je devrais te laisser partir, hein ?"

        scene v10slds3d
        with dissolve

        u "Tant que tu te sentes bien."

        scene v10slds3c
        with dissolve

        li "Ouais je me sens bien."

        scene v10slds3d
        with dissolve

        u "Bon à entendre. On se voit plus tard."

        scene v10slds3c
        with dissolve

        li "Oui, à bientôt [name]."

        scene v10slds5a # TPP. Same camera as v10slds5. Show MC leaving Lindsey's house. The door is closed behind him. (Lindsey is not in sight.)
        with fade
    stop music fadeout 3


if joinwolves: # I don't know this variable name
    jump v10_wolves_redec

else: # RCS - if MC is an ape?
    jump v10_apes_samantha



