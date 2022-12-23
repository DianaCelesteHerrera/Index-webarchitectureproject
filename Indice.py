#Proyecto Indices arquitectura web
import os
#from urllib.request import urlopen
import webbrowser #https://python-para-impacientes.blogspot.com/2015/11/abrir-paginas-web-en-un-navegador-con.html

print('PELIS+....')
print('Este programa enseña el uso de indices dentro de la arquitectura web')

#listas
INDICE =  [['Top Gun','Acción'],['Jurassic World','Acción'],['Turno de dia','Acción'],['Spiderman-Lejos de casa','Acción'],['Rapidos y Furiosos 9','Acción'],
           ['The Black Phone','Terror'],['Jack en la caja maldita','Terror'],['El conjuro 3','Terror'],['Resident Evil: capítulo final','Terror'],['Scream 5','Terror'],
           ['Dog. Un Viaje Salvaje','Comedia'],['Scary Movie','Comedia'],['Super cool','Comedia'],['Minions: nace un villano','Comedia'],['Pasante de moda','Comedia']]

PELICULAS = [['Top Gun'                ,2022,'2h 00m','descripcion','https://www.youtube.com/watch?v=zzBIzYmxatU'],
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

opcion =  None

#abrir el video 
def URL(url_y):
    webbrowser.open(url_y, new=2, autoraise=True)
 
def datos_Pelicula(num):
    print('===========DATOS DE LA PELICULA===========')
    print('NOMBRE:',PELICULAS[num][0])
    print('AÑO:',PELICULAS[num][1])
    print('DURACION:',PELICULAS[num][2])
    print('DESCRIPCION',PELICULAS[num][3])
    print('UBICACION:',PELICULAS[num][4])
    
    print('=========¿Quiere abrir el video?=========')
    print('1) Si')
    print('2) No')
    respuesta = int(input('Escribe la opcion que deseas: '))

    if respuesta == 1:
        URL(PELICULAS[num][4])

def imprimir_Categoria(tipo):
    print('\nCategoria:',tipo)
    for x in range(len(INDICE)):
        if INDICE[x][1] is tipo:
            print('INDICE',x,' ',INDICE[x][0])
        elif tipo == 'Todas':
            print('INDICE',x,' ',INDICE[x][0])
            
    ind = int(input('Escribe un indice: '))
    datos_Pelicula(ind)

#Menu de categoerias peliculas
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
    
#Menu principal peliculas
while opcion != 3:
    try:
        print(' ')
        print('===========BUSQUEDA===========')
        print('1) Todas las categorias')
        print('2) Categoria especifica')
        print('3) Salir')
        opcion = int(input('Escribe la opcion que deseas: '))
        if opcion == 1:
           imprimir_Categoria('Peliculas')
        if opcion == 2:
            menu_Categoria()  
    except Exception as e:
        print(f'Ocurrio un error vuelva a intentar {e}')
        opcion = None
else:
    print('Salir...')


if __name__ == '__main__':
    os.system('cls') #para eliminar