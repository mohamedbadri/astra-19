#this writes Hello World!


#this function writes Hello World!
def Sum():
    x = 3.4
    y = 5.0
    e = 6
    r = 2

    print('x type:', type(x))
    print('y type:', type(y))
    print('e type:', type(e))
    print('r type:', type(r))
    print("Sum of y+x =", y+x, type(y+x))
    print("Diffrence of e-r =", e-r, type(e-r))
    print("Product of r*x =", r*x, type(r*x))



#We call the function 
def main():
    Sum()


#when we run the program this executes main()
if __name__=="__main__":
    main()