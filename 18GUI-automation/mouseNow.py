import pyautogui

# print(pyautogui.size())

print('push CTRL-C to stop')
try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        position_str += ' RBG: (' + str(str(pixel_color[0])).rjust(3)
        position_str += ', ' + str(pixel_color[1]).rjust(3)
        position_str += ', ' + str(pixel_color[2]).rjust(3) + ')'
        print(position_str, end = '')
        # \bはバックスペース文字。*によりposition_str文字列全体を消すことが出来る。
        print('\b' * len(position_str), end='', flush=True) # \bを表示するときはflushをTrueにしなきゃいけないらしい

except KeyboardInterrupt:
    print('\nprogram aborted!')



# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)


# for i in range(10):
#     pyautogui.moveRel(100, 0, duration=0.25)
#     pyautogui.moveRel(0, 100, duration=0.25)
#     pyautogui.moveRel(-100, 0, duration=0.25)
#     pyautogui.moveRel(0, -100, duration=0.25)
