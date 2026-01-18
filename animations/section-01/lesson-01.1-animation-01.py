from manim import *
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from animations.styles import Brand

class ColumnMultiplication(Scene):
    def construct(self):
        # Apply Branding
        Brand.set_default_theme(self)

        # Configuration
        def indicate_carry(mob):
            target = mob.copy().scale(1.2)
            target[1].set_color(Brand.ACTIVE)
            return Transform(mob, target, rate_func=there_and_back, run_time=1)

        digits_scale = 1.5
        carry_scale = 0.8
        
        # Numbers
        n1 = 235
        n2 = 24
        
        # Positioning parameters
        center_x = 0
        center_y = 1
        dx = 0.8
        dy = 1.0
        
        # Side calculation position
        side_x = 4.0
        side_y = 0.5
        
        # Row y-positions
        y_top = center_y + dy
        y_bot = center_y
        y_line1 = center_y - 0.5 * dy
        y_res1 = center_y - dy
        y_res2 = center_y - 2 * dy
        y_line2 = center_y - 2.5 * dy
        y_final = center_y - 3 * dy
        
        # Column x-positions
        x_units = 1.5 * dx
        x_tens = 0.5 * dx
        x_hundreds = -0.5 * dx
        x_thousands = -1.5 * dx
        
        # --- Create Objects ---
        
        # Top number: 235
        t_hundreds = MathTex("2").scale(digits_scale).move_to([x_hundreds, y_top, 0])
        t_tens = MathTex("3").scale(digits_scale).move_to([x_tens, y_top, 0])
        t_units = MathTex("5").scale(digits_scale).move_to([x_units, y_top, 0])
        
        # Bottom number: 24
        b_tens = MathTex("2").scale(digits_scale).move_to([x_tens, y_bot, 0])
        b_units = MathTex("4").scale(digits_scale).move_to([x_units, y_bot, 0])
        operator = MathTex("\\times").scale(digits_scale).move_to([x_thousands, y_bot, 0])
        
        # Line 1
        line1 = Line(start=[x_thousands - dx, y_line1, 0], end=[x_units + dx, y_line1, 0])
        
        # Results & Final Answer placeholders
        r1_hundreds = MathTex("9").scale(digits_scale)
        r1_tens = MathTex("4").scale(digits_scale)
        r1_units = MathTex("0").scale(digits_scale)
        
        r2_thousands = MathTex("4").scale(digits_scale)
        r2_hundreds = MathTex("7").scale(digits_scale)
        r2_tens = MathTex("0").scale(digits_scale)
        r2_units = MathTex("0").scale(digits_scale) # Placeholder
        
        # Final result (5640) - Use ANSWER color
        f_thousands = MathTex("5").scale(digits_scale).set_color(Brand.ANSWER)
        f_hundreds = MathTex("6").scale(digits_scale).set_color(Brand.ANSWER)
        f_tens = MathTex("4").scale(digits_scale).set_color(Brand.ANSWER)
        f_units = MathTex("0").scale(digits_scale).set_color(Brand.ANSWER)

        # --- Animation Sequence ---
        
        # Show setup
        self.play(Write(t_hundreds), Write(t_tens), Write(t_units))
        self.play(Write(operator), Write(b_tens), Write(b_units))
        self.play(Create(line1))
        self.wait(1)
        
        # --- Step 1: Multiply by 4 (Units) ---
        
        # 4 * 5 = 20
        self.play(Indicate(b_units, color=Brand.ACTIVE), Indicate(t_units, color=Brand.ACTIVE))
        
        # Side calculation: 5 x 4 = 20
        sc1 = MathTex("5", "\\times", "4", "=", "20").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
        self.play(Write(sc1))
        self.wait(0.5)
        
        r1_units.move_to([x_units, y_res1, 0])
        c2_in = MathTex("2").scale(carry_scale).move_to([x_tens, y_res1 + 0.4*dy, 0]).set_color(Brand.CARRY)
        c2_in.set_z_index(2)
        c2_out = c2_in.copy().set_color(Brand.BACKGROUND).set_stroke(width=5, color=Brand.BACKGROUND)
        c2_out.set_z_index(1)
        carry_2 = VGroup(c2_out, c2_in)
        
        # Turn carry digit Brand.CARRY first
        self.play(sc1[4][0].animate.set_color(Brand.CARRY))
        self.wait(0.2)
        
        # Animate split: 20 -> 0 (result) + 2 (carry)
        self.play(
            ReplacementTransform(sc1[4][1], r1_units),
            ReplacementTransform(sc1[4][0], c2_in),
            FadeIn(c2_out),
            FadeOut(sc1[:4])
        )
        self.wait(0.5)
        
        # 4 * 3 = 12 + 2 = 14
        self.play(Indicate(b_units, color=Brand.ACTIVE), Indicate(t_tens, color=Brand.ACTIVE))
        self.play(indicate_carry(carry_2))
        
        # Side calculation
        sc2 = MathTex("3", "\\times", "4", "=", "12").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
        self.play(Write(sc2))
        self.wait(0.5)
        
        sc2_add = MathTex("12", "+", "2", "=", "14").scale(digits_scale).move_to([side_x, side_y - 1.0, 0]).set_color(Brand.AUXILIARY)
        sc2_add[2].set_color(Brand.CARRY) # match the carry color being added
        
        self.play(
            TransformFromCopy(sc2[4], sc2_add[0]),
            TransformFromCopy(carry_2[1], sc2_add[2]),
            Write(sc2_add[1]),
            Write(sc2_add[3]),
            Write(sc2_add[4])
        )
        self.wait(0.5)
        
        # Turn carry digit Brand.CARRY first
        self.play(sc2_add[4][0].animate.set_color(Brand.CARRY))
        self.wait(0.2)
        
        r1_tens.move_to([x_tens, y_res1, 0])
        c1_in = MathTex("1").scale(carry_scale).move_to([x_hundreds, y_res1 + 0.4*dy, 0]).set_color(Brand.CARRY)
        c1_in.set_z_index(2)
        c1_out = c1_in.copy().set_color(Brand.BACKGROUND).set_stroke(width=5, color=Brand.BACKGROUND)
        c1_out.set_z_index(1)
        carry_1 = VGroup(c1_out, c1_in)
        
        # Animate split
        self.play(
            FadeOut(carry_2), 
            ReplacementTransform(sc2_add[4][1], r1_tens),
            ReplacementTransform(sc2_add[4][0], c1_in),
            FadeIn(c1_out),
            FadeOut(sc2),
            FadeOut(sc2_add[:4])
        )
        self.wait(0.5)
        
        # 4 * 2 = 8 + 1 = 9
        self.play(Indicate(b_units, color=Brand.ACTIVE), Indicate(t_hundreds, color=Brand.ACTIVE))
        self.play(indicate_carry(carry_1))
        
        sc3 = MathTex("2", "\\times", "4", "=", "8").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
        self.play(Write(sc3))
        self.wait(0.5)
        
        sc3_add = MathTex("8", "+", "1", "=", "9").scale(digits_scale).move_to([side_x, side_y - 1.0, 0]).set_color(Brand.AUXILIARY)
        sc3_add[2].set_color(Brand.CARRY)
        
        self.play(
            TransformFromCopy(sc3[4], sc3_add[0]),
            TransformFromCopy(carry_1[1], sc3_add[2]),
            Write(sc3_add[1]),
            Write(sc3_add[3]),
            Write(sc3_add[4])
        )
        self.wait(0.5)
        
        r1_hundreds.move_to([x_hundreds, y_res1, 0])
        
        self.play(
            FadeOut(carry_1), 
            ReplacementTransform(sc3_add[4], r1_hundreds),
            FadeOut(sc3),
            FadeOut(sc3_add[:4])
        )
        self.wait(1)
        
        # --- Step 2: Multiply by 20 (Tens) ---
        
        # Placeholder 0
        r2_units.move_to([x_units, y_res2, 0]).set_color(Brand.ACTIVE) # Highlighted as it's the placeholder
        self.play(Write(r2_units))
        self.wait(0.5)
        
        # 2 * 5 = 10
        self.play(Indicate(b_tens, color=Brand.ACTIVE), Indicate(t_units, color=Brand.ACTIVE))
        
        sc4 = MathTex("5", "\\times", "2", "=", "10").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
        self.play(Write(sc4))
        self.wait(0.5)
        
        # Turn carry digit color first
        self.play(sc4[4][0].animate.set_color(Brand.CARRY))
        self.wait(0.2)
        
        r2_tens.move_to([x_tens, y_res2, 0])
        c1b_in = MathTex("1").scale(carry_scale).move_to([x_hundreds, y_res2 + 0.4*dy, 0]).set_color(Brand.CARRY)
        c1b_in.set_z_index(2)
        c1b_out = c1b_in.copy().set_color(Brand.BACKGROUND).set_stroke(width=5, color=Brand.BACKGROUND)
        c1b_out.set_z_index(1)
        carry_1_b = VGroup(c1b_out, c1b_in)
        
        # Split
        self.play(
            ReplacementTransform(sc4[4][1], r2_tens),
            ReplacementTransform(sc4[4][0], c1b_in),
            FadeIn(c1b_out),
            FadeOut(sc4[:4])
        )
        self.wait(0.5)
        
        # 2 * 3 = 6 + 1 = 7
        self.play(Indicate(b_tens, color=Brand.ACTIVE), Indicate(t_tens, color=Brand.ACTIVE))
        self.play(indicate_carry(carry_1_b))
        
        sc5 = MathTex("3", "\\times", "2", "=", "6").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
        self.play(Write(sc5))
        self.wait(0.5)
        
        sc5_add = MathTex("6", "+", "1", "=", "7").scale(digits_scale).move_to([side_x, side_y - 1.0, 0]).set_color(Brand.AUXILIARY)
        sc5_add[2].set_color(Brand.CARRY)
        
        self.play(
            TransformFromCopy(sc5[4], sc5_add[0]),
            TransformFromCopy(carry_1_b[1], sc5_add[2]),
            Write(sc5_add[1]),
            Write(sc5_add[3]),
            Write(sc5_add[4])
        )
        self.wait(0.5)
        
        r2_hundreds.move_to([x_hundreds, y_res2, 0])
        
        self.play(
            FadeOut(carry_1_b), 
            ReplacementTransform(sc5_add[4], r2_hundreds),
            FadeOut(sc5),
            FadeOut(sc5_add[:4])
        )
        self.wait(0.5)
        
        # 2 * 2 = 4
        self.play(Indicate(b_tens, color=Brand.ACTIVE), Indicate(t_hundreds, color=Brand.ACTIVE))
        
        r2_thousands.move_to([x_thousands, y_res2, 0])
        
        sc6 = MathTex("2", "\\times", "2", "=", "4").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
        self.play(Write(sc6))
        self.wait(0.5)
        
        self.play(
            ReplacementTransform(sc6[4], r2_thousands),
            FadeOut(sc6[:4])
        ) 
        self.wait(1)
        
        # --- Step 3: Addition ---
        
        line2 = Line(start=[x_thousands - dx, y_line2, 0], end=[x_units + dx, y_line2, 0])
        plus = MathTex("+").scale(digits_scale).move_to([x_thousands - dx + 0.2, y_res2, 0])
        
        self.play(Create(line2), Write(plus))
        
        # 0 + 0 = 0
        f_units.move_to([x_units, y_final, 0])
        self.play(Indicate(r1_units, color=Brand.ACTIVE), Indicate(r2_units, color=Brand.ACTIVE))
        self.play(Write(f_units))
        
        # 4 + 0 = 4
        f_tens.move_to([x_tens, y_final, 0])
        self.play(Indicate(r1_tens, color=Brand.ACTIVE), Indicate(r2_tens, color=Brand.ACTIVE))
        self.play(Write(f_tens))
        
        # 9 + 7 = 16
        f_hundreds.move_to([x_hundreds, y_final, 0])
        
        # carry 1 for addition
        ca_in = MathTex("1").scale(carry_scale).move_to([x_thousands, y_final + 0.4*dy, 0]).set_color(Brand.CARRY)
        ca_in.set_z_index(2)
        ca_out = ca_in.copy().set_color(Brand.BACKGROUND).set_stroke(width=5, color=Brand.BACKGROUND)
        ca_out.set_z_index(1)
        carry_add = VGroup(ca_out, ca_in)
        
        self.play(Indicate(r1_hundreds, color=Brand.ACTIVE), Indicate(r2_hundreds, color=Brand.ACTIVE))
        
        # Side calc for addition
        sc_add = MathTex("9", "+", "7", "=", "16").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
        self.play(Write(sc_add))
        self.wait(0.5)
        
        # Turn carry digit color first
        self.play(sc_add[4][0].animate.set_color(Brand.CARRY))
        self.wait(0.2)
        
        self.play(
            ReplacementTransform(sc_add[4][1], f_hundreds),
            ReplacementTransform(sc_add[4][0], ca_in),
            FadeIn(ca_out),
            FadeOut(sc_add[:4])
        )
        
        # 4 + 1 = 5
        f_thousands.move_to([x_thousands, y_final, 0])
        self.play(Indicate(r2_thousands, color=Brand.ACTIVE), indicate_carry(carry_add))
        self.play(FadeOut(carry_add), Write(f_thousands))
        
        self.wait(2)
