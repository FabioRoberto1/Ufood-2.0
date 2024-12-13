from modelos.av import Avaliacao

class Restaurente:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurente.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'.upper()} ')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.media_av).ljust(20)} | {restaurante.ativo} ')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_av(self):
        if not self._avaliacao:
            return str('Sem Avaliação.')
        soma_da_av = sum(avaliacao._nota for avaliacao in self.
        _avaliacao)
        quantida_de_av = len(self._avaliacao)
        media = round(soma_da_av / quantida_de_av, 1)
        return media

    
