#-*-coding:Latin-1 -*
import os#on importe le module

def som(x,y):#on definit la fonction som avec en paramètre x et y
	total = x + y#on crée une variable qui va contenir la somme des deux nombres
	return total # la fonction va retourner la somme
	
	
def main():#on définit cette fonction qui va faire appel à la fonction som
	print("faire la somme de deux nombres")#on affiche la phrase
	nbre1=int(input("Entrez un nombre "))#l'utilisateur entre un premier nombre
	nbre2=int(input("Entrez un nombre "))#l'utilisateur entre un second nombre
	resultat=som(nbre1,nbre2)#pour avoir le resultat on appelle la fonction som avec ces paramètres
	print("la somme de ",nbre1, "et", nbre2,"est",resultat)#Ici on affiche cette phrase

if __name__ == '__main__':#Ici c'est grâce à cette condition qu'on pourra executer notre programme
	main()
os.system("pause")#On met le system en pause pour pouvoir afficher l'execution du programme 