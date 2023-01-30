# TODO: create a pop-up that pops twice a day, at 10:00 and at 16:00
#   in the pop-up, I can pick a number from 0 to 5 on how much eye strain I feel.
#   the result is recorded with the time and date and appended to a csv file.
import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

from input_monitor import InputMonitor
from recurring_timer import RecurringTimer


class WidgetLogger:
    def __init__(self, widget, csv_file):
        self.widget = widget
        self.csv_file = csv_file

    def log_widget_value(self):
        datetime_str = str(datetime.now())
        value = self.widget.get()
        with open(self.csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime_str, value])


def create_enter_eye_strain_level_message_box():
    messagebox.showinfo(
        'Reminder',
        'Please enter your eye strain level'
    )


def main():
    window = tk.Tk()
    label_healthy_eyes = tk.Label(text='Healthy eyes!')
    label_healthy_eyes.pack()

    label_strain_level = tk.Label(text='Enter your eye-strain levels. 0 is None, 5 is high.')
    label_strain_level.pack()

    spinbox_strain_level = tk.Spinbox(from_=0, to=5)
    spinbox_strain_level.pack()

    strain_level_logger = WidgetLogger(spinbox_strain_level, 'data/strain_levels.csv')
    button_record = tk.Button(text='Record', command=strain_level_logger.log_widget_value)
    button_record.pack()

    enter_eye_strain_level_interval = timedelta(hours=3)
    enter_eye_strain_level_alarm = RecurringTimer(
        delay=enter_eye_strain_level_interval,
        callback=create_enter_eye_strain_level_message_box
    )

    input_monitor = InputMonitor('data/input_monitor.csv', frequency_in_sec=60)

    enter_eye_strain_level_alarm.start()
    input_monitor.start()
    window.mainloop()


if __name__ == '__main__':
    main()
