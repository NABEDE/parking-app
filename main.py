from datetime import datetime, date
import subprocess
 
# --- Application de parking en langage python ---
now = datetime.now()


# La partie de suppresion des tickets
def deleting_tickets():
	commande = ["sudo rm -r -f", "/tickets/ticket*"]
	result = subprocess.run(commande, capture_output=True)
	print(result.stdout.decode("utf-8"))


# La liste des admins de base
info_admin_actuel = []

# Partie des administrateurs
def connexion_administrateur(pseudo, code_connexion):
	liste_compte_ligne = []

	# Vérification des informations de l'administrateur
	with open(f"compte-admin/compte_admins.log", mode="r", encoding="utf-8") as info_admin:
		for ligne in info_admin:
			liste_compte_ligne.append(ligne.strip())

	if (pseudo in list(liste_compte_ligne)) == True: 
		if (code_connexion in list(liste_compte_ligne)) == True:
			print("\n")
			print(5*"-")
			print(" * Vous êtes connecté à votre compte Admin * ")
			print(f"Votre pseudo est (4 éléments) : {pseudo}")
			print(f"Votre code de connexion est (4 éléments) : {code_connexion}")
			print(5*"-"+"\n")

			# La liste des admins de base
			global info_admin_actuel
			info_admin_actuel = [pseudo, code_connexion]
			#print(f"Administrateur actuel : {info_admin_actuel}")

			# Ajouter les actions à faire
			affichage_admin_action()

		else:
			print(f"Erreur : votre code de connexion {code_connexion} ne correspond à aucun code")
	else:
		print(f"Erreur : Votre pseudo {pseudo} ne correspond à aucun pseudo")



# Parties des administrateurs
# Les conditions de la partie administrateur
def condition_choix_administrateur(choix_administrateur):
	if choix_administrateur == "1":
		print(" --- Création d'un compte de l'administrateur --- ")
		
		# Entrez des informations pour l'administrateur		
		pseudo = input("Entrez votre pseudo : ")
		code_connexion = input("Entrez votre code de connexion : ")

		# Condition de la partie du code_connexion
		code_connexion_list = list(code_connexion)
		if len(code_connexion_list) != 4:
			print("Erreur : votre code de connexion ne doit pas dépasser 4 facteurs")
			print("Exemple de ce qui est correct : 0000 ou JKL8")
			print("Reéssayez")
			exit()
		print("\n")
		print(f" -- Confirmation de vos identifiants de connexion -- ")
		print(f"Votre pseudo : {pseudo}")
		print(f"Votre code de connexion : {code_connexion}")
		print(f" --")
		print("\n")

		confirmation_information_client = input("Est ce que vos informations sont correctes ? (Oui ou Non) :")

		if confirmation_information_client.lower() == "oui":
			print("Vous avez confirmé que vos informations sont correctes!")

			# Ajout des informations de l'administrateur dans un fichier
			enregistrement_informations_admin(pseudo, code_connexion)

		elif confirmation_information_client.lower() == "non":
			print("Attention : vos informations ne sont pas correct, réessayez!")
			exit()

	elif choix_administrateur == "2":
		print(" --- Connexion à votre compte en tant que administrateurs --- ")
		pseudo = input("Entrez votre pseudo : ")
		code_connexion = input("Entrez votre code de connexion : ")
		connexion_administrateur(pseudo, code_connexion)

	elif choix_administrateur == "3":
		print(" --- Suppression des anciens tickets --- ")
		reponse = input("Est ce que c'est le système Linux ? : ")

		if reponse.lower() == "oui":
			commande_suppression_ticket()
		elif reponse.lower() == "non":
			print("Attention : vous n'utilisez pas un système Linux")
		else:
			print("Erreur : reéssayez")

		commande = ["sudo rm -r -f"]


	elif choix_administrateur == "99":
		print("Attention : vous avez quitté l'applicarion")
		exit()

	# Partie innachevée


# Partie Administrateur



# La liste des administrateurs disponibles dans la partie des données
def list_admins_base():
	list_admin_dispo_base = []
	with open(f"compte-admin/compte_admins.log", mode="r", encoding="utf-8") as admin_dispo_base:
		for admin_element_base in admin_dispo_base:
			list_admin_dispo_base.append(admin_element_base.strip())
	#print(f"La liste des administrateurs actuellement{list_admin_dispo_base}")
	return list_admin_dispo_base

# Extraction des éléments
list_admins_elements_dispo = list_admins_base()


