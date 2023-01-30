# TODO: add logging
import csv
from datetime import datetime, timedelta
import logging

from pynput import keyboard, mouse

from recurring_timer import RecurringTimer

logging.basicConfig(level=logging.INFO)


class InputMonitor:
    def __init__(self, csv_file: str, activity_interval: timedelta):
        self.activity_recorded = False
        self.activity_interval = activity_interval
        self.mouse_listener = mouse.Listener(
            on_move=self.__track_input,
            on_click=self.__track_input,
            on_scroll=self.__track_input
        )
        self.keyboard_listener = keyboard.Listener(
            on_press=self.__track_input,
            on_release=self.__track_input
        )
        self.recording_timer = RecurringTimer(
            delay=self.activity_interval,
            callback=self.__record_activity
        )
        self.csv_file = csv_file

    def __record_activity(self):
        datetime_str = str(datetime.now())
        with open(self.csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime_str, self.activity_recorded])
        logging.info(f'activity recorded {self.activity_recorded} at {datetime_str}')
        self.activity_recorded = False

    def __track_input(self, *args):
        self.activity_recorded = True

    def start(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.recording_timer.start()
