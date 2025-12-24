from kb import Keyboard
from kmk.keys import KC

keyboard = Keyboard()

# Key layout:
# SW1 -> Undo
# SW2 -> Redo
# SW3 -> Volume Up
# SW4 -> Volume Down
keyboard.keymap = [
    [
        KC.LCTL(KC.Z),   # Undo
        KC.LCTL(KC.Y),   # Redo
        KC.VOLU,         # Volume Up
        KC.VOLD          # Volume Down
    ]
]

if __name__ == "__main__":
    keyboard.go()

