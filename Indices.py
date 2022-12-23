# The webbrowser.open() function is used to open and display a website in your default browser.
import webbrowser
# The OS module in Python provides functions for interacting with the operating system.
import os

# Create index for movies
INDICE_PELICULAS = [{'id': 1, 'name': 'Top Gun', 'categoria': 'Acción', 'anio': 2022, 'duration': '2h 00m', 'url': 'https://www.youtube.com/watch?v=zzBIzYmxatU'}, 
                {'id': 2, 'name': 'Scary Movie', 'categoria': 'Comedia', 'anio': 2000, 'duration': '1h 28m', 'url': 'https://www.youtube.com/watch?v=3iy0pE1FBkc'},
                {'id': 3, 'name': 'El conjuro 3', 'categoria': 'Terror', 'anio': 2022, 'duration': '1h 52m', 'url': 'https://www.youtube.com/watch?v=S8nlMJfE6pc&ab_channel=WarnerBros.PicturesLatinoam%C3%A9rica'},
                {'id': 4, 'name': 'Jurassic World', 'categoria': 'Acción', 'anio': 2022, 'duration': '2h 27m', 'url': 'https://www.youtube.com/watch?v=0Jz_jD1yF0o'},
                {'id': 5, 'name': 'Turno de dia', 'categoria': 'Acción', 'anio': 2022, 'duration': '1h 54m', 'url': 'https://www.youtube.com/watch?v=naXhVe0LC5I'},
                {'id': 6, 'name': 'Spiderman-Lejos de casa', 'categoria': 'Acción', 'anio': 2019, 'duration': '2h 09m', 'url': 'https://www.youtube.com/watch?v=e8In2bTmJy0'},
                {'id': 7, 'name': 'Rapidos y Furiosos 9', 'categoria': 'Acción', 'anio': 2021, 'duration': '2h 23m', 'url': 'https://www.youtube.com/watch?v=HKs6n4GGKdw'},
                {'id': 8, 'name': 'The Black Phone', 'categoria': 'Terror', 'anio': 2021, 'duration': '1h 42m', 'url': 'https://www.youtube.com/watch?v=kQ3EMxTAwXY'},
                {'id': 9, 'name': 'Jack en la caja maldita', 'categoria': 'Terror', 'anio': 2019, 'duration': '1h 27m', 'url': 'https://www.youtube.com/watch?v=te9Tep56PhY'},
                {'id': 10, 'name': 'Resident Evil: capítulo final', 'categoria': 'Terror', 'anio': 2017, 'duration': '1h 46m', 'url': 'https://www.youtube.com/watch?v=iJaVlgoYECw&ab_channel=SonyPicturesM%C3%A9xico'},
                {'id': 11, 'name': 'Scream 5', 'categoria': 'Comedia', 'anio': 2022, 'duration': '1h 54m', 'url': 'https://www.youtube.com/watch?v=vXu42I7_yk0&ab_channel=PARAMOUNTPICTURESM%C3%89XICO'},
                {'id': 12, 'name': 'Dog. Un Viaje Salvaje', 'categoria': 'Comedia', 'anio': 2022, 'duration': '1h 41m', 'url': 'https://www.youtube.com/watch?v=LJcVhteNnSY'},
                {'id': 13, 'name': 'Super cool', 'categoria': 'Comedia', 'anio': 2007, 'duration': '1h 59m', 'url': 'https://www.youtube.com/watch?v=au2Zq8D9RaY'},
                {'id': 14, 'name': 'Minions: nace un villano', 'categoria': 'Comedia', 'anio': 2022, 'duration': '1h 27m', 'url': 'https://www.youtube.com/watch?v=W27moupirnI&ab_channel=universalpicturesmx'},
                {'id': 15, 'name': 'Pasante de moda', 'categoria': 'Comedia', 'anio': 2015, 'duration': '2h 1m', 'url': 'https://www.youtube.com/watch?v=SSUjmrFt69g&ab_channel=WarnerBros.PicturesLatinoam%C3%A9rica'}]

# Print the categories of the movies
def imprimir_categoria(tipo_categoria):
    cat = []
    
    if tipo_categoria == 'Todas':
        for categoria in INDICE_PELICULAS:
            if categoria['categoria'] not in cat:
                cat.append(categoria['categoria'])
                print (categoria['categoria'])
        print ('')

# Open the url for the movies
def abrir_url(url):
    webbrowser.open(url, new=2, autoraise=True)

# Print data of the movie and call to function abrir_url()
def datos_pelicula(indice, tipo_categoria):
    for idx in INDICE_PELICULAS:
        if idx['id'] == indice and idx['categoria'] == tipo_categoria:
            print('===========  DATOS DE LA PELICULA  ===========')
            print('NOMBRE: ' + idx['name'])
            print('AÑO: ' + str(idx['anio']))
            print('DURACION: ' + idx['duration'])
            print('TRAILER: ' + idx['url'])

            print('=========  ¿Quiere abrir el trailer?  =========')
            print('1. Si')
            print('2. No')
            response = int(input('Escribe la opcion deseada: '))

            if response == 1:
                abrir_url(idx['url'])
    print ('')

# Print categories
def imprimir_peliculas(tipo_categoria):
    for categoria in INDICE_PELICULAS:
        if categoria['categoria'] == tipo_categoria:
            print (str(categoria['id']) + '. ' + categoria['name'])
    print ('')
    ind = int(input('Escoge una pelicula: '))
    datos_pelicula(ind, tipo_categoria)

# Main the program
def __main__():
    os.system('cls')
    option = None

    print('PELIS+ ....')
    print('Este programa enseña el uso de indices dentro de la arquitectura web.\n')

    # Main menu
    while option != 3:
        try:
            print('===========  BUSQUEDA  ===========')
            print('1. Todas las categorias')
            print('2. Categoria especifica')
            print('3. Salir')
            option = int(input('Escribe la opcion que deseas: '))
            if option == 1:
                imprimir_categoria('Todas')
            if option == 2:
                pelicula = input('Escribe la categoria a buscar: ')
                imprimir_peliculas(pelicula)
        except Exception as e:
            print(f'Ocurrio un error vuelva a intentar: {e}')
            option = None
    
    print('Salir...')

__main__()