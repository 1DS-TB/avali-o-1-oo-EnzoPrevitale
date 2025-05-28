# Heranças
class ClassePai:
    def __init__(self, var1, var2):
        # Método Construtor, executado ao inicializar objeto
        self.var1 = var1
        self.var2 = var2

    def metodo(self):
        # Método intrínseco à classe
        print("A")


class ClasseFilhaA(ClassePai): # Os parênteses indicam herança
    def __init__(self, var1, var2, var3, var4):
        super().__init__(var1, var2) # Executa a função de inicialização (__init__) da classe pai
        self.var3 = var3
        self.var4 = var4

    def metodo_adicional(self):
        # Método adicional à classe pai
        return self.var1, self.var2, self.var3, self.var4

    # Exemplo de polimorfismo através de herança:
    def metodo(self): # A classe filha terá a mesma função da classe pai, mas ela executará um comando diferente.
        print("B")

class ClasseFilhaB(ClassePai):
    def __init__(self, var1, var2, var3, var4):
        super().__init__(var1, var2)
        self.var3 = var3
        self.var4 = var4

    def metodo(self):
        print("C")

obj_filho_a = ClasseFilhaA(1, 2, 3, 4)
obj_filho_b = ClasseFilhaB(10, 20, 30, 40)

obj_filho_a.metodo()
obj_filho_a.metodo_adicional()

obj_filho_b.metodo()

# A classe filha tem acesso tanto aos métodos definidos na classe pai quanto aos intrínsecos a si

"""
Diferenças entre os dois conceitos: enquanto a herança gera uma classe com as mesmas variáveis e funções da classe pai, 
o polimorfismo serve para uma classe responder de forma distinta ao mesmo método. Os dois conceitos são vantajosos para 
manter o código suscinto.

Referências:
https://blog.grancursosonline.com.br/polimorfismo-em-python/
https://www.alura.com.br/apostila-python-orientacao-a-objetos/heranca-e-classes-abstratas?srsltid=AfmBOooDJpG2ytYlu-rwjiDPKb5TM7lirHwXGvItmgVy_W5stut28ZRG
"""
