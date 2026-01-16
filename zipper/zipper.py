
def ZipBytes(E):
  C=E[0]
  x=0
  Z=E[0]+""
  for i in E:
    #print(C," ",i," ",x)
    if not(i!=C):
      x+=1
    else:
      Z+=str(x)
      x=1
      C=i
  Z+=str(x)
  return Z

def UnZipBytes(Z):
  C=Z[0]
  Z=Z[1:]
  E=""
  for i in Z:
    for e in range(int(i)):
      E+=C
    if C=="1":
      C="0"
    else:
      C="1"
  return E
