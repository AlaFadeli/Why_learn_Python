
from manim import *

class WhyLearnPy(Scene):
    def construct(self):
        # Configs
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        Text.set_default(font="UBUNTU")
        # Logo Elements
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)
        logo.move_to(ORIGIN)
        
        # Text Elements
        logo_txt = Text("This animation was created using the Manim module", font="Ubuntu", font_size=15, color=BLACK)
        logo_txt.move_to(DOWN * 2.2)
        
        # FIRST SHOW
        text = Text("Why learning Python and coding?", font_size=18)
        dot1 = Dot(color=WHITE, radius=0.08)
        dot2 = Dot(color=WHITE, radius=0.08) 
        dot3 = Dot(color=WHITE, radius=0.08) 
        dot4 = Dot(color=WHITE, radius=0.08) 
        dot5 = Dot(color=WHITE, radius=0.08) 

        r1 = Text("Versatility and Wide Applicability", font_size=12, font="Ubuntu").scale(1)
        r2 = Text("High Demand and Career Opportunities", font_size=12, font="Ubuntu")
        r3 = Text("Problem-Solving Skills", font_size=12, font="Ubuntu")
        r4 = Text("Data Analysis and Visualization", font_size=12, font="Ubuntu")
        r5 = Text("Creativity and Innovation", font_size=12, font="Ubuntu")

        line = Line(start=LEFT*0.1, end=RIGHT*0.2, color=WHITE)
        line.move_to(UP*1.6 + LEFT*4.3)
        highlight = Line(start=line.get_start(), end=line.get_end(), color=YELLOW, stroke_width=4)
        
        # R1 show:
        txt1 = Text("Web Development", font_size=10, font="UBUNTU")
        txt1.move_to(UP*0.1)
        
        code_web = Code(
            code="""
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return '<h1>Welcome to My Simple Web App</h1><p>This is a simple Flask app.</p>'

# Define a route for the about page
@app.route('/about')
def about():
    return '<h1>About</h1><p>This page tells you about the app.</p>'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
""",
            language="python",
            style="vim",
            font_size=10,
            line_spacing=0.7,
            insert_line_no=True
        )
        code_web.move_to(ORIGIN)

        # Animations
        self.camera.background_color = "#ece6e2"
        self.play(FadeIn(logo))
        self.play(FadeIn(logo_txt))
        self.wait(3)
        
        self.play(Uncreate(logo_txt))
        self.play(FadeOut(logo))
        self.wait(2)
        
        self.camera.background_color = BLACK
        self.play(Write(text))
        self.wait(1)

        # Move the text to the top right
        self.play(text.animate.shift(UP * 2 + LEFT * 3))
        self.wait(2)

        self.play(FadeIn(dot1))
        self.play(dot1.animate.shift(UP * 1.6 + LEFT * 4.1))
        self.play(FadeIn(r1))
        self.play(r1.animate.shift(UP*1.6 + LEFT*2.6))
        self.play(FadeIn(dot2))
        self.play(dot2.animate.shift(UP * 1.2 + LEFT *4.1))
        self.play(FadeIn(r2))
        self.play(r2.animate.shift(UP*1.2 + LEFT*2.3))
        self.play(FadeIn(dot3))
        self.play(dot3.animate.shift(UP * 0.8 + LEFT *4.1))
        self.play(FadeIn(r3))
        self.play(r3.animate.shift(UP*0.8 + LEFT *2.95))
        self.play(FadeIn(dot4))
        self.play(dot4.animate.shift(UP * 0.4 + LEFT *4.1))
        self.play(FadeIn(r4))
        self.play(r4.animate.shift(UP*0.4 + LEFT*2.65))
        self.play(FadeIn(dot5))
        self.play(dot5.animate.shift(LEFT*4.1))
        self.play(FadeIn(r5))
        self.play(r5.animate.shift(LEFT*2.88))
        
        self.play(Create(highlight))
        
        self.play(
            highlight.animate.set_opacity(1.0).scale(0.3),
            run_time=0.5
        )
        self.play(
            highlight.animate.set_opacity(1.0).scale(0.5),
            run_time=0.5
        )
        self.wait(1)
        self.play(FadeOut(text, highlight, dot1, dot2, dot3, dot4, dot5, r2, r3, r4, r5))
        self.play(r1.animate.shift(RIGHT*2.6 + UP*0.1))
        self.wait()
        self.play(Write(txt1))
        self.play(FadeOut(txt1))
        self.play(Write(code_web))
     
