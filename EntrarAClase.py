#!pip install webbrowser
#!pip install datetime
#!pip install pyautogui
#!pip install pickle

try:
    import webbrowser, datetime, time
    import pyautogui as pag
    import pickle
    
except Exception as e:
    print("\nOcurrió un error:\n")
    print(e)
    input("\nPresiona Enter para salir...")

ahora = datetime.datetime.now()
target_time = None
dia = ahora.day
mes = ahora.month
year = ahora.year
hora = None
minuto = None

coords = {
    "iconoX": 0,
    "iconoY": 0,
    "botonX": 0,
    "botonY": 0,
    "resX": 0,
    "resY": 0
}

zoom_url = input("Ingresa el enlace al que quieras entrar.\n>> ")

def esperar():
        for i in range(10, 0, -1):
            print(i, end="\r")
            time.sleep(1)

def capturar():
    time.sleep(2)
    print("Capturando coordenadas en...")
    esperar()
    pos = pag.position()
    x = pos.x
    y = pos.y
    print("Capturado!")

    return (x, y)
    
def EsperarClase():
    with open("coords.dat", "rb") as archivo:
        coords = pickle.load(archivo)
    
    while True:
        try:
            hora = int(input("Ingresa la hora a la que quieres que se abra el enlace (formato 24 horas).\n>> "))
            if hora <= 0 or hora > 24:
                print("Lo siento, la hora no es válida. (rango de 1 a 24)")
                print("Intenta otra vez.")
                continue
    
            break
    
        except ValueError:
            print("Lo siento, solo se aceptan números, intenta otra vez.")
        
    while True:
        try:
            minuto = int(input("Ingresa los minutos.\n>> "))
            if minuto <= 0 or minuto > 59:
                print("Lo siento, los minutos no es válida. (rango de 0 a 59)")
                print("Intenta otra vez.")
                continue
            
            break
        
        except ValueError:
            print("Lo siento, solo se aceptan números, intenta otra vez.")
    
    target_time = datetime.datetime(year, mes, dia, hora, minuto, 0)

    print(f"Esperando hasta las {target_time.strftime('%H:%M:%S')}...")

    while datetime.datetime.now() < target_time:
        time.sleep(1)

    webbrowser.open(zoom_url)
    
    pag.moveTo(coords["resX"]//2, coords["resY"]//2, duration=1)
    pag.click()
    time.sleep(5)

    pag.moveTo(coords["iconoX"], coords["iconoY"], duration=1)
    pag.click()
    time.sleep(1)
    pag.moveTo(coords["botonX"], coords["botonY"], duration=1)
    pag.click()
    pag.moveTo(coords["resX"]//2, coords["resY"]//2, duration=1)
    pag.hotkey('alt', 'tab')
    time.sleep(2)
    pag.click()
    time.sleep(0.1)
    pag.click()
    


while True:
    opcion = input("Vas a configurar el botón de grabar o esperar a entrar a la clase automáticamente?\n1. Configurar\n2. Entrar\nIngresa el número para elegir\n>> ")
    
    if opcion == "1":
        print("Vamos a configurar el botón de grabar!")
        print("Deja tu puntero puesto en el ícono de el programa que va a grabar en la barra de tareas.")
        capturado = capturar()
        coords["iconoX"] = capturado[0]
        coords["iconoY"] = capturado[1]

        print("Ahora ve a tu programa y deja tu puntero en el botón de grabar. (si es obs tienes primero que configurar la fuente para que el video tenga imagen)")
        capturado = capturar()
        coords["botonX"] = capturado[0]
        coords["botonY"] = capturado[1]
        
        time.sleep(0.5)
        pantalla = pag.size()
        coords["resX"] = pantalla.width
        coords["resY"] = pantalla.height


        with open("coords.dat", "wb") as archivo:
            pickle.dump(coords, archivo)

        print("Configuraciones guardadas!")
        

        
    elif opcion == "2":
        EsperarClase()
        break
        
    else:
        print("Lo siento, opción no válida.")

