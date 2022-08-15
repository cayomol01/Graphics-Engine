# Graphic Engine 
A graphical engine made by **Jose Pablo Monzon**. Made for the class *CC2018 Computer graphics*.
Para ejecutar el programa, se debe ejecutar el archivo **main.py**.

### Medium Shot
![imagen](https://user-images.githubusercontent.com/64183934/184618193-87977114-96eb-4296-bcd0-7462c78d8e51.png)

### Low Angle Shot
![imagen](https://user-images.githubusercontent.com/64183934/184618242-6bcd364c-2288-432e-99d8-75c608c7b25d.png)

### High Angle Shot
![imagen](https://user-images.githubusercontent.com/64183934/184618219-5a849df2-7259-4299-88af-b1177242b954.png)

### Dutch Angle Shot
![imagen](https://user-images.githubusercontent.com/64183934/184618269-6abac54c-f6d8-48b0-8589-80291c15359f.png)

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
