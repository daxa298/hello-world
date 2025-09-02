from manim import *

class AnimatingMethods(Scene):
    def construct(self):
        grid = VGroup(*[Tex(r"$\pi$") for _ in range(100)])
        grid.arrange_in_grid(rows=10, cols=10, buff=0.2)
        grid.set_height(4)
        self.add(grid)

        # 你可以通过.animate语法来动画化物件变换方法
        self.play(grid.animate.shift(LEFT))


        # 这种方法会在mobject的初始状态和应用该方法后的状态间进行插值
        # 在本例中，调用grid.shift(LEFT)会将grid向左移动一个单位

        # 这种用法可以用在任何方法上，包括设置颜色
        self.play(grid.animate.set_color(YELLOW))
        self.wait()
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        # 方法Mobject.apply_complex_function允许应用任意的复函数
        # 将把Mobject的所有点的坐标看作复mai=数

        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()