# La fonction d'affichage de l'application
def affichage_application():
	print("\n")
	print(35*"-")
	print(3*":"+"\t"+"Parking de véhicule"+"\t"+3*":")
	print(35*"-")
	print("\n")
	print(" --- Bienvenu sur notre application de parking --- ")
	print("1. Acheter le ticket")
	print("2. Compte Administration")
	print("0. Quitter l'application")
	print(f"La date actuelle est : {now}")
	#print(list_admins_elements_dispo)

	choix = input(" - Saisissez un chiffre ( 0 à 2 ) : ")
	choix_menu(choix)




# La fonction pour le paiement du ticket et impression du ticket
def paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now):
	print(" --- Création du ticket --- ")

	print("\n")
	print(" * Vérifiez les informations * ")
	print("\n")
	print(f"Votre pseudo est : {pseudo}")
	print(f"Votre numéro de téléphone est : {numero_tel}")
	print(f"L'abonnement que vous avez choisi est : {choix_abonne_name} {choix_abonne}")
	print(f"La place que vous avez choisi est : place {place_one}")
	print(f"Le prix que vous avez payé : {prix} FCFA")
	print("\n")

	verif_information = input("Est ce que vos informations sont correctes (Oui ou Non) : ")

	if verif_information.lower() == "oui":	
		num_ticket = f"{pseudo}{choix_abonne}{place_one}{now}"
		if type(numero_tel) == int:
			with open(f"tickets/ticket-vente1.log", mode="w", encoding="utf-8") as ticket:
				ticket.write(f"\n")
				ticket.write(44*"-"+"\n")
				ticket.write(3*":"+3*"\t"+"Parking de véhicule"+"\n")
				ticket.write(44*"-")
				ticket.write(f"\n")
				ticket.write(f"N° du ticket : {num_ticket}")
				ticket.write(f"\n")
				ticket.write(f"Pseudo : {pseudo}")
				ticket.write(f"\n")
				ticket.write(f"Numéro de téléphone : {numero_tel}")
				ticket.write(f"\n")
				ticket.write(f"Abonnement choisi : {choix_abonne_name} {choix_abonne}")
				ticket.write(f"\n")
				ticket.write(f"Place choisit : Place {place_one}")
				ticket.write(f"\n")
				ticket.write(f"Le prix du ticket : {prix} FCFA")
				ticket.write(f"\n")
				ticket.write(f"Paiement au niveau du Guichet")
				ticket.write(F"\n")
				ticket.write(f"La date actuelle : {now}")
				ticket.write(f"\n")
				ticket.write(44*"-")

				print(" * Votre ticket a été créé avec succès * ")
				print("\n")
				with open(f"tickets/ticket-vente1.log", mode="r", encoding="utf-8") as ticket_file:
					for line in ticket_file:
						print(line.strip())
						print("\n")
		else:
			print(" Erreur : votre numéro de téléphone n'est pas correct")
			print(" Attention : Reéssayez à nouveau")

	elif verif_information.lower() == "non":
		print("Attention : vos informations ne correspondent pas, réessayez")
		exit()

	else:
		print("Erreur : repondez seulement par 'Oui ou Non' simplement, réessayez")
		exit()



# Enregistrement du ticket
def enregistrement_ticket(place_one): # Teste de cette fonction :
	with open(f"tickets/places/places_reserves.log", mode="a", encoding="utf-8") as save_places:
		save_places.write("\n")
		save_places.write(str(place_one))
		save_places.write("\n")
	print("Succès : La place du ticket a été enregistré avec succès")
	print("\n")




# Vérification de la présence du ticket
def verification_tickets(place_one, choix_abonne, choix_abonne_name): # Teste de cette fonction :
	tickets_place = []
	with open(f"tickets/places/places_reserves.log", mode="r", encoding="utf-8") as ticket_place:
		for line in ticket_place:
			#print(line.strip())
			tickets_place.append(line.strip())
		if str(place_one) in tickets_place:
			print("Attention : Cette place est déjà occupé, changez une nouvelle place - ")
			exit()
		else:
			print("Attention : Cette place est libre")

			# Appelle de la fonction choix de la place abonnement et de la partie du ticket
			choix_place_abonnement(place_one, choix_abonne, choix_abonne_name)

			# Enregistré le ticket dans le fichier log
			enregistrement_ticket(place_one)



