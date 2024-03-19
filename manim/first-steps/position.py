from manim import *


class HelloCircle(Scene):
    def construct(self):
        circle = Circle()
        blue_circle = circle.set_color(BLUE).set_opacity(0.5)

        label = Text("A wild circle appears!")
        label.next_to(blue_circle, DOWN, buff=0.5)
        # https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html
        # label.shift(RIGHT)
        # label.to_edge(UP)
        # label.to_corner(RIGHT)

        self.play(Create(blue_circle), Write(label))
        self.wait()