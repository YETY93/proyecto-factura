    
def telefonos2():
    
    comision_1 = 12000
    comision_2 = 14000
    comision_3 = 16000
    comision_4 = 18000
    comision_5 = 21000
    comision_6 = 27000
    comision_7 = 28000
    comision_8 = 30000
    comision_9 = 35000
     
    telefono_1 = int (input ("Ingrese el valor del primer telefono:>   "))
    telefono_2 = int (input ("Ingrese el valor del segundo telefono:>  "))
    
    
    if (telefono_1 >= 20000 and telefono_1 <= 62338):
        print ("El valor de la comision es de :", comision_1)
        resta_1 = telefono_1 - comision_1
        print("El precio del equipo es: ","\t\t",resta_1)     
     
    elif (telefono_1 >= 62339 and telefono_1 <= 93600):
        print ("El valor de la comision es de :", comision_2)
        resta_1 = telefono_1 - comision_2
        print("El precio del equipo es: ","\t\t",resta_1)

    elif (telefono_1 >= 93601 and telefono_1 <= 99999) or (telefono_1 >= 100000 and telefono_1 <= 109200) :
        print ("El valor de la comision es de :", comision_3)
        resta_1 = telefono_1 - comision_3
        print("El precio del equipo es: ","\t\t",resta_1)
        
    elif(telefono_1 >= 109201 and telefono_1 <= 124800):
        print ("El valor de la comision es de :", comision_4)
        resta_1 = telefono_1 - comision_4
        print("El precio del equipo es: ","\t\t",resta_1)
        
    elif(telefono_1 >= 124801 and telefono_1 <= 156000):
        print ("El valor de la comision es de :", comision_5)
        resta_1 = telefono_1 - comision_5
        print("El precio del equipo es: ","\t\t",resta_1)        

    elif(telefono_1 >= 156001 and telefono_1 <= 358800):
        print ("El valor de la comision es de :", comision_6)
        resta_1 = telefono_1 - comision_6
        print("El precio del equipo es: ","\t\t",resta_1)        

    elif(telefono_1 >= 358801 and telefono_1 <= 530400):
        print ("El valor de la comision es de :", comision_7)
        resta_1 = telefono_1 - comision_7
        print("El precio del equipo es: ","\t\t",resta_1)        

    elif(telefono_1 >= 530401 and telefono_1 <= 624000):
        print ("El valor de la comision es de :", comision_8)
        resta_1 = telefono_1 - comision_8
        print("El precio del equipo es: ","\t\t",resta_1)       

    elif(telefono_1 >= 624000 and telefono_1 <= 999999) or  (telefono_1 >= 1000000 and telefono_1 <= 1999999):
        print ("El valor de la comision es de :", comision_9)
        resta_1 = telefono_1 - comision_9
        print("El precio del equipo es: ","\t\t",resta_1)

    else:
        telefono_1 ==1
        resta_1 = 0


    if (telefono_2 >= 20000 and telefono_2 <= 62338):
        print ("El valor de la comision es de :", comision_1)
        resta_2 = telefono_2 - comision_1
        print("El precio del equipo es: ","\t\t",resta_2)     
     
    elif (telefono_2 >= 62339 and telefono_2 <= 93600):
        print ("El valor de la comision es de :", comision_2)
        resta_2 = telefono_2 - comision_2
        print("El precio del equipo es: ","\t\t",resta_2)

    elif (telefono_2 >= 93601 and telefono_2 <= 99999) or (telefono_2 >= 100000 and telefono_2 <= 109200) :
        print ("El valor de la comision es de :", comision_3)
        resta_2 = telefono_2 - comision_3
        print("El precio del equipo es: ","\t\t",resta_2)
        
    elif(telefono_2 >= 109201 and telefono_2 <= 124800):
        print ("El valor de la comision es de :", comision_4)
        resta_2 = telefono_2 - comision_4
        print("El precio del equipo es: ","\t\t",resta_2)
        
    elif(telefono_2 >= 124801 and telefono_2 <= 156000):
        print ("El valor de la comision es de :", comision_5)
        resta_2 = telefono_2 - comision_5
        print("El precio del equipo es: ","\t\t",resta_2)        

    elif(telefono_2 >= 156001 and telefono_2 <= 358800):
        print ("El valor de la comision es de :", comision_6)
        resta_2 = telefono_2 - comision_6
        print("El precio del equipo es: ","\t\t",resta_2)        

    elif(telefono_2 >= 358801 and telefono_2 <= 530400):
        print ("El valor de la comision es de :", comision_7)
        resta_2 = telefono_2 - comision_7
        print("El precio del equipo es: ","\t\t",resta_2)        

    elif(telefono_2 >= 530401 and telefono_2 <= 624000):
        print ("El valor de la comision es de :", comision_8)
        resta_2 = telefono_2 - comision_8
        print("El precio del equipo es: ","\t\t",resta_2)       

    elif(telefono_2 >= 624000 and telefono_2 <= 999999) or  (telefono_2 >= 1000000 and telefono_2 <= 1999999):
        print ("El valor de la comision es de :", comision_9)
        resta_2 = telefono_2 - comision_9
        print("El precio del equipo es: ","\t\t",resta_2)

    else:
        telefono_2 ==1
        resta_2 = 0

    suma = (resta_1 + resta_2)
    
    iva = int((suma * 0.16) / 1.16)   
    sub_total = (suma - iva)



    print("")
    print("")
    print("El  SUB TOTAL es de:","\t\t", sub_total)
    print("")

    print("")
    print("El IVA del equipo es:","\t\t", iva)
    print("")
    print("")

    print("")
    print ("Elvalor total de la facturas es: ""\t", suma)
    print("")
    

    if (suma > 763000):
        print("\t\t","EL VALOR A SUPERADO EL LIMITE A FACTURAR")
