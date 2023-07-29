e = 'e'


def variables1():
    a = 'a'
    b = 'b'

    print(a,b)
    
    def variables2():

        nonlocal b
        b= 'hola'
        e = 'x'
        c = 'c'
        d = a + b
        print(c,d,e,b)


    return variables2  

       
             
    
   
variables1()
