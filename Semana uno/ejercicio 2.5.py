a = float(input('ingrese el valor de a:'))
b = float(input('ingrese el valor de b:'))
c = float(input('ingrese el valor de c:'))

AreaDelRectangulo = a * b
AreaDelTriangulo = a - c  * b / 2
AreaTotal = AreaDelTriangulo + AreaDelRectangulo
print('el area del triangulo es', AreaDelTriangulo, 'el area del rectangulo es', AreaDelRectangulo, 'el area total es', AreaTotal)