import random
import requests
import json

url = 'https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&includePartOfSpeech=noun&minCorpusCount=8000&maxCorpusCount=-1&minDictionaryCount=3&maxDictionaryCount=-1&minLength=6&maxLength=12&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'

masque = []
nombreErreur = 0
# Menu 
print("*****************************")
print("* Bienvenue au jeu du pendu *")
print("*****************************")
print("*1 - Mode 1 joueur(api EN)  *")
print("*2 - Mode 1 joueur(local FR)*")
print("*3 - Mode 2 joueur          *")
print("*****************************")

modeJeu = -1
while modeJeu < 1 or modeJeu > 3:
	modeJeu = int(input("Entrer votre choix : "))


if modeJeu == 1:
	response = requests.get(url)
	data = response.json()
	mot = data['word']

if modeJeu == 2:
	lines = [line.rstrip('\n').lower() for line in open('dictionnaire.txt')]
	mot = lines[random.randint(0, len(lines)-1)]

	
if modeJeu == 3:
	mot = input("Entrez le mot a trouver : ")

print("\n\n\n\n\n\n\n")


# Initialiser le masque
for i in range(len(mot)):
	masque += [0]


# Fonction permettant de verifier si le mot a été trouver
def motTrouver(masque):
	trouver = True
	for elem in masque:
		if elem == 0:
			trouver = False
	return trouver

# Fonction qui afficher le mot recouvert du masque
def afficher(mot, masque):
	for i in range(len(mot)):

		if masque[i] == 1:
			print(mot[i], end='')
		else:
			print("*", end='')
	print("")

# Fonction qui prend une lettre et met a jour le masque
def verifierLettre(lettre,mot,masque):
	lettreContenu = False
	for i in range(len(mot)):
		if lettre == mot[i]:
			lettreContenu = True
			masque[i] = 1
	return lettreContenu		

# Boucle Principale
while not(motTrouver(masque)) and nombreErreur < 8:
	afficher(mot,masque)
	print("Nombre d'erreur : ",nombreErreur)
	lettre = str(input("Entrer une lettre : "))
	if not(verifierLettre(lettre,mot,masque)):
		nombreErreur += 1
		
	print("\n\n")	
	

# A la fin du jeu
if nombreErreur >= 8 :
	print("GAME OVER ! Le mot était :",mot)
else:
	print("Bravo ! Tu as trouver ! Le mot était bien",mot)
