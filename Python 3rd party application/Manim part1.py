from manim import *

class MyScene1(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(FadeOut(square))


class MyScene3(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        dot.shift(UP * 10)
        self.play(dot.animate.move_to(UP * 10))
