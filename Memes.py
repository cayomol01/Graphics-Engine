"""
Hecho por Jose Pablo Mozon 20309
"""

from gl import Window
#import time
import random
#start_time = time.time()

window = Window(1000,500,("black"),("white"))

#window.polygon_fill([(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)],"white")
#window.polygon_fill([(321, 335), (288, 286), (339, 251), (374, 302)],"white")
#window.polygon_fill([(377, 249), (411, 197), (436, 249)],"white")
window.polygon_fill([(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)],"white")
#window.polygon([(682, 175), (708, 120), (735, 148), (739, 170)],"white")
print(window.square(0,0,10,"red"))



#window.finish("Memes")


#print("--- %s seconds ---" % (time.time() - start_time))

exit()

