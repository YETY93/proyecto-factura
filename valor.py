## este es la tabla de comisiones
## v 0.1 por yesid rangel

import bienvenida
import tabla1
import tabla2
import tabla3
import tabla4
import tabla5
import tabla6
import tabla7
import tabla8
import tabla9
import tabla_iva

bienvenida.bienvenida()
def funcionmayor ():

    def principal():
        
        print("")
        print("")
        print("De '1 a 9' cuantos telefonos deseas facturar. ")
        print("")
        opcion = input(">  ")

        print ("Has seleccionado ",opcion,"telefono\S")

        if opcion == "1":
            tabla1.telefono1()
            
        elif opcion == "2":
            tabla2.telefonos2()
            
        elif opcion == "3":
            tabla3.telefonos3()
            
        elif opcion == "4":
            tabla4.telefonos4()
            
        elif opcion == "5":
            tabla5.telefonos5()
            
        elif opcion == "6":
            tabla6.telefonos6()
            
        elif opcion == "7":
            tabla7.telefonos7()
            
        elif opcion == "8":
            tabla8.telefonos8()
            
        elif opcion == "9":
            tabla9.telefonos9()
              
        else:
            print ("Seleccione una opcion valida, o comuniquese con el administrador")
            

    print("")
    print ("Selccione la opcion '1' para facturar o la opcion '2' para mostrar el IVA: ")
    print("")
    seleccion = input(">>>  ")
        
    if (seleccion == "1"):
        principal ()
        funcionmayor ()
        

    elif (seleccion == "2"):
        tabla_iva.IVA()
        funcionmayor ()
        
        

funcionmayor()


input()
