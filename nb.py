# Naive Bayes
# "Solo es imposible sino lo intentas"

### Variables Globales ###
fiebreY=0 #fiebre|Gripa
ffY=0 	  #NoFiebre|Gripa
fiebreN=0 #Fiebre|NoGripa
ffN=0 	  #NoFiebre|NoGripa
cabezaY=0 #cabeza|Gripa
fcY=0	  #NoCabeza|Gripa
cabezaN=0 #cabeza|NoGripa
fcN=0     #NoCabeza|NoGripa
escuY=0	#Escurrimineto|Gripa
feY=0   #NoEscurrimineto|Gripa
escuN=0 #Escurrimiento|NoGripa
feN=0   #NoEscurrimiento|NoGripa
normalY=0 #Normal|Gripa
fnY=0	  #NoNormal|Gripa
normalN=0 #Normal|NoGripa
fnN=0 	  #NoNormal|NoGripa
constiY=0 #Constipacion|Gripa
fconY=0   #NoConstipacion|Gripa
constiN=0 #Constipacion|NoGripa
fconN=0   #NoConstipacion|NoGripa
yes=0	  # Gripa
no=0	  # No Gripa
pYes=1
pNo=1
ins=0

def leer(txt):
	global fiebreY,ffY,fiebreN,ffN,cabezaY,fcY,cabezaN,fcN,escuY,feY,escuN,feN,normalY,fnY,normalN,fnN,constiY,fconY,constiN,fconN,yes,no,ins
	ly=""
	archivo=open(txt,"r")
	ins=0   #Numero de elementos del dataset
	for linea in archivo:
		ly=linea
		analisis(ly)
		ins=ins+1
	print ("Tamano Dataset=",ins)
	print ("---------------------------------")
	print (">>Gripa=", yes)
	print (">>No Gripa=", no)
	print ("---------------------------------")
	print (">>Fiebre|Gripa",fiebreY)
	ffY=yes-fiebreY
	print (">>NoFiebre|Gripa",ffY)
	print (">>Fiebre|NoGripa",fiebreN)
	ffN=no-fiebreN
	print (">>NoFiebre|NoGripa",ffN)
	print ("---------------------------------")
	print (">>DolorC|Gripa", cabezaY)
	fcY=yes-cabezaY
	print (">>NoDolorC|Gripa", fcY)
	print (">>DolorC|NoGripa", cabezaN)
	fcN=no-cabezaN
	print (">>NoDolorC|NoGripa", fcN)
	print ("---------------------------------")
	print (">> Escurrimiento|Gripa", escuY)
	print (">> Escurrimiento|NoGripa", escuN)
	print (">> Normal|Gripa", normalY)
	print (">> Normal|NoGripa", normalN)
	print (">> Constipacion|Gripa", constiY)
	print (">> Constipacion|NoGripa", constiN)
	archivo.close()
	print (" ------------- PRUEBA ------------")
	a2='prueba.txt'
	leer2(a2)

def leer2(txt2):
	global fiebreY,ffY,fiebreN,ffN,cabezaY,fcY,cabezaN,fcN,escuY,feY,escuN,feN,normalY,fnY,normalN,fnN,constiY,fconY,constiN,fconN,yes,no,ins
	global pYes, pNo
	archi2=open(txt2,"r")
	for l in archi2:
		print (">>",l)
	lx=txt2
	sepa3=""
	sepa2=l.split('\n')
	for i in range(len(sepa2)):
		sepa3+= sepa2[i]
		#print ("*w*",sepa2[i])
	#print (separar3)
	sepa=sepa3.split(',')
	if sepa[0] == 'True':
		pFTY=fiebreY/yes
		pFTN=fiebreN/no
		pYes=pYes*pFTY
		pNo=pNo*pFTN

	if sepa[0] == 'False':
		pFFY=ffY/yes
		pFFN=ffN/no
		pYes=pYes*pFFY
		pNo=pNo*pFFN

	if sepa[1] == 'True':
		pDTY=cabezaY/yes
		pDTN=cabezaN/no
		pYes=pYes*pDTY
		pNo=pNo*pDTN

	if sepa[1] == 'False':
		pDFY=fcY/yes
		pDFN=fcN/no
		pYes=pYes*pDFY
		pNo=pNo*pDFN

	if sepa[2] == 'Escurrimiento':
		pEY=escuY/yes
		pEN=escuN/no
		pYes=pYes*pEY
		pNo=pNo*pEN

	if sepa[2] == 'Normal':
		pNY=normalY/yes
		pNN=normalN/yes
		pYes=pYes*pNY
		pNo=pNo*pNN

	if sepa[2] == 'Constipacion':
		pCY=constiY/yes
		pCN=constiN/no
		pYes=pYes*pCY
		pNo=pNo*pCN

	pYes2=pYes*(yes/ins)
	pNo2=pNo*(no/ins)
	pYes3=pYes2/(pYes2+pNo2)
	pNo3=pNo2/(pYes2+pNo2)

	print ("P(Class=Yes)",pYes3)
	print ("P(Class=No)",pNo3)

	compara(pYes3,pNo3)

	archi2.close()

	
def analisis(li):
	global fiebreY, fiebreN,cabezaY,cabezaN,escuY,escuN,normalY,normalN,constiY,constiN,yes,no
	separar3=""
	separar2=li.split('\n')
	for i in range(len(separar2)):
		separar3+= separar2[i]
	separar=separar3.split(',')

	if separar[3]=='Yes':
		yes+=1
	if separar[3]=='No':
		no+=1
	if separar[0] == 'True' and separar[3]=='Yes':
		fiebreY+=1
	if separar[0] == 'True' and separar[3] == 'No':
		fiebreN+=1
	if separar[1] == 'True' and separar[3]=='Yes':
		cabezaY+=1
	if separar[1] == 'True' and separar[3]=='No':
		cabezaN+=1
	if separar[2] == 'Escurrimiento' and separar[3] == 'Yes':
		escuY+=1
	if separar[2] == 'Escurrimiento' and separar[3] == 'No':
		escuN+=1
	if separar[2] == 'Normal' and separar[3] == 'Yes':
		normalY+=1
	if separar[2] == 'Normal' and separar[3] == 'No':
		normalN+=1
	if separar[2] == 'Constipacion' and separar[3] == 'Yes':
		constiY+=1
	if separar[2] == 'Constipacion' and separar[3] == 'No':
		constiN+=1

def compara(y,n):
	print(" \n\n------  RESULTADO   ------")
	if y>n:
		print (" ----> ES GRIPA <---- ")
	elif n>y:
		print (" ----> NO ES GRIPA <---- ")
	print ("--------------------------")


def menu():
	l='gripa.txt'
	a=leer(l)

menu()