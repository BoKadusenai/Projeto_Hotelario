from Class import *
import os

def main():
    countID = 0

    hotel = Hotel("Quality","Av. Brasil", "10.123.321/0001-5")
    quarto_deluxe = DeluxeQuarto(2,4,500,"Quarto com varanda, cama de casal e hidromassagem")
    quarto_casal = CasalQuarto(4,2,300,"Quarto com cama de casal")
    quarto_solteiro = SolteiroQuarto(8,1,150,"Quarto com cama de solteiro")

    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("--- MENU ---")
            print("01 - Cadastrar Cliente")
            print("02 - Disponibilidade de quartos")
            print("03 - Reservar quarto")
            print("04 - Cancelar reserva")
            print("05 - Listar Clientes")
            print("06 - Listar Reserva")
            print("00 - Sair")

            menu = int(input("Qual opção você deseja? \n -"))
            os.system("pause")

            match menu:
                case 1:
                    os.system("cls")
                    print("Cadastro de cliente")
                    print("Informe seus dados")
                    countID += 1
                    id = countID
                    nome = input("Nome -")
                    cpf = int(input("CPF -"))
                    tel = int(input("Telefone -"))

                    hotel.cadastrarCliente(id, nome, cpf, tel)

                case 2:
                    os.system("cls")
                    print("Disponibilidade de quartos")
                    print(f"Quantidade de quartos Deluxe:{quarto_deluxe.getQtdQuarto()}")
                    print(f"Quantidade de quartos de Casal:{quarto_casal.getQtdQuarto()}")
                    print(f"Quantidade de quartos de Solteiro:{quarto_solteiro.getQtdQuarto()}")
                    os.system("pause")

                case 3:
                    os.system("cls")
                    print("Disponibilidade de quartos")
                    print(f"Quantidade de quartos Deluxe:{quarto_deluxe.getQtdQuarto()}")
                    print(f"Quantidade de quartos de Casal:{quarto_casal.getQtdQuarto()}")
                    print(f"Quantidade de quartos de Solteiro:{quarto_solteiro.getQtdQuarto()}")
                    print("=-=-=-=-=-")
                    print("")
                    print("Qual quarto você deseja reservar?")
                    print("01 - Deluxe")
                    print("02 - Casal")
                    print("03 - Solteiro")

                    reserva = int(input("- "))
                    idCLI = int(input("Informe o ID do Cliente \n - "))

                    if reserva > 0 and reserva <= 3:
                        hotel.reservarQuarto(idCLI,reserva)

                    else:
                        print("Opção invalida")

                    match reserva:
                        case 1:
                            quarto_deluxe.setReservaQuarto(quarto_deluxe.getQtdQuarto() - 1)

                        case 2:
                            quarto_casal.setReservaQuarto(quarto_casal.getQtdQuarto() - 1)

                        case 3:
                            quarto_solteiro.setReservaQuarto(quarto_solteiro.getQtdQuarto() - 1)
                    os.system("pause")

                case 4:
                    pass

                case 5:
                    os.system("cls")
                    print("Lista de clientes")
                    hotel.listarClientes()
                    os.system("pause")

                case 6:
                    os.system("cls")
                    print("Lista de reservas")
                    hotel.listarReservas()
                    os.system("pause")

                case 0:
                    print("Saindo...")
                    sair = True

                case _:
                    print("Opção invalida")


        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
