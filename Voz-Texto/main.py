import speech_recognition as sr
from playsound import playsound
def operaciones():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        audio = r.listen(source)
        
        
        try:
            text = r.recognize_google(audio, language='es-ES')
            print("Quisiste decir: {}".format(text))
           
            if format(text).lower() == "activar el modo vigilancia":
                playsound("audios/ModoVigilancia.mp3")
                with sr.Microphone() as source:
                    import dm
        except:
            playsound("audios/finalizado.mp3")

print("------------------------")
print("--- Menú de opciones ---")
print("------------------------")
print("\nOpción 1. Activar el modo vigilancia")
playsound("audios/bienvenida.mp3")
operaciones()

