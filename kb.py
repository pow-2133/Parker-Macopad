import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.RGB import RGB


class Keyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # 4 direct pins (each switch goes to GND)
        self.pins = (
            board.GP26,  # SW1
            board.GP27,  # SW2
            board.GP28,  # SW3
            board.GP29,  # SW4
        )

        # Map 4 physical keys to 4 logical positions
        self.coord_mapping = [0, 1, 2, 3]

        # 2x SK6812 MINI (NeoPixel-compatible)
        rgb = RGB(
            pixel_pin=board.GP6,   # LED data line
            num_pixels=2,          # D1 + D2
            val_default=60,        # brightness (0-255)
        )
        self.extensions.append(rgb)
