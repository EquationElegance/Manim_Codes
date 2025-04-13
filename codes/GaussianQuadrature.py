from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60

def f(x):
    return 1 / (1 + x**2)

def lagrange_basis(j, x_nodes):
    def basis(x):
        result = 1
        for i, xi in enumerate(x_nodes):
            if i != j:
                result *= (x - xi) / (x_nodes[j] - xi)
        return result
    return basis

class GaussQuad(Scene):
    def construct(self):
        self.gaussian_quadrature_plot(n=5)

    def gaussian_quadrature_plot(self, n, a=1, b=3):

        title1 = Text("Numerical Integration", font_size=48)
        title2 = Text("Gaussian Quadrature", font_size=36).next_to(title1, DOWN, buff=0.5)

        self.play(Write(title1), Write(title2))
        self.wait(0.3)
        self.play(FadeOut(title1), FadeOut(title2))

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1.1, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": False}
        ).to_edge(DOWN)

        graph = ax.plot(f, color=WHITE)
        
        label_a = MathTex("a").next_to(ax.c2p(a, 0), DOWN)
        label_b = MathTex("b").next_to(ax.c2p(b, 0), DOWN)

        line_a = ax.get_vertical_line(ax.input_to_graph_point(a, graph), color=PURE_RED)
        line_b = ax.get_vertical_line(ax.input_to_graph_point(b, graph), color=PURE_RED)

        self.play(Create(ax), Create(graph))
        self.play(Create(line_a), Create(line_b), Write(label_a), Write(label_b))

        graph_limited = ax.plot(f, x_range=[a, b], color=WHITE)
        area = ax.get_area(graph_limited, x_range=[a, b], color=YELLOW, opacity=0.5)

        self.play(Transform(graph, graph_limited))
        self.play(Create(area))
        self.wait(0.5)
        self.play(area.animate.shift(DOWN * 5))

        xi, wi = np.polynomial.legendre.leggauss(n)
        x_nodes = 0.5 * (b - a) * xi + 0.5 * (a + b)
        f_nodes = f(x_nodes)

        dots = VGroup(*[
            Dot(point=ax.c2p(x, f(x)), color=RED)
            for x in x_nodes
        ])

        self.play(FadeIn(dots))

        lagrange_graphs = VGroup()
        colors = color_gradient([BLUE, GREEN, YELLOW, PURPLE, TEAL], n)

        local = Text("Local approximation for each node", font_size=28).move_to(UP * 4)

        for j in range(n):
            Lj = lagrange_basis(j, x_nodes)
            fj = f_nodes[j]
            poly = lambda x, j=j: fj * Lj(x)

            graph_poly = ax.plot(poly, color=colors[j], x_range=[a, b])
            lagrange_graphs.add(graph_poly)

        self.wait(0.3)
        self.play(*[Create(g) for g in lagrange_graphs], Write(local))
        self.wait(1)

        global_approx = Text("Global approximation over the whole interval", font_size=28).move_to(UP * 4)

        def P(x):
            total = 0
            for j in range(n):
                Lj = lagrange_basis(j, x_nodes)
                total += f_nodes[j] * Lj(x)
            return total
        
        interp_graph = ax.plot(P, color=ORANGE, x_range=[a, b])

        self.play(*[Uncreate(g) for g in lagrange_graphs], Create(interp_graph), Transform(local, global_approx))
        self.wait(1)

        gauss_area = ax.get_area(interp_graph, x_range=[a, b], color=ORANGE, opacity=0.5)

        self.play(Create(gauss_area))
        self.wait(1)

        all_thing = VGroup(ax, graph, line_a, line_b, label_a, label_b, dots, local, interp_graph)
        approx = MathTex(r"\approx").move_to(ORIGIN)

        self.play(Transform(all_thing, approx), gauss_area.animate.next_to(approx, RIGHT, buff=0.5), area.animate.next_to(approx, LEFT, buff=0.5))
        self.wait(1)

        inte = MathTex(r"\int_a^b f(x) \, dx \approx \frac{b-a}{2} \sum_{i=1}^{n} w_i f\left(\frac{b-a}{2} \xi_i + \frac{a+b}{2}\right)").move_to(ORIGIN)
        frame = SurroundingRectangle(inte, color=PURE_RED, buff=0.2)
        gaussian = Text("Gaussian Quadrature", font_size=36).next_to(inte, UP * 4)

        self.play(Write(gaussian), Transform(all_thing, inte), Uncreate(gauss_area), Uncreate(area))
        self.play(Create(frame))
        self.wait(3)
