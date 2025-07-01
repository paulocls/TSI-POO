class Televisao():
    def __init__(self):
        self.nome = 'Não definido'
        self.ligada = False
        self.canal = 2
        self.tamanho = 20
        self.marca = "Xing-ling"
    
    def configurarTV(self, nome=None, ligada=None, tamanho = None, marca=None):
        if nome is not None:
            self.nome = nome
        if tamanho is not None:
            self.tamanho = tamanho
        if ligada is not None:
            self.ligada = ligada
        if marca is not None:
            self.marca = marca

    def exibirTela(self):
        ligada_str = "S" if self.ligada else "N"
        return f"{self.nome} | {self.canal} | {self.tamanho} | {self.marca} | {ligada_str}"
