"""
Hecho por Jose Pablo Mozon 20309
"""

from gl import Window
#import time
import random
#start_time = time.time()

height = 960
width = 540

window = Window(height, width,("black"),("white"))

window.loadObject("carro.obj",translate=(width-50, height/6, 0), scale=(25, 25, 25))


window.finish("Memes")


#print("--- %s seconds ---" % (time.time() - start_time))

exit()

