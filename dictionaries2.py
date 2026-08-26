# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. OBTENER EL VALOR DE UNA LLAVE (ACCESO DIRECTO)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Creamos un diccionario con nombres de edificios (llave) y sus alturas en metros (valor).
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Para acceder al valor, escribimos el nombre del diccionario y ponemos la llave entre corchetes [].
print(building_heights["Burj Khalifa"]) # Imprime 828
print(building_heights["Ping An"])      # Imprime 599

# También podemos guardar listas enteras como valores. 
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# Al pedir la llave "earth" (tierra), el diccionario nos devuelve la lista completa de esos signos.
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. EL PROBLEMA DE LAS LLAVES INEXISTENTES Y CÓMO EVITARLO
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Si intentamos buscar una llave que NO existe usando corchetes (como "Landmark 81"),
# el programa generará un ERROR y detendrá su ejecución por completo. 
# print(building_heights["Landmark 81"]) # (Mantenemos esta línea con numeral para que no arruine tu programa)

# Una forma lógica de evitar el error es PREGUNTAR primero si la llave existe en el diccionario.
key_to_check = "Landmark 81"

# La palabra clave 'in' (en) verifica la existencia. 
# Si es verdad (True), entra e imprime; si es falso (False), simplemente lo ignora y evita el error.
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

# Para probar que sí funciona, agregamos una llave nueva ("energy") al diccionario del zodiaco.
zodiac_elements["energy"] = "Not a Zodiac element"

# Como ahora sí existe, la condición se cumple y nos imprime su valor.
if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. OBTENER UNA LLAVE DE FORMA SEGURA: El método .get()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Existe una herramienta más profesional que los corchetes: el método .get() (obtener).
# Si la llave existe, te da el valor. Si NO existe, no genera error, sino que te devuelve 'None' (Nada/Nulo).

building_heights.get("Shanghai Tower") # Esta línea internamente devuelve 632.
building_heights.get("My House")       # Esta línea internamente devuelve 'None', manteniendo el programa a salvo.

# Aplicación práctica con IDs de usuarios:
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Verificamos si 'teraCoder' existe. Si el resultado es 'None', le asignamos un ID por defecto (1000).
if user_ids.get("teraCoder") == None:
   tc_id = 1000
# Si no es 'None' (es decir, sí se encontró), guardamos su valor real.
else: 
   tc_id = user_ids.get("teraCoder")

print(tc_id)

# Otro ejemplo: Buscamos un usuario falso ("superStackSmash").
# Como da 'None', la condición se cumple y le asignamos un valor de seguridad (100000).
if user_ids.get("superStackSmash") == None:
     stack_id = 100000

print(stack_id)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. EXTRAER Y BORRAR UN DATO: El método .pop()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# El método .pop() extrae un elemento: te entrega su valor para que lo uses, pero lo BORRA del diccionario.
# Si le pasas un segundo dato después de la coma, ese será su "salvavidas" (valor por defecto) por si no encuentra la llave.
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

# Saca el boleto 320291 y nos entrega "Gift Basket". Al mismo tiempo, lo elimina de la rifa.
print(raffle.pop(320291, "No Prize"))
print(raffle) # Al imprimir, notamos que "Gift Basket" ya desapareció.

# Intentamos sacar un boleto que no existe (100000). Como no está, nos devuelve el salvavidas "No Prize".
print(raffle.pop(100000, "No Prize"))
print(raffle)

# Extraemos otro boleto existente y el diccionario se reduce aún más.
print(raffle.pop(872921, "No Prize"))
print(raffle)

# Ejemplo de uso acumulando puntos en un juego:
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# El operador += significa "súmale esto a lo que ya tengo". 
# Usamos .pop() para consumir los ítems (se borran del inventario) y sumar su valor a la vida.
# Si el ítem no existe (como "mystic bread"), el salvavidas es 0, por lo que no suma nada.
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items) # Los ítems consumidos ya no están.
print(health_points)   # La vida subió a 65.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. OBTENER TODAS LAS LLAVES: El método .keys()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# Si usamos list() para convertir el diccionario, por defecto obtenemos una lista solo con las llaves (nombres).
print(list(test_scores))

# La forma más académica de hacerlo es usando .keys() junto a un ciclo "for" (para cada).
# Esto recorre la estructura y extrae nombre por nombre.
for student in test_scores.keys():
 print(student)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Podemos guardar todas las llaves extraídas en variables nuevas para usarlas después.
users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. OBTENER TODOS LOS VALORES: El método .values()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A la inversa, .values() ignora las llaves y nos entrega únicamente los datos almacenados.
for score_list in test_scores.values():
 print(score_list) # Imprime las calificaciones puras, sin los nombres de los alumnos.

# Ejemplo sumando el total de ejercicios:
total_exercises = 0

for exercises in num_exercises.values():
  # En cada repetición del ciclo, extrae el número de ejercicios de un tema y lo va acumulando.
  total_exercises += exercises

print(total_exercises)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7. OBTENER TODO JUNTO (LLAVE Y VALOR): El método .items()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

# .items() extrae el par completo. Por eso necesitamos dos variables en el ciclo (company y value).
for company, value in biggest_brands.items():
 # Usamos str(value) para convertir el número a texto y así poder encadenarlo (+) en una oración legible.
 print(company + " has a value of " + str(value) + " billion dollars. ")

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# En cada vuelta, 'occupation' guarda la profesión y 'percentage' guarda la estadística numérica.
for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