# Fonction pour le choix sur le menu
def choix_menu(choix): # Teste de cette fonction : 
	print(" ----- Choix des abonnements ----- ")

	# --- Pour la partie des abonnements ---
	if choix == '1':
		print("1. Abonnement classique")
		print("2. Abonnement standard")
		print("3. Abonnement premium")
		print("0. Sortir de l'application")
		choix_abonne = input("Faites un choix de votre abonnement : ")

		# Appelle de la fonction pour le choix de l'abonnement
		choix_abonnement(choix_abonne)

	# --- Pour la partie des administrateurs ---
	elif choix == "2":
		partie_administrateurs(choix)

	elif choix == '0':
		print(" Attention : vous avez quitté l'application")
		exit()
	else:
		print("Erreur : reéssayez")
		exit()



# Partie des administrateurs
# Fonction pour le choix de l'abonnement
def choix_abonnement(choix_abonne):
	print(" ----- Le choix de votre place ----- ")

	# Les conditions pour la partie des abonnements
	if choix_abonne == '1':

		# Nommination de la partie classique
		choix_abonne_name = "Classique"

		# La partie classique pour le menu
		print(" --- Bienvenu dans le choix de l'abonnement classique --- ")
		print("Place 1 : 5000 FCFA / mois")
		print("Place 2 : 10.000 FCFA / mois")
		print("Place 3 : 15.000 FCFA / mois")
		print("Place 4 : 20.000 FCFA / mois")
		print("Place 5 : 25.000 FCFA / mois")
		print("Saisissez 99 pour sortir de l'application")
		place_one = input("Entrez la place que vous souhaitez : ")

		# Vérification des éléments et lancement de la création du ticket
		verification_tickets(place_one, choix_abonne, choix_abonne_name)


	elif choix_abonne == '2':

		# Nommination de la partie standard
		choix_abonne_name = "Standard"

		# La partie standard pour le menu
		print(" --- Bienvenu dans le choix de l'abonnement standard --- ")
		print("Place 6 : 50.000 FCFA / mois")
		print("Place 7 : 55.000 FCFA / mois")
		print("Place 8 : 60.000 FCFA / mois")
		print("Saisissez 99 pour sortir de l'application")

		place_one = input("Entrez la place que vous souhaitez : ")

		# Vérification des éléments et lancement de la création du ticket
		verification_tickets(place_one, choix_abonne, choix_abonne_name)

	elif choix_abonne == '3':

		# Nommination de la partie premium
		choix_abonne_name = "Premium"

		# La partie premium pour le menu
		print(" --- Bienvenu dans le choix de l'abonnement premium --- ")
		print(" Place 9 : 65.000 FCFA / mois")
		print(" Place 10 : 70.000 FCFA / mois")
		print("Saisissez 99 pour sortir de l'application")

		place_one = input("Entrez la place que vous souhaitez : ")

		# Vérification des éléments et lancement de la création du ticket
		verification_tickets(place_one, choix_abonne, choix_abonne_name)

	elif choix_abonne == '0':
		print(" * Attention : vous êtes sorti de l'application * ")
		exit()

	else:
		print("Erreur : reéssayez")



# Partie des administrateurs
# La fonction pour la partie des administrateurs
def partie_administrateurs(choix_partie_administrateur):
	liste_admins = []
	# Création d'un administrateur par defaut au niveau de la partie administration
	with open(f"compte-admin/compte_admins.log", mode="r", encoding="utf-8") as reading_admins:
		for reading_admin in reading_admins:
			element_reading_admin = reading_admin.strip()
			liste_admins.append(element_reading_admin)


	if ('KLIO*' in liste_admins) == False:
		with open(f"compte-admin/compte_admins.log", mode="a", encoding="utf-8") as ajout_admin:
			ajout_admin.write("KLIO*\n")
			ajout_admin.write("KLIO\n")
			ajout_admin.write(5*"-")
			print("***")


	print(" --- Bienvenu dans la partie des administrateurs --- ")
	print("1. Créer un compte administrateur")
	print("2. Se connecter")
	print("99. Quitter l'application")

	choix_administrateur = input("Entrez le numéro de votre choix : ")
	condition_choix_administrateur(choix_administrateur)

	# Partie innachevée



# Ajouter les informations de l'administrateurs pour son compte
def ajout_information_administrateur():
	print(" --- Ajouter les informations --- ")

	# Entrez des informations pour l'administrateur		
	pseudo = input("Entrez votre pseudo (4 éléments) : ")
	code_connexion = input("Entrez votre code de connexion (4 éléments) : ")


	# Condition de la partie du code_connexion
	code_connexion_list = list(code_connexion)
	if len(code_connexion_list) != 4:
		print("Erreur : votre code de connexion ne doit pas dépasser 4 facteurs")
		print("Exemple de ce qui est correct : 0000 ou JKL8")
		print("Reéssayez")
		exit()
	print("\n")
	print(f" -- Confirmation de vos identifiants de connexion -- ")
	print(f"Votre pseudo : {pseudo}")
	print(f"Votre code de connexion : {code_connexion}")
	print(f" --")
	print("\n")

	confirmation_information_client = input("Est ce que vos informations sont correctes ? (Oui ou Non) :")

	if confirmation_information_client.lower() == "oui":
		print("Vous avez confirmé que vos informations sont correctes!")

		# Ajout des informations de l'administrateur dans un fichier
		enregistrement_informations_admin(pseudo, code_connexion)

	elif confirmation_information_client.lower() == "non":
		print("Attention : vos informations ne sont pas correct, réessayez!")
		exit()





