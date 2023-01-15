# Eye-control

Este código é uma implementação de controle de cursor de mouse com a detecção de olhos e boca usando a biblioteca OpenCV e Pyautogui.

A primeira parte do código inicializa a câmera usando a função cv2.VideoCapture(0) da biblioteca OpenCV. Ele também carrega dois classificadores, um para detectar olhos e outro para detectar bocas, a partir de arquivos XML chamados "haarcascade_eye.xml" e "haarcascade_mcs_mouth.xml", respectivamente. Se ocorrer algum problema ao acessar a câmera ou carregar os classificadores, o script imprimirá uma mensagem de erro e sairá.

Em seguida, o script chama uma função calibrate() para solicitar ao usuário que ajuste a sensibilidade do cursor e a distância entre o centro do olho e a posição atual do cursor. Isso permite que o usuário ajuste a precisão do controle de cursor de acordo com suas preferências pessoais.

A partir daí, o script entra em um loop infinito para capturar frames da câmera. Cada frame é convertido para escala de cinza e passado pelos classificadores de olhos e boca para detectar a presença de olhos e bocas na imagem. Se os classificadores detectarem olhos, o script usa as coordenadas dos olhos para calcular a distância entre o centro do olho e a posição atual do cursor do mouse. Ele então usa essa distância e a sensibilidade ajustada pelo usuário para mover o cursor do mouse. Se o classificador detectar uma boca aberta, o script fará clique e rolará para baixo.

Em resumo, este código permite que os usuários controlem o cursor do mouse com movimentos de olhos e bocas, usando a biblioteca OpenCV para detectar olhos e bocas e a biblioteca Pyautogui para controlar o cursor do mouse. Ele também permite que os usuários ajustem a sensibilidade e precisão do controle de cursor de acordo com suas preferências pessoais.
