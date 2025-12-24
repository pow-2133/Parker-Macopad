import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.RGB import RGB


class Keyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # 4 direct pins (switches wired to GND)
        self.pins = (
            board.GP26,  # SW1
            board.GP27,  # SW2
            board.GP28,  # SW3
            board.GP29,  # SW4
        )

        # Map each physical key to a logical position
        self.coord_mapping = [0, 1, 2, 3]

        # SK6812 MINI LEDs (NeoPixel compatible)
        rgb = RGB(
            pixel_pin=board.GP6,  # LED data pin
            num_pixels=2,         # two LEDs
            val_default=60        # brightness
        )
        self.extensions.append(rgb)
