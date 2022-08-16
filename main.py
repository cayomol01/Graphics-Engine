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

window.loadObject("carro.obj",translate=(width-50, height/6, 0), rotate=(0,200,0),scale=(20, 20, 20)) # Medium Shot
window.finish("Meme Medium Shot")

#window.clear()
#window.loadObject("carro.obj",translate=(width-50, height/6, 0), rotate=(-20,180,0),scale=(25, 25, 25)) # Low Angle Shot
#window.finish("Meme Low Angle Shot")
#
#window.clear()
#window.loadObject("carro.obj",translate=(width-50, height/6, 0), rotate=(10,180,0),scale=(25, 25, 25)) # High Angle Shot
#window.finish("Meme High Angle Shot")
#
#window.clear()
#window.loadObject("carro.obj",translate=(width-50, height/6, 0), rotate=(0,160,17),scale=(25, 25, 25)) # DUtch Shot
#window.finish("Meme Dutch Shot")
#

#print("--- %s seconds ---" % (time.time() - start_time))

exit()
