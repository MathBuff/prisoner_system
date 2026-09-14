from pynput import keyboard
from queue import Queue

keys = Queue()

SPECIAL_KEYS = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "enter",
    keyboard.Key.backspace: "backspace",
    keyboard.Key.tab: "tab",
    keyboard.Key.esc: "escape",

    keyboard.Key.up: "up",
    keyboard.Key.down: "down",
    keyboard.Key.left: "left",
    keyboard.Key.right: "right",

    keyboard.Key.home: "home",
    keyboard.Key.end: "end",
    keyboard.Key.delete: "delete",
    keyboard.Key.insert: "insert",

    keyboard.Key.page_up: "page_up",
    keyboard.Key.page_down: "page_down",

    keyboard.Key.shift: "shift",
    keyboard.Key.shift_l: "shift",
    keyboard.Key.shift_r: "shift",

    keyboard.Key.ctrl: "control",
    keyboard.Key.ctrl_l: "control",
    keyboard.Key.ctrl_r: "control",

    keyboard.Key.alt: "alt",
    keyboard.Key.alt_l: "alt",
    keyboard.Key.alt_r: "alt",

    keyboard.Key.caps_lock: "caps_lock",
    keyboard.Key.num_lock: "num_lock",
    keyboard.Key.scroll_lock: "scroll_lock",

    keyboard.Key.f1: "f1",
    keyboard.Key.f2: "f2",
    keyboard.Key.f3: "f3",
    keyboard.Key.f4: "f4",
    keyboard.Key.f5: "f5",
    keyboard.Key.f6: "f6",
    keyboard.Key.f7: "f7",
    keyboard.Key.f8: "f8",
    keyboard.Key.f9: "f9",
    keyboard.Key.f10: "f10",
    keyboard.Key.f11: "f11",
    keyboard.Key.f12: "f12",
}


def on_press(key):
    if key in SPECIAL_KEYS:
        keys.put(SPECIAL_KEYS[key])
    else:
        try:
            keys.put(key.char)
        except AttributeError:
            keys.put("unknown")


listener = keyboard.Listener(on_press=on_press)
listener.start()


def getch():
    return keys.get()


while True:
    key = getch()
    print(key)

    if key == "q":
        break

listener.stop()