
from manim import *

class Createlyscene(Scene):
    def construct(self):
        # Setting objects
        c = Circle(2, color=RED, fill_opacity=0.1)
        title = Tex("Random Animation", font_size=30).shift(UP * 0.3)
        subtitle = Tex("(First)",font_size=20,).shift(DOWN * 0.5)
        after_intro_text = Tex("Hello and welcome to this show", font_size=15)
        s = Square(color=BLUE, side_length=1.0)
        s1 = Square(color=BLUE, side_length=1.0)
        s2 = Square(color=BLUE, side_length=1.0)
        s3 = Square(color=BLUE, side_length=1.0)

        txt_1 = Tex("square01", font_size=20)
        txt_2 = Tex("square02", font_size=20)
        txt_3 = Tex("square03", font_size=20)
        txt_4 = Tex("square04", font_size=20)
  
        # Graph config
        axes = Axes(
            x_range=[-4,4,1],
            y_range=[0,16,2],  
            x_length=3,
            y_length=3,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        ).add_coordinates()
            
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        graph = axes.plot(lambda x: x**2, x_range=[-4, 4], color=BLUE)
        graphing = VGroup(axes, graph, axis_labels)

        # Logo manim : 
        
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        logo_txt = Text("This animation was created using the Manim module",font="ITALIC",font_size=15, color=BLACK)
        logo_txt.move_to(DOWN*2.2)

        # Animating objects

         # Animating logo
        self.camera.background_color = "#ece6e2"
        self.play(FadeIn(logo))
        self.play(FadeIn(logo_txt))
        self.wait(3)
        self.play(Uncreate(logo_txt))
        self.play(FadeOut(logo))
        self.wait(2)
         # Start Animation
        self.camera.background_color = BLACK
        self.play(DrawBorderThenFill(c), run_time=0.5)
        self.play(Write(title), Write(subtitle))
        self.wait()
        self.play(FadeOut(title, subtitle))
         
        self.play(c.animate.set_stroke_width(100))
        self.play(c.animate.scale(50), run_time=2)
        self.play(FadeOut(c))
        self.play(FadeIn(after_intro_text))
        self.wait()
        
        self.play(after_intro_text.animate.shift(UP * 1.2))
        self.play(Uncreate(after_intro_text))
        self.wait()
        
        self.play(DrawBorderThenFill(s), run_time=1)
        self.play(s.animate.move_to(RIGHT * 3 + UP * 1))
        self.play(DrawBorderThenFill(s1), run_time=0.5)
        self.play(s1.animate.move_to(LEFT * 3 + UP * 1))
        self.play(DrawBorderThenFill(s2), run_time=0.5)
        self.play(s2.animate.move_to(LEFT * 3 + DOWN * 1))
        self.play(DrawBorderThenFill(s3), run_time=0.5)
        self.play(s3.animate.move_to(RIGHT * 3 + DOWN * 1))
        self.wait()
        
        self.play(Write(txt_1))
        self.play(txt_1.animate.move_to(RIGHT * 3 + UP * 1))
        self.play(Write(txt_2))
        self.play(txt_2.animate.move_to(LEFT * 3 + UP * 1))
        self.play(Write(txt_3))
        self.play(txt_3.animate.move_to(LEFT * 3 + DOWN * 1))
        self.play(txt_4.animate.move_to(RIGHT * 3 + DOWN * 1))
        self.wait()
        self.play(FadeOut(txt_1, txt_2, s, s1))
        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.wait()

        



