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



# Ejercicio en Java
#import java.util.Scanner;
# class EjercicioTpo1{
#     public class Trapecios {
#         public static void main(String[] args) {
#             Scanner sc = new Scanner(System.in);
#             double a, b, h, area;
#             int n;
#             System.out.println("Ingrese el valor de a");
#             a = sc.nextDouble();
#             System.out.println("Ingrese el valor de b");
#             b = sc.nextDouble();
#             System.out.println("Ingrese la cantidad de intervalos");
#             n = sc.nextInt();
#             h = (b - a) / n;
#             area = calcular(a, b, h, n);
#             System.out.println("El area aproximada de la funcion es de " + area);
#         }
    
#         public static double calcular(double a, double b, double h, int n) {
#             double resultado, sumatoria = 0, x0 = f(a), xn = f(b), xi;
#             int i;
#             xi = a + h;
#             for(i = 1; i < n; i++) {
#                 sumatoria = sumatoria + f(xi);
#                 xi = xi + h;
#             }
#             resultado = (h / 2) * (x0 + xn + (2 * sumatoria));
#             return resultado;
#         }
    
#         public static double f(double x) {
#             // Modulo que almacena la funcion
#             return (5 * Math.pow(x, 2)) + (2 * x) - 3;
#         }
    
#     }
# }