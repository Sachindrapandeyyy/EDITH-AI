import subprocess
import pygame
import io
import sounddevice
def speak(text):
    voice = "en-US-MichelleNeural" 
    command = f'edge-tts -v "{voice}" -t "{text}" --rate=+30%'

    try:
        audio_data = subprocess.check_output(command, shell=True)

       
        pygame.init()
        pygame.mixer.init()

        audio_buffer = io.BytesIO(audio_data)

        pygame.mixer.music.load(audio_buffer)

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
  
    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()



