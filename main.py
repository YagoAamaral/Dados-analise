import speedtest
import time

contador = 0

while True:
    contador += 1

    print(f"\nExecução #{contador}")
    print("             ")
    print("Testando conexão.......")
    print("Isso pode demorar um pouco baseado no seu ping....;)")
    
    
    test = speedtest.Speedtest()

    
    download_speed = test.download()
    upload_speed = test.upload()

    
    download_speed_mbps = download_speed / 1_000_000  
    upload_speed_mbps = upload_speed / 1_000_000  

    
    print(f"Velocidade da conexão: Download = {download_speed_mbps:.2f} Mbps, Upload = {upload_speed_mbps:.2f} Mbps")

    
    time.sleep(10)

    
    if contador == 1:
        break
