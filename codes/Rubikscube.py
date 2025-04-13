from manim import *
from manim_rubikscube import *

config.pixel_width = 320
config.pixel_height = 640
config.frame_rate = 10

class Cube(ThreeDScene):
    def construct(self):
        
        title = Text("Rubik's Cube", font_size=48).move_to(ORIGIN)

        self.play( Write(title))
        self.wait(.1)
        self.play(FadeOut(title))

        cube = RubiksCube().scale(0.6)
        cube.move_to(ORIGIN).rotate(45*DEGREES ,axis=UP).rotate(30*DEGREES ,axis=RIGHT)

        self.renderer.camera.frame_center = cube.get_center()

        state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube.set_state(state)

        self.play(Create(cube))

        eight_corners = Text("8 corners", font_size=48).move_to(UP * 6)

        self.play(Write(eight_corners))
        self.play(
            Indicate(cube.cubies[0, 0, 0]),
            Indicate(cube.cubies[0, 0, 2]),
            Indicate(cube.cubies[2, 0, 0]),
            Indicate(cube.cubies[0, 2, 0]),
            Indicate(cube.cubies[2, 2, 2]),
            Indicate(cube.cubies[2, 0, 2]),
            Indicate(cube.cubies[0, 2, 2]),
            Indicate(cube.cubies[2, 2, 0]), run_time=2
        )

        corner1 = cube.cubies[0, 0, 0].copy()
        corner1.rotate(90*DEGREES ,axis=UP).rotate(210*DEGREES ,axis=OUT).rotate(PI/6 ,axis=RIGHT)
        corner1[2].set_fill("#009B48") # green left
        corner1[3].set_fill("#B90000") # red right

        corner2 = corner1.copy()
        corner2[1].set_fill("#B90000") # red top
        corner2[2].set_fill("#FFD500") # yellow left
        corner2[3].set_fill("#009B48") # green right

        corner3 = corner1.copy()
        corner3[1].set_fill("#009B48") # green top
        corner3[2].set_fill("#B90000") # red left
        corner3[3].set_fill("#FFD500")  # yellow right

        all_corners = VGroup(corner1, corner2, corner3).arrange(RIGHT, buff=0.5)

        arange = Text("Ways to arrange 8 corners :", font_size = 28).move_to(UP * 7)
        arange_math = MathTex(r"8! = 40, 320").next_to(arange, DOWN * 3)

        self.play(Transform(eight_corners, arange), Write(arange_math))
        self.wait(1)

        color_corner = Text("Each set of 3 colors has 3 possible configurations", font_size = 28).move_to(UP * 4)

        self.play(Transform(eight_corners, color_corner), Transform(cube, corner2), Create(corner1), Create(corner3), FadeOut(arange_math))
        self.wait(1.5)

        arange2 = Text("The last corner is fixed by the configuartion of the others", font_size = 28).move_to(UP * 4)
        arange2_math = MathTex(r"3^7 = 2,187").next_to(arange2, DOWN * 4)

        self.play(Transform(eight_corners, arange2), Write(arange2_math))
        self.wait(1.5)

        proba = MathTex(r"3^7 \cdot 8! = 40, 320 \cdot 2,187 = 88, 179, 840").move_to(UP * 6)

        cube2 = RubiksCube().scale(0.6).move_to(ORIGIN).rotate(45*DEGREES ,axis=UP).rotate(30*DEGREES ,axis=RIGHT)
        state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube2.set_state(state)

        self.play(Transform(eight_corners, proba), Uncreate(cube), Uncreate(corner1), Uncreate(corner3), FadeOut(arange2_math), Create(cube2))
        self.wait(1.5)

        edg = Text("12 edges", font_size=48).move_to(UP * 6)

        self.play(Transform(eight_corners, edg))
        self.play(
            Indicate(cube2.cubies[0,2,1]),
            Indicate(cube2.cubies[0,1,2]),
            Indicate(cube2.cubies[1,0,2]),
            Indicate(cube2.cubies[0,1,0]),
            Indicate(cube2.cubies[1,2,0]),
            Indicate(cube2.cubies[0,0,1]),
            Indicate(cube2.cubies[2,1,2]),
            Indicate(cube2.cubies[1,2,2]),
            Indicate(cube2.cubies[2,1,1]), run_time=2
        )

        edg1 = cube2.cubies[0, 2, 1].copy()
        edg1.rotate(15*DEGREES ,axis=RIGHT).rotate(35*DEGREES ,axis=OUT).rotate(PI/6 ,axis=UP)

        edg2 = edg1.copy()
        edg2[4].set_fill("#FFD500") # yellow top
        edg2[2].set_fill("#009B48") # green left

        all_edg = VGroup(edg1, edg2).arrange(RIGHT, buff=0.5)

        edg_text = Text("Ways to arrange 12 edges :", font_size = 28).move_to(UP * 7)
        edg_math = MathTex(r"12! = 479, 001, 600").next_to(edg_text, DOWN * 3)

        self.play(Transform(eight_corners, edg_text), Write(edg_math))
        self.wait(1)

        edg_text2 = Text("Each edge has 2 possible configurations", font_size = 28).move_to(UP * 4)
        edg_text3 = MathTex(r"2^{11} = 2,048").next_to(edg_text2, DOWN * 4)
        edg_text4 = Text("The last edge is fixed by the configuration of the others", font_size = 28).move_to(UP * 4)

        self.play(Transform(eight_corners, edg_text2), Transform(cube2, edg1), Create(edg2), FadeOut(edg_math))
        self.wait(1)

        self.play(Transform(eight_corners, edg_text4), Write(edg_text3))
        self.wait(.5)

        proba2 = MathTex(r"2^{11} \cdot 12! = 479, 001, 600 \cdot 2,048 = 980, 995,276,800").move_to(ORIGIN)

        cube3 = RubiksCube().scale(0.6).move_to(ORIGIN)
        state3 = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube3.set_state(state3)

        self.play(Transform(eight_corners, proba2), Uncreate(cube2), Uncreate(edg2), FadeOut(edg_text3))
        self.wait(.5)

        half_math = MathTex(r"\frac{8! \cdot 3^7 \cdot 12! \cdot 2^{11}}{2}").move_to(ORIGIN)
        half_math2 = MathTex(r" 43,252,003,274,489,856,000").move_to(ORIGIN)

        half = Text("Since a solved cube cannot have a single corner or edge twisted,", font_size = 28).next_to(half_math, UP * 8)
        half2 = Text("we cut the number of permutations in half", font_size = 28).next_to(half_math, UP * 4)

        permutations2 = Text("43 quintillion \n\n252 quadrillion \n\n 3 trillion \n\n 274 billion \n\n 489 million \n\n 856 thousand").move_to(ORIGIN)
        permutations = Text("Number of permutations").next_to(permutations2, UP * 6)

        self.play(Transform(eight_corners, half), Write(half_math), Write(half2))
        self.wait(1)

        self.play(Transform(half_math, half_math2))
        self.wait(.5)

        self.play(Transform(eight_corners, permutations), Transform(half_math, permutations2), FadeOut(half2))
        self.wait(1)

        moves = cube3.solve_by_kociemba(state3)

        self.play(FadeOut(eight_corners))
        self.begin_3dillusion_camera_rotation(1, 60*DEGREES, 60*DEGREES)
        self.play(Create(cube3), FadeOut(half_math))

        for m in moves:
            self.play(CubeMove(cube3, m), run_time=.2)

        self.wait(3)
        self.stop_3dillusion_camera_rotation()

        self.play(Rotating(cube3, axis = OUT, radians = 2*PI, run_time = 1.5))
        self.wait(4)
