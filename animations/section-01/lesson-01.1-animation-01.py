from manim import *

class ColumnMultiplication(Scene):
    def construct(self):
        # Configuration
        def indicate_carry(mob):
            target = mob.copy().scale(1.2)
            target[1].set_color(YELLOW)
            return Transform(mob, target, rate_func=there_and_back, run_time=1)

        digits_scale = 1.5
        carry_scale = 0.8
        CARRY_COLOR = "#FF0000" # Vivid Red
        
        # Numbers
        n1 = 235
        n2 = 24
        
        # Setup alignment grid
        # Columns: Thousands, Hundreds, Tens, Units
        # Let's use coordinates relative to a center point
        
        # Define positions
        # x_step = 0.8
        # y_step = 1.0
        
        # Create Text Objects
        # Top number: 235
        t_hundreds = MathTex("2").scale(digits_scale)
        t_tens = MathTex("3").scale(digits_scale)
        t_units = MathTex("5").scale(digits_scale)
        
        # Bottom number: 24
        b_tens = MathTex("2").scale(digits_scale)
        b_units = MathTex("4").scale(digits_scale)
        operator = MathTex("\\times").scale(digits_scale)
        
        # First row results (940)
        r1_hundreds = MathTex("9").scale(digits_scale)
        r1_tens = MathTex("4").scale(digits_scale)
        r1_units = MathTex("0").scale(digits_scale)
        
        # Second row results (4700)
        r2_thousands = MathTex("4").scale(digits_scale)
        r2_hundreds = MathTex("7").scale(digits_scale)
        r2_tens = MathTex("0").scale(digits_scale)
        r2_units = MathTex("0").scale(digits_scale) # Placeholder
        
        # Final result (5640)
        f_thousands = MathTex("5").scale(digits_scale)
        f_hundreds = MathTex("6").scale(digits_scale)
        f_tens = MathTex("4").scale(digits_scale)
        f_units = MathTex("0").scale(digits_scale)

        # Positioning
        # Center the calculation
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
        
        # Column x-positions (0 is between Tens and Units for symmetry, let's adjust)
        # Units at x=0.5*dx, Tens at -0.5*dx, Hundreds at -1.5*dx, Thousands at -2.5*dx
        x_units = 1.5 * dx
        x_tens = 0.5 * dx
        x_hundreds = -0.5 * dx
        x_thousands = -1.5 * dx
        
        # Set positions
        t_hundreds.move_to([x_hundreds, y_top, 0])
        t_tens.move_to([x_tens, y_top, 0])
        t_units.move_to([x_units, y_top, 0])
        
        b_tens.move_to([x_tens, y_bot, 0])
        b_units.move_to([x_units, y_bot, 0])
        operator.move_to([x_thousands, y_bot, 0])
        
        line1 = Line(start=[x_thousands - dx, y_line1, 0], end=[x_units + dx, y_line1, 0])
        
        # Show setup
        self.play(Write(t_hundreds), Write(t_tens), Write(t_units))
        self.play(Write(operator), Write(b_tens), Write(b_units))
        self.play(Create(line1))
        self.wait(1)
        
        # --- Step 1: Multiply by 4 (Units) ---
        
        # 4 * 5 = 20
        self.play(Indicate(b_units), Indicate(t_units))
        
        # Side calculation: 5 x 4 = 20
        sc1 = MathTex("5", "\\times", "4", "=", "20").scale(digits_scale).move_to([side_x, side_y, 0])
        self.play(Write(sc1))
        self.wait(0.5)
        
        r1_units.move_to([x_units, y_res1, 0])
        c2_in = MathTex("2").scale(carry_scale).move_to([x_tens, y_res1 + 0.4*dy, 0]).set_color(CARRY_COLOR)
        c2_in.set_z_index(2)
        c2_out = c2_in.copy().set_color(BLACK).set_stroke(width=5, color=BLACK)
        c2_out.set_z_index(1)
        carry_2 = VGroup(c2_out, c2_in)
        
        # Turn carry digit red first
        self.play(sc1[4][0].animate.set_color(CARRY_COLOR))
        self.wait(0.2)
        
        # Animate split: 20 -> 0 (result) + 2 (carry)
        # sc1[4] is "20". sc1[4][1] is "0", sc1[4][0] is "2"
        self.play(
            ReplacementTransform(sc1[4][1], r1_units),
            ReplacementTransform(sc1[4][0], c2_in),
            FadeIn(c2_out),
            FadeOut(sc1[:4]) # Fade out 5 x 4 =
        )
        self.wait(0.5)
        
        # 4 * 3 = 12 + 2 = 14
        self.play(Indicate(b_units), Indicate(t_tens))
        self.play(indicate_carry(carry_2))
        
        # Side calculation: 3 x 4 = 12 ... 12 + 2 = 14
        sc2 = MathTex("3", "\\times", "4", "=", "12").scale(digits_scale).move_to([side_x, side_y, 0])
        self.play(Write(sc2))
        self.wait(0.5)
        
        sc2_add = MathTex("12", "+", "2", "=", "14").scale(digits_scale).move_to([side_x, side_y - 1.0, 0])
        sc2_add[2].set_color(CARRY_COLOR) # carry color
        
        self.play(
            TransformFromCopy(sc2[4], sc2_add[0]), # 12
            TransformFromCopy(carry_2[1], sc2_add[2]), # 2
            Write(sc2_add[1]), # +
            Write(sc2_add[3]), # =
            Write(sc2_add[4])  # 14
        )
        self.wait(0.5)
        
        # Turn carry digit red first
        self.play(sc2_add[4][0].animate.set_color(CARRY_COLOR))
        self.wait(0.2)
        
        r1_tens.move_to([x_tens, y_res1, 0])
        c1_in = MathTex("1").scale(carry_scale).move_to([x_hundreds, y_res1 + 0.4*dy, 0]).set_color(CARRY_COLOR)
        c1_in.set_z_index(2)
        c1_out = c1_in.copy().set_color(BLACK).set_stroke(width=5, color=BLACK)
        c1_out.set_z_index(1)
        carry_1 = VGroup(c1_out, c1_in)
        
        # Animate split: 14 -> 4 (result) + 1 (carry)
        self.play(
            FadeOut(carry_2), 
            ReplacementTransform(sc2_add[4][1], r1_tens), # 4
            ReplacementTransform(sc2_add[4][0], c1_in),   # 1
            FadeIn(c1_out),
            FadeOut(sc2),
            FadeOut(sc2_add[:4])
        )
        self.wait(0.5)
        
        # 4 * 2 = 8 + 1 = 9
        self.play(Indicate(b_units), Indicate(t_hundreds))
        self.play(indicate_carry(carry_1))
        
        # Side calc for last digit (optional but good for consistency)
        sc3 = MathTex("2", "\\times", "4", "=", "8").scale(digits_scale).move_to([side_x, side_y, 0])
        self.play(Write(sc3))
        self.wait(0.5)
        
        sc3_add = MathTex("8", "+", "1", "=", "9").scale(digits_scale).move_to([side_x, side_y - 1.0, 0])
        sc3_add[2].set_color(CARRY_COLOR)
        
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
            ReplacementTransform(sc3_add[4], r1_hundreds), # 9
            FadeOut(sc3),
            FadeOut(sc3_add[:4])
        )
        self.wait(1)
        
        # --- Step 2: Multiply by 20 (Tens) ---
        
        # Placeholder 0
        r2_units.move_to([x_units, y_res2, 0]).set_color(YELLOW)
        self.play(Write(r2_units))
        self.wait(0.5)
        
        # 2 * 5 = 10
        self.play(Indicate(b_tens), Indicate(t_units))
        
        sc4 = MathTex("5", "\\times", "2", "=", "10").scale(digits_scale).move_to([side_x, side_y, 0])
        self.play(Write(sc4))
        self.wait(0.5)
        
        # Turn carry digit red first
        self.play(sc4[4][0].animate.set_color(CARRY_COLOR))
        self.wait(0.2)
        
        r2_tens.move_to([x_tens, y_res2, 0])
        c1b_in = MathTex("1").scale(carry_scale).move_to([x_hundreds, y_res2 + 0.4*dy, 0]).set_color(CARRY_COLOR)
        c1b_in.set_z_index(2)
        c1b_out = c1b_in.copy().set_color(BLACK).set_stroke(width=5, color=BLACK)
        c1b_out.set_z_index(1)
        carry_1_b = VGroup(c1b_out, c1b_in)
        
        # Split 10 -> 0, 1
        self.play(
            ReplacementTransform(sc4[4][1], r2_tens), # 0
            ReplacementTransform(sc4[4][0], c1b_in), # 1
            FadeIn(c1b_out),
            FadeOut(sc4[:4])
        )
        self.wait(0.5)
        
        # 2 * 3 = 6 + 1 = 7
        self.play(Indicate(b_tens), Indicate(t_tens))
        self.play(indicate_carry(carry_1_b))
        
        sc5 = MathTex("3", "\\times", "2", "=", "6").scale(digits_scale).move_to([side_x, side_y, 0])
        self.play(Write(sc5))
        self.wait(0.5)
        
        sc5_add = MathTex("6", "+", "1", "=", "7").scale(digits_scale).move_to([side_x, side_y - 1.0, 0])
        sc5_add[2].set_color(CARRY_COLOR)
        
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
        self.play(Indicate(b_tens), Indicate(t_hundreds))
        
        r2_thousands.move_to([x_thousands, y_res2, 0])
        
        # 2 x 2 = 4
        sc6 = MathTex("2", "\\times", "2", "=", "4").scale(digits_scale).move_to([side_x, side_y, 0])
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
        self.play(Indicate(r1_units), Indicate(r2_units))
        self.play(Write(f_units))
        
        # 4 + 0 = 4
        f_tens.move_to([x_tens, y_final, 0])
        self.play(Indicate(r1_tens), Indicate(r2_tens))
        self.play(Write(f_tens))
        
        # 9 + 7 = 16
        f_hundreds.move_to([x_hundreds, y_final, 0])
        # carry 1 for addition (optional visuals, usually we just write 6 and carry 1 mentally or small)
        # Let's write 6 and carry 1 to thousands
        ca_in = MathTex("1").scale(carry_scale).move_to([x_thousands, y_final + 0.4*dy, 0]).set_color(CARRY_COLOR)
        ca_in.set_z_index(2)
        ca_out = ca_in.copy().set_color(BLACK).set_stroke(width=5, color=BLACK)
        ca_out.set_z_index(1)
        carry_add = VGroup(ca_out, ca_in)
        
        self.play(Indicate(r1_hundreds), Indicate(r2_hundreds))
        
        # Let's show side calc for addition too: 9 + 7 = 16
        sc_add = MathTex("9", "+", "7", "=", "16").scale(digits_scale).move_to([side_x, side_y, 0])
        self.play(Write(sc_add))
        self.wait(0.5)
        
        # Turn carry digit red first
        self.play(sc_add[4][0].animate.set_color(CARRY_COLOR))
        self.wait(0.2)
        
        self.play(
            ReplacementTransform(sc_add[4][1], f_hundreds),
            ReplacementTransform(sc_add[4][0], ca_in),
            FadeIn(ca_out),
            FadeOut(sc_add[:4])
        )
        
        # 4 + 1 = 5
        f_thousands.move_to([x_thousands, y_final, 0])
        self.play(Indicate(r2_thousands), indicate_carry(carry_add))
        self.play(FadeOut(carry_add), Write(f_thousands))
        
        self.wait(2)
