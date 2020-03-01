from Grille import Grille
import random
class Compteur(object):
    def __init__(self):
        self.val=0
    def __str__(self):
        return str(self.val)
class Bataille(object):
    def __init__(self):
        self.grille=Grille.genere_grille()
    def victoire(self):#On va vider les cases lorsque l'on touche un bateau sur cette case ainsi on a juste besoin de verifier si la grille est vide ce qui est le cas pour une grille generée par defaut
        if(self.grille.grille == Grille().grille):
            return True
        return False
    def reset(self):
        self.grille=Grille.genere_grille()
    def joue(self,position):
        """
            (int,int) -> Boolean
            Correspond à l'action de lancer une torpille a la position donnée\n
            renvoie un Booleen indiquant si un bateau à été touché
        """
        posx,posy=position
        if self.grille.isPleine(position):
            self.grille.grille[posy][posx]=0
            return True
        return False
    def joue(self,position,compteur=None):
        """
            (int,int) -> Boolean
            Correspond à l'action de lancer une torpille a la position donnée\n
            renvoie un Booleen indiquant si un bateau à été touché
        """
        if(position[0]>=10 or position[1]>=10):
            return False
        posx,posy=position
        if not(compteur is None):
            compteur.val+=1
        if self.grille.isPleine(position):
            self.grille.grille[posy][posx]=0
            return True
        return False
class Joueur(object):
    def __init__(self):
        self.jeu=Bataille()
    def reset(self):
        self.jeu.grille=Grille.genere_grille()
    @staticmethod
    def ChoisisPosition(dico):
        while "La position a deja ete jouee":
                    x=random.randint(0,9)
                    y=random.randint(0,9)
                    if dico.get((x,y)) == None:
                        dico[(x,y)]=True
                        return x,y
    def strategieAleatoire(self):
        emplacementjoue={}
        Compteurcoup=0
        print(not self.jeu.victoire())
        while (not self.jeu.victoire()):
            x,y=Joueur.ChoisisPosition(emplacementjoue)
            self.jeu.joue((x,y))
            Compteurcoup+=1
        print("La partie à été gagnée en",Compteurcoup,"coups")
            #self.jeu.grille.affiche()
    def strategieHeuristique(self):
        emplacementjoue={}
        Compteurcoup=Compteur()
        print(not self.jeu.victoire())
        while (not self.jeu.victoire()):
            x,y=Joueur.ChoisisPosition(emplacementjoue)
            #self.jeu.grille.affiche()
            if self.jeu.joue((x,y),Compteurcoup):
                print(emplacementjoue.get((x+1,y)) is None)
                print("Pleine=",self.jeu.grille.isPleine((x+1,y)))
                i=0
                #if (emplacementjoue.get((x+1,y)) is None) and self.jeu.joue((x+1,y),Compteurcoup):#On commence par verifier toutes les cases d'un coté le décalage se fait par i qui sert d'offset puis on verifie les cases de l'autre coté apres reinitialisation de l'offset
                i=1
                print(emplacementjoue.get((x+i,y)) is None)
                print("Compteur=",Compteurcoup)
                while((emplacementjoue.get((x+i,y)) is None) and self.jeu.joue((x+i,y),Compteurcoup)):
                        i+=1
                i=1
                print(emplacementjoue.get((x,y+i)) is None)
                print("Compteur=",Compteurcoup)
                while((emplacementjoue.get((x,y+i)) is None) and self.jeu.joue((x,y+i),Compteurcoup)):
                        i+=1
                i=1
                print(emplacementjoue.get((x-i,y)) is None)
                print("Compteur=",Compteurcoup)
                while((emplacementjoue.get((x-i,y)) is None) and self.jeu.joue((x+i,y),Compteurcoup)):
                        i+=1
                i=1
                print(emplacementjoue.get((x,y-i)) is None)
                print("Compteur=",Compteurcoup)
                while((emplacementjoue.get((x,y-i)) is None) and self.jeu.joue((x,y+i),Compteurcoup)):
                        i+=1
        print("La partie à été gagnée en",Compteurcoup,"coups")
joueur=Joueur()
joueur.strategieAleatoire()
joueur.reset()
joueur.strategieHeuristique()
print("OU")