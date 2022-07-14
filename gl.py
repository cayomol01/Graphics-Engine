from struct import pack

def char(c):
    return pack('=c', c.encode('ascii'))

def word(w):
    return pack('=h', w)

def dword(d):
    return pack('=l', d)

def color(color:str or tuple):
    """
    (255,255,255)
    """
    colors = {
        "white": (255,255,255),
        "black": (0,0,0),
        "red" : (255,0,0),
        "orange":(255,128,0),
        "yellow":(255,255,0),
        "light-green":(128,255,0),
        "green":(0,255,0),
        "blue-green":(0,255,128),
        "sky-blue":(0,255,255),
        "blue":(0,128,255),
        "dark-blue":(0,0,255),
        "purple":(127,0,255),
        "magenta":(255,0,255),
        "rose":(255,0,127)
    }

    if isinstance(color,str):
        try:
            color = colors[color]
        except KeyError:
            print("Unknown color, using default") 
            color = colors["red"]

    r, g, b = color
    
    if all(isinstance(x,float) for x in (r, g, b)):
        r,g,b = (r*255,g*255,b*255)
    
    try:    
        return bytes([int(b),int(g),int(r)])
    except ValueError:
        print("""!!=-=-=Incorrect color format.=-=-=!! 
    Check you are using the correct notation:
    > Hint: (Min,Mid,Max)
    > "blue" should be a lowercase string
    > (0,127,255) should be a tuple of integers
    > (0.0,0.5,1.0) should be a tuple of floats""")
        raise
        

class Window: # * glInit()
    def __init__(self, width, height, clear_color="red", current_color="black") -> None: # * glCreateWindow(width, height)
        self.width =  width
        self.height = height
        self.clear_color = color(clear_color) # Default "red"
        self.current_color = color(current_color) # Default "black"
        self.setViewPort(0,0,width,height)
        self.clear()
        
    def clear(self): # * glClear()
        self.pixels = [ 
            [self.clear_color for y in range(self.width)] for x in range(self.height)
        ]
        
    def clearColor(self, color_p:str or tuple): # *  glClearColor(r, g, b)
        self.clearColor = color(color_p)
        
    def currentColor(self, color_p:str or tuple): # * glColor(r, g, b)
        self.current_color = color(color_p)
        
    def point(self, x, y, color_p:str or tuple = None): # * glPoint(x, y)
        self.pixels[x][y] = color(color_p) if color_p else self.current_color
    
    #VIEW PORT
    def setViewPort(self, x, y, width, height): # * glViewPort(x, y, width, height)
        self.vp_x = x
        self.vp_y = y
        self.vp_width = width
        self.vp_height = height
    
    def clearViewPort(self, color_p:str or tuple = None):
        for i in [(m,n) for m in range(self.vp_x, self.vp_x + self.vp_width) for n in range(self.vp_y, self.vp_y + self.vp_height)]:
            self.point([*i] ,color_p)
        
        # for x in range(self.vp_x, self.vp_x + self.vp_width):
        #     for y in range(self.vp_y, self.vp_y + self.vp_height):
        #         self.point
        
    def pointViewPort(self, x, y, color_p:str or tuple = None):
        x = int((self.vp_width/2)*(x+1) + self.vp_x)
        y = int((self.vp_height/2)*(y+1) + self.vp_y)
        
        self.point(x,y,color_p)
        
    def finish(self, filename="render"): # * glFinish()
        with open("".join((filename,".bmp")), "wb") as file:
            #header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))
            
            #info header
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
            
            for x in self.pixels: #Faster
                for y in x:
                    file.write(y)

                    
        print("Done")
        
        
        
        
