# parking-app

Une application pour la gestion des tickets de façon automatique au niveau des parking des véhicules.

Dans cette application, vous avez la possibilité de faire l'achat d'un ticket pour votre véhicule (Moto, Voiture, Voiture Gros poids).

Pour cela, nous avons la possibilité de passer par le terminal pour faire l'achat de l'élément du ticket qui est une forme automatique.

`Une application en système embarqué : pour la distribution des tickets de façon automatiques`

--

Voici le sommaire de notre application :

## Sommaires :

## 1. Introduction *

## 2. Présentation de la structure de l'application

## 3. Présentation des avantages de l'application

## 4. Présentation des désavantages de l'application

## 5. Présention des fonctionalités théoriques de l'application

## 6. Présentation des fonctionalités de façon pratique de l'application

## 7. Présentation de la manière dont on exécute l'application

## 8. Conclusion

--

## 1. Introduction

Dans les différentes situations de la société des pays, nous rencontrons des difficultés qui nous poussent à dépenser beaucoup de capacité ou d'énergie, mentale ou physique. C'est pour cette raison qu'il y a des informaticiens qui arrivent à créer des automatisations dans le but de facilité les tâches et aider les urbanistes à continuer leur travail dans les mesures de la civilisation dans le monde et facilté l'accomplissement de certaines tâches en passant par l'automatisation.
C'est dans cette même perspective que nous avons créé une application pour faire l'automatisation de la distribution des tickets payants de façon automatique et unique à chaque personne sans passer par des éléments de distribution compliquée ou parfois par des distributions non sophistiqués. Je vous présente donc une application qui se nomme `Parking-App` qui est une qpplication en ingénierie système pour faire la distribution des tickets pour un parking de véhicule de façon automatique sans dépenser beaucoup d'énergie.

	- Comment cette application est structurée ? 
	- Comment est présentée cette application ?
    - Quelles sont les fonctionnalités de cette application ?
    - Comment appliquer l'utilisation de cette application ?


--

## 2. Présentation de la structure de l'application

Cette application a été créé à partir des langages de programmation qu'on appelle en informatique `langage python` et `langage bash`, ce sont ces deux langages qui ont permis de créer les différentes fonctionnalités de l'application et ensuite l'exécution sur les terminaux des appareils électroniques pour la distribution des tickets. De ce fait, nous avons la partie des fonctionnalités de l'application qui ont été créé précisement à partir du langage python dans un fichier `main.py`, nous avons ensuite le fichier de duplicité pour les fonctionalités de l'application afin de conserver la disponibilité du script qui se nomme `main_duplicite.py`, nous avons le fichier `setup.sh` pour exécuter l'application dans les terminaux normalement et le fichier `setup.sh` est structuré en langage bash, nous avons également le fichier `test.py` pour faire les testes de l'application dans sa globalité afin de vérifier les erreurs, les héradiquer ou bien les éviter par prévision, nous avons également le fichier `workflow.md` qui est un fichier qui avait servis de créer les différentes étapes pour le fonctionnement de l'application. 


-- 

## 3. Présentation des avantages de l'application

C'est une application qui possède plusieurs avantages notement dans les fonctionnalités de création des tickets automatiquement sans perdre de temps ou bien d'énergie inutile. De ce fait, nous avons les avantages tels que :

 - La présence d'un script tout entier pour une automatisation
 - La création d'un ticket automatique directement dans l'application
 - La création des tickets uniques, suivant la date, le pseudo du client et de la place qu'il a choisie, ce qui représente généralement le numéro du ticket du client
 - La possibilité d'ajouter l'application sur un élément éléctronique avec un processeur ESP 232 ou un microcontrolleur Arduino ou Raspberry afin de faire la création et l'impression des tickets
 - La facilitation à l'accès de l'unicité d'un ticket pour un parking
 - L'innovation de l'application qui est unique, c'est à dire qu'elle offre la possibilité de faire quelque chose d'unique dans son genre

  -- 

 ## 4. Présentation des désavantages de l'application

 C'est une application qui possède des désavantages tout comme toutes les autres applications. Pour cela, nous pouvons les cités tels que :

  - L'application est complexe pour son développement, sa maintenance et son déploiement
  - L'application n'est pas directement intégrée à un outil électronique pour la distribution des tickets mais peut être déployé
  - L'application n'est pas réservée à toutes les personnes débutantes mais avec une petite adaptation et un temps d'apprentissage, ces personnes peuvent faire des achats ou vente de ticket de façon automatque
  - L'application ne possède pas d'interface graphique mais plutôt un terminal tout comme les éléments électroniques du système embarqué
  - L'application possède un pourcentage de précision seulement environ 87 % - 97 % sans erreur car les erreurs, les attentions et d'ailleurs les exceptions sont suivies des explications

--

## 5. Présention des fonctionalités théoriques de l'application

Cette application possède des fonctionnalités qui sont très utilisées dans la vie réelle. Nous pouvons reléver que quelques une qui sont importantes :

