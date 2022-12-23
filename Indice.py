# programa para peliculas 
import os
#from urllib.request import urlopen
import webbrowser #https://python-para-impacientes.blogspot.com/2015/11/abrir-paginas-web-en-un-navegador-con.html

print('>>>>>>>>>>>>> Peli+ Pagina web peliculas <<<<<<<<<<<<<<<')

#listas
indice =  [['Top Gun','Acción'],['Jurassic World','Acción'],['Turno de dia','Acción'],['Spiderman-Lejos de casa','Acción'],['Rapidos y Furiosos 9','Acción'],
           ['The Black Phone','Terror'],['Jack en la caja maldita','Terror'],['El conjuro 3','Terror'],['Resident Evil: capítulo final','Terror'],['Scream 5','Terror'],
           ['Dog. Un Viaje Salvaje','Comedia'],['Scary Movie','Comedia'],['Super cool','Comedia'],['Minions: nace un villano','Comedia'],['Pasante de moda','Comedia']]

peliculas = [['Top Gun'                ,2022,'2h 00m','descripcion','https://www.youtube.com/watch?v=zzBIzYmxatU'],
             ['Jurassic World'         ,2022,'2h 27m','descripcion','https://www.youtube.com/watch?v=0Jz_jD1yF0o'],
             ['Turno de dia'           ,2022,'1h 54m','descripcion','https://www.youtube.com/watch?v=naXhVe0LC5I'],
             ['Spiderman-Lejos de casa',2019,'2h 09m','descripcion','https://www.youtube.com/watch?v=e8In2bTmJy0'],
             ['Rapidos y Furiosos 9'   ,2021,'2h 23m','descripcion','https://www.youtube.com/watch?v=HKs6n4GGKdw'],
             
             ['The Black Phone'              ,2021,'1h 42m','descripcion','https://www.youtube.com/watch?v=kQ3EMxTAwXY'],
             ['Jack en la caja maldita'      ,2019,'1h 27m','descripcion','https://www.youtube.com/watch?v=te9Tep56PhY'],
             ['El conjuro 3'                 ,2021,'1h 52m','descripcion','https://www.youtube.com/watch?v=S8nlMJfE6pc&ab_channel=WarnerBros.PicturesLatinoam%C3%A9rica'],
             ['Resident Evil: capítulo final',2017,'1h 46m','descripcion','https://www.youtube.com/watch?v=iJaVlgoYECw&ab_channel=SonyPicturesM%C3%A9xico'],
             ['Scream 5'                     ,2022,'1h 54m','descripcion','https://www.youtube.com/watch?v=vXu42I7_yk0&ab_channel=PARAMOUNTPICTURESM%C3%89XICO'],
             
             ['Dog. Un Viaje Salvaje'      ,2022,'1h 41m','descripcion','https://www.youtube.com/watch?v=LJcVhteNnSY'],
             ['Scary Movie'                ,2000,'1h 28m','descripcion','https://www.youtube.com/watch?v=3iy0pE1FBkc'],
             ['Super cool'                 ,2007,'1h 59 m','descripcion','https://www.youtube.com/watch?v=au2Zq8D9RaY'],
             ['Minions: nace un villano'   ,2022,'1h 27m','descripcion','https://www.youtube.com/watch?v=W27moupirnI&ab_channel=universalpicturesmx'],
             ['Pasante de moda'            ,2015,'2h 1m','descripcion','https://www.youtube.com/watch?v=SSUjmrFt69g&ab_channel=WarnerBros.PicturesLatinoam%C3%A9rica']]


#print(indice[0][0])
#opciones para elegir dentro del menu de nuestra pagina
opcion =  None

def URL(url_y):
    webbrowser.open(url_y, new=2, autoraise=True)
    #r = urlopen(url_y)
    # Cerrar para liberar recursos.
    #r.close()


def datos_Pelicula(num):
    print('===========DATOS DE LA PELICULA===========')
    print('NOMBRE:',peliculas[num][0])
    print('AÑO:',peliculas[num][1])
    print('DURACION:',peliculas[num][2])
    print('DESCRIPCION',peliculas[num][3])
    print('UBICACION:',peliculas[num][4])
    
    print('=========¿Quiere abrir el video?=========')
    print('1) Si')
    print('2) No')
    respuesta = int(input('Escribe la opcion que deseas: '))
    if respuesta == 1:
        URL(peliculas[num][4])




def imprimir_Categoria(tipo):
    print('\nPeliculas de ',tipo)
    for x in range(len(indice)):
        if indice[x][1] is tipo:
            print('indice',x,' ',indice[x][0])
        elif tipo == 'Todas':
            print('indice',x,' ',indice[x][0])
            
    ind = int(input('Escribe un indice: '))
    datos_Pelicula(ind)

def menu_Categoria():
    try:
        print(' ')
        print('===========CATEGORIAS===========')
        print('1) Acccion')
        print('2) Terror')
        print('3) Comedia')
        opcion = int(input('Escribe la opcion que deseas: '))
        if opcion == 1:
            imprimir_Categoria('Acción')
        if opcion == 2:
            imprimir_Categoria('Terror')
        if opcion == 3:
            imprimir_Categoria('Comedia')
    except Exception as e:
        print(f'Ocurrio un error vuelva a intentar {e}')
        opcion = None
    


while opcion != 3:

    try:
        print(' ')
        print('===========BUSQUEDA===========')
        print('1) Todas')
        print('2) Categoria')
        print('3) Salir')
        opcion = int(input('Escribe la opcion que deseas: '))
        if opcion == 1:
           imprimir_Categoria('Todas')
        if opcion == 2:
            menu_Categoria()  
    except Exception as e:
        print(f'Ocurrio un error vuelva a intentar {e}')
        opcion = None
      
else:
    print('Salir...')

    
os.system('cls') #para eliminar