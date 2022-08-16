from struct import unpack

class Model():
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.vertex = []
        self.texcoords = []
        self.normals =  []
        self.faces = []

        for line in self.lines:
            try:
                prefix, value = line.split(' ', 1)
            except:
                continue

            if prefix == 'v': # Vertices
                self.vertex.append( list(map(float,value.split(' '))))
            elif prefix == 'vt':
                self.texcoords.append( list(map(float, value.split(' '))))
            elif prefix == 'vn':
                self.normals.append( list(map(float, value.split(' '))))
            elif prefix == 'f':
                self.faces.append([  list(map(int, vert.strip().split('/'))) for vert in value.strip().split(' ')] ) # ! Puede que sea necesario quitarle el strip()
        
class Texture():
    def __init__(self, filename):
        with open(filename, "rb") as image:
            image.seek(10)
            headerSize = unpack('=l', image.read(4))[0]
            
            image.seek(18)
            self.width = unpack('=l', image.read(4))[0]
            self.height = unpack('=l', image.read(4))[0]
            
            image.seek(headerSize)
            
            self.pixels = []
            
            for y in range(self.height):
                pixelRow = []
                
                for x in range(self.width):
                    b = ord(image.read(1))/255
                    g = ord(image.read(1))/255
                    r = ord(image.read(1))/255
                    
                    pixelRow.append((r, g, b))
                    
                self.pixels.append(pixelRow)
                
    def getColor(self, u, v):
        if 0 <= u <= 1 and 0 <= v <= 1:
            x = int(v * self.width)
            y = int(u * self.height)
            return self.pixels[y][x]
        else:
            return (1,1,1)