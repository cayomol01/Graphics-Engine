"""
Hecho por Jose Pablo Mozon 20309
"""

from gl import Window
#import time
import random
#start_time = time.time()

window = Window(400,400,("black"))

window.square(0,1,100,("red"))

window.triangle(0,102,100,("blue"))

window.rectangle(102,1,100,200,("green"))

window.triangle_90(102,202,100,("yellow"))

window.nepal(204,1,100,("dark-blue"))

window.hexagon(204,150,100,("purple"))
    
window.finish("Memes")

#print("--- %s seconds ---" % (time.time() - start_time))

exit()

