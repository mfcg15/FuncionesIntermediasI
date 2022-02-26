#1.Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def cambiarX(arr, valorBuscar, valorCambiar):
    for sub_lista in arr:
        for indice, elemento in enumerate(sub_lista):
            if elemento == valorBuscar:
                sub_lista[indice] = valorCambiar
    return arr
print(cambiarX(x,10,15))

def cambiarEstudiantes(arrDiccionary,valorBuscar,valorCambiar):
    for diccionario in arrDiccionary:
        for key, value in diccionario.items():
            if(value==valorBuscar):
                diccionario[key] = valorCambiar
    return arrDiccionary
print(cambiarEstudiantes(estudiantes,"Jordan","Bryant"))

def cambiarDirectorioDeportes(diccionario,valorBuscar,valorcambiar):
    for key, value in diccionario.items():
        for i in value:
            if(i==valorBuscar):
                diccionario[str(key)][value.index(i)] = valorcambiar
    return diccionario
print(cambiarDirectorioDeportes(directorio_deportes,"Messi","Andres"))

def cambiarZ(arrDiccionary,valorBuscar,valorCambiar):
    for diccionario in arrDiccionary:
        for key, value in diccionario.items():
            if(value==valorBuscar):
                diccionario[key] = valorCambiar
    return arrDiccionary
print(cambiarZ(z,20,30))
print("\n")

#2.Iterar a través de una lista de diccionarios

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(diccionario):
    respuesta = ""
    for i in range(0, len(diccionario)):
        for key,value in diccionario[i].items():
           respuesta += key+"-"+value+ "," 
        respuesta += "\n"
    print(respuesta)

iterateDictionary(estudiantes)

#3.Obtener valores de una lista de diccionarios

def iterateDictionary2(nombreKey,diccionario):
    for i in range(0, len(diccionario)):
        for key,value in diccionario[i].items():
            if(key==nombreKey):
                print(value)

iterateDictionary2('first_name', estudiantes)
print("\n")
iterateDictionary2('last_name', estudiantes)

#4.Iterar a través de un diccionarios con valores de lista
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(diccionario):
    for key,value in diccionario.items():
        print("\n")
        print(len(value),key.upper())
        for i in range(0, len(value)):
            print(value[i])

printInfo(dojo)