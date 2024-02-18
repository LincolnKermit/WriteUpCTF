myfile = open("clef_stega.txt", "r")
myline = myfile.readline()
dico = []
while myline:
    myline = myfile.readline().strip()
    dico.append(myline)
myfile.close()
decode = "19(5)/2(5)/5(2)/26(1)/47(1)/2(2)/7(2)/2(5)/59(1)/2(4)/24(1)/9(1)/59(1)/24(1)/81(2)/5(2)/10(1)"
tab=decode.split("/")
for i in range(len(tab)):
    clef = tab[i].split("(")
    word = dico[int(clef[0])-2]
    #print(tab[i],word)
    lettre = word[int(clef[1][0])-1]
    print(lettre, end="")
print("")





pgarraud@esiee-it.fr