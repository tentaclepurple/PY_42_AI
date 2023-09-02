from tqdm import tqdm
import time

""" # Simulando un bucle largo
for i in tqdm(range(10)):
    time.sleep(0.5)  # Simulando trabajo """
    

def ft_progress(lst):
    """ Dentro de la función, estamos inicializando algunas variables importantes. 
    total almacena la longitud total de la lista, 
    start_time guarda el momento en que comenzamos el proceso, 
    elapsed_time se utiliza para medir el tiempo transcurrido, 
    progress representa el progreso actual (en forma de fracción) y 
    bar_length establece la longitud total de la barra de progreso en el terminal. """
    total = len(lst)
    start_time = time.time()
    elapsed_time = 0
    progress = 0
    bar_length = 40
    
    for i, elem in enumerate(lst, start=1):
			#enumerate: i es el contador (empieza en 1 por start=1), elem es cada iteracion de lst (el rango listy)
        yield elem
			#devolver el elemento actual (elem) del rango en cada iteración. 
			#El uso de yield convierte automáticamente la función en un generador, 
			#lo que nos permite pausar y reanudar la función sin perder su estado interno.
        progress = i / total
			#Calculamos el progreso actual dividiendo el índice actual (i) 
			#por la longitud total de la lista (total), 
			#lo que nos da un valor entre 0 y 1 representando el porcentaje completado.
        elapsed_time = time.time() - start_time
			#Calculamos el tiempo transcurrido restando el momento en que comenzamos (start_time) al tiempo actual (time.time()).
        eta = (elapsed_time / progress) * (1 - progress) if progress != 0 else 0
			#Calculamos la estimación del tiempo restante (eta) dividiendo el tiempo transcurrido (elapsed_time) 
			#por el progreso actual (progress). Multiplicamos este valor por (1 - progress) 
			#para obtener una estimación más precisa. 
			#Operador ternario. Si el progreso es cero, establecemos eta en cero para evitar una división por cero.
        bar = "[" + "=" * int(progress * bar_length) + ">" + " " * (bar_length - int(progress * bar_length)) + "]"
			#Generamos una representación de la barra de progreso utilizando caracteres. int(progress * bar_length) 
			#nos da el número de caracteres '=' necesarios para representar el progreso actual. 
			#Agregamos un caracter '>' al final de la barra para indicar el punto actual y rellenamos el resto con espacios en blanco.
        print(f"\rETA: {eta:.2f}s [ {(progress * 100):3.0f}%]{bar} {i}/{total} | elapsed time {elapsed_time:.2f}s", end="",)
		#Utilizamos print con formato para mostrar la información de la barra de progreso en una línea. 
		#Utilizamos \r al principio para que la siguiente impresión sobrescriba la línea anterior. 
		#En el formato, usamos placeholders {} para insertar los valores de eta, progress, bar, i, total y elapsed_time.
    
    print("\n")

listy = range(80)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	time.sleep(0.09)
print()
print(ret)



