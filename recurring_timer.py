import threading
import time
from collections.abc import Callable
from datetime import timedelta


class RecurringTimer:
    """This class is to enable recurring events."""
    def __init__(self, delay: timedelta, callback: Callable):
        self.delay = delay
        self.callback = callback
        self.mainloop_thread = threading.Thread(target=self.__mainloop, daemon=True)

    def __mainloop(self):
        while True:
            self.callback()
            time.sleep(self.delay.seconds)

    def start(self):
        self.mainloop_thread.start()
