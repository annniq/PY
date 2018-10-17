#Iga variant koosneb kolmest ülesandest. Vormistage kõik kolm samas failis eraldi funktsioonis.
#Ärge unustage nimetada korralikult muutujaid ja lisata kommentaare.
#Variant 1


#Ülesanne 1
#Kirjutage funktsiooni list_sum(list) mis võtab argumendiks listi (massiivi) ja tagastab tema elementide summa. 
#Write a function list_sum(list) that takes a list of numbers as an argument and returns the sum of all numbers

def list_sum(numList):
    '''funktsioon listi sumeerimine '''
    tulemus=[]
    if len(numList) == 1:
        tulemus= numList[0]
    else:
        tulemus= numList[0] + list_sum(numList[1:])
    return tulemus    

print(list_sum([1,10,5]))

 

#Ülesanne 2
#Kirjutage funktsiooni liblikas(string), mis võtab argumendiks lause (sõnad jagatud tühikutega) ja kui sõna algab tähega "a" asendab teda sõnaga "liblikas". Kui lauses on kaks või rohkem sõna mis algavad "a"-ga asendada ainult viimane.
#Näide 1:

# lisada kommentaarid

def liblikas(lause):
    '''liblika funktsioon''' 
    uusLause= str.split(lause, " ")
    uusLause=uusLause[::-1]
    esimeneSona=0
    sonaMassiivis=0
    while sonaMassiivis<len(uusLause):
            if uusLause[sonaMassiivis][esimeneSona]=="a":
                uusLause[sonaMassiivis]="liblikas"
                return uusLause[::-1]
            else:
                sonaMassiivis=sonaMassiivis+1
        

lause="Kui alanud on allla"
print(liblikas(lause))


#Ülesanne 3
#Kirjutage funktsiooni common_symbols(string, string), mis võtab vastu kaks string-tüüpi sama pikkuse muutujat, mis koosnevad suurtest tähetest ja väljastab kommaga jagatud numbid, mis vastavad järgmisele tingimustele:
#Samad sümbolid samades kohtades
#Sümbolite mis leiduvad mõlemas muutujates arv kokku

def common_symbols(string1, string2):
    ''' common symbol funktsioon'''  
    samaSymbol=0
    koht=0
    count=0
    while koht<len(muutuja1):
        if muutuja1[koht]==muutuja2[koht]:
            samaSymbol=samaSymbol+1
        for el in muutuja1 and muutuja2:
            if el==muutuja1[koht] and el==muutuja2[koht]:
                count = count + 1
        koht=koht+1

    return (samaSymbol,count)

muutuja1="AATVN"
muutuja2="TAAVI"
#muutuja1=str(input("Sisesta lause 1:")).upper()
#muutuja2=str(input("Sisesta lause 2:")).upper()   
print(common_symbols(muutuja1, muutuja2))

print("Tere tulemust")