from os import system,listdir
from cookie.bingimg import ucookie
def generate_image (promt):
    system(  f'python -m BingImageCreator --prompt "{promt}" -U "{ucookie}"'
)

    return listdir('output')
generate_image ('a hosre and a dog')
     
