import math

# récupération de la taille du caré
taille = input("Enter la taille du cercle :")
rayon = int(taille)/2

print(rayon)

# création de la matrice vide (matrice = [[0] * int(taille) for _ in range (int(taille)) ])
for i in range(1,int(taille)):
    for j in range(1,int(taille)):
        val1 = math.sqrt(pow((i-int(rayon)),2)+pow((j-int(rayon)),2))
        if val1<=(rayon-(int(rayon)/10)) :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print("")

