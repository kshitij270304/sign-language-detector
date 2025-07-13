a=10
b=14
c=b//a  

d = b % a                   ##data types = int, float (1.03, 0.2), string , double, bolean(t / f, 1 / 0) ,etc     int(1.4) = 1, float(1.4)
##print("the modulo is :" ,d)

##print("the ans is :" ,c)   # how to write string ""

## array

array = [9,5,3,7]                 ##array ind0 ,ind1,ind2 in...............
d = array[1] + 1
##print(d)


##loop

##for i in range(4):
    ##print("the element of array are :" , 4*array[i])                    ## range4 = 0 - 3 range 10  ,,, array[3]


#condition 
##if(a != b):                                                         ## = , == , !=
    ##print("they are not same")
##else:
    ##print("they are same")

#### logical operation : AND , OR , NAND !=
## AND = 1 && 0 = 0 , 0 && 0 = 0 , 1 && 1= 1
## OR = 1 || 0 = 1 , 1 || 1 = 1, 0|| 0 = 0 


arrayi = [3,9,5,3,98,6,4,2]
even = 0
odd = 0
for i in range(8):
    if(arrayi[i] % 2 == 0):
        even = even +1
    else:
        odd = odd +1

print("number of even elements are:" ,even)
print("number of odd elements are:" ,odd)
