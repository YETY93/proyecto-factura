## TABAL DE IVA
## VERSION 0.5


def IVA ():

    print ("")
    print ("")
    valor_producto = (int (input ("Ingrese el valor del producto :>   ")))

    iva_producto = int((valor_producto * 0.16) / 1.16)
    sub_total = (valor_producto - iva_producto)

    print (" El subtotal del producto es: ""\t\t", sub_total)
    print ("")
    print (" El iva del producto es:      ""\t\t",iva_producto)
    print ("")
    print (" El valor del producto es:    ""\t\t",valor_producto)
    print ("")

