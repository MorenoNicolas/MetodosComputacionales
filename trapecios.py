class trapecios:
    @staticmethod
    def main():
        a = int(input("Ingrese el valor de a "))
        b = int(input("Ingrese el valor de b "))
        n = int(input("ingrese vantidad de intervalos "))
        h = (b-a)/n
        area = trapecios.calcular(a,b,h,n)
        print("el are aproximada es ", area )

    @staticmethod
    def calcular(a,b,h,n):
        sumatoria  = 0
        x0 = trapecios.f(a) 
        xn = trapecios.f(b)
        xi = a+h
        for i in range(1,n):
            sumatoria += trapecios.f(xi)
            xi += h
        resultado = (h/2)*(x0+xn+(2*sumatoria))
        return resultado      

    @staticmethod
    def f(x):
        return ((5 * x ** 2) + (2 * x) - 3)           

    if __name__ == "__main__":
        main()