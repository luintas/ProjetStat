from random import randint
import matplotlib.pyplot as py
class Grille():
    horizontal =0
    vertical=1

    vide = 0
    porteAvion=5
    croiseur=4
    contreTorpilleur=3
    sousMarin=3
    torpilleur=2
    plein=1
    vide=0
    def __init__(self):
        self.grille=[]
        for i in range(10):
            self.grille.append([0]*10)
    def isPleine(self,position):
        posx,posy=position
        if posx<10 and posy<10:
            return (self.grille[posy][posx]==self.plein)
        return False
    def peut_placer(self,bateau,position,direction):
        #TODO Faire en sorte qu'on puisse choisir les directions gauche droite haut bas
        currentx,currenty=position
        if direction == self.horizontal :
            if currentx+bateau > 9:
                return False
            for i in range(bateau):
                if self.grille[currenty][currentx+i] != self.vide:
                    return False
        if direction == self.vertical :
            if currenty+bateau > 9:
                return False
            for i in range(bateau):
                if self.grille[currenty+i][currentx] != self.vide:
                    return False
        return True
    def place(self,bateau,position,direction):
        if self.peut_placer(bateau,position,direction):
            currentx,currenty=position
            if direction == self.horizontal :
                for i in range(bateau):
                    self.grille[currenty][currentx+i] = self.plein
            if direction == self.vertical :
                for i in range(bateau):
                    self.grille[currenty+i][currentx] = self.plein
            return self.grille
        else:
            return False
    def enleve(self,bateau,position,direction):
        currentx,currenty=position
        if direction == self.horizontal :
            for i in range(bateau):
                self.grille[currenty][currentx+i] = self.vide
        if direction == self.vertical :
            for i in range(bateau):
                self.grille[currenty+i][currentx] = self.vide
    def place_alea(self,bateau):
        Reussi=False
        while Reussi is False :
            position=(randint(0,9),randint(0,9))
            direction=randint(0,1)
            if Reussi is False:
                Reussi=self.place(bateau,position,direction)
            if Reussi is False:
                Reussi=self.place(bateau,position,direction)

        return Reussi
    def copy(self):
        newGrille=Grille()
        for i in range(10):
            for j in range(10):
                newGrille.grille[i][j] = self.grille[i][j]
        return newGrille
    def affiche(self):
        print("OUI")
        py.imshow(self.grille)
        py.show(block=False)
        py.pause(1)
        py.close()
    @staticmethod
    def eq(grilleA,grilleB):
        for i in range(10):
            for j in range(10):
                if grilleA[i][j] != grilleB[i][j]:
                    return False
        return True
    @staticmethod
    def genere_grille():
        listeBateau=(Grille.porteAvion,Grille.croiseur,Grille.contreTorpilleur,Grille.sousMarin,Grille.torpilleur)
        newGrille=Grille()
        for bateau in listeBateau:
            newGrille.grille=newGrille.place_alea(bateau)
        return newGrille
    def denombre1(self,bateau):
        cpt=0
        gr=Grille()
        #for bateau in listeBateau:
        for direction in (Grille.horizontal,Grille.vertical):
            for i in range(10):
                for j in range(10):
                    if gr.peut_placer(bateau,(i,j),direction):
                        cpt+=1
        return cpt


    
    def denombre2(self,listeBateau):
        """
            Dans cette fonction on va créer des sets auquel on donnera une valeur correspondant à la combinatoire des sets les sets comprendront la position des bateaux indice selon le bateau selon l'ordre dans genere Grille
        """
        cpt=0
        bateau=listeBateau[0]
        if  len(listeBateau)==1:
            for direction in (Grille.horizontal,Grille.vertical):
                for i in range(10):
                    for j in range(10):
                        if self.peut_placer(bateau,(i,j),direction):
                            cpt+=1
        else :
            for direction in (Grille.horizontal,Grille.vertical):
                for i in range(10):
                    for j in range(10):
                        if self.peut_placer(bateau,(i,j),direction):
                            self.place(bateau,(i,j),direction)
                            cpt+=self.denombre2(listeBateau[1:])
                            self.enleve(bateau,(i,j),direction)
        return cpt
    @staticmethod
    def denombre3(grille):
        cpt=1
        while(grille != Grille.genere_grille()):
            cpt+=1
        return cpt
    #TODO Refaire denombre 3 plein de fois ce qui nous donnera une approximation du nombre de possibilitées ensuite faire en sorte de pouvoir faire ça assez de fois pour que la variance dans nos resultats soit assez faible on pourra ainsi considerer cette approximation comme acceptable
if __name__ == "__main__":
    listeBateau=(Grille.porteAvion,Grille.croiseur,Grille.contreTorpilleur,Grille.sousMarin,Grille.torpilleur)
    gr=Grille()
    print(gr.denombre2(listeBateau[0:2]))
