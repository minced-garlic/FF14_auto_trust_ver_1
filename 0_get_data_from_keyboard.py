import keyboard
import os
from pynput.keyboard import Key, Listener
import numpy as np
class get_data_from_key:
    def __init__(self):
        self.keys = set()
        self.line = np.zeros(14, dtype=np.int32)
        self.on = False
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release
        ) as listener:
            listener.join()

    def start(self):
        if not self.on:
            i=0
            while os.path.isfile("./raw data/data_" + str('{0:03d}'.format(i))+'.npy'):i += 1
            self.data_file_txt = "./raw data/data_" + str('{0:03d}'.format(i))+'.npy'
            print('start the save!')
            self.line = np.zeros(14)
            np.save(self.data_file_txt,np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'u', 'd', 'r', 'l']))
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
            elif key.char in '123456789':   self.line[int(key.char) - 1] = 1
            elif key.char in '0':           self.line[9] = 1
            ori_txt=np.load(self.data_file_txt)
            sumof= int(np.sum([2**i*self.line[i] for i in range(14)]))
            print('{0:014b}'.format(sumof))
            ori_txt=np.hstack((ori_txt, sumof))
            np.save(self.data_file_txt,ori_txt)
        else:
            try:
                if key.char== 's':                self.start()
            except:
                print('it is not a start key!')

    def on_release(self, key):
        if self.on:
            if key == Key.up:               self.line[10] = 0
            elif key == Key.down:           self.line[11] = 0
            elif key == Key.left:           self.line[12] = 0
            elif key == Key.right:          self.line[13] = 0
            elif key.char in '0':           self.line[9] = 0
            elif key.char in '123456789':   self.line[int(key.char) - 1] = 0


if __name__ == '__main__':
    #print("start of data.")
    print('1 2 3 4 5 6 7 8 9 0 u d r l')
    get_data_from_key()
