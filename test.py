from datetime import datetime, date
 
# --- Application de parking en langage python ---
now = datetime.now()



# La fonction d'affichage de l'application
def affichage_application():
	print(" --- Bienvenu sur notre application de parking --- ")
	print("1. Acheter le ticket")
	print("0. Quitter l'application")
	print(f"La date actuelle est : {now}")

	choix = eval(input(" - Saisissez 1 pour acheter le ticket : "))
	choix_menu(choix)




# La fonction pour le paiement du ticket et impression du ticket
def paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now):
	print(" --- Création du ticket --- ")
	id_ticket = f"{pseudo}{choix_abonne}{place_one}{now}"
	if type(numero_tel) == int:
		with open(f"tickets/ticket{now}.log", mode="w", encoding="utf-8") as ticket:
			ticket.write(f" --- Ticket de parking ---")
			ticket.write(f"\n")
			ticket.write(f"ID du ticket : {id_ticket}")
			ticket.write(f"\n")
			ticket.write(f"Pseudo : {pseudo}")
			ticket.write(f"\n")
			ticket.write(f"numero de téléphone : {numero_tel}")
			ticket.write(f"\n")
			ticket.write(f"Abonnement choisit : {choix_abonne_name} {choix_abonne}")
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
	print(" ----- Fonction pour le choix ----- ")

	# --- Pour la partie des abonnements ---
	if choix == 1 and type(choix) == int:
		print(" --- Bienvenu dans la partie de l'abonnement --- ")
		print("1. Abonnement classique")
		print("2. Abonnement standard")
		print("3. Abonnement premium")
		print("0. Sortir de l'application")
		choix_abonne = eval(input(" - Faites un choix de votre abonnement :"))

		# Appelle de la fonction pour le choix de l'abonnement
		choix_abonnement(choix_abonne)
	elif choix == 0 and type(choix) == int:
		print(" --- Vous avez quitté l'application --- ")
		exit()
	else:
		print("Erreur de choix : reéssayez")




# Fonction pour le choix de l'abonnement
def choix_abonnement(choix_abonne):
	print(" ----- Fonction pour le choix de l'abonnement ----- ")

	# Les conditions pour la partie des abonnements
	if choix_abonne == 1 and type(choix_abonne) == int:

		# Nommination de la partie classique
		choix_abonne_name = "Classique"

		# La partie classique pour le menu
		print(" --- Bienvenu dans le choix de l'abonnement classique --- ")
		print("Place 1 : 5000 FCFA / mois")
		print("Place 2 : 10.000 FCFA / mois")
		print("Place 3 : 15.000 FCFA / mois")
		print("Place 4 : 20.000 FCFA / mois")
		print("Place 5 : 25.000 FCFA / mois")
		print("Saisissez 0 pour sortir de l'application")
		place_one = eval(input(" - Entrez la place que vous souhaitez :"))

		# Appelle de la fonction choix de la place abonnement et de la partie du ticket
		choix_place_abonnement(place_one, choix_abonne, choix_abonne_name)

	elif choix_abonne == 2 and type(choix_abonne) == int:

		# Nommination de la partie standard
		choix_abonne_name = "Standard"

		# La partie standard pour le menu
		print(" --- Bienvenu dans le choix de l'abonnement standard --- ")
		print("Place 6 : 50.000 FCFA / mois")
		print("Place 7 : 55.000 FCFA / mois")
		print("Place 8 : 60.000 FCFA / mois")
		print("Saisissez 0 pour sortir de l'application")

		place_one = eval(input(" - Entrez la place que vous souhaitez :"))

		# Appelle de la fonction choix de la place abonnement et de la partie du ticket
		choix_place_abonnement(place_one, choix_abonne, choix_abonne_name)

	elif choix_abonne == 3 and type(choix_abonne) == int:

		# Nommination de la partie premium
		choix_abonne_name = "Premium"

		# La partie premium pour le menu
		print(" --- Bienvenu dans le choix de l'abonnement premium --- ")
		print(" Place 9 : 65.000 FCFA / mois")
		print(" Place 10 : 70.000 FCFA / mois")
		print("Saisissez 0 pour sortir de l'application")

		place_one = eval(input(" - Entrez la place que vous souhaitez :"))

		# Appelle de la fonction choix de la place abonnement et de la partie du ticket pour le Parking
		choix_place_abonnement(place_one, choix_abonne, choix_abonne_name)

	elif choix_abonne == 0 and type(choix_abonne) == int:
		print(" * Attention : vous êtes sorti de l'application * ")
		exit()

	else:
		print("Erreur de choix : reéssayez")





# La fonction pour le choix de la place et de l'abonnement
def choix_place_abonnement(place_one, choix_abonne, choix_abonne_name):
	print(" ----- Fonction pour le choix de la place ---- ")

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
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)


	elif place_one == 2 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 2 --- ")
		print(" * 10.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 10000

		# Ajout des informations du client
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Création du ticker et son impression
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 3 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 3 --- ")
		print(" * 15.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 15000

		# Ajout des informations du client
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Création du ticket et son impression
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 4 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 4 --- ")
		print(" * 20.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 20000

		# Ajout des information du client pour la création du ticket
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Création du ticket et de son impression physique pour le client
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 5 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 5 --- ")
		print(" * 25.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 25000

		# Ajout des informations supplémentaires au niveau du ticket
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Ajout de la partie pour la création et l'impression du ticket
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 6 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 6 --- ")
		print(" * 50.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 50000

		# Ajout des informations supplémentaires au niveau du ticket du parking
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Ajout de la partie pour la création et l'impression du ticket de parking
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 7 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 7 --- ")
		print(" * 55.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 55000

		# Ajout des informations supplémentaires au niveau du ticket du parking
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Ajout de la partie de la création du ticket pour le parking et pour l'impression du ticket
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 8 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 8 --- ")
		print(" * 60.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 60000

		# Ajout des informations du client pour le véhicule
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Appel de la partie de la création et de l'impression du ticket
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 9 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 9 --- ")
		print(" * 65.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 65000

		# Ajout des informations pour le client
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Appel de la partie de la création et de l'impression du ticket de parking
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 10 and type(choix_abonne) == int:
		print(" --- Vous avez choisi la place 10 --- ")
		print(" * 70.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 70000

		# Ajout des informations du client dans le ticket du parking
		pseudo = input("Entrez votre pseudo :")
		numero_tel = eval(input("Entrez votre numéro de téléphone :"))

		# Appel de la fonction pour l'impression du ticket pour le parking
		paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)

	elif place_one == 0 and type(choix_abonne) == int:
		print(" Attention : vous avez quitté l'application --- ")
		exit()

	else:
		print(" Erreur : veillez reéssayer")
		exit()



# Appel de la fonction
affichage_application()