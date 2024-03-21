from manim import *


class SimpleColor(Scene):
    def construct(self):
        col = Text("RED", color=RED)
        self.add(col)