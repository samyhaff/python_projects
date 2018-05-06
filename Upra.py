import math
import random
import numpy as np

#Texte à gogo

Message="Paroles.netParoles Bigflo & OliParoles Alors Alors PAROLES DE LA CHANSON ALORS ALORS PAR BIGFLO & OLI Auteurs: Florian Ordonez,Olivio Ordonez Compositeurs: Clément Libes,Florian Ordonez,Olivio Ordonez Editeurs: Warner Chappell Music France,Bmg Rights Management (France),La Main Invisible Publishing Chanson manquante pour Bigflo & Oli ? Proposer les paroles Proposer une correction des paroles de Alors Alors Paroles de la chanson Alors Alors par Bigflo & Oli - Le numéro que vous avez demandé n'est pas attribué ou n'est pas accessible, votre appel ne peut aboutir - Pfff... Putain [Bigflo & Oli] Alors alors Dis-moi qu't'es resté avec elle Tu m'disais : C'est la bonne et bordel, qu'elle est belle On refaisait le monde, sur le canap' de l'appart Maintenant j'voudrais savoir où tu te caches sur la carte Alors alors On s'est promis de pas s'lâcher, alors alors, et je crois bien qu'on s'est raté T'as changé de numéro ou t'avais pas envie de me parler quand je t'ai appelé, hein ? Alors alors Est-ce que t'as fini tes études ? T'avais plein d'rêves, mais juste pas assez d'thune J'ai une liste de tout c'que j'voudrais dire Toi qui répondais présent quand on parlait d'avenir Alors alors On devait faire le tour de la Terre Tu sais, moi, ma valise est encore prête Et si jamais tu nous reviens, est-ce que j'vais te reconnaître ? Faut pas qu'on laisse mourir nos promesses.. (non) Alors alors T'es où ? Tu m'manques C'est fou ! J'y pense Chaque jour, j'te vois partout ! Ils disent que tu reviendras pas, que t'es malade, que t'es mort J'aimerais que tu sois là, juste pour leur donner tort Alors, dis moi qu'est ce qu'tu deviens ? C'est vrai, ça fait longtemps Alors, dis moi qu'est ce qu'tu deviens ? C'est vrai, ça fait longtemps, qu'tu dis rien J'ai cherché dans le quartier mais non, non J'ai fait le tour de la Terre mais non, non J'ai demandé à ta mère mais non, non Pas d'nouvelles (pas d'nouvelles) J'ai attendu tout l'été mais non, non J'ai espéré tout l'hiver mais non, non Mais comme dit le proverbe, (ah !) Bonne nouvelle [Bigflo & Oli] Alors alors T'es parti, chercher ton Eldorado ? Tout le monde t'adore-adore On s'kiffait à mort, amore T'es peut-être à Bora-Bora, en maillot ou en tongs Si c'est une de tes blagues, celle là elle est trop longue Alors Alors, comment c'est ailleurs ? J'attends un SMS ou un pigeon voyageur Y'a encore nos tags sur le banc, lisibles et entiers Faut qu'tu vois comme la ville a changée.. Alors alors Tu sais que je suis un peu râleur T'as toujours eu du retard, t'étais jamais à l'heure-à l'heure Allô allô ? Y'a comme une latence C'est plus que du retard là, c'est une absence Alors alors Des nouvelles ? Même si elle sont mauvaises J'ai fait tous les hôpitaux, appelé tous les hôtels Si t'en as marre, dis le moi en face, cash ! Tu sais, j'ai passé l'âge de jouer à cache cache Alors alors Faut qu'tu sortes de ta planque On suffoque dans la pente On supporte plus l'attente J'en ai marre, il m'tardes tellement le dénouement Est-ce ça t'plait, de savoir que tu nous manques ? Alors, dis moi qu'est-ce tu deviens ? C'est vrai, ça fait longtemps Alors, dis moi qu'est-ce tu deviens? C'est vrai, ça fait longtemps, qu'tu dis rien J'ai cherché dans le quartier mais non, non J'ai fait le tour de la Terre mais non, non J'ai demandé à ta mère mais non, non Pas d'nouvelles (d'nouvelles) J'ai attendu tout l'été mais non, non J'ai espéré tout l'hiver mais non, non Mais comme dit le proverbe, (ah !) Bonne nouvelle Alors, alors, alors, alors, alors... Alors, alors, alors, alors, alors... (tu nous manques frérot) Alors, alors, alors, alors, alors... (Ouais, on a cherché partout !) Alors, alors, alors, alors, alors... (ça fait longtemps) Alors, dis moi qu'est ce qu'tu deviens? C'est vrai, ça fait longtemps Alors, dis moi qu'est ce qu'tu deviens? C'est vrai, ça fait longtemps, qu'tu dis rien Je suis Enfin là, cette terre n'est plus un mirage. Je suis, arrivé par bateau mais surtout par miracle. Une nouvelle vie m'attend ici, bien plus calme et plus stable. Ce matin j'ai écrit tout va bien au dos de la carte postale. Je suis Fier, mais comment vous décrire tout ce que j'ressens. Quand je marche en ville, de moins en moins de gens me ressemblent. Dans l'ascenseur, je parle même plus la langue de ma voisine. A force de planter des arbres, y'aura plus d'places pour nos racines. Je suis Fatigué, mal au dos et mal aux reins. Les rides sur mon visage me rappellent les montagnes de là où j'viens. On m'a menti, et c'est trop tard que je l'ai compris. On dit qu'ce pays n'est pas le mien alors qu'c'est moi qui l'ai construit. Je suis Assis, et le destin a fait que j'me relèverai jamais. Dans cet océan j'ai l'impression d'avoir toujours ramé. Un casse-tête pour monter dans le bus. Aller au taff, passer leurs portes Souvent les gens me regardent et me répondent que c'est pas de leur faute. Je suis Heureux, jeune diplômé, j'ai étonné ceux qui rêvaient de me voir abandonner. Ma famille est loin d'ici, j'espère que là-bas ils sont fiers. Je viens de gagner le combat qu'avait commencé ma mère. Je suis Confiante, j'regarde ma classe un peu trop pleine pour moi. Et j'leur tiendrais la main jusqu'à ce que la réussite leur ouvre les bras. J'ai compris que parfois, les adultes sont paumés. Parce que les plus grandes leçons c'est eux qui me les ont données. Je suis Énervé, dans mon quartier on s'ennuie loin de la ville. On écrit, on prie, on crie et j'ai des amis qui dealent. Mon grand frère est au chômage, mon pote se fait 5000 par mois. Au collège c'est le bordel, bientôt j'devrai faire un choix. Je suis Loin, ce qu'il se passe chez moi n'intéresse pas grand monde. Pour les autres on vit un rêve mais pourtant souvent on tourne en rond. Tout est cher, avec le continent y'a comme une latence. Je suis Enfermé, à l'étroit dans ma cellule. Tous les jours le même café mais c'est le temps qui est soluble. Ces bonnes actions que l'on regrette. Ces erreurs que l'on refait. Au parloir je parle autant à mon fils qu'à mon reflet. Je suis Gelé, j'enchaîne les verres et les hivers. Pour se rassurer les passants doivent tous penser que l'on hiberne. Bercé par le son des pas et le bruit des pièces dans les poches. Entre ce type et mon chien, je me demande de qui j'suis le plus proche. Je suis Riche, ils veulent me faire croire que c'est une honte, Comme si j'étais responsable de toute la misère du monde. Moi j'dois rien à personne, même si l'argent vient à manquer. Ils veulent tous goûter au fruit de l'arbre que j'ai planté. Je suis Malade, mais j'préfère dire futur soigné. Mes pupilles fixent l'aiguille de la montre qui brille sur mon poignet. A l'étroit dans mon corps, j'regarde le monde par le trou d'la serrure. Les gens diront que je n'ai fait qu'agrandir celui de la Sécu. Je suis Croyant, on me reproche souvent de l'être. On me reproche ma barbe pourtant j'ai la même que Jean Jaurès. On me compare à des barbares auxquels je n'ai jamais cru. Les mosquées sont trop petites alors parfois je prie dans la rue. Je suis Un peu perdu, mes p'tits poumons se remplissent d'air. Nouveau venu sur Terre, mes premières larmes déclenchent celles de mon père. Une chance, auprès de ma famille je m'sens à ma place. Mais je n'oublie pas que j'aurais pu naître dans la chambre d'en face. Je suis Seul, au fond d'un couloir, on demande pas mon avis. J'ai pris de l'âge donc voilà j'ai bien plus de rides que d'amis. J'aimerais partager mes erreurs, vous faire part de mes doutes. Parfois j'me parle à moi-même pour être sûr que quelqu'un m'écoute. Je suis Épuisé, mais plus pour longtemps j'en suis sûr. Les sonneries de téléphone, la pression ont élargi mes blessures. J'me souviens pas d'la date de mon dernier fou rire."
Nombre_de_caractères_à_afficher=1000  #Modifie ça stv
Taille=5                                #mais, ça pas touche pour l'instant

