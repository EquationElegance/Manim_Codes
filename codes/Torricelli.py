from manim import *
import numpy as np

config.pixel_width = 2160
config.pixel_height = 3840
config.frame_rate = 60

class Torricelli(Scene):
    def construct(self):

        title = Text("Torricelli's Law", font_size=48)

        self.play(Write(title))
        self.wait(0.1)
        self.play(FadeOut(title))

        tank_lines = VGroup(
            Line([-1,2,0], [1,2,0], color=BLUE),
            Line([1 , 2, 0], [1, -1.5, 0], color=BLUE),
            Line([1, -1.5, 0], [1.3, -1.5, 0], color=BLUE),
            Line([1.3, -1.8, 0], [1, -1.8, 0], color=BLUE),
            Line([1, -1.8, 0], [1, -2, 0], color=BLUE),
            Line([1, -2, 0], [-1, -2, 0], color=BLUE),
            Line([-1, -2, 0], [-1, 2, 0], color=BLUE),
        )

        water = Polygon(
            [-0.9, 1.5, 0],[0.9, 1.5, 0],
            [0.9, -1.9, 0], [-0.9, -1.9, 0],
            color=BLUE, fill_opacity=0.5
        )

        self.play(Create(tank_lines))
        self.play(FadeIn(water))

        tank_group = VGroup(tank_lines, water)

        water_point = Dot(point = [0, 1.5, 0], color=RED)
        water_label = MathTex("A").next_to(water_point, UP)
        water_point2 = Dot(point = [1.3, -1.65, 0], color=RED)
        water_label2 = MathTex("B").next_to(water_point2, RIGHT * 0.5)

        arrow_h = DoubleArrow(start = [-1.2, 1.5, 0], end = [-1.2, -1.65, 0], color=WHITE)
        h_label = MathTex("h").next_to(arrow_h, LEFT)
        lvl = DashedLine(start = [-1.2, -1.65, 0], end = [1.3, -1.65, 0], color=WHITE)
        
        self.play(Create(water_point), Create(water_label), Create(water_point2), Create(water_label2), Create(arrow_h), Create(h_label), Create(lvl))

        points_list, points_inv_list, water_states, water_levels = [], [], [], []

        for j in np.arange(1,15,0.5):

            points = [[1.3 + i/10, -1.6 - (i/10)** (1+j/10), 0] for i in range(50)]
            points_inv = [[1.3 + i/10, -1.7 - (i/10)** (1+j/10), 0] for i in range(50)]
            
            points_inv.reverse()
            points_list.append(points)
            points_inv_list.append(points_inv)

            new_water_level = 1.5 - j *0.2
            new_water = Polygon(
                [-0.9, new_water_level, 0],[0.9, new_water_level, 0],
                [0.9, -1.9, 0], [-0.9, -1.9, 0],
                color=BLUE, fill_opacity=0.5
            )

            water_states.append(new_water)
            water_levels.append(new_water_level)

        for idx, (points, points_inv, new_water, level) in enumerate(zip(points_list, points_inv_list,water_states,water_levels)):
            
            new_jet = Polygon([0.9, -1.6, 0], *points, *points_inv, [0.9, -1.7, 0], color=BLUE, fill_opacity=0.5)
            new_arrow = DoubleArrow(start = [-1.2, level, 0], end = [-1.2, -1.65, 0], color=WHITE)
            new_h_label = MathTex("h").next_to(new_arrow, LEFT)

            if idx == 0:

                jet = new_jet

                self.play(FadeIn(jet), Transform(water, new_water), water_point.animate.move_to([0, level, 0]), run_time = 0.0166667)
                self.remove(arrow_h, h_label)

                arrow_h = DoubleArrow(start = [-1.2, level, 0], end = [-1.2, -1.65, 0], color=WHITE)
                h_label = MathTex("h").next_to(arrow_h, LEFT)

                self.add(arrow_h, h_label)
                water.become(new_water)

            else : 

                self.play(
                    Transform(jet, new_jet),
                    Transform(water, new_water),
                    Transform(arrow_h, new_arrow),
                    Transform(h_label, new_h_label),

                    water_point.animate.move_to([0, level, 0]),
                    water_label.animate.move_to([0, level + 0.8, 0]),
                    run_time = 0.0166667
                )

                jet.become(new_jet)
                water.become(new_water)

        self.wait(0.5)

        self.play(ApplyMethod(water_label.shift, UP * 8),
                  ApplyMethod(water_label2.shift, UP * 8),
                  ApplyMethod(water_point.shift, UP * 8),
                  ApplyMethod(water_point2.shift, UP * 8),
                  ApplyMethod(arrow_h.shift, UP * 8),
                    ApplyMethod(h_label.shift, UP * 8),
                    ApplyMethod(lvl.shift, UP * 8),
                    ApplyMethod(tank_group.shift, UP * 8),
                    ApplyMethod(jet.shift, UP * 8),
        )

        alll = VGroup(water_label, water_label2, water_point, water_point2, arrow_h, h_label, lvl, tank_group, jet)

        title = Text("Bernoulli's Law", font_size=48).move_to(UP * 2)
        bernou = MathTex(r"\frac{p_A}{\rho} + \frac{v_A^2}{2} + gz_A = \frac{p_B}{\rho} + \frac{v_B^2}{2} + gz_B")
        bernou.next_to(title, DOWN *  4)

        self.play(Write(title), Write(bernou))

        eqalpressure = MathTex(r"p_A = p_B = p_{atm} \quad ||")
        high = MathTex(r"z_A = z_B = h").next_to(eqalpressure, RIGHT * 4)
        hypothesis = Text("Hypothesis : ", font_size=48).next_to(bernou, DOWN * 5)
        highpressure = VGroup(eqalpressure, high).next_to(hypothesis, DOWN * 4)

        self.play(Write(hypothesis), Write(highpressure))

        velocity = MathTex(r"\frac{v_A^2}{2} + gh = \frac{v_B^2}{2}").next_to(title, DOWN * 4)

        self.play(FadeOut(highpressure), Transform(bernou, velocity))

        eqcont = Text("Continuity equation :", font_size=48).next_to(bernou, DOWN * 5)

        continuity_eq = MathTex(r"\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0")
        continuity_eq2 = MathTex(r"\implies v_A S_A = v_B S_B")
        continuity = VGroup(continuity_eq, continuity_eq2).next_to(hypothesis, DOWN * 4)
        continuity_eq2.next_to(continuity_eq, RIGHT)

        torri = Text("Torricelli's Law : ", font_size=48).move_to(UP * 2)
        both = MathTex(r" gh = \frac{v_A^2}{2} \left(1 - \frac{S_B^2}{S_A^2}\right)").next_to(title, DOWN * 4)

        self.play(Transform(hypothesis, eqcont), Write(continuity))
        self.play(Transform(bernou, both))
        self.wait(0.5)

        final = MathTex(r"v_A = \sqrt{\frac{2gh}{1 - \frac{S_B^2}{S_A^2}}}").next_to(title, DOWN * 4)

        self.play(Transform(bernou, final), Transform(title, torri))

        hypothesis2 = Text("Hypothesis : ", font_size=48).next_to(bernou, DOWN * 5)
        area = MathTex(r"S_A \gg S_B").next_to(hypothesis2, DOWN *4)

        self.play(Transform(hypothesis, hypothesis2), Transform(continuity, area))

        final2 = MathTex(r"v_A = \sqrt{2gh}", font_size=48).next_to(title, DOWN * 4)
        frame = SurroundingRectangle(final2, color=RED, buff=0.2)

        self.play(FadeOut(hypothesis), FadeOut(continuity), Transform(bernou, final2), Create(frame),FadeOut(alll))

        self.wait(3)
