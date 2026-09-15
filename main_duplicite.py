from datetime import datetime, date
 
# --- Application de parking en langage python ---
now = datetime.now()

# La fonction d'affichage
def affichage_application():
	print(" --- Bienvenu sur notre application de parking --- ")
	print("1. Faire un abonnement de parking")
	print("2. Renouveller son abonnement")
	print("3. Annuller son abonnement")
	print("4. Retirer un ticket pour le parking")
	print("5. Marquer l'entrer du véhicule")
	print("6. Marquer la sortie du parking")
	print("0. Quitter l'application")
	print(f"La date actuelle est : {now}")

	choix = eval(input(" - Faites votre choix de numéro : "))
	return choix

# La fonction pour le paiement du ticket et impression du ticket
def paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now):
	print(" --- Création du ticket --- ")
	if type(numero_tel) == int:
		with open(f"tickets/ticket{now}.log", mode="w", encoding="utf-8") as ticket:
			ticket.write(f" --- Ticket de l'abonnement {choix_abonne} de la place {place_one} ---")
			ticket.write(f"\n")
			ticket.write(f"Pseudo : {pseudo}")
			ticket.write(f"\n")
			ticket.write(f"numero de téléphone : {numero_tel}")
			ticket.write(f"\n")
			ticket.write(f"Abonnement choisit : {choix_abonne}")
			ticket.write(f"\n")
			ticket.write(f"Place choisit : {place_one}")
			ticket.write(f"\n")
			ticket.write(f"Le prix est : {prix} FCFA")
			ticket.write(f"\n")
			ticket.write(f"Paiement au niveau du Guichet")
			ticket.write(F"\n")
			ticket.write(f"La date actuelle : {now}")
			ticket.write(f"\n")
			ticket.write(f" --- Fin --- ")
		print(" * Votre ticket a été créé avec succès * ")
	else:
		print(" -- Erreur, votre numéro de téléphone n'est pas correct --")
		print(" Reéssayez à nouveau")

# Fonction pour le choix sur le menu
def choix_menu(choix):
	print("Fonction pour le choix")
	# --- Pour la partie des abonnements ---
if choix == 1 and type(choix) == int:
	print(" --- Bienvenu dans la partie de l'abonnement --- ")
	print("1. Abonnement classique")
	print("2. Abonnement standard")
	print("3. Abonnement premium")
	print("0. Sortir de l'application")

	choix_abonne = eval(input(" - Faites un choix de votre abonnement :"))

	# Les conditions pour la partie des abonnements
	if choix_abonne == 1 and type(choix_abonne) == int:
		print(" --- Bienvenu dans le choix de l'abonnement classique --- ")
		print("Place 1 : 5000 FCFA / mois")
		print("Place 2 : 10.000 FCFA / mois")
		print("Place 3 : 15.000 FCFA / mois")
		print("Place 4 : 20.000 FCFA / mois")
		print("Place 5 : 25.000 FCFA / mois")
		print("Saisissez 0 pour sortir de l'application")
		place_one = eval(input(" - Entrez la place que vous souhaitez :"))

		#pseudo = eval(input(" - Entrez votre pseudo :"))
		if place_one == 1 and type(place_one) == int:
			print(" --- Vous avez choisi la place 1 --- ")
			prix = 5000

			# Action du guichet ( Utilisation du langage Bash )
			print(" --- Paiement sur le guichet --- ")
			print(" * 5000 FCFA / mois * ")

			# Informations à ajouter
			pseudo = input(" - Entrez votre pseudo :")
			numero_tel = eval(input(" - Entrez votre numéro de téléphone :"))

			# Création du ticket et de son impression
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 2 and type(choix_abonne) == int:
			print(" --- Vous avez choisi la place 2 --- ")
			print(" * 10.000 FCFA / mois * ")
			print("Paiement au niveau du guichet")
			prix = 10000

			# Ajout des informations du client
			pseudo = input("Entrez votre pseudo :")
			numero_tel = eval(input("Entrez votre numéro de téléphone :"))

			# Création du ticker et son impression
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 3 and type(choix_abonne) == int:
			print(" --- Vous avez choisi la place 3 --- ")
			print(" * 15.000 FCFA / mois * ")
			print("Paiement au niveau du guichet")
			prix = 15000

			# Ajout des informations du client
			pseudo = input("Entrez votre pseudo :")
			numero_tel = eval(input("Entrez votre numéro de téléphone :"))

			# Création du ticket et son impression
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 4 and type(choix_abonne) == int:
			print(" --- Vous avez choisi la place 4 --- ")
			print(" * 20.000 FCFA / mois * ")
			print("Paiement au niveau du guichet")
			prix = 20000

			# Ajout des information du client pour la création du ticket
			pseudo = input("Entrez votre pseudo :")
			numero_tel = eval(input("Entrez votre numéro de téléphone :"))

			# Création du ticket et de son impression physique pour le client
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 5 and type(choix_abonne) == int:
			print(" --- Vous avez choisi la place 5 --- ")
			print(" * 25.000 FCFA / mois * ")
			print("Paiement au niveau du guichet")
			prix = 25000

			# Ajout des informations supplémentaires au niveau du ticket
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 0 and type(choix_abonne) == int:
			print(" --- Vous avez quitté l'application --- ")
			exit()

		else:
			print(" Erreur : veillez reéssayer")
	else:
		print("Erreur de choix : reéssayez")
