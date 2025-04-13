from manim import *
import numpy as np

config.pixel_width = 2160 
config.pixel_height = 3840
config.frame_rate = 60

class Gibbs(Scene):
    def construct(self):
        
        title = Text("Gibbs Phenomenon", font_size=48)
        self.play(Write(title))
        self.wait(0.1)
        self.play(FadeOut(title))

        def graph(square = False, zoom = False):

            if zoom == False:
                axes = Axes(x_range=[-2, 20, 2], y_range=[-2, 5, 1], axis_config={"color": WHITE})
            else:
                axes = Axes(x_range=[10, 14, 2], y_range=[1.5, 5, 1], axis_config={"color": WHITE})

            seg = VGroup()

            A = 0.5

            for i in range(1,2):

                if square == True:

                    L = 8
                    x0 = i * L 
                    x_mid = x0 + L / 2
                    x1 = (i + 1) * L
                    y = 3

                    seg.add(Line(axes.c2p(x0, 0), axes.c2p(x0, y), color=WHITE))
                    seg.add(Line(axes.c2p(x0, y), axes.c2p(x_mid, y), color=WHITE))
                    seg.add(Line(axes.c2p(x_mid, y), axes.c2p(x_mid, 0), color=WHITE))
                    seg.add(Line(axes.c2p(x_mid, 0), axes.c2p(x1, 0), color=WHITE))

                    def fourier(t, N):
                        C = 1.5
                        return C + 6/np.pi * sum((1/(2*k-1)) * np.sin(2 * np.pi * (2*k-1) * t / L)  for k in range(1, N+1))
                    
                    fourier_curve = axes.plot(lambda x: fourier(x, 1000), x_range=[7, 15.8], color=RED)
                else:

                    L = 6
                    x0, x1 = i * L, (i + 1) * L
                    y0, y1 = 0, A * L

                    seg.add(Line(axes.c2p(x0, y0), axes.c2p(x1, y1), color=WHITE))
                    seg.add(Line(axes.c2p(x1, y1), axes.c2p(x1, y0), color=WHITE))

                    def fourier(t, N):
                        C = 1.5
                        delta_x = 3
                        return C - 3/np.pi * sum(((-1)**k / k) * np.sin(2 * np.pi * k * (t - delta_x) / L) for k in range(1, N+1))
                    fourier_curve = axes.plot(lambda x: fourier(x, 1000), x_range=[6.2, 12.4], color=RED)

                graph = VGroup(axes, seg, fourier_curve)
                return graph
            
        graph_top = graph()
        graph_bottom = graph(square = True)

        graph_bottom.shift(DOWN * 5)
        graph_top.shift(UP * 5)

        graph_top_zoom = graph(zoom = True)
        graph_bottom_zoom = graph(square = True, zoom = True)

        graph_bottom_zoom.shift(DOWN * 5)
        graph_top_zoom.shift(UP * 5)

        self.play(Create(graph_top), Create(graph_bottom), run_time = 4)
        self.wait(.5)
        self.play(Transform(graph_top, graph_top_zoom), Transform(graph_bottom, graph_bottom_zoom), run_time = 3)

        circle = Circle(radius = 1.5, color = TEAL)
        circle.move_to(graph_bottom.get_center() + UP * 0.5 + RIGHT * 5.5)
        circle2 = Circle(radius = 1.5, color = TEAL)
        circle2.move_to(graph_top.get_center() + DOWN * 0.5 + RIGHT * 5.5)

        self.play(Create(circle), Create(circle2), run_time = 2)
        self.wait(0.5)

        title2 = Text("Fourier Series", font_size=48).move_to(np.array([0, 7, 0]))

        sum1_bot = MathTex(r"f(t) = \sum_{k=1}^{N} \frac{2}{\pi} \frac{(-1)^{k + 1}}{k} \sin\left(2\pi kt \right)").to_edge(DOWN, buff=7)
        sum1_top = MathTex(r"f(t) = \sum_{k=0}^{N} \frac{4}{\pi} \frac{1}{2k - 1} \sin\left(2\pi(2k - 1)t \right)").to_edge(UP, buff=7)

        sum2_top = MathTex(r"f(t) = \frac{4}{\pi} \int_0^x\left[\sum_{k = 0}^N cos((2k + 1)t) \right] dt").to_edge(UP, buff=7)
        sum2_bot = MathTex(r"f(t) = 4\int_0^x \left[(-1)^{k + 1} cos(2\pi kt)\right] dt").to_edge(DOWN, buff=7)

        sum3_top = MathTex(r"f(t) = \frac{4}{\pi} \int_0^x \frac{sin((2N + 2)t)}{(2sin(t)} dt").to_edge(UP, buff=7)
        sum3_bot = MathTex(r"f(t) = 2\int_0^x \frac{sin((2N + 1)\pi t)}{(2sin(\pi t)} dt").to_edge(DOWN, buff=7)

        sum4_top = MathTex(r"f(\frac{\pi}{2N + 2}) = \frac{4}{\pi} \int_0^{\pi} \frac{sin(\mathring{t})}{2\sin \left(\frac{\mathring{t}}{2N+2}\right)} \frac{d\mathring{t}}{2N + 2}").to_edge(UP, buff=7)
        sum4_bot = MathTex(r"f(\frac{1}{2N + 1}) = 2\int_0^{\pi} \frac{sin(\mathring{t})}{sin(\frac{\mathring{t}}{2N + 1})} \frac{d\mathring{t}}{\pi(2N + 1)}").to_edge(DOWN, buff=7)

        N_inf = MathTex(r"N \rightarrow \infty", font_size=48)

        sum5_top = MathTex(r"\text{Overshoot} = \frac{4}{\pi} \int_0^{\pi} \frac{sin(\mathring{t})}{\mathring{t}} d\mathring{t}").to_edge(UP, buff=7)
        sum5_bot = MathTex(r"\text{Overshoot} = \frac{2}{\pi} \int_0^{\pi} \frac{sin(\mathring{t})}{\mathring{t}} d\mathring{t}").to_edge(DOWN, buff=7)
                
        sum6 = MathTex(r"\text{Overshoot} \approx \frac{17,9\%}{2}").center()
        
        sum7 = MathTex(r"\text{Overshoot} \approx 9\%").center()

        frame = SurroundingRectangle(sum7, color=RED, buff=0.2)

        self.play(FadeOut(circle, circle2), Write(title2), Transform(graph_top, sum1_top), Transform(graph_bottom, sum1_bot))
        self.wait(0.5)
        self.play(FadeOut(title2), Transform(graph_top, sum2_top), Transform(graph_bottom, sum2_bot), run_time = .9)
        self.play(Transform(graph_top, sum3_top), Transform(graph_bottom, sum3_bot), run_time = .9)
        self.play(Transform(graph_top, sum4_top), Transform(graph_bottom, sum4_bot), run_time = .9)

        before = VGroup(graph_top, graph_bottom)

        self.play(Transform(before, N_inf), run_time = 1.5)
        self.wait(.2)

        self.play(Transform(graph_top, sum5_top), Transform(graph_bottom, sum5_bot), run_time = 1.1)
        self.play(Transform(before, sum6), run_time = .9)
        self.play(Transform(before, sum7), Create(frame))

        self.wait(2)
