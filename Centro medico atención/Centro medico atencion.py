#creado por Rodrigo Maureira
#crear un sistema de centro medico atencion pacientes
''' uid, nom, dir, email, sex, reg, prev '''
# menu 1.- reg 2.- att 3.- cons .-4 exit

rut_reg = []
nam_reg = []
dir_reg = []
mai_reg = []
age_reg = []
sex_reg = []
prv_reg = []
reg_reg = []
at_pac = []

#pos_0 = muestra
rut_reg.insert(0,5000000)
nam_reg.insert(0,"admin")
dir_reg.insert(0,"0 street ")
mai_reg.insert(0,"admin@admin.com")
age_reg.insert(0,"0")
sex_reg.insert(0,"F")
prv_reg.insert(0,"Fonasa")
reg_reg.insert(0,"")
#estos registros en posicion 0 son para probar


sw1 = 1
while sw1 == 1:
    print ("\t <<< MeNuE >>> \t\n")
    try:
        op1 = int(input("\t ¿Que necesita?\n\n1) Registrar Paciente\n2) Atencion Paciente\n3) Consultar\n4) Salir\n\n <<< Opcion >>> : "))
        if op1 == 1:
            #no valida el rut pide el nombre
            sw2 = 1
            while sw2 == 1:
                try:
                    rut = int(input(" ingresa rut : "))
                    if rut > 5000000 and rut <= 90000000:
                        sw2 = 0
                except:
                    print (" error ingresa solo numeros : ")    
                rut_reg.append (rut)

            #esto esta bien no lo rompas
            nam = input(" ingrese nombre del paciente : ")
            nam_reg.append(nam)
            dir = input(" ingrese direccion del paciente : ")
            dir_reg.append(dir)
            #debe poder metersele un @
            mail = input(" ingrese email del paciente : ")
            mai_reg.append(mail)
            #edad entre 0 y 110
            sw3 = 1
            while sw3 == 1:
                try:
                    age = int(input(" ingrese edad del paciente : "))
                    if age >= 0 and age <= 110:
                        sw3 = 0
                except:
                    print (" Opcion invalida, reintente : ")
            age_reg.append(age)
            #sexo solo letra f o m, aceptan mayusculas
            sw4 = 1
            while sw4 == 1:
                try:
                    sex = input(" ingrese sexo paciente F/M : ")
                    if sex == "F" or sex == "f" or sex == "M" or sex == "m":
                        sw4 = 0
                except:
                    print (" ingrese edad valida : ")
            sex_reg.append(sex)

            #prevision solo ISAPRE O FONASA
            sw5 = 1
            while sw5 == 1:
                try:
                    prev = input(" ingrese prevision FONASA o ISAPRE : ")
                    if prev == "FONASA" or prev == "ISAPRE":
                        sw5 = 0
                except:
                    print (" ingrese prevision correspondiente FONASA o ISAPRE : ")
                prv_reg.append(prev)

            reg_med = input( " ingrese condiciones del paciente : ")
            reg_reg.append(reg_med)

        elif op1 == 2:
            #soy un tonto rompi el programa no carga los ruts
            #al ingresar el rut, luego pedir fecha
            c = False
            while (True):
                b = int(input(" ingrese rut : "))
                if b < 5000000 or b >= 90000000:
                    b=int(input(" ingrese rut : "))
                else:
                    break
            for i in range(len(rut_reg)):
                if (b==rut_reg[i]):
                    c = True
                    d = i
                    break
            if (c):
                print (" Rut encontrado ")
                at_reg_dat = input(" ingresar fecha de atencion ")
                at_reg_reg = input (" ingrese observaciones del paciente ")
                at_pac[d]=([at_reg_dat,at_reg_reg])

        elif op1 == 3:
            print (" Los ruts registrados son : ")
            print ()
            print (rut_reg)
            print ()
            a = int(input(" ingrese id rut = "))
            print ("\t\n el rut del paciente es = \n")
            print (rut_reg[a])
            print ("\t\n los nombres registrados son = \n")
            print (nam_reg[a])
            print ("\t\n el mail registrado es = \n")
            print (mai_reg[a])
            print ("\t\n la direccion registrada es = \n")
            print (dir_reg[a])
            print ("\t\n la edad registrada es = \n")
            print (age_reg[a])
            print ("\t\n la preivision es = \n")
            print (prv_reg[a])
            print ("\t\n las condiciones del paciente son = \n")
            print (reg_reg[a])
        
        if op1 == 4:
            print (" Gracias uwu ")
            print (" ha salido del sistema :C ")
            sw1 = 0

    except:
        print ("\n >>> ~ ingrese opcion valida @_@ ~ <<<\nVolviendo al menu ... \n ")