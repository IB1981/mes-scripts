#def table_multiplication(x):
#	i=0
#	while i < 10:
#		print(i, "*",x, "=", (i + 1) * x)
#		i += 1
#Exemple d'utilisation de la boucle for pour extraire les lettres qui composent un mot
print("PREMIER SCRIPT")
fruits=["poire","mangues","kiwi"]#liste des fruits
for x in "mangues":#Utilisons la boucle for pour extraire les lettres qui composent le mot mangues
	print(x )	#on affiche les differentes lettres

#
print("SECOND SCRIPT UTILISATION DU MOT CLE BREAK")

fruits=["poire","mangues","kiwi"]#liste des fruits
for x in fruits:#On utilise la boucle for pour parcourrir la liste des fruits
	print(x)#On affiche les fruits mais...
	if x == "mangues":#il parcours la liste jusqu'a ce qu'il trouve mangues 
		break#met fin au script sans parcourir le reste de la liste


print("TROISIEME SCRIPT UTILISATION DU MOT CLE CONTINUE")
fruits=["poire","mangues","kiwi"]#liste des fruits
for x in fruits:#On utilise la boucle for pour parcourrir la liste des fruits
	print(x)#On affiche les fruits mais...
	if x == "mangues":#il parcours la liste jusqu'a ce qu'il trouve mangues 
		continue#ce mot cle permet de poursuivre l'execution avec la prochaine instruction
	print(x)#On affiche la suite des fruits

print("QUATRIEME SCRIPT UTILISATION D'UNE LISTE'")
for x in range(6):#On compte de la liste des 6 premiers elements a partir de 0
	print(x)#On compte de 0 a 5


print("Cinquieme script")
for x in range(2,30,3):#On parcours la liste de 2 a 29 par pas de 3
	print(x)#on a 2 5 8 11 ect....