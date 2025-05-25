def perimeter(a,b,c,d):
    p=a+b+c+d
    return p

def rectangle(sidea,sideb,sidec,sided):
    perimeter( sidea,sideb,sidec,sided)
    print("the primeter of the rectangle is ",+ perimeter( sidea,sideb,sidec,sided))
rectangle(4,3,4,3)

def area(L,w):
    a=(L*w)*2
    return a

def square(c,d):
    area(c,d)
    print("area of a square is ", + area(c,d))
square(4,4)

def circular(r):
    c=3.14*r
    return c

def circle(d):
    circular(d)
    print("the area of a circle is ", + circular(d))
circle(7)

def fibonacci():
    a=0
    b=1
    print(a)
    print(b)
    for fibo in range(18):
        c=b+a
        a=b
        b=c
        print(c)
fibonacci()




    