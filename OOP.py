# Vamos criar um exemplo de classe Carro
class Carro:
    total_carros = 0
    def __init__(self, marca, modelo, ano, cor, preco, placa, combustivel=0, velocidade = 0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco
        self.placa = placa
        self.combustivel = combustivel
        self.velocidade = 0
        Carro.total_carros += 1

    def abastecer(self, valor):
      self.combustivel += valor

    def consumir_combustivel(self, valor):
      self.combustivel -= valor

    def ligar(self):
      print("O carro está ligado")
    
            
    def acelerar(self, valor):
        self.velocidade += valor
        
    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
            print("O carro parou")
          
            
    def mostrar_velocidade(self):
        print(f"A velocidade atual é de {self.velocidade} km/h.")


    def media(valores):
      return sum(valores) / len(valores)

    @classmethod
    def total_objetos(cls):
      return cls.total_carros
  

carros = [
      Carro("Chevrolet","Onix",2010,"gray",6000, "BCT-6666"),
      Carro("Fiat","Uno",2010,"gray", 35000, "BCT-6666"),                    Carro("Ford", "Ka",2010,"gray", 45000, "BCT-6666")
         ]

precos = [carro.preco for carro in carros]

media_precos = Carro.media(precos)




        
carro1 = Carro("Chevrolet", "Camaro", 2021, "Amarelo", 280000, "DXD-3750", 5.30)
carro2 = Carro("Ferrari", "458 Spider", 2020, "Vermelho", 1250000, "BCT-6969", 5.30)



print("Carro 1:")
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")
print(f"Cor: {carro1.cor}")
print(f"Preço: {carro1.preco}")
print(f"Placa: {carro1.placa}")
print(f"Combustivel: {carro1.combustivel}")
carro1.ligar()
carro1.consumir_combustivel(5)
carro1.acelerar(80)
carro1.mostrar_velocidade()

print("\n\nCarro 2:")
print(f"Marca: {carro2.marca}")
print(f"Modelo: {carro2.modelo}")
print(f"Ano: {carro2.ano}")
print(f"Cor: {carro2.cor}")
print(f"Preço: {carro2.preco}")
print(f"Placa: {carro2.placa}")
print(f"Combustivel: {carro2.combustivel}")
carro2.ligar()
carro2.consumir_combustivel(5)
carro2.frear(50)
carro2.mostrar_velocidade()

print(f"A media de de preços dos carros é R${media_precos:.2f}")

#carro1.total_objetos()
print(f"Total Objetos {Carro.total_objetos()}")



class moto:
  def __init__(self, marca, modelo, ano, cor, preco, placa, combustivel = 0, velocidade = 0,):

    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.cor = cor
    self.preco = preco
    self.placa = placa
    self.combustivel = combustivel
    self.velocidade = velocidade

  def empinar(self):
    print("\n\nA moto esta dando grau")

     
    
      
moto = moto("Yamaha", "XRE 300c", 2011, "Vermelha/branca","R$ 17.000,00", "SXT-6666", 5.30, "360km/h")

moto.empinar()



  