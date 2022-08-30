"""
Hecho por Jose Pablo Mozon 20309
"""

from gl import Window
from object_literally import Texture
#import time
import random

#start_time = time.time()

height = 960
width = 540

window = Window(height, width,("black"),("white"))


window.active_texture = Texture("assets/ash.bmp")

for x in ["negative","dissolvefade","pride"]:
    window.clear()
    window.active_shader = window.shaders[x]
    window.loadObject("assets/carro.obj",translate=(width-50, height/6, 0), rotate=(-10,190,0),scale=(20, 20, 20))
    window.finish(x)

#window.clear()
#window.active_shader = window.shaders["duality"]
#window.light_direction = (1,0,0)
#window.loadObject("carro.obj",translate=(width-50, height/6, 0), rotate=(0,180,0),scale=(20, 20, 20))
#window.finish("duality")


#print("--- %s seconds ---" % (time.time() - start_time))

exit()
