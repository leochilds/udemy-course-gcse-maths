from manim import *
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from animations.styles import Brand

class FreeEntryCalculation(Scene):
    def construct(self):
        # Apply Branding
        Brand.set_default_theme(self)

        # Configuration
        text_scale = 0.8
        math_scale = 1.0
        
        # --- Part 1: Context & Division Strategy ---
        
        # Header info
        t_children = Text("613 Children").scale(text_scale).to_edge(UP).shift(LEFT * 2)
        t_rule = Text("1 Free Adult / 15 Children").scale(text_scale).next_to(t_children, DOWN)
        
        self.play(Write(t_children))
        self.play(Write(t_rule))
        self.wait(0.5)
        
        # Division Setup
        # We want to show: 613 / 15
        # And the mental math: 40 x 15 = 600
        
        eq_div = MathTex("613", "\\div", "15").scale(math_scale).shift(UP * 0.5)
        self.play(Write(eq_div))
        self.wait(0.5)
        
        # Estimation Steps (Mental Math)
        # 2 * 15 = 30
        # 4 * 15 = 60
        # 40 * 15 = 600
        
        est_1 = MathTex("2", "\\times", "15", "=", "30").scale(text_scale).set_color(Brand.AUXILIARY)
        est_2 = MathTex("4", "\\times", "15", "=", "60").scale(text_scale).set_color(Brand.AUXILIARY)
        est_3 = MathTex("40", "\\times", "15", "=", "600").scale(text_scale).set_color(Brand.ACTIVE)
        
        # Position them below the main equation
        est_1.next_to(eq_div, DOWN, buff=1.0).shift(LEFT * 2)
        est_2.next_to(est_1, DOWN, buff=0.3)
        est_3.next_to(est_2, DOWN, buff=0.3)
        
        # Animation sequence for estimation
        self.play(Write(est_1))
        self.wait(0.5)
        self.play(Write(est_2))
        self.wait(0.5)
        self.play(Write(est_3))
        self.wait(1.0)
        
        # Show Subtraction and Remainder
        # 613 - 600 = 13
        
        # Align subtraction under the division equation or to the right
        sub_eq = MathTex("613", "-", "600", "=", "13").scale(math_scale)
        sub_eq.next_to(eq_div, DOWN, buff=1.0).shift(RIGHT * 2)
        # Color the 600 to match the estimation
        sub_eq[2].set_color(Brand.ACTIVE)
        
        self.play(Write(sub_eq))
        self.wait(1.0)
        
        # Conclusion of Part 1
        # 40 groups -> 40 Free Adults
        t_free = Text("40 Free Adults").scale(text_scale).set_color(Brand.ANSWER)
        t_free.next_to(sub_eq, DOWN, buff=0.5)
        
        self.play(Indicate(est_3[0], color=Brand.ANSWER)) # Highlight '40' in estimation
        self.play(Write(t_free))
        self.wait(2.0)
        
        # Cleanup for Part 2
        # Keep '40 Free Adults' but move it or clear others
        
        group_part1 = VGroup(eq_div, est_1, est_2, est_3, sub_eq, t_children, t_rule)
        
        self.play(
            FadeOut(group_part1),
            t_free.animate.to_edge(UP).shift(LEFT * 2)
        )
        self.wait(0.5)
        
        # --- Part 2: Paying Adults ---
        
        t_total_adults = Text("Total Adults: 59").scale(text_scale).next_to(t_free, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(t_total_adults))
        self.wait(0.5)
        
        # Calculation: 59 - 40 = 19
        final_calc = MathTex("59", "-", "40", "=", "19").scale(math_scale).move_to(ORIGIN)
        final_calc[2].set_color(Brand.ANSWER) # 40 was the previous answer
        final_calc[4].set_color(Brand.ANSWER) # 19 is the new answer
        
        self.play(Write(final_calc))
        self.wait(1.0)
        
        t_paying = Text("19 Paying Adults").scale(1.2).set_color(Brand.ANSWER).next_to(final_calc, DOWN, buff=0.5)
        
        self.play(Write(t_paying))
        self.play(Indicate(t_paying, color=Brand.ACTIVE))
        self.wait(3.0)
