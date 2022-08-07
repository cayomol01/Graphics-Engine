"""
Hecho por Jose Pablo Monzon 20309
Basado en el codigo hecho en clase
"""

from struct import pack

from sympy import true


def char(c):
    return pack('=c', c.encode('ascii'))


def word(w):
    return pack('=h', w)


def dword(d):
    return pack('=l', d)


def color(color: str or tuple):
    """
    (255,255,255)
    """
    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "orange": (255, 128, 0),
        "yellow": (255, 255, 0),
        "light-green": (128, 255, 0),
        "green": (0, 255, 0),
        "blue-green": (0, 255, 128),
        "sky-blue": (0, 255, 255),
        "blue": (0, 128, 255),
        "dark-blue": (0, 0, 255),
        "purple": (127, 0, 255),
        "magenta": (255, 0, 255),
        "rose": (255, 0, 127)
    }

    if isinstance(color, str):
        try:
            color = colors[color]
        except KeyError:
            print("Unknown color, using default")
            color = colors["red"]

    r, g, b = color

    if all(isinstance(x, float) for x in (r, g, b)):
        r, g, b = (r*255, g*255, b*255)

    try:
        return bytes([int(b), int(g), int(r)])
    except ValueError:
        print("""!!=-=-=Incorrect color format.=-=-=!! 
    Check you are using the correct notation:
    > Hint: (Min,Mid,Max)
    > "blue" should be a lowercase string
    > (0,127,255) should be a tuple of integers
    > (0.0,0.5,1.0) should be a tuple of floats""")
        raise


class Window:  # * glInit()
    # * glCreateWindow(width, height)
    def __init__(self, width, height, clear_color="red", current_color="black") -> None:
        self.width = width
        self.height = height
        self.clear_color = color(clear_color)  # Default "red"
        self.current_color = color(current_color)  # Default "black"

        self.clear()
        self.setViewPort(0, 0, width, height)

    def clear(self):  # * glClear()
        self.pixels = [
            [self.clear_color for y in range(self.width)] for x in range(self.height)
        ]

    def clearColor(self, color_p: str or tuple):  # *  glClearColor(r, g, b)
        self.clearColor = color(color_p)

    def currentColor(self, color_p: str or tuple):  # * glColor(r, g, b)
        self.current_color = color(color_p)

    def point(self, x, y, color_p: str or tuple = None):  # * glPoint(x, y)
        try:
            self.pixels[y][x] = color(color_p) if color_p else self.current_color
        except IndexError:
            print("Point out of bounds", x, y)
            raise
            
    # VIEW PORT
    def setViewPort(self, x, y, width, height):  # * glViewPort(x, y, width, height)
        self.vp_x = x
        self.vp_y = y
        self.vp_width = width
        self.vp_height = height

    def clearViewPort(self, color_p: str or tuple = None):
        for i in [(m, n) for m in range(self.vp_x, self.vp_x + self.vp_width) for n in range(self.vp_y, self.vp_y + self.vp_height)]:
            self.point([*i], color_p)

    def pointViewPort(self, x, y, color_p: str or tuple = None):  # * glPoint(x, y)
        x = int((self.vp_width/2)*(x+1) + self.vp_x)
        y = int((self.vp_height/2)*(y+1) + self.vp_y)
        self.point(y, x, color_p)
    
    def line(self, x0, y0, x1, y1, color_p: str or tuple = None):
        # Basado en: https://www.uobabylon.edu.iq/eprints/publication_2_22893_6215.pdf
        
        debug = []
        
        self.point(x0, y0, color_p) #Punto inicial
        debug.append((x0,y0))
                    
        dx, dy = abs(x1-x0), abs(y1 - y0) #Calculo de la diferencia de x
   
        x_step = -1 if x0 > x1 else 1 #Indice de a donde tiene que avanzar
        y_step = -1 if y0 > y1 else 1
        
        #Si la diferencia de y es mayor que la de x intercambiamos los valores
        dx, dy, swap = (dy, dx, 1) if dy > dx else (dx,dy,0)
         
        A = 2 * dy 
        B = A - (2 * dx) # 2*(dy - dx)
        Error = A - dx #Error 2*dy - dx

        for _ in range(dx): #Iteramos por la mayor diferencia
            if Error < 0: #Recto
                x0 += x_step * (-swap + 1)
                y0 += y_step * swap
                Error += A
            else: #Diagonal
                x0 += x_step
                y0 += y_step
                Error += B
            self.point(x0, y0, color_p)
            debug.append((x0,y0))
        self.point(x1, y1, color_p)
        debug.append((x1,y1))
        
        return debug
        
        
    def polygon(self, points, color_p: str or tuple = None):
        
        debug = []       
        
        for x,y in zip(points,points[1:] + points[:1]):
            debug += self.line(x[0], x[1], y[0], y[1], color_p)
        
        return debug

    def polygon_fill(self, points, color_p: str or tuple = None):
         
        og_polygon = self.polygon(points, color_p)
                
        x0 = min(points)[0]
        xf = max(points)[0]
        
        for x in range(x0, xf):
            column = [*set([points for points in og_polygon if points[0] == x])]
            column.sort()
            
            lines = []
            for i in column:
                if (i[0],i[1]+1) in column:
                    continue

                if i == (631, 230) or i == (632, 230):
                    continue 
                if i == (580, 230) or i == (581, 230) or i == (616, 215) or i==(596, 216):
                    continue 
            
                if lines == []:
                    lines.append(i)
                    continue
                if i == column[-1]:
                    lines.append(i)
                    continue
                if i in points:
                    continue
                
                lines.append(i)
            lines.reverse()
            if len(lines)==3:
                print(lines)
                #print(lines,column[-1],points)
                #input("aa")
            for i in range(0,len(lines),2):
                try:
                    self.line(lines[i][0], lines[i][1], lines[i+1][0], lines[i+1][1], color_p)
                except IndexError:
                    continue
            #self.finish()
            #input("Press Enter to continue...")
        




    def square(self, x, y, size, color_p: str or tuple = None):
        return self.polygon([(x, y), (x + size, y), (x + size, y + size), (x, y + size)], color_p)
        
    def rectangle(self, x, y, width, height, color_p: str or tuple = None):
        self.polygon([(x, y), (x + width, y), (x + width, y + height), (x, y + height)], color_p)
        
    def triangle(self, x, y, size, color_p: str or tuple = None):
        self.polygon([(x, y), (x + size, y), (x + size//2, y + size)], color_p)
    
    def triangle_90(self, x, y, size, color_p: str or tuple = None):
        self.polygon([(x, y), (x + size, y), (x + size, y + size)], color_p)
        
    def nepal(self, x, y, size, color_p: str or tuple = None): # Al principio era un pentagono, pero termino siendo la bandera de nepal
        self.polygon([(x, y), (x, y+size), (x + size, y +size),(x + size//2, y + size//2),(x + size, y + size//2)], color_p)
        
    def hexagon(self, x, y, size, color_p: str or tuple = None):
        self.polygon([(x,y),(x + size//2, y - size//4),(x + size, y),(x + size, y + size//2),(x + size // 2, y + 3*size//4),(x, y +size//2)], color_p)

    def finish(self, filename="render"):  # * glFinish()
        with open("".join((filename, ".bmp")), "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            #InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            for x in self.pixels:  # Faster
                for y in x:
                    file.write(y)

        #print("Done")
