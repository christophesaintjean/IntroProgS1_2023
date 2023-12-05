import csv

with open('park.csv', newline='') as f:
   lecteur = csv.reader(f, delimiter=',', quotechar='"')
   for ligne in lecteur:
      print(ligne)