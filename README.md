# Graphic Engine 
A graphical engine made by **Jose Pablo Monzon**. Made for the class *CC2018 Computer graphics*.
Para ejecutar el programa, se debe ejecutar el archivo **main.py**.

### Final Render
![imagen](https://user-images.githubusercontent.com/64183934/187344672-886e6dff-bbd0-4a18-a750-31d075679dc8.png)

Los modelos con shaders por separado:
### carro.obj / smooth-shading
Un carro con una version del gourad con un shading mas estilo caricatura
![imagen](https://user-images.githubusercontent.com/64183934/187341963-2c67dd4a-d578-4597-98ff-51f737f66df6.png)

### pumpkin.obj / negative
Una calabaza con filtro negativo
![imagen](https://user-images.githubusercontent.com/64183934/187342676-0249c352-e7cf-4c0d-bf0b-81bb92f88b58.png)

### hair-female / rainbow
Un cuerpo de mujer con heatmap arcoiris
![imagen](https://user-images.githubusercontent.com/64183934/187343132-a0422e13-f649-4284-a1df-14341d6bbe52.png)

### objBuilding / duality
Una iglesia con la mitad blanca mitad negra, como el ying yang
![imagen](https://user-images.githubusercontent.com/64183934/187343500-5eefa1ce-0f41-4583-a284-b1a9f71e0752.png)

### objDome / dissolvefade
Un domo que se disuelve hacia su sombra
![imagen](https://user-images.githubusercontent.com/64183934/187343952-692cd0ef-2cec-40fc-a406-f24356af2ee5.png)

## What is it?
* **No**, it is not a game engine.
* **No**, it is not a chat bot.
* **No**, it is not a calculator.
* **No**, it is not a meme generator.
* **Yes**, it is a graphic engine.
* **Yes**, it is BETTER than any other engine.

## How to use it?
Add `gl.py` to your project, next import the engine in your code:
```python
from gl import Window
```
To initialize the engine, you create a new `Window` object (There is no need to call the `init` function):
```python
window = Window(width=800, height=600)
```
## Features
Has the following features: *(From newest to oldest)*
## Ej.5 - Transformations
- [x] Model
- [x] View
- [x] Projection
- [x] Viewport
- [x] Awful Camera
## Ej.4 - Shaders and textures
- [x] Accepts textures 
- [x] Renders vertices with shaders
- [x] Flat Shader
## Ej.3 - 3d Objects **DONE**
- [x] Its able to handle an `.obj` file.
- [x] Provides an .obj file.
- [x] Each polygon has a random color.
## Ej.2 - Lines **DONE**
- [x] Function that draws a line.
- [x] That function is able to draw 5 different shapes.
## Ej.1 - Points **DONE**
- [x] Init function
- [x] Generate the framebuffer
- [x] Define a viewport
- [x] Clear the framebuffer
- [x] Change the color of the framebuffer
- [x] Add a point to the framebuffer
- [x] Change the color of a point
- [x] Render the image as a `.bmp` file
