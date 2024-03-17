from manim import *


# https://docs.manim.community/en/stable/tutorials/output_and_config.html#sections
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.next_section("create square")
        self.play(Transform(square, circle))
        self.next_section("transform to circle")
        self.play(FadeOut(square))
        self.next_section("fade out")

