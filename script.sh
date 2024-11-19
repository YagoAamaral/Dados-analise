#!/bin/bash
clear
gcc operacoes.c -o sysinfo

./sysinfo

func_roda() {
    python3 testsp.py &
}

fuc_sys() {
    python3 callsystem.py &
}

echo "Fazendo vários testes, aguarde... ;)"
echo " Direcionando você para o aplicativo"
ping -c 4 google.com >/dev/null 2>&1

func_roda
cont=0
sleep 25
clear
echo ".......Welcome to aspir......."

while [ "$cont" -eq 0 ]; do

    echo "Escolha uma opção:"
    echo "1. Verificar portas de rede"
    echo "2. Varredura de informações"
    echo "3. Surpreenda-me"
    echo "4. Baixar dependências"
    echo "5. Sair"

    read -p "Digite a opção desejada (1-5): " opcao

    case $opcao in
        1)
            echo "Verificando portas....:"
            lsof -i -P -n
            ;;
        2)
            echo "essa parte ainda está em desenvolvimento, pode apresentar erros"
            echo "Lembre-se, a integridade é um pilar fundamental:"
            read -p "Digite o domínio: " dominio
            echo "Domínio: $dominio"
            ;;
        3)
            echo "Um pouco sobre..."
            python3 p.py &
            ;;
        4)
            echo "Baixando dependências necessárias..."

            if command -v python3 &>/dev/null; then
                echo "Python3 encontrado. Instalando dependências..."

                if [ -f requirements.txt ]; then
                    while IFS= read -r dependencia; do
                        if python3 -m pip install "$dependencia"; then
                            echo "Dependência '$dependencia' instalada com sucesso."
                        else
                            echo "Falha ao instalar '$dependencia'. Tentando a próxima..."
                            sudo pacman -S --noconfirm "python-$dependencia" || echo "Dependência '$dependencia' não encontrada no pacman."
                        fi
                    done < requirements.txt
                else
                    echo "Arquivo requirements.txt não encontrado."
                fi
            else
                echo "Python3 não está instalado."
            fi
            ;;
        5)
            echo "Saindo..."
            cont=1 
            ;;
        *)
            echo "Opção inválida!"
            ;;
    esac
done
