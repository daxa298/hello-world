from manim import *

class DrawCircle(Scene):
    def construct (self):
      circle = Circle()
      circle.set_fill(BLUE , opacity=0.5)
      circle.set_stroke(BLUE_E ,width = 4)
      square = Square()
      text = Text("这是一个圆形变成正方形的一个动画", font="SimHei")


      self.add(circle)
      
      self.play(Create(circle))
      self.wait()
      self.play(ReplacementTransform(circle,square))
      self.wait()
      self.play(Write(text))
      self.wait()
