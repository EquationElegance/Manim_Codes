from manim import * 
import numpy as np

config.pixel_width = 2160
config.pixel_height = 3840
config.frame_rate = 60

class SquareWave(Scene):
    def construct(self):
        
        title = Text("Fourier Series", font_size=48)
        subtitle = Text("Square Wave", font_size=36).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(0.1)
        self.play(FadeOut(title), FadeOut(subtitle))

        axes = Axes( x_range=[-2, 24, 2], y_range=[-2, 5, 1], axis_config={"color": WHITE})
                              
        self.play(Create(axes), run_time = 2)

        L = 8
        num_periods = 3
        y = 3

        square_wave = VGroup()

        for i in range(num_periods):

            x0 = i * L
            x_mid = i * L + L / 2
            x1 = (i + 1) * L

            square_wave.add(Line(axes.c2p(x0, y), axes.c2p(x_mid, y), color=WHITE))
            square_wave.add(Line(axes.c2p(x_mid, y), axes.c2p(x_mid, 0), color=WHITE))
            square_wave.add(Line(axes.c2p(x_mid, 0), axes.c2p(x1, 0), color=WHITE))

            if i < num_periods - 1:
                square_wave.add(Line(axes.c2p(x1, 0), axes.c2p(x1, y), color=WHITE))

        self.play(Create(square_wave), run_time = 2)

        def fourier_approx(t, N):
            C = 1.5
            return C + 6/np.pi * sum((1/(2*k-1)) * np.sin(2 * np.pi * (2*k-1) * (t)/L ) for k in range(1, N + 1))
        
        fourier_curve = axes.plot(lambda t: fourier_approx(t, 1), x_range=[0, 23], color=RED)
        fourier_expression = MathTex(r"f(t) = \sum_{k=1}^{N} \frac{4}{\pi} \frac{1}{2k-1} \sin\left(2\pi(2k-1)t\right)").next_to(square_wave, UP, buff=4)

        self.play(Create(fourier_curve), Write(fourier_expression), run_time = 2)

        for i, N in enumerate(range(2, 10)):

            if N == 6 : N = 10
            elif N == 7 : N = 50; i = 3
            elif N == 8 : N = 100; i = 0

            new_expression = MathTex("f(t) = \\sum_{{k=1}}^{{{}}} \\frac{{4}}{{\\pi}} \\frac{{1}}{{2k-1}} \\sin(2\\pi(2k-1)t)".format(N)).next_to(square_wave, UP, buff=4)

            if N == 9:
                N = 1000; i = 0
                new_expression = MathTex(r"f(t) = \sum_{k=1}^{N} \frac{4}{\pi} \frac{1}{2k-1} \sin\left(2\pi(2k-1)t\right)").next_to(square_wave, UP, buff=4)

            new_curve = axes.plot(lambda t: fourier_approx(t, N), x_range=[0, 23], color=RED)

            self.play(Transform(fourier_curve, new_curve), Transform(fourier_expression, new_expression), run_time = 1 - i / 7)

        frame = SurroundingRectangle(fourier_expression, color=RED, buff=0.2)

        self.play(Create(frame))

        x_focus = 0
        y_focus = 3

        circles = []
        ca = [None, None, None]

        inter = Text("?", font_size=72, color=WHITE)
        end = Text("To be continued...", font_size=72, color=WHITE)

        for i in range(3):
            ca[i] = inter.copy()

            x_focus += 8 

            if i == 0:
                x_focus = 8/2
            
            circles.append(Circle(radius=0.5, color=TEAL))
            circles[i].move_to(axes.c2p(x_focus, y_focus))
            ca[i].move_to(circles[i]).shift(UP + RIGHT)

            self.play(Create(circles[i]), Create(ca[i]))

        self.wait(0.5)
        self.play(Write(end), FadeOut(frame, circles[0], ca[0], circles[1], ca[1], circles[2], ca[2], axes, fourier_curve, fourier_expression))
        self.wait(2)
