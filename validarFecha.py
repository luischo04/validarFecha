from datetime import datetime

try:
    fecha = input('Ingresa una fecha (dd/MM/yyyy):')
    formato = '%d/%m/%Y'
    conversion = datetime.strptime(fecha, formato)
    if conversion:
        print(f'La fecha {fecha}, tiene un formato correcto')
    else:
        print(f'La fecha {fecha}, tiene un formato incorrecto')
except ValueError:
    print('Ha ocurrido un error con la fecha ingresa, verifica que sea valida')