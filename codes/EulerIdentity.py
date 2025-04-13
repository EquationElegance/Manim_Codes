from manim import *
import math
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_rate = 30

class Euler(Scene):
    def construct(self):
        
        title = Text("Euler's Identity", font_size=48)

        self.play(Write(title))
        self.wait(.5)
        self.play(FadeOut(title))

        axes = Axes(x_range=[-2,4,1], y_range=[-2,10,1], tips=False)

        label_expo = MathTex("e^x").move_to(UP * 3  + RIGHT * 3.5).scale(1.5)
        graph = axes.plot(lambda x: np.exp(x), stroke_width = 4)
        labels = axes.get_axis_labels(Text("x").scale(0.7), Text("y").scale(0.7))

        self.play(Create(axes), Write(labels), Create(graph), Write(label_expo))
        self.wait(1)

        taylor_title = Text("Taylor Series Approximation", font_size=48).move_to(UP * 8)
        taylor1 = MathTex(r"e^x \approx 1 + x").move_to(UP * 6)
        taylor2 = MathTex(r"e^x \approx 1 + x + \frac{x^2}{2!}").move_to(UP * 6 )
        taylor3 = MathTex(r"e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!}").move_to(UP * 6)

        def taylor_approximation(x, n):
            return sum([x**k/math.factorial(k) for k in range(n+1)])
        
        for N in range(1,8):

            if N==5: N=10
            if N==6: N=50
            if N==7: N=100

            taylor_sum = MathTex("e^{{x}} \\approx \\sum_{{k=0}}^{{{}}} \\frac{{x^k}}{{k!}}".format(N)).move_to(UP * 6)
            taylor_sum_exact = MathTex(r"e^{x} = \sum_{k=0}^{N} \frac{x^k}{k!} ").move_to(UP * 6)

            new_taylor_curve = axes.plot(lambda x: taylor_approximation(x, N), stroke_width = 2, color=PURE_RED)

            if N== 1:
                taylor_curve = new_taylor_curve
                self.play(Create(taylor_curve), Transform(label_expo, taylor1), Write(taylor_title))
            elif N==2:
                self.play(Transform(taylor_curve, new_taylor_curve), Transform(label_expo, taylor2), run_time = .7)
            elif N==3:
                self.play(Transform(taylor_curve, new_taylor_curve), Transform(label_expo, taylor3), run_time = .7)
            elif N==100:
                self.play(Transform(taylor_curve, new_taylor_curve), Transform(label_expo, taylor_sum_exact), run_time = .8)
            else:
                self.play(Transform(taylor_curve, new_taylor_curve), Transform(label_expo, taylor_sum), run_time = .7)
                

        all_curves = VGroup(taylor_curve, graph, taylor_title)

        axes2 = ComplexPlane(x_range=[-1.5,1.5,0.5], y_range=[-1.5,1.5,0.5], background_line_style={"stroke_opacity": 0.4}).add_coordinates(font_size = 12).scale(2)

        curve = ParametricFunction(lambda t : np.array([-np.cos(t), -np.sin(t), 0]), t_range=[0, TAU], stroke_width = 4).scale(2)

        label = MathTex("e^{ix} ").next_to(curve.get_start(), RIGHT * 2 + UP * 2)
        final2 = MathTex(r"e^{ix} + 1 = 0").move_to(ORIGIN)

        euler_formula = Text("Euler's Formula", font_size=48).move_to(UP * 8)
        euler_identity = Text("Euler's Identity", font_size=48).next_to(final2, UP * 4)

        eipi = MathTex(r"e^{ix} = \sum_{k=0}^{N} \frac{(ix)^k}{k!}").next_to(euler_formula, DOWN * 4)
        eipi2 = MathTex(r"e^{ix} = \sum_{k=0}^{N} \frac{(ix)^k}{k!} + i \sum_{k=0}^{N} \frac{(x^k}{k!}").next_to(euler_formula, DOWN * 4)
        eipi3 = MathTex(r"e^{ix} = \cos(x) + i \sin(x)").next_to(euler_formula, DOWN * 4)

        xpi = MathTex(r"x = \pi").next_to(euler_formula, DOWN * 4)
        final = MathTex(r"e^{i\pi} = -1").move_to(ORIGIN)

        frame = SurroundingRectangle(eipi3, color=PURE_RED, buff=.2)
        frame2 = SurroundingRectangle(final2, color=PURE_RED, buff=.2)

        self.play(FadeOut(labels), Transform(axes, axes2), Transform(label_expo, label), Transform(all_curves, curve))
        self.wait(1)

        self.play(Write(euler_formula), Transform(label_expo, eipi), run_time = 1.2)
        self.play(Transform(label_expo, eipi2), run_time = 1)
        self.play(Create(frame), Transform(label_expo, eipi3), run_time = 1.2)

        test = VGroup(euler_formula, label_expo, frame)

        self.play(Transform(test, xpi))

        dot = Dot(color=PURE_RED).scale(2)
        dot.move_to(curve.point_from_proportion(.5))

        self.play(MoveAlongPath(dot, curve, rate_func = linear), run_time = 2)

        self.play(FadeOut(all_curves))

        all = VGroup(dot, axes, label_expo, euler_formula, frame)
        allfinal = VGroup(final2, euler_identity)

        self.play(Transform(all, final))
        self.wait(1)
        self.play(Transform(all, allfinal), Create(frame2))
        self.wait(3)
