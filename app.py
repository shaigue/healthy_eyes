# TODO: create a pop-up that pops twice a day, at 10:00 and at 16:00
#   in the pop-up, I can pick a number from 0 to 5 on how much eye strain I feel.
#   the result is recorded with the time and date and appended to a csv file.
import csv
import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from datetime import datetime, timedelta
import logging

from input_monitor import InputMonitor
from recurring_timer import RecurringTimer
from symptoms_menu import get_symptoms_window

logging.basicConfig(level=logging.INFO)


def create_enter_eye_strain_level_message_box():
    messagebox.showinfo(
        'Reminder',
        'Please enter your eye strain level'
    )


def main():
    enter_eye_strain_level_interval = timedelta(hours=3)
    enter_eye_strain_level_alarm = RecurringTimer(
        delay=enter_eye_strain_level_interval,
        callback=create_enter_eye_strain_level_message_box
    )

    activity_interval = timedelta(minutes=1)
    input_monitor = InputMonitor(
        csv_file='data/input_monitor.csv',
        activity_interval=activity_interval,
    )

    symptoms_logfile = Path('data/symptoms.log')
    window = get_symptoms_window(symptoms_logfile)

    enter_eye_strain_level_alarm.start()
    input_monitor.start()
    window.mainloop()


if __name__ == '__main__':
    main()
