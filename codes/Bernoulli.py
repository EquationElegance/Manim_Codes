from manim import *

config.pixel_width = 2160
config.pixel_height = 1080
config.frame_width = 60

class Bernoulli(Scene):
    def construct(self):
        title = Text("Bernoulli's Principle", font_size=48)
        self.play(Write(title))
        self.wait(0.1)
        self.play(FadeOut(title))

        cylinder = Cylinder(radius=1, height=5, resolution=(30,30), color = BLACK, fill_opacity=1, stroke_color = WHITE)
        cylinder.rotate(PI/2, axis = Y_AXIS)
        
        section1 = DashedLine(start=LEFT * 0.5 + UP, end = LEFT * 0.5 + DOWN, color = WHITE)
        section2 = DashedLine(start=RIGHT * 0.5 + UP, end = RIGHT * 0.5 + DOWN, color = WHITE)

        label_A = MathTex("A").next_to(section1,LEFT)
        dx_arrow = MathTex("\\longleftrightarrow").move_to(DOWN * 1.2)
        dx_label =  MathTex("dx").move_to(DOWN * 1.5)
        rho_label =  MathTex("\\rho").next_to(cylinder, UP)
        cylinder.set_fill(BLACK, opacity=0.5)

        self.play(Create(cylinder))
        self.play(Create(section1), Create(section2))
        self.play(Write(label_A), Write(dx_arrow), Write(dx_label), Write(rho_label))

        self.play(cylinder.animate.shift(UP * 6),
                  section1.animate.shift(UP * 6),
                  section2.animate.shift(UP * 6),
                  label_A.animate.shift(UP * 6),
                  dx_arrow.animate.shift(UP * 6),
                  dx_label.animate.shift(UP * 6),
                  rho_label.animate.shift(UP * 6))
        
        theorem_statement = MathTex(r"\text{Newton's $2^{nd} Law :$}")
        newton_law = MathTex(r"\vec{F} = m \vec{\frac{dv}{dt}}")
        newton2 = MathTex(r"\rho A dx \frac{dv}{dt} = - A dp")
        newton3 = MathTex(r"\rho \frac{dv}{dt} = - \frac{dp}{dx}")

        theorem_statement.next_to(cylinder, DOWN * 15)
        newton_law.next_to(theorem_statement, DOWN * 5)
        newton2.next_to(theorem_statement, DOWN * 5)
        newton3.next_to(theorem_statement, DOWN * 5)

        self.play(Write(theorem_statement),Write(newton_law))
        self.play(Transform(newton_law, newton2))

        frame = SurroundingRectangle(newton3, color = RED, buff = 0.2)
        self.play(Transform(newton_law, newton3),Create(frame))

        speed = MathTex(r"\frac{dv}{dt}").next_to(newton3, DOWN * 4)
        speed2 = MathTex(r"\frac{dv}{dx}\frac{dx}{dt}").next_to(newton3, DOWN * 4)
        speed3 = MathTex(r"\frac{d}{dx}\left(\frac{v^2}{2}\right)").next_to(newton3, DOWN * 4)

        self.play(Write(speed))
        self.play(Transform(speed, speed2))
        self.play(Transform(speed, speed3))

        final_newton = MathTex(r"\rho \frac{d}{dx}\left(\frac{v^2}{2}\right) = - \frac{dp}{dx}")
        bernou = MathTex(r"\text{Bernoulli's Law : }").next_to(final_newton, UP)
        bernou2 = MathTex(r"\int_0^x \rho \frac{d}{dx}\left(\frac{v^2}{2}\right) dx = - \int_0^x \frac{dp}{dx} dx").next_to(theorem_statement, DOWN * 5)
        bernou3 = MathTex(r"\rho \left(\frac{v^2}{2}\right) + p = \text{constant}").next_to(theorem_statement, DOWN * 5)
        total = VGroup(speed, newton_law)

        self.play(FadeOut(frame))
        self.play(Transform(total, final_newton), Transform(theorem_statement, bernou))
        self.wait(0.5)
        self.play(Transform(total, bernou2))
        self.wait(0.5)

        self.play(Transform(total, bernou3))
        frame = SurroundingRectangle(bernou3, color = RED, buff = 0.2)
        self.play(Create(frame))
        self.wait(0.5)
