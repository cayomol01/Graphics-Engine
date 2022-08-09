"""
Hecho por Jose Pablo Mozon 20309
"""

from gl import Window
from ObjectLiterally import Texture
#import time
import random

#start_time = time.time()

height = 960
width = 540

window = Window(height, width,("black"),("white"))

window.active_shader = window.shaders["flat"]
window.active_texture = Texture("ash.bmp")

window.loadObject("carro.obj",translate=(width-50, height/6, 0), rotate=(-10,2000,0),scale=(25, 25, 25))


window.finish("Memes")


#print("--- %s seconds ---" % (time.time() - start_time))

exit()

