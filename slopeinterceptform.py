'''
BY: Dcai169
TO USE:
Input two coordinates
Read output
Repeat
'''
global debug
global fail
global pointax
global pointay
global pointbx
global pointby
global m
global f
global b
debug=False
fail=False
m=0
f=0
b=0

def logic(pointax, pointay, pointbx, pointby):
  try:
    m=float((pointby-pointay)/(pointbx-pointax))
  finally:
    if m==1:
  	  m=""
    elif m==0:
      print("Vertical/Horizontal Line")
      fail=True
  try:
    f=float((pointax-pointay)/m)
  finally:
    s=str(int(f))
    if s[0]=="-":
      parity="-"
      b=s[1:len(s)]
    else:
      parity="+"
  if fail==False:
    if b==0:
      print("y="+str(m)+"x")
    else:
      print("y="+str(m)+"x"+parity+str(b))

def debug(debug):
  if debug==True:
  	print("ax: "+str(pointax))
  	print("ay: "+str(pointay))
  	print("bx: "+str(pointbx))
  	print("by: "+str(pointby))
  	print("m: "+str(m))
  	print("f: "+str(f))
  	print("s: "+str(s))
  	print("b: "+str(b))

logic(input("ax"), input("ay"), input("bx"), input("by"))
debug(False)