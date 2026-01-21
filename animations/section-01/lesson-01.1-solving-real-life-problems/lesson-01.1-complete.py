from manim import *
import importlib.util
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from animations.styles import Brand

def load_scene_class(filename, class_name):
    """
    Dynamically loads a Scene class from a file in the same directory.
    """
    path = os.path.join(os.path.dirname(__file__), filename)
    spec = importlib.util.spec_from_file_location(f"dynamic_{class_name}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"dynamic_{class_name}"] = module
    spec.loader.exec_module(module)
    return getattr(module, class_name)

class Lesson011Complete(Scene):
    def construct(self):
        Brand.set_default_theme(self)
        
        # --- Slide 1: Introduction ---
        self.slide_01_introduction()
        self.clear_screen()
        
        # --- Slide 2: The Strategy ---
        self.slide_02_strategy()
        self.clear_screen()
        
        # --- Slide 3: Example 1 - The Supermarket ---
        self.slide_03_example_1_context()
        self.clear_screen()
        
        # --- Slide 4: Calculation Methods ---
        self.slide_04_calculations()
        self.clear_screen()
        
        # --- Slide 5: Example 1 - Part B (Context) ---
        self.slide_05_part_b_context()
        self.clear_screen()
        
        # --- Slide 6: Example 1 - Part B (Calculation) ---
        self.slide_06_part_b_calc()
        self.clear_screen()
        
        # --- Slide 7: Example 2 - Theme Park (Context) ---
        self.slide_07_example_2_context()
        self.clear_screen()
        
        # --- Slide 8: Example 2 - Interpreting ---
        self.slide_08_interpreting()
        self.clear_screen()
        
        # --- Slide 9: Example 2 - Part B (Free Entry) ---
        self.slide_09_free_entry()
        self.clear_screen()
        
        # --- Slide 10: Summary ---
        self.slide_10_summary()
        self.wait(2)

    def clear_screen(self):
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(0.5)

    def slide_01_introduction(self):
        title = Text("Solving Real-Life Problems").scale(1.2).to_edge(UP)
        underline = Line(LEFT, RIGHT).next_to(title, DOWN).scale(2)
        
        self.play(Write(title), Create(underline))
        
        strategies = VGroup(
            Text("Key Strategies:").scale(0.8).set_color(Brand.ACTIVE),
            Text("• Read").scale(0.7),
            Text("• Plan").scale(0.7),
            Text("• Calculate").scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT).shift(LEFT * 2)
        
        methods = VGroup(
            Text("Methods:").scale(0.8).set_color(Brand.ACTIVE),
            Text("• Grid Method").scale(0.7),
            Text("• Column Method").scale(0.7),
            Text("• Long Division").scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 2)
        
        # Align tops
        methods.match_y(strategies)
        
        self.play(Write(strategies), Write(methods))
        self.wait(2)

    def slide_02_strategy(self):
        title = Text("The Strategy").scale(1.2).to_edge(UP)
        self.play(Write(title))
        
        # Create steps
        s1 = Text("1. READ").scale(0.9).move_to([-4, 2, 0])
        t1 = Text("Read the question carefully").scale(0.6).next_to(s1, DOWN)
        
        s2 = Text("2. PLAN").scale(0.9).move_to([4, 2, 0])
        t2 = Text("Decide on a strategy").scale(0.6).next_to(s2, DOWN)
        
        s3 = Text("3. CALCULATE").scale(0.9).move_to([-4, -1, 0])
        t3 = Text("Work out the answer").scale(0.6).next_to(s3, DOWN)
        
        s4 = Text("4. CHECK").scale(0.9).move_to([4, -1, 0])
        t4 = Text("Does it make sense?").scale(0.6).next_to(s4, DOWN)
        
        steps = [(s1, t1), (s2, t2), (s3, t3), (s4, t4)]
        
        for s, t in steps:
            self.play(Write(s))
            self.play(FadeIn(t))
            self.wait(0.5)
        
        self.wait(1)

    def slide_03_example_1_context(self):
        title = Text("Example 1: The Supermarket").scale(1.0).to_edge(UP)
        self.play(Write(title))
        
        icon_case = Square().scale(0.5).set_fill(Brand.AUXILIARY, opacity=0.5)
        t_delivery = Text("Delivery: 235 Cases").scale(0.8).next_to(icon_case, RIGHT)
        g_delivery = VGroup(icon_case, t_delivery).move_to([0, 1, 0])
        
        t_contents = Text("Each Case: 24 Tins").scale(0.8).next_to(g_delivery, DOWN, buff=0.5)
        
        self.play(Create(icon_case), Write(t_delivery))
        self.play(Write(t_contents))
        self.wait(1)
        
        t_question = Text("How many tins altogether?").scale(1.0).set_color(Brand.ACTIVE).next_to(t_contents, DOWN, buff=1.0)
        self.play(Write(t_question))
        self.wait(1)
        
        t_calc = MathTex("235 \\times 24").scale(1.5).set_color(Brand.ANSWER).next_to(t_question, DOWN, buff=0.5)
        self.play(Write(t_calc))
        self.wait(2)

    def slide_04_calculations(self):
        # 1. Grid Method
        title = Text("Grid Method").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))
        
        BoxClass = load_scene_class("lesson-01.1-animation-02.py", "BoxMultiplication")
        # We need to run the construct method of the imported class on THIS scene.
        # Since the imported classes are Scenes, they use 'self.play' etc.
        # We can bind the construct method to this instance.
        BoxClass.construct(self)
        
        self.clear_screen()
        
        # 2. Column Method
        title = Text("Column Method").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))
        
        ColClass = load_scene_class("lesson-01.1-animation-01.py", "ColumnMultiplication")
        ColClass.construct(self)

    def slide_05_part_b_context(self):
        title = Text("Example 1: Part B").scale(1.0).to_edge(UP)
        self.play(Write(title))
        
        t_damaged = Text("• 5% of tins damaged (thrown away)").scale(0.8).move_to([0, 1, 0])
        t_sales = Text("• Sales: 250 tins/day").scale(0.8).next_to(t_damaged, DOWN, buff=0.5)
        t_q = Text("How many days will stock last?").scale(1.0).set_color(Brand.ACTIVE).next_to(t_sales, DOWN, buff=1.0)
        
        self.play(Write(t_damaged))
        self.play(Write(t_sales))
        self.play(Write(t_q))
        self.wait(2)

    def slide_06_part_b_calc(self):
        StockClass = load_scene_class("lesson-01.1-animation-03.py", "StockDaysCalculation")
        StockClass.construct(self)

    def slide_07_example_2_context(self):
        title = Text("Example 2: Theme Park").scale(1.0).to_edge(UP)
        self.play(Write(title))
        
        t_kids = Text("613 Children").scale(0.8).shift(LEFT * 3 + UP * 1)
        t_adults = Text("59 Adults").scale(0.8).next_to(t_kids, DOWN, buff=0.5)
        
        self.play(Write(t_kids), Write(t_adults))
        
        # Addition animation
        line = Line(start=t_adults.get_left() + DOWN * 0.2, end=t_adults.get_right() + RIGHT * 2 + DOWN * 0.2)
        
        calc = MathTex("613 + 59 = 672").scale(1.2).next_to(t_adults, RIGHT, buff=2).set_color(Brand.ANSWER)
        
        self.play(Write(calc))
        self.wait(1)
        
        t_total = Text("Total People: 672").scale(1.0).move_to([0, -1, 0]).set_color(Brand.ANSWER)
        self.play(TransformFromCopy(calc, t_total))
        self.wait(1)
        
        t_coach = Text("Coach Capacity: 53").scale(0.8).next_to(t_total, DOWN, buff=0.5)
        self.play(Write(t_coach))
        
        t_strategy = MathTex("672 \\div 53").scale(1.2).set_color(Brand.ACTIVE).next_to(t_coach, DOWN, buff=0.5)
        self.play(Write(t_strategy))
        self.wait(2)

    def slide_08_interpreting(self):
        TPClass = load_scene_class("lesson-01.1-animation-04.py", "ThemeParkDivision")
        TPClass.construct(self)

    def slide_09_free_entry(self):
        FreeClass = load_scene_class("lesson-01.1-animation-05.py", "FreeEntryCalculation")
        FreeClass.construct(self)

    def slide_10_summary(self):
        title = Text("Summary").scale(1.2).to_edge(UP)
        self.play(Write(title))
        
        bullets = VGroup(
            Text("• Understand the context"),
            Text("• Choose your method"),
            Text("• Interpret the answer"),
            Text("• Check your results")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8)
        
        for b in bullets:
            self.play(FadeIn(b, shift=RIGHT))
            self.wait(0.5)
            
        self.wait(2)
