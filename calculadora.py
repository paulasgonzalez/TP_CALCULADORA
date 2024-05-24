#------------------TP CALCULADORA CON FUNCIONES------------------#
# ALUMNA: GONZALEZ, PAULA
# COMISION 312


from func_calculadora import *

flag_primer_operando = False
flag_segundo_operando = False
flag_operacion = False


while True:
    match menu():
        case 'A':
            primer_numero = int(input('Ingrese el primer operando: '))
            flag_primer_operando = True
        case 'B':
            if flag_primer_operando == True:
                segundo_numero = int(input('Ingrese el segundo operando: '))
                flag_segundo_operando = True
            else:
                print('Antes de seleccionar esta opcion debe ingresar un primer operando')
        case 'C':
            if flag_segundo_operando == True:
                operacion = input('A - Suma \nB - Resta \nC - Multiplicacion \nD - Division \nE - Factorial \nIngrese el tipo de operacion que desea realizar: ')
                realizar_operaciones(primer_numero, segundo_numero, operacion)
                flag_operacion = True
            else:
                print('Antes de seleccionar esta opcion debe ingresar un segundo operando')
        case 'D':
            if flag_operacion == True:
                mostrar_resultados(primer_numero, segundo_numero, operacion)
            else:
                print('Antes de seleccionar esta opcion debe seleccionar la operacion a realizar')
        case 'E':
             break
        case _:
            print("La opcion seleccionada es invalida")
        
    
    pausar()
    
print('Fin del programa')