class Hotel:
     
    def __init__(self, nome, endereço, cnpj):
        self.nome = nome
        self.endereço = endereço
        self.cnpj = cnpj
        self.cliente = {}
        self.reservas = {}

    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
       
        self.cliente[self.id] = [self.nome, self.cpf, self.tel]

    def listarClientes(self):
        for chave,valor in self.cliente.items():
            print(f"Id: {chave} - Nome: {valor[0]} - CPF: {valor[1]} - Telefone: {valor[2]}")
            
    def reservarQuarto(self, idCLI, reserva):
        self.idCLI = idCLI
        self.reserva = reserva

        match self.reserva:
            case 1:
                x = "Quarto Deluxe"
            case 2:
                x = "Quarto de Casal"
            case 3:
                x = "Quarto de Solteiro"
            case _:
                x = "N/A"

        self.reservas[self.idCLI] = x

    def listarReservas(self):
        for chave,valor in self.reservas.items():
            print(f"Id: {chave} - Quarto: {valor}")
    
    def cancelarReserva():
        pass

    def disponibilidadeQuartos():
        pass

class Quarto:
    def __init__(self, qtd, capacidade, valor, descrição):
        self.qtd = qtd
        self.capacidade = capacidade
        self.valor = valor
        self.descrição = descrição

    def getQtdQuarto(self):
        return self.qtd
    
    def setReservaQuarto(self,qtd):
        self.qtd = qtd

class DeluxeQuarto(Quarto):
    pass
class CasalQuarto(Quarto):
    pass

class SolteiroQuarto(Quarto):
    pass