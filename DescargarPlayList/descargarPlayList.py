#Instalar pytube (pip install pytube)
from pytube import YouTube
from pytube import Playlist
 
#DESCARGAR PLAYLIST
print("Código en ejecución")
print("Descargar Playlist de Youtube")


enlacePlayList = 'https://www.youtube.com/watch?v=K9mTSekTktw&list=PLxZHtuv5hUL94eMtcOOV0BiZu6a4cRo4J&ab_channel=RauwAlejandro'
p = Playlist(enlacePlayList)

#Saco el título de la PlayList
print(f'Playlist: {p.title}')
#Contador para saber cuantos videos van descargados
contador = 0
#Ciclo for para recorrer toda la PlayList desde Youtube e ir descargando cada uno de los videos
for video in p.videos:
	video.streams.first().download()
	#Aumento el contador
	contador = contador + 1
	#Imprimo una vez finalice de descargar cada video
	print("Videos descargados: " + str(contador))

	