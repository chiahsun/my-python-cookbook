from manim import *


class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)

        self.add(index_labels(text[0]))

        text[0][0].set_color(BLUE)
        text[0][1:3].set_color(YELLOW)
        text[0][3:6].set_color(RED)
        text[0][6].set_color(BLUE)
        self.add(text)
