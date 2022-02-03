from typing import ContextManager
import speech_recognition as sr
import os  # para crear una carpeta o directorio

#Contar archivos de tipo wav
from os import listdir

from moviepy.editor import *

#se realiza la división del audio y el video.
videoEnlace = input("\nDigite la ruta donde se encuentra el video\nEjemplo: D:\Proyectos\Python\VideoSub\ed.mp4\n")
video = VideoFileClip(videoEnlace.lstrip())
audio = video.audio
name = input('\n¿Qué nombre desea colocarle al audio?\n')


nombreAudio = name + ".wav"
audio.write_audiofile(nombreAudio)



#Recortar un audio en lapsos de 1 minuto
from pydub import AudioSegment
from pydub.utils import make_chunks

## bluesfile 30s
audio = AudioSegment.from_file(nombreAudio, "wav")

size = 60000 ## Los milisegundos de corte

chunks = make_chunks (audio, size) ## Corta el archivo en trozos de 60 segundos

for i, chunk in enumerate(chunks):
         ## Enumeración, i es el índice, chunk es el archivo cortado
         ##llamo a name porque esa variable no tiene el .wav
    chunk_name = name+"{0}.wav".format(i)
    print(chunk_name)
         ## guardar documento
    chunk.export(chunk_name, format="wav")


#contar cuantos archivos hay de tipo "wap"
contarArchivos = 0
for i in listdir("D:\Proyectos\Python\VideoSub"):   
   for x in enumerate(i.split('.', 2)):
       if str(x[1]) == "wav":
           contarArchivos = contarArchivos + 1
    
#se resta 1 porque no se cuenta el archivo de audio separado del video, sino
#los otros divididos por lapsos de 1 minuto
contarArchivos = contarArchivos - 1



#Sacar texto de un audio
r = sr.Recognizer()
texto1 = ""

print("Extrayendo texto de cada audio...")
#depende del número de archivos de tipo "wav" que haya
for i in range(contarArchivos):
    audio_file = sr.AudioFile(name+str(i)+".wav")
    with audio_file as source:
        audio_analizar = r.record(source)
    texto1 =  r.recognize_google(audio_analizar, language='es-US')
    #Creo un archivo de texto
    f = open (name+str(i)+".txt",'w')
    f.write(texto1)
    f.close()
    print("Texto del audio " + str(i) + " finalizado")



print("Fin del programa")

