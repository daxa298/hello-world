# 导入Manim所有内容
from manim import *

# 创建一个简单的场景类
class HelloManim(Scene):
    def construct(self):
        # 创建文字对象，使用SimHei字体以显示中文
        text = Text("你好，Manim！", font="SimHei")

        # 使用Write动画显示文字
        self.play(Write(text))

        # 等待2秒
        self.wait(2)

       