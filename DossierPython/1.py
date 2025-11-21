import random
liste = []
def createMat():
    global liste 
    liste = []
    try:
        num = int(input("Entre la taille de la matrice: "))
        for i in range(num):
            ligne = []
            for j in range(num):
                ligne.append(random.randint(1,1000))
            liste.append(ligne)
    except ValueError:
        print("Erreue tu dois Entrer un entier")  
createMat()        
def afficheMat():
    for i in (liste):
            print(i)
def matDiagSup():
    t = 0
    for i in range (len(liste)):
        j = 1
        for j in range (j+i,len(liste)) :
            print(liste[i][j],i+1,j+1)
            t+=1
    print(f"Pour une matrice de taile {len(liste)} * {len(liste)} on a fait : {t} tours")
afficheMat()
matDiagSup()