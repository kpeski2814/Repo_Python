def validar_nombre():
    """ aaaaaa """
    string = False
    while not string:
        try:
            string = input("Ingrese nombre: ")
            if not all(x.isalpha() or x.isspace() for x in string):
                string = ""
                raise ValueError()
        except ValueError:
            print("el nombre no puede contener numeros o signos")
    return string

def validar_dni():
    string = False
    while not string:
        try:
            cadena = input("Ingrese dni: ")
            valor = int(cadena)
            if len(cadena)!= 8:
                raise ValueError("La cadena debe tener exactamente 8 caracteres")
            return valor
        except ValueError as e:
            print(f"Error: {e}")
    return False
    