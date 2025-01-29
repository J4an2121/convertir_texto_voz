from gtts import gTTS  # Importa la clase gTTS de la librería gtts

def main():
    # Pide al usuario que ingrese el texto que desea convertir a voz
    text = input('Por favor, ingresa el texto que deseas convertir a voz: ')
    
    # Crea un objeto gTTS con el texto y el idioma especificado (español)
    tts = gTTS(text, lang='es')
    
    # Guarda el archivo de audio como 'output.mp3'
    tts.save('output.mp3')
    
    # Muestra un mensaje indicando que el archivo se ha guardado
    print('Archivo de voz guardado como output.mp3')

if __name__ == '__main__': # Llama a la función principal si el script se ejecuta directamente
    main()  