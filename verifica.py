#1
import pprint
pp=pprint.PrettyPrinter(indent=4)
atletica= {"Giuseppe Gullo" : [("corsa campestre",(40,21,0),"Allievi"),("corsa 100mt",(0,12,0),"Juniores mas"),("corsa 200mt",(0,29,19),"Juniores mas")],
           "Antonia Barbera": [("corsa campestre",(0,39,11),"Juniores fem"),("corsa 100mt",(0,18,0),"Juniores fem"),("corsa 200mt",(0,0,0),"Juniores fem")],
           "Nicola Esposito": [("corsa campestre",(0,43,22),"Allievi"),("corsa 100mt",(0,14,0),"Juniores mas"),("corsa 200mt",(0,36,19),"Juniores mas")]}

#2
atletica["Elisa Freddi"]= [("corsa campestre",(20,30,2),"Allieve"),("corsa 100mt",(0,20,25),"Juniores fem"),("corsa 200mt",(0,40,19),"Juniores fem")]

#3    controllato prof Spinarelli
discipline= atletica["Giuseppe Gullo"]
discipline.append(("corsa ad ostacoli 400 mt",(0,40,34),"Allievi"))
atletica["Giuseppe Gullo"]= discipline
discipline= atletica["Antonia Barbera"]
discipline.append(("corsa ad ostacoli 400 mt",(0,39,10),"Allieve"))
atletica["Antonia Barbera"]= discipline
discipline= atletica["Nicola Esposito"]
discipline.append(("corsa ad ostacoli 400 mt",(0,40,10),"Allievi"))
atletica["Nicola Esposito"]= discipline
discipline= atletica["Elisa Freddi"]
discipline.append(("corsa ad ostacoli 400 mt",(0,40,26),"Allieve"))
atletica["Elisa Freddi"]= discipline

#4    controllato prof Spinarelli
print("corsa campestre dell'atleta Giuseppe Gullo")
print(atletica["Giuseppe Gullo"][0])
print("")

#5    controllato prof Spinarelli
print("200mt dell'atleta Nicola Esposito")
print(atletica["Nicola Esposito"][2][0])
print(atletica["Nicola Esposito"][2][1])
print(atletica["Nicola Esposito"][2][2])
print("")

#6    controllato prof Spinarelli
print("tempo di Antonia Barbera nella corsa 100 mt")
print(atletica["Antonia Barbera"][1][1])
print("")

#7    controllato prof Spinarelli
min=(atletica["Giuseppe Gullo"][1][1])
for chiave in atletica.keys():
  if ((atletica[chiave][1][2])=="Juniores mas"):
    if ((atletica[chiave][1][1])>min):
      min=min
    else:
      min=(atletica[chiave][1][1])
print(f"Il tempo minore nella categoria Juniores mas dei 100 mt è: {min}")
print("")

#8    controllato prof Spinarelli
mag=(atletica["Giuseppe Gullo"][2][1])
for chiave in atletica.keys():
  if ((atletica[chiave][2][2])=="Juniores mas"):
    if ((atletica[chiave][2][1])<mag):
      mag=mag
    else:
      mag=(atletica[chiave][2][1])
print(f"Il tempo maggiore nella categoria Juniores mas dei 200 mt è: {mag}")
print("")

#9    controllato prof Spinarelli
somma=(0,0,0)
cont=0
for chiave in atletica.keys():
  if ((atletica[chiave][0][2])=="Allievi"):
    somma= (somma[0]+(atletica[chiave][0][1][0]),somma[1]+(atletica[chiave][0][1][1]),somma[2]+(atletica[chiave][0][1][2]))
    cont= cont+1
media=(somma[0]/cont,somma[1]/cont,somma[2]/cont)
print(f"La media dei tempo nella categoria Allievi della corsa campestre è: {media}")
