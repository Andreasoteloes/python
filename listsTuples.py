# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. LISTAS: ESTRUCTURAS MODIFICABLES
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Las listas son colecciones ordenadas de datos. Se escriben entre corchetes [].
# Su característica principal es que SON MUTABLES (se pueden modificar, agregar o quitar elementos).
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

# La función input() pausa el programa esperando que el usuario escriba algo. 
# La dejamos como comentario para que no detenga el código ahora mismo.
# input()

# Imprimimos la lista completa.
print(my_lista)

# type() nos dice qué tipo de dato es la variable. Aquí nos confirmará que es una clase 'list'.
print(type(my_lista))

# Accedemos a un elemento específico usando su índice (posición).
# OJO: En programación, siempre empezamos a contar desde el CERO. El índice [2] es 'Amarillo', no 'Azul'.
print(my_lista[2])

# len() viene de "length" (longitud). Nos dice cuántos elementos totales hay en la lista.
print("my_lista size: ", len(my_lista))

# EXTRAER FRAGMENTOS (Slicing):
# my_lista[0:2] significa "trae desde la posición 0 hasta la 2, PERO sin incluir la 2". (Trae 0 y 1).
print(my_lista[0:2])

# Si omites el primer número, Python asume que empiezas desde el inicio (0). Hace lo mismo que la línea anterior.
print(my_lista[:2])

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. MODIFICAR UNA LISTA (Agregar y Quitar)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# .append() agrega un solo elemento nuevo, siempre al FINAL de la lista.
my_lista.append('Blanco')      
print(my_lista)

# .insert() agrega un elemento en una posición ESPECÍFICA. 
# Aquí mete 'Negro' en la posición 3, empujando a los demás hacia la derecha.
my_lista.insert(3, 'Negro')
print(my_lista)

# .extend() permite fusionar o "pegar" otra lista entera al final de nuestra lista actual.
my_lista.extend(['Marron', 'Gris'])   
print(my_lista)

# .index() busca un elemento por su nombre y nos dice en qué posición (número) está ubicado.
print(my_lista.index('Azul'))

# .remove() busca el elemento por su nombre y lo elimina de la lista. 
# my_lista.remove('Magenta') # Daría ERROR porque 'Magenta' no existe en la lista.
my_lista.remove('Marron')
print(my_lista)

# Volvemos a insertar 'Marron', esta vez en la posición 8.
my_lista.insert(8, 'Marron')
print(my_lista)

# .pop() sin ningún número adentro extrae y borra el ÚLTIMO elemento de la lista (en este caso, 'Gris').
print(my_lista.pop())

# Guardamos el tamaño actual de la lista en una variable llamada 'size'.
size = len(my_lista)
print("size = ", size)
# print(my_lista.pop(size)) # Daría ERROR porque el índice máximo es size-1 (por empezar a contar en cero).

# Multiplicar una lista por un número simplemente repite sus elementos esa cantidad de veces.
my_lista_3 = my_lista * 3
print("my_lista_3: ", my_lista_3)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. ORDENAR UNA LISTA
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Sort:")
print()

# NOTA ACADÉMICA IMPORTANTE: El método .sort() ordena la lista directamente por dentro, pero NO devuelve nada (devuelve None).
# Por eso, al imprimir 'my_listaSort', verás que dice 'None'. 
my_listaSort = my_lista.sort()
print(my_listaSort)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")

# Así es la forma correcta de usar .sort(): Se aplica a la lista sola en una línea.
# Por defecto, ordena de menor a mayor.
my_NumList.sort()
print(my_NumList)

# Si queremos que ordene al revés (de MAYOR a menor), le ponemos 'reverse = True'.
# Nota: En tu código original decía "De menor a mayor", pero reverse=True hace lo contrario (descendente).
my_NumList.sort(reverse = True)
print("De mayor a menor: ", my_NumList)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. TUPLAS: ESTRUCTURAS INMUTABLES
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

print("###########################")
print("############TUPLAS#########")

# Las tuplas son como las listas, pero usan paréntesis ().
# Su diferencia fundamental es que SON INMUTABLES: una vez creadas, no se les puede agregar, quitar ni alterar nada.

# tuple() convierte una lista existente en una tupla fija.
my_tupla = tuple(my_lista)
print("\nmy_tuple: ", my_tupla)

# Podemos acceder a sus datos igual que en una lista, usando los corchetes de posición.
print(my_tupla[0])
print(my_tupla[2])

# 'in' evalúa si un elemento existe dentro de la tupla. Devuelve un valor Booleano (True si está, False si no).
print('Rojo' in my_tupla)

# .count() nos dice cuántas veces se repite exactamente esa palabra adentro.
print(my_tupla.count('Rojo'))

# NOTA ACADÉMICA SOBRE TUPLAS UNITARIAS:
# Para que Python entienda que es una tupla de un solo elemento, DEBES poner una coma al final: ('Blanco',).
# Si solo pones ('Blanco'), Python asume que es un texto normal (String) encerrado en paréntesis.
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria) 

# EMPAQUETADO: Puedes crear una tupla sin usar paréntesis, solo separando los datos con comas.
# Python los agrupa (empaqueta) automáticamente en una tupla.
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

# DESEMPAQUETADO: Es el proceso inverso. Sacamos los datos de la tupla y los repartimos
# ordenadamente en diferentes variables (una variable por cada dato).
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

# Imprimimos todas las variables juntas en una frase legible.
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# list() hace lo contrario que tuple(): Convierte una tupla bloqueada en una lista modificable.
my_lista2 = list(my_tupla)
print(my_lista2)
