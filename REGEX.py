# EXPRESIONES_REGULARES
import re

opcion=0
while opcion!=11:

    print ("\nBUSCADOR")
    print ("1. Palabras que tengan 7 ó más letras \n2. Expresiones que no finalicen en vocal \n3. Palabras que inicien con M sin que la segunda letra sea vocal \n4. Expresiones entre comillas \n5. Ip's \n6. Horas \n7. Teléfonos \n8. E-mails \n9. Url's \n10. Códigos postales \n11. Finalizar programa")
    opcion= int (input("¿Qué desea buscar? "))

    if opcion==1:
        filename ="LDC.txt"
        textfile=open(filename,"r")
        ex = r"[a-zA-Z]+"
        reg=re.compile(ex)
        for line in textfile:
            lista=reg.findall(line)
            patron=r"[A-Za-z]{7,}"
            for elemento in lista:
                if re.search(patron, elemento):
                    print(elemento)
        textfile.close()
                    
    if opcion == 2:        
        filename = "LDC.txt"
        textfile = open(filename, "r")
        regex = r"[A-Za-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            regex = r"[A-Za-z]+[^aeiouAEIOU]$"
            for elemento in lista:
                if re.search(regex,elemento):
                    print(elemento)
        textfile.close()

    if opcion == 3:
        text = "LDC.txt"
        texto = open(text,"r")
        rex = "[Mm][^aeiouAEIOUáéíóúÁÉÍÓÚ]"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elemento in lista:
                if re.search(rex, elemento):
                    print(elemento)
        texto.close() 

    if opcion == 4:
        text = "LDC.txt"
        texto = open(text,"r")
        rex = r"(\"[^\"]+\")"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)            
            if re.search(rex, line):
                print(lista)            
        texto.close()

    if opcion == 5:
        text = "LDC.txt"
        texto = open(text,"r")
        rex = r"([0-9]{3}\.[0-9]{2}\.[0-9]{1,3}\.[0-9]{1,3})"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elemento in lista:
                if re.search(rex, elemento):
                    print(elemento)
        texto.close()

    if opcion == 6:
        text = "LDC.txt"
        texto = open(text,"r")
        rex = r"(\d\d\:\d\d\s[AaPp][Mm])"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)
        texto.close()

    if opcion == 7:
        text = "LDC.txt"
        texto = open(text,"r")
        rex = r"(\d\d\d\d\d\d\d\d\d\d)"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)
        texto.close()

    if opcion == 8:
        text = "LDC.txt"
        texto = open(text,"r")
        rex = "([0-9a-zA-Z0-9._%+-]+@[0-9a-zA-Z0-9.-]+\.[0-9a-zA-Z]{2,6})"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)
        texto.close()

    if opcion == 9:
        text = "LDC.txt"
        texto = open(text,"r")
        rex = r"(http:|https:\/\/[0-9a-zA-Z0-9._%+-]+\.[0-9a-zA-Z]+\/[^\r\n\s]+)"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)
        texto.close()

    if opcion == 10:
        text = "LDC.txt"
        texto = open(text,"r")
        rex = r"([1-4][0-9][0-9][0-9][0-9]|0?=[1-9][0-9][0-9][0-9]|5?=[0-2][0-9][0-9][0-9])"
        reg = re.compile(rex)
        for line in texto:
            lista = reg.findall(line)
            for elem in lista:
                if re.search(rex, elem):
                    print(elem)
        texto.close()

    if opcion == 11:
        print("Programa finalizado")    
else :
    print("\n Opción inválida. Ingrese otro número")
