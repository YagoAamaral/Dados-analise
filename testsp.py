import os
import platform

def test_ping():
    
    host = "google.com"
    
    
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 4 {host}"
    
    
    response = os.system(command)
    
    if response == 0:
        print("Conexão ativa com sucesso!")
        print("finalizando testes")
    else:
        print("Não foi possível se conectar ao site.")

test_ping()
