import json
import logging
import tkinter as tk
from datetime import datetime
from pathlib import Path

LEVELS = ['none', 'weak', 'strong']
SYMPTOMS = [
    'dryness, itchiness, redness',
    'difficulty focusing, blurry vision, light sensitivity',
    'neck pain, shoulder pain, back pain',
    'headaches'
]

logging.basicConfig(level=logging.INFO)


def get_symptoms_window(symptom_level_logfile: Path):
    window = tk.Tk()
    symptom_to_variable = {symptom: tk.IntVar(window, value=0) for symptom in SYMPTOMS}
    for symptom_i, symptom in enumerate(SYMPTOMS):
        tk.Label(master=window, text=symptom).grid(row=symptom_i, column=0, sticky='W')
        for level_i, level in enumerate(LEVELS):
            radio_button = tk.Radiobutton(
                master=window,
                text=level,
                variable=symptom_to_variable[symptom],
                value=level_i
            )
            radio_button.grid(row=symptom_i, column=level_i+1, sticky='W')

    def get_symptoms_levels() -> dict:
        return {symptom: symptom_to_variable[symptom].get() for symptom in SYMPTOMS}

    def record_symptoms_levels():
        data = get_symptoms_levels()
        logging.info(f'symptoms recorded {data}')
        data['time'] = str(datetime.now())
        with symptom_level_logfile.open('a') as f:
            f.write(json.dumps(data))
            f.write('\n')

    submit_button = tk.Button(
        master=window,
        text='submit',
        command=record_symptoms_levels
    )
    submit_button.grid(row=len(SYMPTOMS), column=0)
    return window


def main():
    dummy_logfile = Path('data/dummy.txt')
    window = get_symptoms_window(symptom_level_logfile=dummy_logfile)
    window.mainloop()


if __name__ == '__main__':
    main()
