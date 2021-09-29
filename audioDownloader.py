from pytube import YouTube
from pytube import Playlist
import os

#Función que descarga los Vídeos de Youtube en Formato MP3
def lista():
    print("Introduce el Enalce de tu Playlist: ")
    lista = str(input(">> "))

    #Creamos el Objeto Playlist
    yt = Playlist(lista)
    destination = "./Musica"
    
    #Recorremos lo que contiene Playlist y cogemos las URL de los Vídeos
    #De toda la Playlist
    for video_url in yt.video_urls:
        audios = YouTube(video_url)
        audio = audios.streams.filter(only_audio=True).first()
        
        #Cogemos solo el Sonido y ponemos nosotros el .MP3 al Archivo
        out_file = audio.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Descarga Completada con Exito")

def cancion():
    print("Introduce el Enalce de YouTube: ")
    audio = str(input(">> "))
    
    #Creamos el Objetos YouTube
    yt = YouTube(audio)
    destination = "./Musica"
    
    #Descarga el Audio del Enlace pedido por Teclado
    audio = yt.streams.filter(only_audio=True).first()
    out_file = audio.download(output_path=destination)

    #Cogemos solo el Sonido y ponemos nosotros el .MP3 al Archivo
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print("Descarga Completada con Exito")

#Opciones
print("¿Que quieres hacer?")
print("1 => Descargar una Playlist de Youtube")
print("2 => Descargar una Cancion de Youtube")
opcion = str(input("Opcion >> "))

if int(opcion) == 1:
    lista()
elif int(opcion) == 2:
    cancion()
else:
    print("Escoge una Opción Válida")