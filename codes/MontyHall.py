from manim import * 
import numpy as np

config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 60

class MontyHall(Scene):
    def construct(self):

        title = Text("Monty Hall Problem", font_size=48)

        self.play(Write(title))
        self.wait(0.1)
        self.play(FadeOut(title))

        doors = VGroup(
            Rectangle(width=2, height=3, color=YELLOW_D).shift(LEFT*3),
            Rectangle(width=2, height=3, color=YELLOW_D),
            Rectangle(width=2, height=3, color=YELLOW_D).shift(RIGHT*3),
            Dot(color=BLACK).shift(LEFT*3.7).set_z_index(1),
            Dot(color=BLACK).shift(LEFT*.7).set_z_index(1),
            Dot(color=BLACK).shift(RIGHT*3.7).set_z_index(1),
        )

        doors2 = VGroup(
            Rectangle(width=1.8, height=2.8, color=YELLOW_D, fill_opacity = 1).shift(LEFT*3),
            Rectangle(width=1.8, height=2.8, color=YELLOW_D, fill_opacity = 1),
            Rectangle(width=1.8, height=2.8, color=YELLOW_D, fill_opacity = 1).shift(RIGHT*3)
        )

        labels = VGroup(
            Text("1").next_to(doors[0], DOWN * 2),
            Text("2").next_to(doors[1], DOWN * 2),
            Text("3").next_to(doors[2], DOWN * 2)
        )

        doors_open = VGroup(
            Polygon([0.8,1.45,0], [0.8,-1.45,0], [1.4,-1.7,0], [1.4,1.4, 0], color=YELLOW_D, fill_opacity = 1).shift(LEFT*3),
            Polygon([0.8,1.45,0], [0.8,-1.45,0], [1.4,-1.7,0], [1.4,1.4, 0], color=YELLOW_D, fill_opacity = 1),
            Polygon([0.8,1.45,0], [0.8,-1.45,0], [1.4,-1.7,0], [1.4,1.4, 0], color=YELLOW_D, fill_opacity = 1).shift(RIGHT*3)
        )

        knobs = VGroup(
            Dot(color=BLACK, radius = 0.1).shift(LEFT*1.8).set_z_index(1),
            Dot(color=BLACK, radius = 0.1).shift(RIGHT*1.2).set_z_index(1),
            Dot(color=BLACK, radius = 0.1).shift(RIGHT*4.2).set_z_index(1)
        )

        goats = Text("2 Goats and 1 Car", font_size=36).to_edge(UP)

        prob1 = MathTex(r"P_{car} = \frac{1}{3}").next_to(doors2[0], DOWN * 10)
        prob2 = MathTex(r"P_{car} = \frac{1}{3}").next_to(doors2[1], DOWN * 10)
        prob3 = MathTex(r"P_{car} = \frac{1}{3}").next_to(doors2[2], DOWN * 10)

        arrow1 = Arrow(labels[0].get_bottom(), prob1.get_top(), buff=0.5, color=WHITE)
        arrow2 = Arrow(labels[1].get_bottom(), prob2.get_top(), buff=0.5, color=WHITE)
        arrow3 = Arrow(labels[2].get_bottom(), prob3.get_top(), buff=0.5, color=WHITE)

        """
        Insert your images here
        
        imgr = ImageMobject("").scale(0.2).shift(RIGHT*3).set_z_index(-1)
        imgc = ImageMobject("").scale(0.2).shift(LEFT*3).set_z_index(-1)
        imgl = ImageMobject("").scale(0.2).set_z_index(-1)
        
        """

        self.play(Create(doors), Create(doors2), Write(labels), Write(goats), Write(prob1), Write(prob2), Write(prob3), 
                  Create(arrow1), Create(arrow2), Create(arrow3))
        
        self.wait(1)

        choose = Text("Choose a Door", font_size=36).to_edge(UP)

        choice = doors[0].copy().set_stroke(color = PURE_GREEN, width = 8)

        self.play(Transform(goats, choose))
        self.wait(.5)
        self.play(Create(choice))

        lost = Text("I will open a door with a goat behind it", font_size=36).to_edge(UP)
        change_text = Text("Now, do you want to switch door ?", font_size=36).to_edge(UP)

        self.play(Transform(goats, lost))
        self.wait(1)
        self.play(Transform(doors2[2], doors_open[2]), Transform(doors[5], knobs[2])) #, FadeIn(imgr)
        self.wait(2)
        self.play(Transform(goats, change_text))
        self.wait(1)

        frame = Rectangle(width=6, height=4.5, color=PURE_RED).shift(RIGHT * 1.8 + DOWN * .5)

        all = VGroup(arrow2, arrow3, prob2, prob3)

        prob4 = MathTex(r"P_{car} = \frac{2}{3}").next_to(frame.get_bottom(), DOWN * 10)
        prob5 = MathTex(r"P_{car} = \frac{2}{3}").next_to(doors2[1], DOWN * 10)
        prob6 = MathTex(r"P_{car} = 0").next_to(doors2[2], LEFT * .3 + DOWN * 10)

        arrow4 = Arrow(frame.get_bottom(), prob4.get_top(), buff=0.5, color=WHITE)
        arrow5 = Arrow(labels[1].get_bottom(), prob5.get_top(), buff=0.5, color=WHITE)
        arrow6 = Arrow(labels[2].get_bottom(), prob6.get_top(), buff=0.5, color=WHITE)

        ap = VGroup(arrow4, prob4)
        ap2 = VGroup(arrow5, prob5, arrow6, prob6)

        highlight = doors[1].copy().set_stroke(color = PURE_GREEN, width = 8)

        self.play(Transform(choice, highlight), 
                  Create(frame))
        self.play(Transform(all, ap), 
        )
        self.wait(1)
        self.play(FadeOut(frame), 
                  Transform(all, ap2), 
        )
        self.wait(1)

        congrats = Text("Congratulations ! ", font_size=36).to_edge(UP)

        self.play(Transform(goats, congrats), Transform(doors2,doors_open), Transform(doors[3], knobs[0]), 
                  Transform(doors[4], knobs[1])) #, FadeIn(imgc,imgl)
        
        self.wait(3)
