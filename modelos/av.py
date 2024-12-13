class Avaliacao:
    def __init__(self, cliente, nota):
        if not isinstance(nota, (int, float)) or not (0<= nota <= 5):
            raise ValueError('A nota deve ser um número entre 0 e 5.')
        self._cliente = cliente
        self._nota = nota


