#algoritmo para mdc
def mdc(a, b):
  a = abs(a)
  b = abs(b)
  if a < b:
    extra = a
    a = b
    b = extra
  if a % b == 0:
    return b
  c = 1
  while a > (b * c):
    c += 1
  c = c - 1
  resto = a - (b * c)
  return mdc(b, resto)

def sol(a,b,mdc):
  if b == 0:
        mdc, x, y = mdc, 1, 0
  else:
        [mdc, p, q] = sol(b, a % b,mdc)
        x = q
        y = p - q * (a // b)
  assert mdc == a * x + b * y

  return [mdc, x, y]
  
# check se equacao tem solucao 
def makeEquation(a,b,c):
  v =[]
  if c%mdc(a,b)==0:
    v =  sol(a,b,mdc(a,b))
    i=0
    while v[0]*i!=c:
      i+=1 
    v = [i*x for x in v]
    return f'o Resposta e :- \n {a}*({v[1]}) + {b}*({v[2]}) = {v[0]} \n todas as Solucoes para x sao: \n\n x = {v[1]}+{b}/{mdc(a,b)} x t , Onde t e Z \n Solucoes para \n\n y = {v[2]}+{a}/{mdc(a,b)} x t ,Onde t e Z '
  return "nao tem solucao"


v = input("escreva valor de a,b,c com virgula EX: 2,4,5  \n").split(',')
v =[int(x)for x in v]
  
print("mdc e igual :",mdc(v[0],v[1]))  
print(makeEquation(v[0],v[1],v[2]))

#new solution






#y= (c-ax)/b
#x = (c -by)/a


    
# Implementacao de elucidean algorithm
#a = b.q +r        usando mesmo nome para variaveis
 
equacoes=[]
dict={}
def algorithm(a,b,mdc):
  q=1
  while a>b*q:
    q+=1
  q-=1
  r = a- (b*q)
  temp= [a,b,q,r]
  equacoes.append(temp)
  dict[a]=[b,q,r]
  if r ==mdc:
    return
  return algorithm(dict[a][0],dict[a][2],mdc)

# ordenacao de vetor equacoes=[]
def ordenar(equacoes):
  for x in equacoes:
    one,two,three,four = x[3],x[0],x[1],-1*x[2]
    x[0],x[1],x[2],x[3]=one,two,three,four


# algoritmo para resolver equacao
dict_new={}
def equationMaker(v,a,b):
  for x in v:
    dict_new[x[0]]=[x[1],x[2],x[3]]
  new_v = [x[1:] for x in v]
  while len(new_v)>1:
    new_v[1][1] = '('+str(new_v[0][0])+'+('+str(new_v[0][1])+"*"+str(new_v[0][2])+')'+')'
    del new_v[0]

  n_equation = '('+str(new_v[0][0])+'+('+str(new_v[0][1])+"*"+str(new_v[0][2])+')'+')'


  
  

        
  

a,b=47,30
x =mdc(a,b)
algorithm(a,b,x)
ordenar(equacoes)
equationMaker(equacoes,a,b)


