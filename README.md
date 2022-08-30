# Graphic Engine 
A graphical engine made by **Jose Pablo Monzon**. Made for the class *CC2018 Computer graphics*.
Para ejecutar el programa, se debe ejecutar el archivo **main.py**.

### Rainbow Heatmap
![imagen](https://user-images.githubusercontent.com/64183934/185731998-7d91a1c5-808d-46fe-bf9f-b3bce4d44efe.png)

### Negative
![imagen](https://user-images.githubusercontent.com/64183934/185732004-924deb85-d1ac-42cc-9f34-75579a36a194.png)

### Duality
![imagen](https://user-images.githubusercontent.com/64183934/185732009-5809b837-42aa-4584-91da-69eb60bacd6a.png)

### DissolveFade
![imagen](https://user-images.githubusercontent.com/64183934/185732016-f66215a0-f54f-4276-bd4d-7d07fd2f474e.png)

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
