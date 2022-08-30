class Matrix(list):
    def __matmul__(self, B):
        # Fuente: https://www.codingem.com/numpy-at-operator/
        # Equivalente a @
        return [sum(a*b for a,b in zip(C,B)) for C in self]  

def mul(A, B):
    # Equivalente a *
    return [sum(a*b for a,b in zip(C,B)) for C in A] 

def dot(a,b): # np.dot
    return sum(a*b for a,b in zip(a,b))

def sub(a,b): # np.subtract || a-b
    return [a[i]-b[i] for i in range(len(a))]

def cross(a,b): # np.cross 
    # For Vector3
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def norm(a): # np.linalg.norm
    return (sum(a[i]**2 for i in range(len(a))))**0.5

def div(a,b): # np.divide || a/b
    if b == 0:
        return a
    return [a[i]/b for i in range(len(a))]

                
                