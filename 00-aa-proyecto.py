import cv2
import mediapipe as mp
import serial


WINDOW_NAME = "RECOGNITION"
ID_CAMERA = 0
ARDUINO_PORT = "COM3"

try:
    puerto = serial.Serial(ARDUINO_PORT, 9600, timeout=1)
except:
    print("No se pudo establecer conexión")


mp_dibujo = mp.solutions.drawing_utils
mp_manos = mp.solutions.hands
objeto_hands = mp_manos.Hands(
    static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5
)

CAP = cv2.VideoCapture(ID_CAMERA)
cv2.namedWindow(WINDOW_NAME)


def getCoords(landmark):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    return {"y": int(landmark.y * WINDOW_HEIGHT), "x": int(landmark.x * WINDOW_WIDTH)}


def hasLowFingers(arr: list, center):
    c = 0
    for e in arr:
        if e["y"] <= center["y"]:
            c += 1
    if c > 0:
        return False
    else:
        return True


def hasUpFingers(arr: list, center):
    c = 0
    for e in arr:
        if e["y"] > center["y"]:
            c += 1
    if c > 0:
        return False
    else:
        return True


def hasSame(arr: list, pulgar):
    c = 0
    for e in arr:
        if e["y"] < pulgar["y"] - 20:
            c += 1
        elif e["y"] > pulgar["y"] + 20:
            c += 1
    if c > 0:
        return False
    else:
        return True


OPTIONS = ["A", "E", "I", "O", "U"]
fingers = {
    "pulgar": 0,
    "indice": 0,
    "medio": 0,
    "anular": 0,
    "menique": 0,
}
CENTRO = 0
CURRENT = None
REFERENCES = [0, 1]
""" 
Pulgar = 4
Indice = 8
Medio = 12
Anular = 16
Menique = 20
"""
WINDOW_WIDTH = 0
WINDOW_HEIGHT = 0

while True:
    ret, frame = CAP.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = objeto_hands.process(rgb_frame)
    WINDOW_HEIGHT, WINDOW_WIDTH, _ = frame.shape
    if resultados.multi_hand_landmarks:
        for puntos in resultados.multi_hand_landmarks:
            mp_dibujo.draw_landmarks(frame, puntos, mp_manos.HAND_CONNECTIONS)
            fingers["pulgar"] = getCoords(puntos.landmark[4])
            fingers["indice"] = getCoords(puntos.landmark[8])
            fingers["medio"] = getCoords(puntos.landmark[12])
            fingers["anular"] = getCoords(puntos.landmark[16])
            fingers["menique"] = getCoords(puntos.landmark[20])
            REFERENCES[0] = getCoords(puntos.landmark[10])
            REFERENCES[1] = getCoords(puntos.landmark[11])
            CENTRO = getCoords(puntos.landmark[5])
            if (
                hasLowFingers(
                    [
                        fingers["anular"],
                        fingers["indice"],
                        fingers["medio"],
                        fingers["menique"],
                    ],
                    CENTRO,
                )
                and fingers["pulgar"]["y"] < REFERENCES[1]["y"]
            ):
                CURRENT = OPTIONS[0]
            elif hasLowFingers(
                [
                    fingers["anular"],
                    fingers["indice"],
                    fingers["medio"],
                    fingers["menique"],
                ],
                CENTRO,
            ) and (
                fingers["pulgar"]["y"] >= REFERENCES[1]["y"]
                or fingers["pulgar"]["y"] >= REFERENCES[0]["y"]
            ):
                CURRENT = OPTIONS[1]
            elif (
                hasLowFingers(
                    [
                        fingers["anular"],
                        fingers["indice"],
                        fingers["medio"],
                    ],
                    CENTRO,
                )
                and (
                    fingers["pulgar"]["y"] >= REFERENCES[1]["y"]
                    or fingers["pulgar"]["y"] <= REFERENCES[0]["y"]
                )
                and fingers["menique"]["y"] < CENTRO["y"]
            ):
                CURRENT = OPTIONS[2]
            elif hasSame(
                [
                    fingers["anular"],
                    fingers["medio"],
                    fingers["menique"],
                    fingers["indice"],
                ],
                fingers["pulgar"],
            ):
                CURRENT = OPTIONS[3]
            elif (
                hasLowFingers(
                    [
                        fingers["anular"],
                        fingers["menique"],
                    ],
                    CENTRO,
                )
                and hasUpFingers([fingers["indice"], fingers["medio"]], CENTRO)
                and (
                    fingers["pulgar"]["y"] >= REFERENCES[1]["y"]
                    or fingers["pulgar"]["y"] <= REFERENCES[0]["y"]
                )
            ):
                CURRENT = OPTIONS[4]
            else:
                CURRENT = "..."

            try:
                puerto.write(f"{CURRENT}".encode())
            except:
                # print("No se pueden enviar los datos")
                print()

            cv2.putText(
                frame,
                CURRENT,
                (100, 100),
                cv2.FONT_ITALIC,
                1,
                (87, 50, 255),
                thickness=3,
            )

    cv2.imshow(WINDOW_NAME, frame)

    salir = cv2.waitKey(1)
    if salir == 27:
        break

CAP.release()
cv2.destroyAllWindows()


""" 
CÓDIGO DE ARDUINO = 
const byte R = 3, G = 5, B = 6;
char color = '';

void setup() {
  Serial.begin(9600);
  while(!Serial){}
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);
}

void loop() {
  if(Serial.available()){
    color = Serial.read();
  }

  switch(color){
      case 'A':{
        analogWrite(R,0)
        analogWrite(G,0)
        analogWrite(B,255);
        break;
      }
      case 'E':{
        analogWrite(R,0)
        analogWrite(G,255)
        analogWrite(B,0);
        break;
      }
      case 'I':{
        analogWrite(R,255)
        analogWrite(G,0)
        analogWrite(B,0);
        break;
      }
      case 'O':{
        analogWrite(R,255)
        analogWrite(G,255)
        analogWrite(B,10);
        break;
      }
      case 'U':{
        analogWrite(R,0)
        analogWrite(G,255)
        analogWrite(B,255);
        break;
      }
      default:{
        analogWrite(R,0)
        analogWrite(G,0)
        analogWrite(B,0);
        break;
      }
  }
}

"""