TMes=len(Message)
Dictionnaire = []

for i in range(0,TMes):
    n=0
    Recherche=True
    while n<len(Caractères) and Recherche:
        if Caractères[n]==Message[i]:
            Recherche=False
        n=n+1
    if Recherche:
        Caractères.append(Message[i])

#print(Caractères)

Liste = np.zeros([len(Caractères)]*(Taille+1))

for i in range(Taille,TMes):
    Liste[Caractères.index(Message[i-5]),Caractères.index(Message[i-4]),Caractères.index(Message[i-3]),Caractères.index(Message[i-2]),Caractères.index(Message[i-1]),Caractères.index(Message[i])]+=1

#TSor=int(input("Taille: "))
TSor=Nombre_de_caractères_à_afficher

Sortie="Je su"
for i in range(Taille,TSor):
    if i<Taille:
        Sortie=Sortie+Caractères[random.randint(0,len(Caractères)-1)]
    else:
        SortiesPossibles=[]
        for n in range(0,len(Caractères)):
            a=int(Liste[Caractères.index(Sortie[i-5]),Caractères.index(Sortie[i-4]),Caractères.index(Sortie[i-3]),Caractères.index(Sortie[i-2]),Caractères.index(Sortie[i-1]),n])
            for m in range(0,a):
                SortiesPossibles.append(Caractères[n])
        if len(SortiesPossibles)==0:
            Sortie=Sortie+Caractères[random.randint(0,len(Caractères)-1)]
        else:
            Sortie=Sortie+SortiesPossibles[random.randint(0,len(SortiesPossibles)-1)]

#print(i)
#print(SortiesPossibles)
print(Sortie)
