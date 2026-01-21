from manim import *
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from animations.styles import Brand

class StockDaysCalculation(Scene):
    def construct(self):
        # Apply Branding
        Brand.set_default_theme(self)

        # --- Part 1: Percentage & Subtraction ---
        
        # Initial Text
        title = Text("Stock Calculation").scale(0.8).to_corner(UL).set_color(Brand.AUXILIARY)
        self.play(Write(title))
        
        total_tins_label = Text("Total Tins:").scale(0.8).move_to([-2, 2, 0])
        total_tins_val = MathTex("5640").scale(1.2).next_to(total_tins_label, RIGHT)
        
        self.play(Write(total_tins_label), Write(total_tins_val))
        self.wait(1)
        
        # 10% Calculation
        p10_label = MathTex("10\\% = ").scale(0.8).move_to([-2, 1, 0])
        p10_val = MathTex("564").scale(0.8).next_to(p10_label, RIGHT)
        
        self.play(Write(p10_label))
        self.play(TransformFromCopy(total_tins_val, p10_val)) # Visual cue derived from total
        self.wait(0.5)
        
        # 5% Calculation
        p5_label = MathTex("5\\% = ").scale(0.8).next_to(p10_label, DOWN, aligned_edge=LEFT)
        p5_calc = MathTex("564 \\div 2 = ").scale(0.8).next_to(p5_label, RIGHT)
        p5_val = MathTex("282").scale(0.8).next_to(p5_calc, RIGHT).set_color(Brand.CARRY) # Highlight as 'damaged'
        
        self.play(Write(p5_label))
        self.play(Write(p5_calc))
        self.play(Write(p5_val))
        self.wait(1)
        
        # Subtraction
        sub_label = Text("Saleable Tins:").scale(0.8).move_to([-2, -1, 0])
        sub_calc = MathTex("5640 - 282 = ").scale(0.8).next_to(sub_label, RIGHT)
        sub_val = MathTex("5358").scale(1.2).next_to(sub_calc, RIGHT).set_color(Brand.ANSWER)
        
        self.play(Write(sub_label))
        self.play(
            TransformFromCopy(total_tins_val, sub_calc[0][0:4]),
            Write(sub_calc[0][4]),
            TransformFromCopy(p5_val, sub_calc[0][5:8]),
            Write(sub_calc[0][8])
        )
        self.wait(0.5)
        self.play(Write(sub_val))
        self.wait(2)
        
        # Cleanup Part 1
        part1_group = VGroup(
            total_tins_label, total_tins_val,
            p10_label, p10_val,
            p5_label, p5_calc, p5_val,
            sub_label, sub_calc, sub_val
        )
        
        # Keep the result (5358) but move it for Part 2
        self.play(
            FadeOut(part1_group),
            sub_val.animate.scale(0.8).to_corner(UR).set_color(Brand.TEXT) # Move to corner as reference
        )
        
        # --- Part 2: Division ---
        
        # Setup Division
        div_problem = MathTex("5358", "\\div", "250").scale(1.2).move_to([0, 2.5, 0])
        self.play(ReplacementTransform(sub_val, div_problem[0]), Write(div_problem[1:]))
        self.wait(1)
        
        # Estimations
        est_box = VGroup()
        est_title = Text("Estimations:").scale(0.6).set_color(Brand.AUXILIARY)
        
        est1 = MathTex("4 \\times 250 = 1000").scale(0.8)
        est2 = MathTex("20 \\times 250 = 5000").scale(0.8)
        
        est_group = VGroup(est_title, est1, est2).arrange(DOWN, aligned_edge=LEFT).move_to([-3, 0, 0])
        
        self.play(Write(est_title))
        self.play(Write(est1))
        self.wait(0.5)
        self.play(Write(est2))
        self.play(Indicate(est2, color=Brand.ACTIVE))
        self.wait(1)
        
        # Subtraction Step 1
        step1_calc = MathTex("5358", "-", "5000", "=", "358").scale(1.0).move_to([2, 0.5, 0])
        
        self.play(
            TransformFromCopy(div_problem[0], step1_calc[0]),
            Write(step1_calc[1]),
            TransformFromCopy(est2[0][-4:], step1_calc[2]), # Grab 5000
            Write(step1_calc[3]),
            Write(step1_calc[4])
        )
        self.wait(1)
        
        # Check remainder
        rem_check = Text("How many 250s in 358?").scale(0.6).next_to(step1_calc, DOWN, buff=0.5).set_color(Brand.AUXILIARY)
        rem_ans = MathTex("1 \\times 250 = 250").scale(0.8).next_to(rem_check, DOWN)
        
        self.play(Write(rem_check))
        self.wait(0.5)
        self.play(Write(rem_ans))
        self.wait(1)
        
        # Final Days Sum
        # Days = 20 + 1
        
        final_days_label = Text("Total Days:").scale(0.8).move_to([0, -2.5, 0])
        final_days_calc = MathTex("20", "+", "1", "=", "21").scale(1.2).next_to(final_days_label, RIGHT)
        final_days_calc[4].set_color(Brand.ANSWER)
        
        self.play(Write(final_days_label))
        
        # Animate taking the 20 and 1
        self.play(
            TransformFromCopy(est2[0][0:2], final_days_calc[0]), # 20
            Write(final_days_calc[1]),
            TransformFromCopy(rem_ans[0][0], final_days_calc[2]), # 1
            Write(final_days_calc[3]),
            Write(final_days_calc[4])
        )
        
        self.play(Circumscribe(final_days_calc[4], color=Brand.ANSWER))
        self.wait(3)
