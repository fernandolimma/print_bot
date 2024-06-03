import pyautogui
import schedule
import time
import os

from winotify import Notification

pyautogui.PAUSE = 2



def tarefa():

    print("Iniciando processo. Não mexa!")    

    time.sleep(4) #tela de notificação no windows
    notificacao = Notification(app_id="Catch Oil", title="Aviso de automação!!!", msg="Não utilize este equipamento até o processo terminar!")
    notificacao.show()

    # faz print de tela e salva a imagem
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screenshot.png")

    # abre o chrome
    pyautogui.press("winleft")
    time.sleep(4)
    pyautogui.write("chrome")
    time.sleep(4)
    pyautogui.press("enter")

    # escolhe qual conta do chrome será aberta, caso o crome só tenha uma conta, retire esse código
    time.sleep(4)
    pyautogui.click (x=916, y=339) #posição para click da conta do chrome

    # abre o google drive
    time.sleep(4)
    pyautogui.click(x=265, y=61) #posição da barra de navegação do chrome
    time.sleep(4)
    pyautogui.write("drive.google.com/drive")
    time.sleep(4)
    pyautogui.press("enter")

    #faz o up-load da imagem salva
    time.sleep(4)
    pyautogui.click(x=61, y=216) #clica no botão + novo
    time.sleep(4)
    pyautogui.click(x=186, y=260) #clica no botão upload    
    time.sleep(4)
    pyautogui.write(r"C:\GitHub\print_bot\screenshot.png") #caminho do arquivo para upload que deverá ficar na pasta da aplicação
    time.sleep(4)
    pyautogui.press("enter")
    
    # mensagem de permissão do drive para atualizar a imagem
    time.sleep(4)
    pyautogui.click(x=844, y=544)

    # atualiza a imagem
    time.sleep(4)
    pyautogui.hotkey("fn", "f5")

    # fecha o navegador
    time.sleep(4)
    pyautogui.hotkey("alt", "f4")

    time.sleep(2)
    os.unlink("screenshot.png") #exclui a última imagem

    print("Processo finalizado!")
    
# aqui especifica o intervalo que a aplicação irá rodar "em minhutos"
schedule.every(1).minutes.do(tarefa)


while True:
    schedule.run_pending()
    time.sleep(2)