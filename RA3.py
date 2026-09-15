class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i**2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i

    def __str__(self):
        """Display Complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"    # This is a string representation of the Complex object, not a Complex object
        else:
           return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__

    def conjugate(self):
        """Returns a Complex object that represents the Complex conjugate"""
        return Complex(self._real, -self._imag)
   
    def __mul__(self,other):
        """Multiply a Complex number"""
        if isinstance(other, Complex):
            real_part = self._real * other._real - self._imag * other._imag   
            imag_part = self._real * other._imag + self._imag * other._real    
            ans = Complex(real_part, imag_part)
        else:
           real_part = self._real * other - self._imag * 0   
           imag_part = self._real * 0 + self._imag * other    
           ans = Complex(real_part, imag_part)
        return ans

    def __rmul__(self,other):
            """Multiply a Complex number"""
            if isinstance(other, Complex):
                real_part = self._real * other._real - self._imag * other._imag   
                imag_part = self._real * other._imag + self._imag * other._real    
                ans = Complex(real_part, imag_part)
            else:
               real_part = self._real * other - self._imag * 0   
               imag_part = self._real * 0 + self._imag * other    
               ans = Complex(real_part, imag_part)
            return ans

a=Complex(5,-6)
b=Complex(2,14)
print(a*b)
print(b*5)
print(5*b)
print(isinstance(5*b, Complex))
print(a.conjugate())
print(b.conjugate())      
