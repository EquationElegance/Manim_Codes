from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60

class Simps(Scene):
    def construct(self):
        
        title1 = Text("Numerical Integration", font_size=48)
        title = Text("Simpson’s Rule", font_size=36).next_to(title1, DOWN , buff=0.5)

        self.play(Write(title1), run_time = .8)
        self.play(Write(title), run_time = 0.6)
        self.wait(0.1)
        self.play(FadeOut(title1), FadeOut(title))

        ax = Axes(x_range=[0, 5, 1], y_range=[0, 1.1, 0.5])

        def f(x):
            return 1 / (1 + x**2)
        
        graph = ax.plot(f, color=WHITE)
        
        a = 1
        b = 3

        a_point = ax.input_to_graph_point(a, graph)
        b_point = ax.input_to_graph_point(b, graph)

        left_line = ax.get_vertical_line(ax.input_to_graph_point(a, graph), color=PURE_RED)
        right_line = ax.get_vertical_line(ax.input_to_graph_point(b, graph), color=PURE_RED)

        label_a = MathTex("a", font_size = 72).next_to(ax.c2p(a, 0), DOWN, buff=0.5)
        label_b = MathTex("b", font_size = 72).next_to(ax.c2p(b, 0), DOWN, buff=0.5)

        self.play(Create(ax), Create(graph), Write(label_a), Write(label_b))
        self.wait(0.5)
        self.play(Create(left_line), Create(right_line))

        graph_limited = ax.plot(f, color=WHITE, x_range=[a, b])

        self.play(Transform(graph, graph_limited))

        area = ax.get_area(graph, x_range=[a, b], color=YELLOW, opacity=0.5)

        self.play(Create(area))
        self.wait(0.5)
        self.play(area.animate.move_to(UP * 6))
        
        m = (a + b) / 2

        def parabola(x):
            fa = f(a)
            fm = f(m)
            fb = f(b)
            return fa * ((x - m) * (x - b)) / ((a - m) * (a - b)) + \
                     fm * ((x - a) * (x - b)) / ((m - a) * (m - b)) + \
                     fb * ((x - a) * (x - m)) / ((b - a) * (b - m))

        graph_parabola = ax.plot(parabola, color=RED, x_range=[a, b])
        simpson_area = ax.get_area(graph_parabola, x_range=[a, b], color=RED, opacity=0.5)

        self.play(Create(graph_parabola))
        self.play(Create(simpson_area))

        approx = MathTex(r"\approx").move_to(ORIGIN)
        all = VGroup(graph, right_line, left_line, ax, label_a, label_b, graph_parabola)

        self.play(Transform(all, approx), area.animate.next_to(approx, LEFT, buff=1), simpson_area.animate.next_to(approx, RIGHT, buff=1))
        self.wait(0.5)

        simps_formula = MathTex(r"\int_a^b f(x) dx \approx \frac{b-a}{6} \left( f(a) + 4f(m) + f(b) \right)")
        frame = SurroundingRectangle(simps_formula, color=PURE_RED, buff=.3)
        end = Text("Simpson’s Rule", font_size=36).next_to(simps_formula, UP * 4)

        self.play(FadeOut(all), Write(end), Transform(area, simps_formula), Uncreate(simpson_area))
        self.play(Create(frame))
        self.wait(0.5)
