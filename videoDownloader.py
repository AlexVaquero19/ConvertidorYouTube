from pytube import YouTube
from pytube import Playlist

#Función que descarga los Vídeos de Youtube
def lista():
    print("Introduce el Enalce de tu Playlist:")
    lista = str(input(">> "))

    #Creamos el Objeto Playlist
    yt = Playlist(lista)
    destination = "./Videos"
    
    #Recorremos lo que contiene Playlist y cogemos las URL de los Vídeos
    #De toda la Playlist
    for video_url in yt.video_urls:
        videos = YouTube(video_url)

        video = videos.streams.get_highest_resolution()
        video.download(destination)
        print("Descarga Completada con Exito")

def video():
    print("Introduce el Enalce de YouTube: ")
    video = str(input(">> "))

    #Creamos el Objetos YouTube
    yt = YouTube(video)
    destination = "./Videos"

    #Descarga el Vídeo del Enlace pedido por Teclado
    stream = yt.streams.get_highest_resolution()
    stream.download(destination)

#Opciones
print("¿Que quieres hacer?")
print("1 => Descargar una Playlist de Youtube")
print("2 => Descargar un Video de Youtube")
opcion = str(input("Opcion >> "))

if int(opcion) == 1:
    lista()
elif int(opcion) == 2:
    video()
else:
    print("Escoge una Opción Válida")