# Suppression d'un compte d'un administrateur
def deleting_admin_account():

	# Affichage des informations de l'administrateur en cours d'utilisation
	#print(f"l'administrateur actuel : {info_admin_actuel}")

	list_file_log_admin = []
	pseudo_admin_supp = input("Entrez le pseudo de l'administrateur à supprimer : ")
	code_connexion_supp = input("Entrez le code de connexion de l'administrateur à supprimer : ")

	with open(f"compte-admin/compte_admins.log", mode="r", encoding="utf-8") as admin_supp:
		for ligne_element in admin_supp:
			admin_supp_content = ligne_element.strip()
			list_file_log_admin.append(admin_supp_content)

	if (str(pseudo_admin_supp) in info_admin_actuel) == False:
		if(str(code_connexion_supp) in info_admin_actuel) == False:
			if len(list_file_log_admin) != 0:

				# Condition de vérification des informations de l'administrateur
				if (str(pseudo_admin_supp) in list(list_file_log_admin)) == True:
					if (str(code_connexion_supp) in list(list_file_log_admin)) == True:
						with open(f"compte-admin/compte_admins.log", mode="w", encoding="utf-8") as nouveau_log_admin:
							if (str(pseudo_admin_supp) in list_file_log_admin) == True:
								print(f"Le pseudo à supprimer : {pseudo_admin_supp}")
								list_file_log_admin.remove(pseudo_admin_supp)
								if (str(code_connexion_supp) in list_file_log_admin) == True:
									print(f"Le code à supprimer : {code_connexion_supp}")
									list_file_log_admin.remove(code_connexion_supp)

									if (5*"-" in list_file_log_admin) == True:
										list_file_log_admin.remove(5*"-")

									# Remplissage des informations de l'administrateur dans le fichier des administrateurs	
									for element in list_file_log_admin:
										if element != '':
											nouveau_log_admin.write(element)
											nouveau_log_admin.write("\n")
									print("Succès : le compte de l'administrateur a été supprimé avec succès.")

								else:
									print("Erreur : aucun administrateur avec ce code de connexion")
									print("Réessayez !")

							else:
								print("Erreur : aucun administrateur avec ce pseudo")
								print("Réessayez !")

					else:
						print("Erreur : aucun administrateur avec ce code de connexion")

				else:
					print("Erreur : aucun administrateur avec ce pseudo de connexion")
			else:
				print("Erreur : le fichier des admins n'existe pas")
		else:
			print("Erreur : le code de connexion est le vôtre")
	else:
		print("Erreur : le pseudo de connexion est le vôtre")






# Création de la fonction pour la partie admin
def execution_choix_admin(choix_admin):

	if choix_admin == "1":
		print(" --- Ajout d'un administrateur --- ")
		# Ajout des informations
		ajout_information_administrateur()

	elif choix_admin == "2":
		print(" --- Suppression du compte d'un administrateur --- ")
		# Suppression du compte d'un administrateur
		deleting_admin_account()

	elif choix_admin == "99":
		print("Attention : attention vous avez quitté l'application!")
		exit()



# Les actions des admins
def affichage_admin_action():
	print("1. Ajouter un administrateur")
	print("2. Supprimer un administrateur")
	print("99.Se déconnecter en tant qu'admin")

	choix_admin = input("Choisissez un numéro qui vous convient : ")
	execution_choix_admin(choix_admin)



	# [ Partie innachevée dans le top ]



