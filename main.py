# Heranças
class ClassePai:
    def __init__(self, var1, var2):
        # Método Construtor, executado ao inicializar objeto
        pass

    def metodo(self):
        # Método intrínseco ao objeto
        pass

class ClasseFilha(ClassePai):
    def __init__(self, var1, var2, var3, var4):
        super().__init__(var1, var2)
        self.var3 = var3
        self.var4 = var4

    def metodo_adicional(self):
        # Método adicional à classe pai
        return self.var1, self.var2, self.var3, self.var4

obj_filho = ClasseFilha(1, 2, 3, 4)

obj_filho.metodo()
obj_filho.metodo_adicional()

# A classe filha tem acesso tanto aos métodos definidos na classe pai quanto aos intrínsecos a si
