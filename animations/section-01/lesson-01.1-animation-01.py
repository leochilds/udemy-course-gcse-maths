from manim import *

class ColumnMultiplication(Scene):
    def construct(self):
        # Configuration
        digits_scale = 1.5
        carry_scale = 0.8
        
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
        
        r1_units.move_to([x_units, y_res1, 0])
        carry_2 = MathTex("2").scale(carry_scale).move_to([x_tens, y_res1 + 0.4*dy, 0]).set_color(RED)
        
        self.play(Write(r1_units)) # Write 0
        self.play(Write(carry_2))  # Carry 2
        self.wait(0.5)
        
        # 4 * 3 = 12 + 2 = 14
        self.play(Indicate(b_units), Indicate(t_tens))
        self.play(Indicate(carry_2))
        
        r1_tens.move_to([x_tens, y_res1, 0])
        carry_1 = MathTex("1").scale(carry_scale).move_to([x_hundreds, y_res1 + 0.4*dy, 0]).set_color(RED)
        
        self.play(FadeOut(carry_2), Write(r1_tens)) # Write 4
        self.play(Write(carry_1)) # Carry 1
        self.wait(0.5)
        
        # 4 * 2 = 8 + 1 = 9
        self.play(Indicate(b_units), Indicate(t_hundreds))
        self.play(Indicate(carry_1))
        
        r1_hundreds.move_to([x_hundreds, y_res1, 0])
        
        self.play(FadeOut(carry_1), Write(r1_hundreds)) # Write 9
        self.wait(1)
        
        # --- Step 2: Multiply by 20 (Tens) ---
        
        # Placeholder 0
        r2_units.move_to([x_units, y_res2, 0]).set_color(YELLOW)
        self.play(Write(r2_units))
        self.wait(0.5)
        
        # 2 * 5 = 10
        self.play(Indicate(b_tens), Indicate(t_units))
        
        r2_tens.move_to([x_tens, y_res2, 0])
        carry_1_b = MathTex("1").scale(carry_scale).move_to([x_hundreds, y_res2 + 0.4*dy, 0]).set_color(RED)
        
        self.play(Write(r2_tens)) # Write 0
        self.play(Write(carry_1_b)) # Carry 1
        self.wait(0.5)
        
        # 2 * 3 = 6 + 1 = 7
        self.play(Indicate(b_tens), Indicate(t_tens))
        self.play(Indicate(carry_1_b))
        
        r2_hundreds.move_to([x_hundreds, y_res2, 0])
        
        self.play(FadeOut(carry_1_b), Write(r2_hundreds)) # Write 7
        self.wait(0.5)
        
        # 2 * 2 = 4
        self.play(Indicate(b_tens), Indicate(t_hundreds))
        
        r2_thousands.move_to([x_thousands, y_res2, 0])
        self.play(Write(r2_thousands)) # Write 4
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
        carry_add = MathTex("1").scale(carry_scale).move_to([x_thousands, y_final + 0.4*dy, 0]).set_color(RED)
        
        self.play(Indicate(r1_hundreds), Indicate(r2_hundreds))
        self.play(Write(f_hundreds))
        self.play(Write(carry_add))
        
        # 4 + 1 = 5
        f_thousands.move_to([x_thousands, y_final, 0])
        self.play(Indicate(r2_thousands), Indicate(carry_add))
        self.play(FadeOut(carry_add), Write(f_thousands))
        
        self.wait(2)
