import keyboard
import os
from pynput.keyboard import Key, Listener
import numpy as np
class get_data_from_key:
    def __init__(self):
        self.keys = set()
        self.line = np.zeros(14)
        self.on = False
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release
        ) as listener:
            listener.join()

    def start(self):
        if not self.on:
            i=0
            while os.path.isfile("./data/data_" + str('{0:03d}'.format(i))):i += 1
            self.data_file_txt = "./data/data_" + str('{0:03d}'.format(i))
            self.line = np.zeros(14)
            self.on=True

    def end(self):
        if self.on: self.on=False

    def on_press(self, key):
        if self.on:
            if key == Key.up:               self.line[10] = 1
            elif key == Key.down:           self.line[11] = 1
            elif key == Key.left:           self.line[12] = 1
            elif key == Key.right:          self.line[13] = 1
            elif key.char== 'e':            self.end()
            elif key.char in '1234567890':  self.line[int(key.char) - 1] = 1
            print(self.line)
            ori_txt=np.load(self.data_file_txt)
            ori_txt=np.concat([ori_txt, self.line], axis = 0)
            np.save(self.data_file_txt,ori_txt)
        else:
            try:
                if key.char== 's':                self.start()
            except:
                print('it is not a start key!')

    def on_release(self, key):
        if self.on:
            if key == Key.up:           self.line[10] = 0
            elif key == Key.down:       self.line[11] = 0
            elif key == Key.left:       self.line[12] = 0
            elif key == Key.right:      self.line[13] = 0
            elif key.char in '1234567890':
                self.line[int(key.char) - 1] = 0


if __name__ == '__main__':
    #print("start of data.")
    print('[1 2 3 4 5 6 7 8 9 0 u d r l]')
    get_data_from_key()
