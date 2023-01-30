import csv
import threading
from datetime import datetime
from time import sleep

from pynput import keyboard, mouse
from threading import Thread


class InputMonitor:
    def __init__(self, csv_file: str, frequency_in_sec: int = 1, ):
        self.recorded = False
        self.frequency_in_sec = frequency_in_sec
        self.mouse_listener = mouse.Listener(
            on_move=self.__record_input,
            on_click=self.__record_input,
            on_scroll=self.__record_input
        )
        self.keyboard_listener = keyboard.Listener(
            on_press=self.__record_input,
            on_release=self.__record_input
        )
        self.mainloop_thread = Thread(target=self.__mainloop, daemon=True)
        self.csv_file = csv_file

    def __mainloop(self):
        while True:
            datetime_str = str(datetime.now())
            with open(self.csv_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([datetime_str, self.recorded])
            self.recorded = False
            sleep(self.frequency_in_sec)

    def __record_input(self, *args):
        self.recorded = True

    def start(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.mainloop_thread.start()


if __name__ == "__main__":
    x = InputMonitor('dummy_time_recorder.csv')
    x.start()
    while True:
        sleep(1)
