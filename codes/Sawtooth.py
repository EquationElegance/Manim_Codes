from manim import *
import numpy as np

config.pixel_height =  1920
config.pixel_width =  1080
config.frame_rate = 60

class Sawtooth(Scene):
    def construct(self):

        title = Text("Fourier Series", font_size=48)

        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        axes = Axes(
            x_range=[-2, 20, 2],
            y_range=[-2, 5, 1],
            axis_config={"color": WHITE},)
        
        A = 0.5 
        L = 6

        seg = VGroup()

        for i in range(3):
            x0, x1 = i * L, (i + 1) * L
            y0, y1 = 0, A * L

            seg.add(Line(axes.c2p(x0, y0), axes.c2p(x1, y1), color=WHITE))
            seg.add(Line(axes.c2p(x1, y1), axes.c2p(x1, y0), color=WHITE))

        def fourier_approx(t, N):
            C = 1.5 
            delta_x = 3
            return C + -3/np.pi * sum(((-1)**k / k) * np.sin(2 * np.pi * k * (t - delta_x) / L) for k in range(1, N + 1))
        
        fourier_curve = axes.plot(lambda t: fourier_approx(t, 1), x_range=[0, 18], color=RED)
        fourier_expression = MathTex(r"f(t) = \sum_{k=1}^{1} \frac{-2}{\pi} \frac{(-1)^{k}}{k} \sin\left(2\pi kt \right)").next_to(seg, UP, buff=4)

        self.play(Create(axes), run_time = 2)
        self.play(Create(seg), run_time = 2)
        self.play(Create(fourier_curve), Write(fourier_expression), run_time = 2)

        for i, N in enumerate(range(2,10)):
            
            if N == 6:
                N = 10
            elif N == 7:
                N = 50; i=3
            elif N == 8:
                N = 100; i=0

            new_expression = MathTex("f(t) = \\sum_{{k=1}}^{{{}}} \\frac{{-2}}{{\\pi}} \\frac{{(-1)^{{k}}}}{{k}} \\sin(2\\pi kt)".format(N)).next_to(seg, UP, buff=4)

            if N == 9:
                N = 500; i=0
                new_expression = MathTex(r"f(t) = \sum_{k=1}^{N} \frac{-2}{\pi} \frac{(-1)^{k}}{k} \sin\left(2\pi kt \right)").next_to(seg, UP, buff=4)
            
            new_curve = axes.plot(lambda t: fourier_approx(t, N), x_range=[0, 18], color=RED)
            self.play(Transform(fourier_curve, new_curve), Transform(fourier_expression, new_expression), run_time = 1 - i/7)

        x_focus = 0
        y_focus = 3
        circle = []
        inter = Text("?", font_size=72, color = TEAL)
        end = Text("To be continued...", font_size=72, color = WHITE)
        ca = [None, None, None]

        for i in range(3):
            
            ca[i] = inter.copy()
            x_focus += 6
            circle.append(Circle(radius=0.5, color=TEAL))
            circle[i].move_to(axes.c2p(x_focus, y_focus))
            ca[i].move_to(circle[i]).shift(UP + RIGHT)

            self.play(Create(circle[i]), Write(ca[i]))
        self.wait(0.5)

        all_things = VGroup(circle, ca, fourier_curve, fourier_expression, seg, axes)
        
        self.play(Write(end), FadeOut(all_things))
        self.wait(1) 
