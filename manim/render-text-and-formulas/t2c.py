from manim import *


class Textt2cExample(Scene):
    def construct(self):
        t2indices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2words = Text('World', t2c={'rl': RED}).next_to(t2indices, RIGHT)
        self.add(t2indices, t2words)