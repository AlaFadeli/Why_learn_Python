
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
        txt1.move_to(UP*0.5)
        
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
        code_txt = Text("This is an example of coding a web app using the Python framework Flask",font_size=10, font="UBUNTU")
        code_txt.move_to(LEFT*2 + UP*2)
        
        
            
        txt2 = Text("Data Science and Machine Learning", font_size=10,font="UBUNTU")
        txt2_ex = Text("This is an example of a visualization using Python packages",font_size=10,font="UBUNTU")
        txt2.move_to(UP*0.5)
        txt2_ex.move_to(LEFT*2 + UP*2)
            
        code_datas = Code(
            code = '''  

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# Apply a seaborn style
sns.set(style="whitegrid")

# Data
c19_cases_by_country = {
    "USA": 111820082,
    "India": 45035393,
    "France": 40138560,
    "Germany": 38828995,
    "Brazil": 38743918,
    "S. Korea": 34571873,
    "Japan": 33803572,
    "Italy": 26723249,
    "UK": 24910387,
    "Russia": 24124215
}

# Plot
categories = list(c19_cases_by_country.keys())
values = list(c19_cases_by_country.values())

fig, ax = plt.subplots(figsize=(12, 7))  # Adjust figure size for better readability

# Create a bar plot with improved style
bars = ax.bar(categories, values, color=sns.color_palette("viridis", len(categories)), edgecolor='w', linewidth=1.2)

def millions_formatter(x, pos):
    """Formatter function to display y-axis values in millions."""
    return f'{x * 1e-6:.1f}M'

# Apply the custom formatter to the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

# Customization
plt.title("Top 10 Total COVID-19 Cases by Country", fontsize=18, fontweight='bold', pad=20, backgroundcolor='#e0e0e0')
plt.xlabel("Country", fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel("Cases", fontsize=14, fontweight='bold', labelpad=15)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Add gridlines for y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7, linewidth=0.7)

# Add data labels on bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval * 1e-6:.1f}M', ha='center', va='bottom', fontsize=10, color='black', weight='bold')

# Add a background color
ax.set_facecolor('#f5f5f5')

# Improve layout
plt.tight_layout()

# Save the plot to a PNG file
plt.savefig('plot_styled_updated.png')

# Display the plot
plt.show()

# DataFrame csv file :

df = pd.read_csv("country_wise_latest.csv")

print(df)

''',            
            language = "python",
            style = "vim",
            font_size = 7,
            line_spacing = 0.5,
            insert_line_no = True,
)    
        code_datas.move_to(ORIGIN)
        
            
            
            
            
            
            

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
        self.play(FadeOut(r1,txt1))
        self.wait(1)
        self.play(Write(code_txt))
        self.play(Write(code_web), run_time = 2)
        self.wait(3)
        self.play(Uncreate(code_txt,code_web))
        self.play(Write(txt2))
        self.wait()
        self.play(FadeOut(txt2))
        self.play(FadeIn(txt2_ex))
        self.play(Write(code_datas), run_time=2)
        self.wait(2)
