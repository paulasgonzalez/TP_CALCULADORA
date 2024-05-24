from os import system

def limpiar_pantalla():
    """funcion que limpia la pantalla
    """
    system("clear")


def menu()-> str:
    """muestra menu para elegir una opcion

    Returns:
        str: retorna un input para que el usuario ingrese la opcion elegida
    """
    limpiar_pantalla()
    print(" ***MENU CALCULADORA*** ")
    print("A- Ingresar primer operando")
    print("B- Ingresar segundo operando")
    print("C- Operaciones")
    print("D- Mostrar resultados")
    print("E- Salir")
    
    return input('Ingrese opcion: ')


def pausar()-> str:
    input('Aprete una tecla para continuar...')
    
    
def calcular_suma (numero_a: int, numero_b: int)->int:
    """calcula la suma entre dos numeros enteros

    Args:
        numero_a (int): primer numero
        numero_b (int): segundo numero

    Returns:
        int: retorna la suma entre los numeros pasados por parametro
    """
    return numero_a + numero_b


def calcular_resta (numero_a: int, numero_b: int)->int:
    """calcula la resta entre dos numeros

    Args:
        numero_a (int): primer numero
        numero_b (int): segundo numero

    Returns:
        int: retorna la resta entre los numeros pasados por parametros
    """
    return numero_a - numero_b


def calcular_multiplicacion (numero_a: int, numero_b: int)->int:
    """calcula la multiplicacion entre dos numeros enteros

    Args:
        numero_a (int): primer numero
        numero_b (int): segundo numero

    Returns:
        int: retorna la multiplicacion entre los numeros recibidos
    """
    return numero_a * numero_b


def calcular_division (numero_a: int, numero_b: int)->int:
    """calcula la division entre dos numeros enteros

    Args:
        numero_a (int): primer numero
        numero_b (int): segundo numero

    Raises:
        ZeroDivisionError: excepcion en caso de recibir un valor negativo como segundo parametro

    Returns:
        int: retorna la division de los numeros recibidos
    """
    if numero_b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return numero_a / numero_b
    
    
def calcular_factorial(n: int) -> int:
    """calcula el factorial de un numero

    Args:
        n (int): numero para calcular factorial

    Raises:
        ValueError: excepcion en caso de recibir un valor negativo

    Returns:
        int: retorna el factorial del numero recibido
    """
    if n < 0:
        raise ValueError('No existe el factorial de un negativo')
    
    resultado = 1
    for numero in range(1, n+1):
        resultado *= numero
    return resultado


def mostrar_resultados (numero_a: int, numero_b: int, operacion:str)-> None:
    """muestra el resultado de la operacion ingresada entre dos numeros

    Args:
        numero_a (int): primer numero
        numero_b (int): segundo numero
        operacion (str): letra asociada a la operacion se desea realizar
    """
    match operacion:
        case 'A':
            print(f"El resultado de {numero_a} + {numero_b} es {calcular_suma(numero_a, numero_b)}")
        case 'B':
            print(f"El resultado de {numero_a} - {numero_b} es {calcular_resta(numero_a, numero_b)}")
        case 'C':
            print(f"El resultado de {numero_a} x {numero_b} es {calcular_multiplicacion(numero_a, numero_b)}")
        case 'D':
            print(f"El resultado de {numero_a} / {numero_b} es {calcular_division(numero_a, numero_b)}")
        case 'E':
            print(f"El factorial de {numero_a} es {calcular_factorial(numero_a)} y el factorial de {numero_b} es {calcular_factorial(numero_b)}")
        case _:
            print("La opcion seleccionada es invalida")
            

def realizar_operaciones (numero_a:int, numero_b:int, operacion:str) -> None:
    """realiza una operacion matematica entre dos numeros

    Args:
        numero_a (int): primer numero
        numero_b (int): segundo numero
        operacion (str): letra que indica que operacion se desea realizar
    """
    match operacion:
        case 'A':
            calcular_suma(numero_a, numero_b)
        case 'B':
            calcular_resta(numero_a, numero_b)
        case 'C':
            calcular_multiplicacion(numero_a, numero_b)
        case 'D':
            calcular_division(numero_a, numero_b)
        case 'E':
            calcular_factorial(numero_a)
            calcular_factorial(numero_b)
        case _:
            print("La opcion seleccionada es invalida")
            
