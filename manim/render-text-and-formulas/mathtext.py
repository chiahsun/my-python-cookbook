from manim import *


class MathTexDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6x^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6x^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))