- Accès à un terminal pour faire l'achat d'un ticket pour un parking de véhicule
- Interaction avec l'application de façon conviviale et respectueuse des normes de l'application pour faire l'achat du ticket pour le parking
- Gestion des erreurs suivant les normes du développement `MIT` qui soutient le fait de gerer les erreurs au moins à conserver une communication `Universelle`.
- Gestion de l'achat des tickets dans un échelonnement de la classe du véhicule et de la classe sociale du client.

--

## 6. Présentation des fonctionalités de façon pratique de l'application

Dans cette application, on peut facilement remarquer les différentes parties de lancement de l'application. Vous aurez le droit de rentrer dans le dossier principal, si vous êtes sur le système `Linux`, tapez seulement cette commande : `cd parking-app`

Vous allez remarquer un fichier `Bash` qu'on appelle `setup.sh`, après cette remarque, il faut saisir ces deux commandes si l'une ne fonctionne pas, il faut saisir l'autre.

Assurez vous d'avoir le setup du langage `Bash` installé sur votre système.

### Les commandes de lancement :

- Première commande : `./setup.sh`
Cette commande permet de lancer le setup global de l'application.
Dans la mesure du possible également, assurez vous que vous avez une bonne version de lanceur python, une version `python 3.11`, avec cette version, vous aurez la possibilité de lancer l'application en toute règle.
Si cette commande ne fonctionne pas, utiliser cette commande.

- Deuxième commande : `bash setup.sh`
Cette commande permet d'utiliser le lanceur bash pour exécuter le `setup.sh` en utilisant directement le lanceur bash pour que cela puisse fonctionner en un coup sûr. Dans un cas extrême, dans un élément électronique pour l'impression des tickets qui sont en log. De ce fait, je vous recommande d'avoir de base l'élément `bash` installé ou à jour ensuite l'élément `python` installé ou à jour.

Dans un cas extrême si les deux commandes ne fonctionnent pas, il faut utiliser cette commande.

- Troisième commande : `python3 main.py`
Cette commande permet de lancer le main de l'application que j'ai eu à créer. Cette commande permet de lancer le main.py qui est le noyau de l'application. De ce fait, je vous recommande d'avoir au préalable le setup du langage python à jour, sous cette version `python 3.9` ou `python 3.11`.

Après avoir ouvert le setup de l'application, on aura la possibilité de voir un menu bien structuré.

### La structure de l'application et ses fonctions

Nous avons les différentes structurées sous cette forme :

-----------------------------------
::: Parking de véhicule :::
-----------------------------------


 --- Bienvenu sur notre application de parking --- 
1. Acheter le ticket
2. Compte Administration
0. Quitter l'application
La date actuelle est : 2026-10-01 09:19:48.469958
 - Saisissez un chiffre ( 0 à 2 ) :


- Nous avons le menu, au niveau du menu, nous avons l'achat de ticket sous cette forme : `1. Acheter le ticket`

- La partie du compte administrateur sous cette forme : `2. Compte Administration` 

- La partie pour quitter l'application complètement sous cette forme : `0. Quitter l'application`

- La partie de la date du jour sous cette forme : `La date actuelle est : 2026-10-01 09:19:48.469958`

Comme vous allez le remarquer le terminal ou bien l'élément électronique va donner la main pour écrire un chiffre pour faire un choix.

Exemple : `1` pour passer à l'achat du ticket pour le parking.
Ou `2` pour passer à la partie des comptes administrateurs.

Au niveau de l'achat du ticket, vous avez les éléments d'un autre menu sous cette forme :


----- Choix des abonnements ----- 
1. Abonnement classique
2. Abonnement standard
3. Abonnement premium
0. Sortir de l'application
Faites un choix de votre abonnement :

Vous allez choisir un numéro pour acheter un abonnement au ticket.

Si vous choisissez `1. Abonnement classique`, vous aurez cette structure sous cette forme.

 ----- Le choix de votre place ----- 
 --- Bienvenu dans le choix de l'abonnement classique --- 
Place 1 : 5000 FCFA / mois
Place 2 : 10.000 FCFA / mois
Place 3 : 15.000 FCFA / mois
Place 4 : 20.000 FCFA / mois
Place 5 : 25.000 FCFA / mois
Saisissez 99 pour sortir de l'application
Entrez la place que vous souhaitez : 

Vous allez choisir la place `1` par exemple pour faire l'achat du ticket.

Vous aurez problamenent un ticket sous cette forme.

--------------------------------------------
:::         Parking de véhicule
--------------------------------------------
N° du ticket : JEROME112026-09-24 13:43:55.571407
Pseudo : JEROME
Numéro de téléphone : 72336147
Abonnement choisi : Classique 1
Place choisit : Place 1
Le prix du ticket : 5000 FCFA
Paiement au niveau du Guichet
La date actuelle : 2026-09-24 13:43:55.571407
--------------------------------------------

Après avois enregistré vos informations pour l'achat du ticket, les informations que vous souhaitez que ça soit visible.

`[Innachevé]` -> `[Faire un git commit à la fin des modification et faire un push à la fin]`




