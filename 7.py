#i=j i+j=8 j=4




def estrella(numero):
    
 #   for i in range(numero):
  #      for j in range(numero):
   #         if i==j or i+j==2*numero-2 or j==4:
    #            print( " "*(j),  "*", " "*(numero-2),   "*",   " "*(numero-2), "*")



    for i in range(numero):
        
        if(i != numero-1):
            print(" "*(i), "*", " "*(numero-2-i), "*", " "*(numero-2-i), "*")
        else:
            print(" "*(i+2), "*")

    n=numero
    w=0
    for i in range(numero-1):
        

        print(" "*(n-2), "*", " "*(i), "*", " "*(i), "*")
        n-=1






estrella(5)