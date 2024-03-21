from manim import *


class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex(
            r'Hello 你好 \LaTeX',
            tex_template=TexTemplateLibrary.ctex,
            font_size=144,
        )
        self.add(tex)