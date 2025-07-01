from eletrodomesticos import Televisao

tv_sala = Televisao()
tv_sala.configurarTV('tv_sala', tamanho=32, marca='Filipys')

tv_quarto = Televisao()
tv_quarto.configurarTV('tv_quarto', marca='xilco', ligada=True)

print("Nome | Canal Atual | Tamanho | Marca | Ligada (S/N)?")
print(tv_sala.exibirTela())
print(tv_quarto.exibirTela())