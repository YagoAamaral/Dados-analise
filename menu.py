from simple_term_menu import TerminalMenu

def exibir_menu():
    opcoes = [
        "Verificar portas de rede",
        "Varredura de informações",
        "Surpreenda-me",
        "Baixar dependências",
        "Sair"
    ]

    menu = TerminalMenu(opcoes, title=".......Welcome to aspir.......")
    escolha = menu.show()

    if escolha == 0:
        print("\nVerificando portas....:")
        print("Nenhuma porta aberta encontrada.")
    elif escolha == 1:
        print("\nVarredura de informações em desenvolvimento.")
        dominio = input("Digite o domínio: ")
        print(f"Domínio informado: {dominio}")
    elif escolha == 2:
        print("\nSurpresa! Algo interessante aqui...")
    elif escolha == 3:
        print("\nBaixando dependências necessárias...")
       
        print("Dependências instaladas.")
    elif escolha == 4:
        print("\nSaindo do menu...")
        return False

    return True

if __name__ == "__main__":
    while exibir_menu():
        pass