# La fonction pour la création des comptes des administrateurs
def enregistrement_informations_admin(pseudo, code_connexion):

	liste_compte_ligne = []
	print(" --- Enregistrement des informations de l'administrateur --- ")

	# Changement des éléments de type pour les informations des administrateurs


	# Vérification des informations de l'administrateur
	with open(f"compte-admin/compte_admins.log", mode="r", encoding="utf-8") as info_admin:
		for ligne in info_admin:
			liste_compte_ligne.append(ligne.strip())


	# Ajout de la partie des informations des administrateur dans la partie des logs
	for element in liste_compte_ligne:
		if str(element) == str(pseudo):
			print("Erreur : il existe un compte qui est déjà au même pseudo")
			if str(element) == str(code_connexion):
				print("Erreur : il existe un compte qui est déjà au même code de connexion")
				exit()
			exit()

	# Enregistrement du compte de l'administrateur
	with open(f"compte-admin/compte_admins.log", mode="a", encoding="utf-8") as info_compte:
		#info_compte.write(5*"-")
		info_compte.write("\n")
		info_compte.write(f"{pseudo}\n")
		info_compte.write(f"{code_connexion}\n")
		info_compte.write(5*"-")
		info_compte.write("\n")
	print(" --- Votre compte a été créé avec succès --- ")

	# Partie innachevée 1




# La fonction pour le choix de la place et de l'abonnement
def choix_place_abonnement(place_one, choix_abonne, choix_abonne_name): # Teste de cette fonction :
	print(" ----- Fonction pour le choix de la place ---- ")

	#pseudo = eval(input(" - Entrez votre pseudo :"))
	if place_one == '1':
		print(" --- Vous avez choisi la place 1 --- ")
		prix = 5000

		# Action du guichet ( Utilisation du langage Bash )
		print(" --- Paiement sur le guichet --- ")
		print(" * 5000 FCFA / mois * ")

		# Informations à ajouter
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = input("Entrez votre numéro de téléphone : ")

		# Condition d'acceptation du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")



	elif place_one == '2':
		print(" --- Vous avez choisi la place 2 --- ")
		print(" * 10.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 10000

		# Ajout des informations du client
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = input("Entrez votre numéro de téléphone : ")

		# Partie de condition pour l'acception du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '3':
		print(" --- Vous avez choisi la place 3 --- ")
		print(" * 15.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 15000

		# Ajout des informations du client
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = input("Entrez votre numéro de téléphone : ")

		# Partie de la condition de l'acception du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '4':
		print(" --- Vous avez choisi la place 4 --- ")
		print(" * 20.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 20000

		# Ajout des information du client pour la création du ticket
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = input("Entrez votre numéro de téléphone : ")

		# Partie de condition d'acception du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '5':
		print(" --- Vous avez choisi la place 5 --- ")
		print(" * 25.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 25000

		# Ajout des informations supplémentaires au niveau du ticket
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = input("Entrez votre numéro de téléphone : ")

		# La partie de la condition d'acception du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '6':
		print(" --- Vous avez choisi la place 6 --- ")
		print(" * 50.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 50000

		# Ajout des informations supplémentaires au niveau du ticket du parking
		pseudo = input("Entrez votre pseudo :")
		numero_tel = input("Entrez votre numéro de téléphone : ")

		# Partie de la condition d'acceptation du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '7':
		print(" --- Vous avez choisi la place 7 --- ")
		print(" * 55.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 55000

		# Ajout des informations supplémentaires au niveau du ticket du parking
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = eval(input("Entrez votre numéro de téléphone : "))

		# Partie de la condition d'acception du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '8':
		print(" --- Vous avez choisi la place 8 --- ")
		print(" * 60.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 60000

		# Ajout des informations du client pour le véhicule
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = input("Entrez votre numéro de téléphone : ")

		# Partie de condition pour l'acception du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '9':
		print(" --- Vous avez choisi la place 9 --- ")
		print(" * 65.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 65000

		# Ajout des informations pour le client
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = input("Entrez votre numéro de téléphone : ")

		# Partie de condition pour l'acception du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '10':
		print(" --- Vous avez choisi la place 10 --- ")
		print(" * 70.000 FCFA / mois * ")
		print("Paiement au niveau du guichet")
		prix = 70000

		# Ajout des informations du client dans le ticket du parking
		pseudo = input("Entrez votre pseudo : ")
		numero_tel = eval(input("Entrez votre numéro de téléphone : "))

		# Partie de condition d'acceptation du numéro de téléphone
		if type(numero_tel) == str:
			if int(numero_tel) == int:
				# Création du ticket et de son impression
				paiement_impression_ticket(numero_tel, choix_abonne_name, choix_abonne, prix, place_one, pseudo, now)
		else:
			#Création de la partie qui ne pas fait pas parti de la condition
			print("Votre numéro de téléphone n'est pas correct !")
			print("Réessayez")


	elif place_one == '99':
		print("Attention : vous avez quitté l'application --- ")
		exit()

	else:
		print("Erreur : veillez reéssayer")
		exit()



# Appel de la fonction
affichage_application()

	


	
	

