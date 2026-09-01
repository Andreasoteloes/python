# --------------------------------------------------------------------------------------------------------------------------------------
# 1. CREACIÓN BÁSICA DE DICCIONARIOS
# --------------------------------------------------------------------------------------------------------------------------------------
# Creamos un diccionario relacionando los cuartos de la casa (texto) con su temperatura (número).
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

# Creamos otro diccionario relacionando áreas externas con su número de cámaras.
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Mostramos en pantalla el contenido de los dos diccionarios anteriores.
print(sensors)
print(num_cameras)

# Creamos un diccionario que funciona como traductor (relaciona texto con texto).
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations)

# -------------------------------------------------------------------------------------------------------------------------------------
# 2. EL ERROR DE USAR LISTAS COMO LLAVES
# -------------------------------------------------------------------------------------------------------------------------------------

# Verificando un error:
# Las listas (los números entre corchetes []) no pueden ser las "claves" del diccionario porque se pueden modificar. 
# Si le quito el numeral a la línea de abajo el programa marcará un error.
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}

# Sin embargo las listas si pueden ser los "valores" que se guardan adentro.
# Relacionamos un apellido (clave) con una lista de nombres (valor).
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

# Creamos un diccionario totalmente vacío, para prepararlo y llenarlo más adelante.
my_empty_dictionary = {}
print(my_empty_dictionary)

# ------------------------------------------------------------------------------------------------------------------------------------
# 3. AGREGAR Y SOBRESCRIBIR DATOS
# ------------------------------------------------------------------------------------------------------------------------------------

# Creamos un menú inicial con productos y sus precios.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)

# Para AGREGAR un dato nuevo: nombramos el diccionario creamos la clave en corchetes y le asignamos un valor.
menu["cheesecake"] = 8
print("After", menu)

# ERROR COMÚN:
# Si uso el signo igual (=) con llaves {} repetidas veces, no se están agregando animales. 
# Se está borrando el diccionario entero y creando uno nuevo cada vez. Al final solo quedan los caballos.
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)

# Agregar múltiples claves a la vez:
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

# La función .update() nos permite meter varios pares de datos al mismo tiempo sin hacerlo uno por uno.
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

# Otro ejemplo usando .update() con IDs de usuarios:
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# SOBRESCRIBIR VALORES:
# En un diccionario no se pueden repetir claves, si a una clave que ya existe le asigno un valor nuevo, el viejo se borra.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)

# "oatmeal" existía y costaba 3. Aquí le cambiamos el valor a 5.
menu["oatmeal"] = 5
print("After", menu)

# Ejemplo con premios Oscar:
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)

# Agregamos una categoría nueva con .update().
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After 1", oscar_winners)

# Sobrescribimos el valor de "Best Picture", corrigiendo el error de la ganadora.
oscar_winners["Best Picture"] = "Moonlight"
print("After 2", oscar_winners)

# -------------------------------------------------------------------------------------------------------------------------------------------
# 4. COMPRENSIÓN DE DICCIONARIOS (Unir listas)
# -------------------------------------------------------------------------------------------------------------------------------------------

# Digamos que tenemos dos listas separadas y queremos combinarlas en un solo diccionario.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# zip() funciona como el cierre de una chaqueta: junta el elemento 1 de la primera lista con el elemento 1 de la segunda.
# La instrucción "for" recorre esos pares, nombrando al primero "key" (clave) y al segundo "value" (valor), guardándolos en "students".
students = {key:value for key, value in zip(names, heights)}
print(students)

# Hacemos lo mismo con una lista de canciones y una lista de cuántas veces se reprodujeron.
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Unimos las dos listas creando el diccionario "plays".
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)

# Agregamos una canción totalmente nueva al diccionario.
plays.update({"Purple Haze": 1})

# Sobrescribimos el valor de "Respect", actualizando sus reproducciones a 94.
plays.update({"Respect": 94})
print("After: ", plays)

# DICCIONARIOS ANIDADOS:
# Se puede guardar un diccionario entero dentro de otro diccionario.
# La llave "The Best Songs" guarda el diccionario "plays". La llave "Sunday Feelings" guarda un diccionario vacío.
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)



