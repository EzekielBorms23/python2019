# bincon_loopy.py zlb
# Convert a base 10 number to binary
# Use 191 base 10 equal to 1011 1111 base 2
# q(quotient) d(divisor) r(remainder) n(integer input)
#div 128 * * * * * * *
n = int(input("Input an integer less than 256 : "))
n_original = n
d = 128
binString = ""#create a string called binString
for i in range(0,8):
         q = int(n / d)
         r = int(n % d)
         print(d,q,r)# debug line
         n = r
         d = int(d / 2)
         binString = binString+str(q)
print("\n*********\t")
print
print(str(n_original)+" base 10 = "+binString+" base 2")
print("\n*********\t")
