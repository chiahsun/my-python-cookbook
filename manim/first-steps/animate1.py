from manim import *

class CircleAnnouncement(Scene):

    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        announcement = Text("Let's draw a circle")

        self.play(Write(announcement))
        self.wait()

        # self.add(announcement.next_to(blue_circle, UP, buff=0.5))
        self.play(announcement.animate.next_to(blue_circle, UP, buff=0.5))
        self.play(Create(blue_circle))