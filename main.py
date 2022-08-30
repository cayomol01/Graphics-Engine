"""
Hecho por Jose Pablo Mozon 20309
Basa
"""
from gl import Window
from object_literally import Texture

height = 480
width = 270

window = Window(height, width,("white"),("white"))

window.background = Texture("assets/windows.bmp")
window.clear_background()

window.active_texture = Texture("assets/pumpkin.bmp")
window.active_shader = window.shaders["gourad"]
window.loadObject("assets/pumpkin.obj",translate=(width-95, height/6, -140), rotate=(-10,190   ,0),scale=(75,75,75))

window.active_texture = Texture("assets/ash.bmp")
window.active_shader = window.shaders["negative"]
window.loadObject("assets/carro.obj",translate=(width+50, height/12-10, -100), rotate=(-5,240,0),scale=(8, 8, 8))

window.active_texture = Texture("assets/church.bmp")
window.active_shader = window.shaders["dissolvefade"]
window.loadObject("assets/objDome.obj",translate=(width+120, height/6, 0), rotate=(-7,175,-1),scale=(150,150,150))

window.active_texture = Texture("assets/school.bmp")
window.active_shader = window.shaders["duality"]
window.loadObject("assets/objBuilding.obj",translate=(60, height/6, 0), rotate=(0,150,0),scale=(30,30,30))

window.activetexture = Texture("assets/human.bmp")
window.active_shader = window.shaders["pride"]
window.loadObject("assets/hair femele 1.obj",translate=(width-50, height/6, 0), rotate=(-1,200,0),scale=(1,1,1))

window.finish("finalrender")

exit()
