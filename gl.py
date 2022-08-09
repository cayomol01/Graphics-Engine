"""
Hecho por Jose Pablo Monzon 20309
Basado en el codigo hecho en clase
"""

from random import randint, random
from struct import pack
from ObjectLiterally import Model
from Numeme import mul

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
        if color.lower() == "random":
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        elif color.lower() in colors:
            color = colors[color.lower()]
        else:
            print("Unknown color:", color, "using white")
            color = (255, 255, 255)
    
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
            #print("Point out of bounds", x, y)
            pass
            
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
    
    def line(self, v0, vf, color_p: str or tuple = None):
        # Basado en: https://www.uobabylon.edu.iq/eprints/publication_2_22893_6215.pdf
        
        x0,y0 = v0[0],v0[1]
        x1,y1 = vf[0],vf[1]
        
        x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)
        
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
        # TODO Update vector
        debug = []       
        
        for x,y in zip(points,points[1:] + points[:1]):
            try:
                debug += self.line(x[0], x[1], y[0], y[1], color_p)
            except TypeError:
                print("A")
                print(x[0], x[1], y[0], y[1], color_p)
                print("A")
                raise TypeError
        
        return debug

    def polygon_fill(self, points, color_p: str or tuple = None):
        # TODO Update vector
         
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
            self.finish()
            input("Press Enter to continue...")

    def createObjectMatrix(self, translate, rotate, scale):
        
        translation = [[1,0,0,translate[0]],
                       [0,1,0,translate[1]],
                       [0,0,1,translate[2]],
                       [0,0,0,1]]

        rotation = [[1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]]
        
        scalation = [[scale[0],0,0,0],
                     [0,scale[1],0,0],
                     [0,0,scale[2],0],
                     [0,0,0,1]]
                
        matrix = [mul(scalation,x) for x in list(zip(*[mul(translation,x) for x in rotation]))]
                
        return matrix
                   
    def objectTransform(self, vertex, matrix):
    
        vector = (*vertex,1)
        
        vt = mul(matrix,vector)
        
        vf = list(x/vt[3] for x in vt[:3])
      
        return vf 
    
    def loadObject(self, filename, translate = (0,0,0), rotate=(0,0,0), scale=(1,1,1)):
        model = Model(filename)
        model_matrix = self.createObjectMatrix(translate, rotate, scale)
        
        for face in model.faces:

            v0 = model.vertex[ face[0][0] - 1]
            v1 = model.vertex[ face[1][0] - 1]
            v2 = model.vertex[ face[2][0] - 1]        

            v0 = self.objectTransform(v0, model_matrix)
            v1 = self.objectTransform(v1, model_matrix)
            v2 = self.objectTransform(v2, model_matrix)

            self.glTriangle_std(v0, v1, v2, color((random(),
                                                  random(),
                                                  random())))

    def glTriangle_std(self, A, B, C, clr = None):
            
        if A[1] < B[1]:
            A, B = B, A
        if A[1] < C[1]:
            A, C = C, A
        if B[1] < C[1]:
            B, C = C, B

        self.line(A,B, clr)
        self.line(B,C, clr)
        self.line(C,A, clr)
        
        def flatBottom(vA,vB,vC):
            try:
                mBA = (vB[0] - vA[0]) / (vB[1] - vA[1])
                mCA = (vC[0] - vA[0]) / (vC[1] - vA[1])
            except:
                pass
            else:
                x0 = vB[0]
                x1 = vC[0]
                for y in range(int(vB[1]), int(vA[1])):
                    self.line((x0, y), (x1, y), clr)
                    x0 += mBA
                    x1 += mCA

        def flatTop(vA,vB,vC):
            try:
                mCA = (vC[0] - vA[0]) / (vC[1] - vA[1])
                mCB = (vC[0] - vB[0]) / (vC[1] - vB[1])
            except:
                pass
            else:
                x0 = vA[0]
                x1 = vB[0]
                for y in range(int(vA[1]), int(vC[1]), -1):
                    self.line((x0, y),(x1, y), clr)
                    x0 -= mCA
                    x1 -= mCB

        if B[1] == C[1]:
            # Parte plana abajo
            flatBottom(A,B,C)
        elif A[1] == B[1]:
            # Parte plana arriba
            flatTop(A,B,C)
        else:
            # Dibujo ambos tipos de triangulos
            # Teorema de intercepto
            D = A[0] + ((B[1] - A[1]) / (C[1] - A[1])) * (C[0] - A[0]), B[1]
            flatBottom(A,B,D)
            flatTop(B,D,C)


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
