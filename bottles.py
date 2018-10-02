firstl = " bottles of beer"
secl = " on the wall"
thrdl = "Take one down and pass it around, "
singl = " bottle of beer"

def verse(n):
    print (str(n)+firstl+secl+", "+str(n)+firstl+".")
    print (thrdl+str(n-1)+firstl+".")
    print (" ")
    
def thirdtolast():
    print ("2"+firstl+secl+", 2"+firstl+".")
    print(thrdl+"one"+singl+secl+".")
    print (" ")
    
def secondtolast():
    print ("One"+singl+secl+", one"+singl+".")
    print (thrdl+"no more "+firstl+secl+".")
    print (" ")
    
def last(n):
    print ("No more"+firstl+secl+", no more"+firstl)
    print ("Go to the store and buy some more, "+str(n)+firstl+secl+".")
    
n = 99
i=n

while i>2:
    verse(i)
    i=i-1
    
thirdtolast()
secondtolast()
last(n)         