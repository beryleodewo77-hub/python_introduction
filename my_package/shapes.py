def  triangle_area(a:float, b:float, c:float):
    s =(a+b+c)/2
    area=s*(s-a)*(s-b)*(s-c)
    return area**0.5