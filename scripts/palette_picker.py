from palette_dict import colors


class PalettePicker(object):
    def __init__(self, palette="mint_chip", palette_type="quick5s", shift_coef=0, as_hex=False):
        self.palette = palette
        self.palette_type = palette_type
        self.shift_coef = shift_coef
        self.as_hex = as_hex

        self.colors = self.get_colors()
        print(self.colors)


    def get_colors(self):

        if self.as_hex:
            return [f"#{col}" for col in colors[f"{self.palette_type}"][f"{self.palette}"]]
        else:
            # Converts to RGB values. (0 - 255)
            return [tuple(int(col[i:i+2], 16) for i in (0, 2, 4)) for col
                    in colors[f"{self.palette_type}"][f"{self.palette}"]]


    def print_palette_sample(self):

        import matplotlib.pyplot as plt
        from matplotlib.patches import Patch

        fig, ax - plt.subplots()
        patches = [Patch(1, 1, color=color) for color in self.colors]

        plt.show()









pp = PalettePicker()
pp.print_palette_sample()