else:
	print("Erreur de choix : reéssayez")




# Fonction pour le choix de l'abonnement
def choix_abonnement(choix_abonne):
	print("Fonction pour le choix de l'abonnement")

def choix_place_abonnement(place_one):
	print("Fonction pour le choix de la place")

# Création des différentes parties de condition pour le choix

# Appel de la fonction
choix = affichage_application()


# --- Pour la partie des abonnements ---
if choix == 1 and type(choix) == int:
	print(" --- Bienvenu dans la partie de l'abonnement --- ")
	print("1. Abonnement classique")
	print("2. Abonnement standard")
	print("3. Abonnement premium")
	print("0. Sortir de l'application")

	choix_abonne = eval(input(" - Faites un choix de votre abonnement :"))

	# Les conditions pour la partie des abonnements
	if choix_abonne == 1 and type(choix_abonne) == int:
		print(" --- Bienvenu dans le choix de l'abonnement classique --- ")
		print("Place 1 : 5000 FCFA / mois")
		print("Place 2 : 10.000 FCFA / mois")
		print("Place 3 : 15.000 FCFA / mois")
		print("Place 4 : 20.000 FCFA / mois")
		print("Place 5 : 25.000 FCFA / mois")
		print("Saisissez 0 pour sortir de l'application")
		place_one = eval(input(" - Entrez la place que vous souhaitez :"))

		#pseudo = eval(input(" - Entrez votre pseudo :"))
		if place_one == 1 and type(place_one) == int:
			print(" --- Vous avez choisi la place 1 --- ")
			prix = 5000

			# Action du guichet ( Utilisation du langage Bash )
			print(" --- Paiement sur le guichet --- ")
			print(" * 5000 FCFA / mois * ")

			# Informations à ajouter
			pseudo = input(" - Entrez votre pseudo :")
			numero_tel = eval(input(" - Entrez votre numéro de téléphone :"))

			# Création du ticket et de son impression
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 2 and type(choix_abonne) == int:
			print(" --- Vous avez choisi la place 2 --- ")
			print(" * 10.000 FCFA / mois * ")
			print("Paiement au niveau du guichet")
			prix = 10000

			# Ajout des informations du client
			pseudo = input("Entrez votre pseudo :")
			numero_tel = eval(input("Entrez votre numéro de téléphone :"))

			# Création du ticker et son impression
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 3 and type(choix_abonne) == int:
			print(" --- Vous avez choisi la place 3 --- ")
			print(" * 15.000 FCFA / mois * ")
			print("Paiement au niveau du guichet")
			prix = 15000

			# Ajout des informations du client
			pseudo = input("Entrez votre pseudo :")
			numero_tel = eval(input("Entrez votre numéro de téléphone :"))

			# Création du ticket et son impression
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 4 and type(choix_abonne) == int:
			print(" --- Vous avez choisi la place 4 --- ")
			print(" * 20.000 FCFA / mois * ")
			print("Paiement au niveau du guichet")
			prix = 20000

			# Ajout des information du client pour la création du ticket
			pseudo = input("Entrez votre pseudo :")
			numero_tel = eval(input("Entrez votre numéro de téléphone :"))

			# Création du ticket et de son impression physique pour le client
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 5 and type(choix_abonne) == int:
			print(" --- Vous avez choisi la place 5 --- ")
			print(" * 25.000 FCFA / mois * ")
			print("Paiement au niveau du guichet")
			prix = 25000

			# Ajout des informations supplémentaires au niveau du ticket
			paiement_impression_ticket(numero_tel, choix_abonne, prix, place_one, pseudo, now)

		elif place_one == 0 and type(choix_abonne) == int:
			print(" --- Vous avez quitté l'application --- ")
			exit()

		else:
			print(" Erreur : veillez reéssayer")
	else:
		print("Erreur de choix : reéssayez")
else:
	print("Erreur de choix : reéssayez")

	


	
	

