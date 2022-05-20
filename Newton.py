import math

def f(x):
  return x-3.5*x*(1-x)

def df(x):
  return -2.5 + 7*x

def Newton():
  ''' 
  Find root of equation using Newton-Raphson method,
  provided an initial guess and desired tolerance
  '''
  
 # Chute inicial
  x0 = float(input(" Provide initial value: "))
  x = x0

  # Tolerância do metodo (erro aceitado)
  tol = float(input("\n Provide tolerance: "))

  # Número máximo de iteracoes já que Newton-Raphson
  # não garante convergência
  maxiter = 1000

  for i in range(maxiter):
    # expressao para atualizar x da iteração k+1 com valores da iteração k
    x = x0 - f(x0)/df(x0)
    # checando convergência: se convergiu, vai sair do loop com break!
    if (math.fabs(x-x0) < tol):
      print("\n Newton-Raphson converged in {} iterations.\n".format(i+1))
      break
    # se ainda não convergiu, novo valor calculado vai ser usado na iteração seguinte
    x0 = x
    # porém, se atingir o máximo número de iterações, melhor parar, parece
    # que o método não vai convergir...
    if (i == (maxiter-1)):
      print("\n Newton-Raphson did not converge within {} iterations.\n".format(maxiter))
  
  # saímos do loop for! Repare a indentação!
  return x0

# saímos da função Newton()!
def Bissecao():
  '''
  Find root of equation using Bisection method, provided
  an interval and desired tolerance. If the given interval
  does not contain the solution, Newton-Raphson will be called!
  '''
  # bordas do intervalo de busca [a,b]
  a = float(input(" Enter mininum value in interval: "))
  b = float(input("\n Enter maximum value in interval: "))

  # Tolerância
  tol = float(input("\n Provide tolerance: "))

  # O método da Bisseção garante convergência se a raiz realmente estiver
  # dentro do intervalo [a,b]. Podemos checar isso avaliando se o sinal da
  # função avaliada em cada borda do intervalo muda:
  if (f(a)*f(b) > 0.0):
    print("\n Interval doen not contain root.\n")
    print("Switching to Newton-Raphson to search for root.\n")
    return Newton()
  
  # Se o if anterior não for verdadeiro, continuamos aqui:
  while (math.fabs(f(a)-f(b)) > tol):
    if (math.fabs(f(a)) < math.fabs(f(b))):
      b = (a+b)/2.
    else:
      a = (a+b)/2.
  
  # saímos do while
  return min(a, b)

# saímos da função Bissecao()!
# A execução do nosso script vai começar por aqui:
print("This is a script to calculate the root of the function\n")
print("x-3.5*x*(1-x)\n")
method = input("Please select the method. Press 1 for Newton-Raphson and 2 for Bisection.\n")

if (method == '1'):
  root = Newton()
  print("\n\n The root of the function was found to be {}.\n".format(root))
elif (method == '2'):
  root = Bissecao()
  print("\n\n The root of the function was found to be {}.\n".format(root))
else:
  print("\n\n ERROR: Unknown method. Try again using either 1 or 2.\n")