from manim import *


class AddPackageLatex(Scene):
    def construct(self):
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=my_template,
            font_size=144,
        )
        self.add(tex)