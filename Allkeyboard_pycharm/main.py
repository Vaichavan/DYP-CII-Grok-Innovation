import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 4000)  # Increase width of the camera screen
cap.set(4, 900)   # Set height to a reduced value (adjust as needed)

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I"],
        ["O", "P", "A", "S", "D", "F", "G", "H"],
        ["J", "K" ,"L", ";" ,"Z", "X", "C", "V"],
        ["B", "N", "M", ",", ".", "/", "Bk","Sp"]]

finalText = ""
keyboard = Controller()

class Button():
    def __init__(self, pos, text, size=[60, 60]):  # Smaller button size
        self.pos = pos
        self.size = size
        self.text = text

buttonList = []
buttonWidth = 2  # Smaller button width
buttonHeight = 5  # Smaller button height
spaceButtonHeight = 50  # Increased height for space bar button
gap = 75  # Increased gap between buttons
x_offset = -60  # Adjust the x offset to reduce space from the left
y_offset = -60   # Remove top margin

for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        x = j * (buttonWidth + gap) + gap + x_offset
        y = i * (buttonHeight + gap) + gap + y_offset

        if key == "Sp":
            buttonList.append(Button([x, y], " ", size=[buttonWidth * 5 + gap * 4, spaceButtonHeight]))  # Customize size for space
        else:
            buttonList.append(Button([x, y], key))

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 10, y + 40),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 10, y + 40),
                            cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                l, _, _ = detector.findDistance(8, 12, img, draw=False)
                print(l)

                if l < 50:  # Adjust the distance threshold for "Enter" key
                    if button.text == "Enter":
                        keyboard.press('\n')  # Press Enter
                    elif button.text == "Bk":
                        keyboard.press('\b')  # Press Backspace
                    elif button.text == "Sp":
                        keyboard.press(' ')  # Press Space
                    else:
                        keyboard.press(button.text)

                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 10, y + 40),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                    finalText += button.text
                    sleep(0.25)

    cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
