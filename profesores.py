



import json

archivo = open("publicacion.json")
contenido = json.load(archivo)
profesores = []

def construir():
    for docente in contenido:
        cedula = docente['cedula']
        apellidos = docente['apellidos']
        datos = {
            'cedula': cedula,
            'apellidos': apellidos,
            'publicaciones': 0,
            'tipos': {'CIENTIFICAS':0,'REGIONALES':0},
            'areas': []
        }
        if datos not in profesores:
            profesores.append(datos)
    publicaciones()
    areas()
    tipo_de_publicaciones()
    imprimir()


def publicaciones():
    for docente in profesores:
        cedula = docente['cedula']
        for profesor in contenido:
            if profesor['cedula'] == cedula:
                docente['publicaciones'] += 1


def tipo_de_publicaciones():
    for docente in profesores:
        cedula = docente['cedula']
        tipos = docente['tipos']
        for profesor in contenido:
            if profesor['cedula'] == cedula:
                tipo = profesor['tipobases']
                if tipo == "CIENTIFICAS":
                   tipos['CIENTIFICAS'] += 1
                else:
                    tipos['REGIONALES'] += 1


def areas():
    for docente in profesores:
          cedula = docente['cedula']
          areas_trabajadas = docente['areas']
          for profesor in contenido:
            if profesor['cedula'] == cedula:
                area = profesor['area']
                if not area in areas_trabajadas:
                   areas_trabajadas.append(area);


def imprimir():
    for docente in profesores:
        print(" ")
        print("==========================")
        print(f"Nombre: {docente['apellidos']}")
        print(f"Cedula: {docente['cedula']}")
        print(f"Publicaciones: {docente['publicaciones']}")
        print(" ")
        tipos = docente['tipos']
        print(f"Tipo de articulos publicados:")
        print(f"Cientificos: {tipos['CIENTIFICAS']}")
        print(f"Regionales: {tipos['REGIONALES']}")
        print(" ")
        areas = docente['areas'];
        print('Areas trabajadas:')
        for key in areas:
            print(key)
        print("==========================")
        print(" ")


if __name__ == "__main__":
    construir();



