from modelos.restaurante import Restaurente

# BAR DO MANÉ
restaurente_praca = Restaurente('bar do mané', 'Bar')

restaurente_praca.alternar_status()

restaurente_praca.receber_avaliacao('Fab', 3)
restaurente_praca.receber_avaliacao('Bia', 3)
restaurente_praca.receber_avaliacao('Carlos', 5)

# PIZZARIA DOM PAULO 

restaurente_pizza = Restaurente('Dom Paulo', 'Pizzaria')


#MARMITEX DO BOLA 

restaurante_bola = Restaurente('Marmitex do Bola', 'Comida Caseira')


#COXINHA DA VOVÓ

restaurante_vovo = Restaurente('Coxinha da Vovó', 'Lanchonete')

restaurante_vovo.alternar_status()

restaurante_vovo.receber_avaliacao('Adilson', 4)
restaurante_vovo.receber_avaliacao('Claudio', 5)
restaurante_vovo.receber_avaliacao('Rodrego', 5)





def main():
    Restaurente.listar_restaurantes()

if __name__ == '__main__':
    main()

