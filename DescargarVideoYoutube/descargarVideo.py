#Importo las librerias necesarias
from pytube import YouTube
from pytube import Playlist
 
#Imprimo el incio del código
print("Ejecutando")

#Guardo en una variable el enlace del video de youtube que deseo descargar
enlaceVideo = 'https://www.youtube.com/watch?v=x-lRA6MvB44&ab_channel=FlowHot.NetLaPaginaMasRankia%21'

#Procedo con la descarga del video
yt = YouTube(enlaceVideo).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

#Imprimo la finalización del código
print("Video Descargado")
