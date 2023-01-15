import cv2
import pyautogui
import time

def calibrate():
    while True:
        # Solicitar ao usuário para ajustar a sensibilidade do cursor
        sensitivity = input("Insira a sensibilidade do cursor (ex: 0.1): ")
        try:
            sensitivity = float(sensitivity)
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número decimal válido.")
    while True:
        # Solicitar ao usuário para ajustar a distância entre o centro do olho e a posição atual do cursor
        distance = input("Insira a distância entre o centro do olho e a posição atual do cursor (ex: 0.1): ")
        try:
            distance = float(distance)
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número decimal válido.")

    return sensitivity, distance


try:
    # Inicializar a câmera
    cap = cv2.VideoCapture(0)
except:
    print("Erro ao acessar a câmera. Certifique-se de que a câmera esteja conectada e habilitada.")
    exit()

try:
    # Carregando o Classificador de olhos e boca
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")
except:
    print("Erro ao carregar os arquivos Haar em cascata. Certifique-se de que os arquivos haarcascade_eye.xml e haarcascade_mcs_mouth.xml estejam no mesmo diretório do script.")
    exit()


# Definir o limite de frame
frame_rate = 10

# Chama a função de calibragem antes de iniciar a captura de frames
sensitivity, distance = calibrate()

# Iniciar a captura de frames
while True:
    # Aumentar a velocidade de captura de frame
    start_time = time.time()

    ret, frame = cap.read()

    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar os olhos e boca na imagem
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    mouths = mouth_cascade.detectMultiScale(gray, 1.3, 5)

    # Desenhar retângulos em torno dos olhos e boca detectados
    if len(eyes) > 0:
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            eye_center = (ex + ew / 2, ey + eh / 2)

            # Calcular a posição do cursor do mouse
            mouse_x, mouse_y = pyautogui.position()

            # Calcular a distância entre o centro do olho e a posição atual do cursor do mouse
            dx = eye_center[0] - mouse_x
            dy = eye_center[1] - mouse_y

            # Mover o cursor do mouse usando a sensibilidade e distância ajustadas pelo usuário
            pyautogui.moveRel(dx * sensitivity, dy * sensitivity, duration=0.2)

            # Se a boca estiver aberta, clique
            if eh > 20:
                pyautogui.click()
                pyautogui.scroll(200)

            if len(mouths) > 0:
                for (mx, my, mw, mh) in mouths:
                    cv2.rectangle(frame, (mx, my), (mx + mw, my + mh), (255, 0, 0), 2)

                    # Se a boca estiver aberta, clique
                    if mh > 20:
                        pyautogui.click()
                        pyautogui.scroll(200)

    # Mostrar o frame capturado
    cv2.imshow("Frame", frame)

    # Controlar o frame rate
    end_time = time.time()
    if (end_time - start_time) < 1.0 / frame_rate:
        time.sleep(1.0 / frame_rate - (end_time - start_time))

    # Parar a execução do loop com a tecla "q"
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Quando tudo estiver feito, libere os recursos
cap.release()
cv2.destroyAllWindows()
