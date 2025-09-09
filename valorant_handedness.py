from time import sleep
import mouse, keyboard

# 0 right, 1 left
hand = 0

# 1920x1080 display
def changeHand():
	keyboard.press_and_release('esc')
	sleep(0.1)
	if hand == 0:
		mouse.move(1080, 950, True)
	else:
		mouse.move(1324, 950, True)
	sleep(0.3)
	keyboard.press_and_release('esc')
	hand = (hand + 1) % 2

while (True):
	if keyboard.is_pressed('h'):
		changeHand()
	if keyboard.is_pressed('l'):
		quit()
