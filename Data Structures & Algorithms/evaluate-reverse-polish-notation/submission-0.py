import math 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pilha = []
        operador = ['+', '-', '*', '/']
        resultado = 0


        for token in tokens:
            if token  in operador:
                b = pilha.pop()
                a = pilha.pop()

                if token == "-":
                    resultado = int(a - b)
                    pilha.append(resultado)
                
                elif token == "+":
                    resultado = int(a + b)
                    pilha.append(resultado)
                
                elif token == "*":
                    resultado = int(a*b)
                    pilha.append(resultado)

                elif token == "/":
                    resultado = math.trunc(int(a/b))
                    pilha.append(resultado)
            else:
                pilha.append(int(token))


        return pilha[0]









            
                
                

        