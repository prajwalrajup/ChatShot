import pyautogui,time,mouse,cv2
print('Beginning the logging process')
i = 1

def mouse_scroll():
    x,y = mouse.get_position()
    mouse.move(500, 250, absolute=True, duration=0)
    mouse.wheel(2)
    mouse.move(x, y, absolute=True, duration=0)


def screen():
    global i

    img = pyautogui.screenshot(region=(410,133,955,542))  # screen x = 410,133,1365,675
    img.save('result_images/'+str(i)+".jpg")
    i += 1
    print(i)



#screen()
while True:

    try:
        time.sleep(1)
        if (pyautogui.locate('compare_images/loding.jpg', pyautogui.screenshot(region=(863,144 ,45,45)),grayscale=False, confidence=0.9)):
            print('no screenshot')
        else:  # refresh 860, 147,911,190
            screen()
            mouse_scroll()

        #mouse.wheel(1)

    except KeyboardInterrupt:
        print ('Pausing...  (Hit ENTER to continue, type quit to exit.)')

        try:
            while True :

                print("",end="")

        except KeyboardInterrupt:
            print ('Resuming...')
