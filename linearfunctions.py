global m
global o
global b
debug=False
fail=0
ax=0
ay=0
bx=0
by=0
m=0
n=0
b=0

def syiCal(ax, ay, bx, by):
  try:
    m=(ay-by)/(ax-bx)
    n=(ax-ay)/m
  except:
    pass
  o=str(int(n))
def sifLogic(ax, ay, bx, by):
  
def sifPrint(m, b, o)
  if o[0]=="-":
    parity="-"
    b=o[1:len(o)]
  else:
    parity="+"
  if m==1:
    m=""
  elif m==0:
    print("Vertical/Horizontal Line")
    fail=True
  if fail!=True:
    if b==0:
      print("y="+str(m)+"x")
    else:
      print("y="+str(m)+"x"+parity+str(b))

def psf(ax, ay, yparity, xparity):
  print(ay+yparity+"="+m+"(x"+xparity+ax+")"
def debug(debug):
  if debug==True:
    print(ax)
    print(ay)
    print(bx)
    print(by)
    print(m)
    print(n)
  
sifLogic(float(input("ax: ")), float(input("ay: ")), float(input("bx: ")), float(input("by: ")))
sifPrint()
debug(True)