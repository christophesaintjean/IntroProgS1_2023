f = open('fichier.txt', mode='w')
n = f.write("une première ligne\n")
print("La seconde ligne", file=f)
f.close()