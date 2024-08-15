
from manim import *

class Simpleanim(Scene):
    def construct(self):
        # Setting objects
        c = Circle(2, color=RED, fill_opacity=0.1)
        title = Text("Ala's Random Animation", font_size=20, font="ITALIC").shift(UP * 0.3)
        subtitle = Text("(First)", font="ITALIC").shift(DOWN * 0.5)
        after_intro_text = Text("Hello and welcome to this show", font_size=15, font="ITALIC")
        body_text = Text("See the animation ...", font="ITALIC", font_size=10)
        s = Square(color=BLUE, side_length=1.0)
        s1 = Square(color=BLUE, side_length=1.0)

        txt_1 = Tex("square01", font_size=20)
        txt_2 = Tex("square02", font_size=20)

        # Graph config
        axes = Axes(
            x_range=[0,3,1],
            y_range=[0,2,0.5],  
            x_length=3,
            y_length=3,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        ).add_coordinates()
        
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        graph = axes.plot(lambda x: x**2, x_range=[-4, 4], color=BLUE)
        graphing = VGroup(axes, graph, axis_labels)
        # Animating objects
        self.camera.background_color = BLACK
        self.play(DrawBorderThenFill(c), run_time=1)
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
        self.play(DrawBorderThenFill(s1), run_time=1)
        self.play(s1.animate.move_to(LEFT * 3 + UP * 1))
        self.wait()
        self.play(Write(txt_1))
        self.play(txt_1.animate.move_to(RIGHT * 3 + UP * 1.8))
        self.play(Write(txt_2))
        self.play(txt_2.animate.move_to(LEFT * 3 + UP * 1.8))
        self.wait()
        self.play(FadeOut(txt_1, txt_2, s, s1))
        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
