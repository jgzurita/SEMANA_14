###  UEA  ###
## JUAN ZURITA ##

# DEFINIMOS LA FUNCIÓN Y ESTABLECEMOS EN %10 EL VALOR DE DESCUENTO POR DEFECTO

def calcular_descuento(monto_total, porcentaje_descuento=10):
    # SE CALCULA EL DESCUENTO
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento


### INGRESAMOS EL MONTO Y EL DESCUENTO
monto = float(input("Ingresa el valor de la compra:  "))
porcentaje_descuento = input("Ingrese el % de  descuento de la compra: ")

# VERIFICAMOS SI SE INGRESO UN VALOR DE %
if porcentaje_descuento == "":
    descuento = calcular_descuento(monto)
else:
    porcentaje_descuento = float(porcentaje_descuento)
    descuento = calcular_descuento(monto, porcentaje_descuento)
#IMPRIMIMOS EL VALOR DEL MONTO EL DESCUENTO Y EL VALOR FINAL DEL MONTO

monto_final = monto - descuento
print("Monto total:", monto, "Descuento:", descuento, "Monto final:", monto_final)