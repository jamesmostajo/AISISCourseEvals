import random
import sys
import time

from pynput.keyboard import Controller as KeyboardControl
from pynput.keyboard import Key
from pynput.mouse import Button
from pynput.mouse import Controller as MouseControl

keyboard = KeyboardControl()
mouse = MouseControl()

responses = [
    # bad
    [
        "Not much",
        "The lessons were quite hard to digest",
        "Structure it in a way easier to understand",
        "Studying the topics as they weren't discussed with much detail",
        "N/A",
        "The teacher doesn't make the lessons appealing",
        "Please don't make the lessons boring",
        "N/A",
        "N/A",
    ],
    # good
    [
        "The lessons are entertaining",
        "Nothing, the course was enjoyable overall",
        "Nothing, the course was enjoyable overall",
        "Some topics are slightly difficult but manageable",
        "The teacher was very good at simplifying difficult concepts",
        "The pace was sometimes too fast",
        "Keep up the good work",
        "Reviewing the lectures before class helped me prepare for the day's lecture",
        "A difficult course can still be fun if taught properly",
    ],
]


def exec(good):
    time.sleep(2)
    mouse.position = (200, 500)
    mouse.click(Button.left, 1)
    for i in range(35):
        time.sleep(0.025)
        keyboard.press(Key.tab)
        rate = random.randint(4, 5) if good else random.randint(2, 4)
        for j in range(rate):
            keyboard.press(Key.down)
            time.sleep(0.025)

    for k in range(9):
        time.sleep(0.1)
        keyboard.press(Key.tab)
        for l in responses[good][k]:
            for m in l:
                keyboard.press(m)
                time.sleep(0.001)


if __name__ == "__main__":
    good_val = sys.argv[1]
    exec(int(good_val))
