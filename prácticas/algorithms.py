from numpy import *
from numpy.linalg import *
from numpy import abs, sum, max, min

def mat_arange(k):
    return array([[k*i+j+1 for j in range(k)] for i in range(k)])

def hilbert(n):
    return array([[1/(i+j+1) for j in range(n)] for i in range(n)])

def vandermonde(n, alphas):
    return array([[alphas[i]**(j) for j in range(n)] for i in range(n)])

def conjugada(A):
    if len(A.shape) == 1 or A.shape[0] == 1:
        return conjugate(A.reshape(-1,1))
    elif A.shape[1] == 1:
        return conjugate(A.reshape(1,-1))
    else:
        return conjugate(transpose(A))
    
def norma_vec(X, p):
    inf_norm = max(abs((1.0 + 0j)*X))
    if p == inf:
        return inf_norm
    if p >= 1:
        if inf_norm > 1:
            return inf_norm*((sum((abs((1.0 + 0j)*X)/inf_norm)**p))**(1/p))
        else:
            return (sum(abs((1.0 + 0j)*X)**p))**(1/p)
    else:
        return "error"
def norma_mat(A, p):
    #arreglar esto
    return norm(A,p)