"""
Script de debug para calibrar a detecção de rosto.
Rode este script e observe:
1. A janela mostra seu rosto com um retângulo
2. O terminal mostra os valores de X e Área
3. Mova a cabeça para esquerda/direita e veja os valores de X
4. Incline para frente e veja o valor de Área aumentar
"""
import cv2

cap = cv2.VideoCapture(0)

# Verificar resolução real da câmera
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"Resolução da câmera: {int(width)}x{int(height)}")
print(f"Centro horizontal: {int(width // 2)}")
print("-" * 50)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Variáveis para suavizar detecção
last_x = None
last_area = None
detection_count = 0
no_detection_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Espelhar
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostos
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    centro_tela = int(width // 2)
    
    if len(faces) > 0:
        detection_count += 1
        no_detection_count = 0
        
        (x, y, w, h) = faces[0]  # Pegar primeiro rosto
        area = w * h
        x_centro = x + (w // 2)
        
        # Desenhar retângulo e informações
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Linha do centro da tela
        cv2.line(frame, (centro_tela, 0), (centro_tela, int(height)), (255, 0, 0), 1)
        
        # Linha do centro do rosto
        cv2.line(frame, (x_centro, y), (x_centro, y+h), (0, 255, 255), 2)
        
        # Mostrar valores na tela
        cv2.putText(frame, f"X: {x_centro}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Area: {area}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Indicar direção
        if x_centro < centro_tela - 80:
            direcao = "ESQUERDA"
            cor = (0, 255, 255)
        elif x_centro > centro_tela + 80:
            direcao = "DIREITA"
            cor = (255, 0, 255)
        else:
            direcao = "CENTRO"
            cor = (0, 255, 0)
        
        cv2.putText(frame, direcao, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, cor, 2)
        
        # Indicar inclinação
        if area > 80000:
            cv2.putText(frame, "INCLINADO (CONFIRMAR)", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Print apenas a cada 10 frames para não sobrecarregar
        if detection_count % 10 == 0:
            print(f"X: {x_centro:4d} | Area: {area:6d} | Direção: {direcao}")
        
        last_x = x_centro
        last_area = area
    else:
        no_detection_count += 1
        if no_detection_count % 30 == 0:
            print("Nenhum rosto detectado...")
        cv2.putText(frame, "SEM DETECCAO", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.imshow('Debug Camera - Pressione Q para sair', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("\n" + "=" * 50)
print("RESUMO:")
print(f"Resolução: {int(width)}x{int(height)}")
print(f"Centro da tela: {int(width // 2)}")
if last_x and last_area:
    print(f"Último X detectado: {last_x}")
    print(f"Última Área detectada: {last_area}")
print("=" * 50)
