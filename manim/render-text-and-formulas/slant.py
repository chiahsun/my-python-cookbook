from manim import *


class SlantsExample(Scene):
    def construct(self):
        # a = Text("Italic", slant=ITALIC)
        a = Text("Oblique", slant=ITALIC)
        self.add(a)