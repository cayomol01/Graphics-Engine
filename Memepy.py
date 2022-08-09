class Matrix(list):
    def __matmul__(self, B):
        # Fuente: https://www.codingem.com/numpy-at-operator/
        # Equivalente a @
        return [sum(a*b for a,b in zip(C,B)) for C in self]  

def mul(A, B):
    # Equivalente a *
    return [sum(a*b for a,b in zip(C,B)) for C in A] 
        

                
                