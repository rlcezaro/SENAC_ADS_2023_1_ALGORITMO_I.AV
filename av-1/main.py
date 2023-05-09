from Desktop import Desktop
from Notebook import Notebook

d1 = Desktop("Dell", "Cinza", 5000, 400)

n1 = Notebook("Lenovo", "Cinza", 2000, 12)

print(d1.cadastrar())
print(d1.getInformacoes())
print("--------------------------------")
print(n1.cadastrar())
print(n1.getInformacoes())
