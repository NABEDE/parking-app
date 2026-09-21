#!/bin/bash


echo "Lancement de l'application parking-app"

python3 main.py

if [[ $? -eq 0 ]]; then
	echo "Le lancement de l'application est très bien fait"
else
	echo "Echec du lancecmenent de l'application"
fi