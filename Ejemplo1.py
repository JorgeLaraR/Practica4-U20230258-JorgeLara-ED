from string import printable


persona = {
    'nombres' : 'Josue Isai',
    'apellidos' : 'Herrera Benitez'
}

print(persona.get('nombres'))
print(persona['apellidos'])

claves = ('nota1', 'nota2', 'nota3')
notas = dict.fromkeys(claves) #diccionario

#print(notas.get['nota4'])
#print(notas['nota4'])

#print(persona.items())
print(persona.values())
print(persona.keys())

#borrar el apellido del diccionario personas
persona.pop('apellido')
print(persona)
persona.popitem()
print(persona)

#agregar nuevos elementos o actualizar si existe
persona.setdefault('edad', 23)
print(persona)

persona.update(nombres = 'Marcos Alexis')
print(persona)

print('Total elementos {0}'.format(len(persona)))

del persona['edad']