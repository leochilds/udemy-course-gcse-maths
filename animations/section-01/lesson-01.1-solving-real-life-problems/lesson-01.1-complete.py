from manim import *
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from animations.styles import Brand
from manim_voiceover import VoiceoverScene
from animations.voxcpm_service import VoxCPMService

class Lesson011Complete(VoiceoverScene):
    def construct(self):
        Brand.set_default_theme(self)
        self.set_speech_service(VoxCPMService(
            checkpoint_dir="/home/leo/code/udemy-course-gcse-maths/checkpoints/myvoice/step_0002000",
            base_model_path="/home/leo/code/udemy-course-gcse-maths/models/VoxCPM1.5"
        ))
        
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
        with self.voiceover(text="Welcome to this lesson on solving real-life problems. Throughout your maths course and in daily life, you will encounter problems set in real-world contexts.") as tracker:
            title = Text("Solving Real-Life Problems").scale(1.2).to_edge(UP)
            underline = Line(LEFT, RIGHT).next_to(title, DOWN).scale(2)
            
            self.play(Write(title), Create(underline))

        strategies = VGroup(
            Text("Key Strategies:").scale(0.8).set_color(Brand.ACTIVE),
            Text("• Read").scale(0.7),
            Text("• Plan").scale(0.7),
            Text("• Calculate").scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT).shift(LEFT * 3.5)
        
        methods = VGroup(
            Text("Methods:").scale(0.8).set_color(Brand.ACTIVE),
            Text("• Grid Method").scale(0.7),
            Text("• Column Method").scale(0.7),
            Text("• Long Division").scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 3.5)
        
        # Align tops
        methods.match_y(strategies)

        with self.voiceover(text="These require you to read carefully, plan a strategy, and apply arithmetic skills.") as tracker:
            self.play(Write(strategies))

        with self.voiceover(text="In this lesson, we will look at how to approach these problems effectively, using long multiplication and division strategies.") as tracker:
            self.play(Write(methods))

        self.wait(2)

    def slide_02_strategy(self):
        with self.voiceover(text="When facing a word problem, it's helpful to have a consistent approach.") as tracker:
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
        
        with self.voiceover(text="First, read the question carefully to identify the key information.") as tracker:
            self.play(Write(s1))
            self.play(FadeIn(t1))

        with self.voiceover(text="Second, plan your strategy—decide which mathematical operations you need to use.") as tracker:
            self.play(Write(s2))
            self.play(FadeIn(t2))

        with self.voiceover(text="Third, perform the calculation. You might need to use long multiplication or long division if a calculator isn't allowed.") as tracker:
            self.play(Write(s3))
            self.play(FadeIn(t3))

        with self.voiceover(text="Finally, always check your answer. Ask yourself: is this a reasonable number for this situation?") as tracker:
            self.play(Write(s4))
            self.play(FadeIn(t4))
            self.wait(0.5)

    def slide_03_example_1_context(self):
        with self.voiceover(text="Let's apply this to an example.") as tracker:
            title = Text("Example 1: The Supermarket").scale(1.0).to_edge(UP)
            self.play(Write(title))
            
        icon_case = Square().scale(0.5).set_fill(Brand.AUXILIARY, opacity=0.5)
        t_delivery = Text("Delivery: 235 Cases").scale(0.8).next_to(icon_case, RIGHT)
        g_delivery = VGroup(icon_case, t_delivery).move_to([0, 1, 0])
        
        t_contents = Text("Each Case: 24 Tins").scale(0.8).next_to(g_delivery, DOWN, buff=0.5)

        with self.voiceover(text="A supermarket receives a delivery of two hundred and thirty-five cases of tins of beans.") as tracker:
            self.play(Create(icon_case), Write(t_delivery))

        with self.voiceover(text="Each case contains twenty-four tins.") as tracker:
            self.play(Write(t_contents))
            self.wait(1)
            
        t_question = Text("How many tins altogether?").scale(1.0).set_color(Brand.ACTIVE).next_to(t_contents, DOWN, buff=1.0)
        
        with self.voiceover(text="We need to calculate how many tins the supermarket receives altogether.") as tracker:
            self.play(Write(t_question))
            self.wait(1)
            
        t_calc = MathTex("235 \\times 24").scale(1.5).set_color(Brand.ANSWER).next_to(t_question, DOWN, buff=0.5)

        with self.voiceover(text="Since we have two hundred and thirty-five groups of twenty-four, our strategy is multiplication. We need to calculate two hundred and thirty-five multiplied by twenty-four.") as tracker:
            self.play(Write(t_calc))
            self.wait(1)

    def slide_04_calculations(self):
        # --- Grid Method ---
        with self.voiceover(text="There are several ways to perform this calculation. You should use the method you are most comfortable with. Let's start with the Grid Method, also known as the Box Method.") as tracker:
            title = Text("Grid Method").scale(1.0).to_edge(UP)
            self.play(Write(title))
            self.wait(0.5)
            self.play(FadeOut(title))
            
            # Setup Grid Logic
            digits_scale = 1.0
            header_scale = 1.2
            col_x = [-6, -3.5, -1, 1] # Shifted LEFT
            row_y = [2, 0, -2]       # Y coords for rows
            h_lines_y = [1, -1]      # Y coords for horizontal separators
            v_lines_x = [-4.5]       # Shifted LEFT
            
            # 1. Introduction
            problem = MathTex("235", "\\times", "24").scale(1.5).move_to([0, 3, 0])
            self.play(Write(problem))
            self.play(problem.animate.scale(0.7).to_corner(UL))
            
            # 2. Setup Grid Headers
            h_200 = MathTex("200").scale(header_scale).move_to([col_x[1], row_y[0], 0])
            h_30 = MathTex("30").scale(header_scale).move_to([col_x[2], row_y[0], 0])
            h_5 = MathTex("5").scale(header_scale).move_to([col_x[3], row_y[0], 0])
            h_20 = MathTex("20").scale(header_scale).move_to([col_x[0], row_y[1], 0])
            h_4 = MathTex("4").scale(header_scale).move_to([col_x[0], row_y[2], 0])
            mult_sign = MathTex("\\times").scale(header_scale).move_to([col_x[0], row_y[0], 0])
            
            line_h1 = Line(start=[-7, h_lines_y[0], 0], end=[2, h_lines_y[0], 0])
            line_h2 = Line(start=[-7, h_lines_y[1], 0], end=[2, h_lines_y[1], 0])
            line_v1 = Line(start=[v_lines_x[0], 3, 0], end=[v_lines_x[0], -3, 0])
            grid_group = VGroup(line_h1, line_h2, line_v1)

        with self.voiceover(text="We break two hundred and thirty-five into two hundred, thirty, and five.") as tracker:
            self.play(
                ReplacementTransform(problem[0][0].copy(), h_200),
                ReplacementTransform(problem[0][1].copy(), h_30),
                ReplacementTransform(problem[0][2].copy(), h_5)
            )

        with self.voiceover(text="We break twenty-four into twenty and four.") as tracker:
            self.play(
                ReplacementTransform(problem[2][0].copy(), h_20),
                ReplacementTransform(problem[2][1].copy(), h_4)
            )
            self.play(Create(grid_group), Write(mult_sign))
        
        # Calculations
        def animate_cell(row_header, col_header, result_val, pos_idx_x, pos_idx_y):
            pos = [col_x[pos_idx_x], row_y[pos_idx_y], 0]
            result_mob = MathTex(str(result_val)).scale(digits_scale).move_to(pos)
            self.play(
                Indicate(row_header, color=Brand.ACTIVE), 
                Indicate(col_header, color=Brand.ACTIVE),
                run_time=1
            )
            self.play(Write(result_mob))
            return result_mob
        
        with self.voiceover(text="Now we multiply each part. Two hundred times twenty is four thousand.") as tracker:
            c_20_200 = animate_cell(h_20, h_200, "4000", 1, 1)

        with self.voiceover(text="Thirty times twenty is six hundred.") as tracker:
            c_20_30 = animate_cell(h_20, h_30, "600", 2, 1)

        with self.voiceover(text="Five times twenty is one hundred.") as tracker:
            c_20_5 = animate_cell(h_20, h_5, "100", 3, 1)

        with self.voiceover(text="Then we multiply by four: Two hundred times four is eight hundred.") as tracker:
            c_4_200 = animate_cell(h_4, h_200, "800", 1, 2)

        with self.voiceover(text="Thirty times four is one hundred and twenty.") as tracker:
            c_4_30 = animate_cell(h_4, h_30, "120", 2, 2)

        with self.voiceover(text="Five times four is twenty.") as tracker:
            c_4_5 = animate_cell(h_4, h_5, "20", 3, 2)

        with self.voiceover(text="Finally, we add all these answers together: Four thousand plus six hundred plus one hundred is four thousand seven hundred.") as tracker:
            row1_group = VGroup(c_20_200, c_20_30, c_20_5)
            row1_sum_text = MathTex("4000", "+", "600", "+", "100", "=", "4700").scale(0.8)
            row1_sum_text.to_edge(RIGHT).shift(UP * 1)
            self.play(TransformFromCopy(row1_group, row1_sum_text[:5]))
            self.play(Write(row1_sum_text[5:]))
            self.play(row1_sum_text[6].animate.set_color(Brand.ACTIVE))

        with self.voiceover(text="Eight hundred plus one hundred and twenty plus twenty is nine hundred and forty.") as tracker:
            row2_group = VGroup(c_4_200, c_4_30, c_4_5)
            row2_sum_text = MathTex("800", "+", "120", "+", "20", "=", "940").scale(0.8)
            row2_sum_text.next_to(row1_sum_text, DOWN, aligned_edge=RIGHT)
            self.play(TransformFromCopy(row2_group, row2_sum_text[:5]))
            self.play(Write(row2_sum_text[5:]))
            self.play(row2_sum_text[6].animate.set_color(Brand.ACTIVE))

        with self.voiceover(text="Adding four thousand seven hundred and nine hundred and forty gives us a total of five thousand six hundred and forty.") as tracker:
            line_sum = Line(start=row2_sum_text.get_left(), end=row2_sum_text.get_right()).next_to(row2_sum_text, DOWN)
            final_sum_text = MathTex("5640").scale(1.2).set_color(Brand.ANSWER)
            final_sum_text.next_to(line_sum, DOWN, aligned_edge=RIGHT)
            plus_sign = MathTex("+").next_to(row2_sum_text, LEFT)
            self.play(Create(line_sum), Write(plus_sign))
            final_sum_text.set_z_index(10)
            self.play(Write(final_sum_text))
            self.wait(1)

        self.clear_screen()
        
        # --- Column Method ---
        with self.voiceover(text="Now let's look at the Column Method.") as tracker:
            title = Text("Column Method").scale(1.0).to_edge(UP)
            self.play(Write(title))
            self.wait(0.5)
            self.play(FadeOut(title))
            
            # Configuration
            def indicate_carry(mob):
                target = mob.copy().scale(1.2)
                target[1].set_color(Brand.ACTIVE)
                return Transform(mob, target, rate_func=there_and_back, run_time=1)

            digits_scale = 1.5
            carry_scale = 0.8
            n1 = 235
            n2 = 24
            center_x = 0
            center_y = 1
            dx = 0.8
            dy = 1.0
            side_x = 4.0
            side_y = 0.5
            y_top = center_y + dy
            y_bot = center_y
            y_line1 = center_y - 0.5 * dy
            y_res1 = center_y - dy
            y_res2 = center_y - 2 * dy
            y_line2 = center_y - 2.5 * dy
            y_final = center_y - 3 * dy
            x_units = 1.5 * dx
            x_tens = 0.5 * dx
            x_hundreds = -0.5 * dx
            x_thousands = -1.5 * dx
            
            # Create Objects
            t_hundreds = MathTex("2").scale(digits_scale).move_to([x_hundreds, y_top, 0])
            t_tens = MathTex("3").scale(digits_scale).move_to([x_tens, y_top, 0])
            t_units = MathTex("5").scale(digits_scale).move_to([x_units, y_top, 0])
            b_tens = MathTex("2").scale(digits_scale).move_to([x_tens, y_bot, 0])
            b_units = MathTex("4").scale(digits_scale).move_to([x_units, y_bot, 0])
            operator = MathTex("\\times").scale(digits_scale).move_to([x_thousands, y_bot, 0])
            line1 = Line(start=[x_thousands - dx, y_line1, 0], end=[x_units + dx, y_line1, 0])
            
            r1_hundreds = MathTex("9").scale(digits_scale)
            r1_tens = MathTex("4").scale(digits_scale)
            r1_units = MathTex("0").scale(digits_scale)
            r2_thousands = MathTex("4").scale(digits_scale)
            r2_hundreds = MathTex("7").scale(digits_scale)
            r2_tens = MathTex("0").scale(digits_scale)
            r2_units = MathTex("0").scale(digits_scale)
            f_thousands = MathTex("5").scale(digits_scale).set_color(Brand.ANSWER)
            f_hundreds = MathTex("6").scale(digits_scale).set_color(Brand.ANSWER)
            f_tens = MathTex("4").scale(digits_scale).set_color(Brand.ANSWER)
            f_units = MathTex("0").scale(digits_scale).set_color(Brand.ANSWER)

            self.play(Write(t_hundreds), Write(t_tens), Write(t_units))
            self.play(Write(operator), Write(b_tens), Write(b_units))
            self.play(Create(line1))

        with self.voiceover(text="First, we multiply two hundred and thirty-five by four.") as tracker:
            self.play(Indicate(b_units, color=Brand.ACTIVE), Indicate(t_units, color=Brand.ACTIVE))

        with self.voiceover(text="Four times five is twenty, so write the zero and carry the two.") as tracker:
            sc1 = MathTex("5", "\\times", "4", "=", "20").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
            self.play(Write(sc1))
            r1_units.move_to([x_units, y_res1, 0])
            c2_in = MathTex("2").scale(carry_scale).move_to([x_tens, y_res1 + 0.4*dy, 0]).set_color(Brand.CARRY)
            c2_in.set_z_index(2)
            c2_out = c2_in.copy().set_color(Brand.BACKGROUND).set_stroke(width=5, color=Brand.BACKGROUND)
            c2_out.set_z_index(1)
            carry_2 = VGroup(c2_out, c2_in)
            self.play(sc1[4][0].animate.set_color(Brand.CARRY))
            self.play(
                ReplacementTransform(sc1[4][1], r1_units),
                ReplacementTransform(sc1[4][0], c2_in),
                FadeIn(c2_out),
                FadeOut(sc1[:4])
            )

        with self.voiceover(text="Four times three is twelve, plus the carried two is fourteen. Write the four and carry the one.") as tracker:
            self.play(Indicate(b_units, color=Brand.ACTIVE), Indicate(t_tens, color=Brand.ACTIVE))
            self.play(indicate_carry(carry_2))
            sc2 = MathTex("3", "\\times", "4", "=", "12").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
            self.play(Write(sc2))
            sc2_add = MathTex("12", "+", "2", "=", "14").scale(digits_scale).move_to([side_x, side_y - 1.0, 0]).set_color(Brand.AUXILIARY)
            sc2_add[2].set_color(Brand.CARRY)
            self.play(
                TransformFromCopy(sc2[4], sc2_add[0]),
                TransformFromCopy(carry_2[1], sc2_add[2]),
                Write(sc2_add[1]),
                Write(sc2_add[3]),
                Write(sc2_add[4])
            )
            self.play(sc2_add[4][0].animate.set_color(Brand.CARRY))
            r1_tens.move_to([x_tens, y_res1, 0])
            c1_in = MathTex("1").scale(carry_scale).move_to([x_hundreds, y_res1 + 0.4*dy, 0]).set_color(Brand.CARRY)
            c1_in.set_z_index(2)
            c1_out = c1_in.copy().set_color(Brand.BACKGROUND).set_stroke(width=5, color=Brand.BACKGROUND)
            c1_out.set_z_index(1)
            carry_1 = VGroup(c1_out, c1_in)
            self.play(
                FadeOut(carry_2), 
                ReplacementTransform(sc2_add[4][1], r1_tens),
                ReplacementTransform(sc2_add[4][0], c1_in),
                FadeIn(c1_out),
                FadeOut(sc2),
                FadeOut(sc2_add[:4])
            )

        with self.voiceover(text="Four times two is eight, plus the one is nine. This gives us nine hundred and forty.") as tracker:
            self.play(Indicate(b_units, color=Brand.ACTIVE), Indicate(t_hundreds, color=Brand.ACTIVE))
            self.play(indicate_carry(carry_1))
            sc3 = MathTex("2", "\\times", "4", "=", "8").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
            self.play(Write(sc3))
            sc3_add = MathTex("8", "+", "1", "=", "9").scale(digits_scale).move_to([side_x, side_y - 1.0, 0]).set_color(Brand.AUXILIARY)
            sc3_add[2].set_color(Brand.CARRY)
            self.play(
                TransformFromCopy(sc3[4], sc3_add[0]),
                TransformFromCopy(carry_1[1], sc3_add[2]),
                Write(sc3_add[1]),
                Write(sc3_add[3]),
                Write(sc3_add[4])
            )
            r1_hundreds.move_to([x_hundreds, y_res1, 0])
            self.play(
                FadeOut(carry_1), 
                ReplacementTransform(sc3_add[4], r1_hundreds),
                FadeOut(sc3),
                FadeOut(sc3_add[:4])
            )

        with self.voiceover(text="Next, we multiply by the twenty. We start by placing a zero in the units column.") as tracker:
            r2_units.move_to([x_units, y_res2, 0]).set_color(Brand.ACTIVE)
            self.play(Write(r2_units))

        with self.voiceover(text="Then, two times five is ten; write zero, carry one.") as tracker:
            self.play(Indicate(b_tens, color=Brand.ACTIVE), Indicate(t_units, color=Brand.ACTIVE))
            sc4 = MathTex("5", "\\times", "2", "=", "10").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
            self.play(Write(sc4))
            self.play(sc4[4][0].animate.set_color(Brand.CARRY))
            r2_tens.move_to([x_tens, y_res2, 0])
            c1b_in = MathTex("1").scale(carry_scale).move_to([x_hundreds, y_res2 + 0.4*dy, 0]).set_color(Brand.CARRY)
            c1b_in.set_z_index(2)
            c1b_out = c1b_in.copy().set_color(Brand.BACKGROUND).set_stroke(width=5, color=Brand.BACKGROUND)
            c1b_out.set_z_index(1)
            carry_1_b = VGroup(c1b_out, c1b_in)
            self.play(
                ReplacementTransform(sc4[4][1], r2_tens),
                ReplacementTransform(sc4[4][0], c1b_in),
                FadeIn(c1b_out),
                FadeOut(sc4[:4])
            )

        with self.voiceover(text="Two times three is six, plus one is seven.") as tracker:
            self.play(Indicate(b_tens, color=Brand.ACTIVE), Indicate(t_tens, color=Brand.ACTIVE))
            self.play(indicate_carry(carry_1_b))
            sc5 = MathTex("3", "\\times", "2", "=", "6").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
            self.play(Write(sc5))
            sc5_add = MathTex("6", "+", "1", "=", "7").scale(digits_scale).move_to([side_x, side_y - 1.0, 0]).set_color(Brand.AUXILIARY)
            sc5_add[2].set_color(Brand.CARRY)
            self.play(
                TransformFromCopy(sc5[4], sc5_add[0]),
                TransformFromCopy(carry_1_b[1], sc5_add[2]),
                Write(sc5_add[1]),
                Write(sc5_add[3]),
                Write(sc5_add[4])
            )
            r2_hundreds.move_to([x_hundreds, y_res2, 0])
            self.play(
                FadeOut(carry_1_b), 
                ReplacementTransform(sc5_add[4], r2_hundreds),
                FadeOut(sc5),
                FadeOut(sc5_add[:4])
            )

        with self.voiceover(text="Two times two is four. This gives us four thousand seven hundred.") as tracker:
            self.play(Indicate(b_tens, color=Brand.ACTIVE), Indicate(t_hundreds, color=Brand.ACTIVE))
            r2_thousands.move_to([x_thousands, y_res2, 0])
            sc6 = MathTex("2", "\\times", "2", "=", "4").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
            self.play(Write(sc6))
            self.play(
                ReplacementTransform(sc6[4], r2_thousands),
                FadeOut(sc6[:4])
            )

        with self.voiceover(text="Finally, we add nine hundred and forty and four thousand seven hundred together to get five thousand six hundred and forty.") as tracker:
            line2 = Line(start=[x_thousands - dx, y_line2, 0], end=[x_units + dx, y_line2, 0])
            plus = MathTex("+").scale(digits_scale).move_to([x_thousands - dx + 0.2, y_res2, 0])
            self.play(Create(line2), Write(plus))
            
            f_units.move_to([x_units, y_final, 0])
            self.play(Indicate(r1_units, color=Brand.ACTIVE), Indicate(r2_units, color=Brand.ACTIVE))
            self.play(Write(f_units))
            
            f_tens.move_to([x_tens, y_final, 0])
            self.play(Indicate(r1_tens, color=Brand.ACTIVE), Indicate(r2_tens, color=Brand.ACTIVE))
            self.play(Write(f_tens))
            
            f_hundreds.move_to([x_hundreds, y_final, 0])
            ca_in = MathTex("1").scale(carry_scale).move_to([x_thousands, y_final + 0.4*dy, 0]).set_color(Brand.CARRY)
            ca_in.set_z_index(2)
            ca_out = ca_in.copy().set_color(Brand.BACKGROUND).set_stroke(width=5, color=Brand.BACKGROUND)
            ca_out.set_z_index(1)
            carry_add = VGroup(ca_out, ca_in)
            self.play(Indicate(r1_hundreds, color=Brand.ACTIVE), Indicate(r2_hundreds, color=Brand.ACTIVE))
            sc_add = MathTex("9", "+", "7", "=", "16").scale(digits_scale).move_to([side_x, side_y, 0]).set_color(Brand.AUXILIARY)
            self.play(Write(sc_add))
            self.play(sc_add[4][0].animate.set_color(Brand.CARRY))
            self.play(
                ReplacementTransform(sc_add[4][1], f_hundreds),
                ReplacementTransform(sc_add[4][0], ca_in),
                FadeIn(ca_out),
                FadeOut(sc_add[:4])
            )
            
            f_thousands.move_to([x_thousands, y_final, 0])
            self.play(Indicate(r2_thousands, color=Brand.ACTIVE), indicate_carry(carry_add))
            self.play(FadeOut(carry_add), Write(f_thousands))

        with self.voiceover(text="Both methods give us the same result: five thousand six hundred and forty tins.") as tracker:
            self.wait(1)

    def slide_05_part_b_context(self):
        with self.voiceover(text="Now for the second part of the problem.") as tracker:
            title = Text("Example 1: Part B").scale(1.0).to_edge(UP)
            self.play(Write(title))
            
        with self.voiceover(text="We are told that five percent of the tins were damaged and thrown away.") as tracker:
            t_damaged = Text("• 5% of tins damaged (thrown away)").scale(0.8).move_to([0, 1, 0])
            self.play(Write(t_damaged))

        with self.voiceover(text="The supermarket sells two hundred and fifty tins a day.") as tracker:
            t_sales = Text("• Sales: 250 tins/day").scale(0.8).next_to(t_damaged, DOWN, buff=0.5)
            self.play(Write(t_sales))

        with self.voiceover(text="We need to find out how many days the remaining beans will last. This is a multi-step problem. First, we must calculate how many tins are left after removing the damaged ones. Second, we divide that number by the daily sales of two hundred and fifty.") as tracker:
            t_q = Text("How many days will stock last?").scale(1.0).set_color(Brand.ACTIVE).next_to(t_sales, DOWN, buff=1.0)
            self.play(Write(t_q))
            self.wait(1)

    def slide_06_part_b_calc(self):
        # --- Stock Calculation ---
        with self.voiceover(text="Let's work through the numbers. We started with five thousand six hundred and forty tins.") as tracker:
            title = Text("Stock Calculation").scale(0.8).to_corner(UL).set_color(Brand.AUXILIARY)
            self.play(Write(title))
            
            total_tins_label = Text("Total Tins:").scale(0.8).move_to([-2, 2, 0])
            total_tins_val = MathTex("5640").scale(1.2).next_to(total_tins_label, RIGHT)
            self.play(Write(total_tins_label), Write(total_tins_val))
            
        with self.voiceover(text="To find five percent, we can first find ten percent, which is five hundred and sixty-four.") as tracker:
            p10_label = MathTex("10\\% = ").scale(0.8).move_to([-2, 1, 0])
            p10_val = MathTex("564").scale(0.8).next_to(p10_label, RIGHT)
            self.play(Write(p10_label))
            self.play(TransformFromCopy(total_tins_val, p10_val))
            
        with self.voiceover(text="Five percent is half of ten percent, so half of five hundred and sixty-four is two hundred and eighty-two.") as tracker:
            p5_label = MathTex("5\\% = ").scale(0.8).next_to(p10_label, DOWN, aligned_edge=LEFT)
            p5_calc = MathTex("564 \\div 2 = ").scale(0.8).next_to(p5_label, RIGHT)
            p5_val = MathTex("282").scale(0.8).next_to(p5_calc, RIGHT).set_color(Brand.CARRY)
            self.play(Write(p5_label), Write(p5_calc))
            self.play(Write(p5_val))

        with self.voiceover(text="We subtract these damaged tins from the total: five thousand six hundred and forty minus two hundred and eighty-two leaves us with five thousand three hundred and fifty-eight saleable tins.") as tracker:
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
            self.play(Write(sub_val))
            
        with self.voiceover(text="Now we need to divide five thousand three hundred and fifty-eight by two hundred and fifty to find the number of days.") as tracker:
             # Cleanup Part 1
            part1_group = VGroup(
                total_tins_label, total_tins_val,
                p10_label, p10_val,
                p5_label, p5_calc, p5_val,
                sub_label, sub_calc, sub_val
            )
            self.play(
                FadeOut(part1_group),
                sub_val.animate.scale(0.8).to_corner(UR).set_color(Brand.TEXT)
            )
            
            # Setup Division
            div_problem = MathTex("5358", "\\div", "250").scale(1.2).move_to([0, 2.5, 0])
            self.play(ReplacementTransform(sub_val, div_problem[0]), Write(div_problem[1:]))

        with self.voiceover(text="We can estimate this. We know that four lots of two hundred and fifty make one thousand.") as tracker:
            est_box = VGroup()
            est_title = Text("Estimations:").scale(0.6).set_color(Brand.AUXILIARY)
            est1 = MathTex("4 \\times 250 = 1000").scale(0.8)
            est2 = MathTex("20 \\times 250 = 5000").scale(0.8)
            est_group = VGroup(est_title, est1, est2).arrange(DOWN, aligned_edge=LEFT).move_to([-3, 0, 0])
            self.play(Write(est_title))
            self.play(Write(est1))

        with self.voiceover(text="Therefore, twenty lots of two hundred and fifty make five thousand.") as tracker:
            self.play(Write(est2))
            self.play(Indicate(est2, color=Brand.ACTIVE))

        with self.voiceover(text="If we subtract five thousand from five thousand three hundred and fifty-eight, we are left with three hundred and fifty-eight.") as tracker:
            step1_calc = MathTex("5358", "-", "5000", "=", "358").scale(1.0).move_to([2, 0.5, 0])
            self.play(
                TransformFromCopy(div_problem[0], step1_calc[0]),
                Write(step1_calc[1]),
                TransformFromCopy(est2[0][-4:], step1_calc[2]), 
                Write(step1_calc[3]),
                Write(step1_calc[4])
            )

        with self.voiceover(text="How many two hundred and fifties are in three hundred and fifty-eight? There is one lot of two hundred and fifty, with a remainder.") as tracker:
            rem_check = Text("How many 250s in 358?").scale(0.6).next_to(step1_calc, DOWN, buff=0.5).set_color(Brand.AUXILIARY)
            rem_ans = MathTex("1 \\times 250 = 250").scale(0.8).next_to(rem_check, DOWN)
            self.play(Write(rem_check))
            self.play(Write(rem_ans))

        with self.voiceover(text="So, we have twenty days plus one day, giving us twenty-one full days. The remainder means we have a few beans left over, but not enough for a twenty-second day.") as tracker:
            final_days_label = Text("Total Days:").scale(0.8).move_to([0, -2.5, 0])
            final_days_calc = MathTex("20", "+", "1", "=", "21").scale(1.2).next_to(final_days_label, RIGHT)
            final_days_calc[4].set_color(Brand.ANSWER)
            self.play(Write(final_days_label))
            self.play(
                TransformFromCopy(est2[0][0:2], final_days_calc[0]), 
                Write(final_days_calc[1]),
                TransformFromCopy(rem_ans[0][0], final_days_calc[2]), 
                Write(final_days_calc[3]),
                Write(final_days_calc[4])
            )
            self.play(Circumscribe(final_days_calc[4], color=Brand.ANSWER))
            self.wait(1)

    def slide_07_example_2_context(self):
        with self.voiceover(text="Let's look at a second example. A party of six hundred and thirteen children and fifty-nine adults are going to a theme park.") as tracker:
            title = Text("Example 2: Theme Park").scale(1.0).to_edge(UP)
            self.play(Write(title))
            
            t_kids = Text("613 Children").scale(0.8).shift(LEFT * 3 + UP * 1)
            t_adults = Text("59 Adults").scale(0.8).next_to(t_kids, DOWN, buff=0.5)
            self.play(Write(t_kids), Write(t_adults))

        with self.voiceover(text="We need to determine how many coaches are needed if each holds fifty-three people.") as tracker:
             self.wait(1)

        with self.voiceover(text="First, we find the total number of people by adding six hundred and thirteen and fifty-nine, which gives us six hundred and seventy-two.") as tracker:
            line = Line(start=t_adults.get_left() + DOWN * 0.2, end=t_adults.get_right() + RIGHT * 2 + DOWN * 0.2)
            calc = MathTex("613 + 59 = 672").scale(1.2).next_to(t_adults, RIGHT, buff=2).set_color(Brand.ANSWER)
            self.play(Write(calc))
            
            t_total = Text("Total People: 672").scale(1.0).move_to([0, -1, 0]).set_color(Brand.ANSWER)
            self.play(TransformFromCopy(calc, t_total))

        with self.voiceover(text="The strategy here is division: we divide the total people, six hundred and seventy-two, by the coach capacity, fifty-three.") as tracker:
            t_coach = Text("Coach Capacity: 53").scale(0.8).next_to(t_total, DOWN, buff=0.5)
            self.play(Write(t_coach))
            
            t_strategy = MathTex("672 \\div 53").scale(1.2).set_color(Brand.ACTIVE).next_to(t_coach, DOWN, buff=0.5)
            self.play(Write(t_strategy))
            self.wait(1)

    def slide_08_interpreting(self):
        # --- Division & Interpretation ---
        
        # Setup
        digits_scale = 1.2
        note_scale = 0.8
        d_53 = MathTex("5", "3").scale(digits_scale).move_to([-3, 2, 0])
        div_6 = MathTex("6").scale(digits_scale).next_to(d_53, RIGHT, buff=0.5)
        div_7 = MathTex("7").scale(digits_scale).next_to(div_6, RIGHT, buff=0.3)
        div_2 = MathTex("2").scale(digits_scale).next_to(div_7, RIGHT, buff=0.3)
        dividend_group = VGroup(div_6, div_7, div_2)
        p_bottom_left = div_6.get_corner(DL) + LEFT * 0.2 + DOWN * 0.1
        p_top_left = div_6.get_corner(UL) + LEFT * 0.2 + UP * 0.1
        p_top_right = div_2.get_corner(UR) + RIGHT * 0.1 + UP * 0.1
        bus_stop_curve = ArcBetweenPoints(start=p_top_left, end=p_bottom_left, angle=-TAU/4)
        bus_stop_line = Line(p_top_left, p_top_right)
        bus_stop = VGroup(bus_stop_curve, bus_stop_line)

        with self.voiceover(text="We need to calculate six hundred and seventy-two divided by fifty-three using long division.") as tracker:
            self.play(Write(d_53), Create(bus_stop), Write(dividend_group))

        with self.voiceover(text="First, how many fifty-threes go into sixty-seven? The answer is one. We write the one above the line.") as tracker:
            self.play(
                Indicate(d_53, color=Brand.ACTIVE),
                Indicate(VGroup(div_6, div_7), color=Brand.ACTIVE)
            )
            ans_1 = MathTex("1").scale(digits_scale).next_to(div_7, UP, buff=0.3)
            ans_1.set_x(div_7.get_x())
            self.play(Write(ans_1))

        with self.voiceover(text="One times fifty-three is fifty-three. Subtracting fifty-three from sixty-seven gives us fourteen.") as tracker:
            mult_res_53 = MathTex("5", "3").scale(digits_scale)
            mult_res_53[0].move_to([div_6.get_x(), div_6.get_y() - 1.0, 0])
            mult_res_53[1].move_to([div_7.get_x(), div_7.get_y() - 1.0, 0])
            minus_sign_1 = MathTex("-").scale(digits_scale).next_to(mult_res_53, LEFT, buff=0.2)
            line_sub_1 = Line(
                start=mult_res_53.get_corner(DL) + DOWN * 0.1 + LEFT * 0.2,
                end=mult_res_53.get_corner(DR) + DOWN * 0.1 + RIGHT * 0.2
            )
            self.play(Write(mult_res_53), Write(minus_sign_1), Create(line_sub_1))
            res_14 = MathTex("1", "4").scale(digits_scale)
            res_14[0].move_to([div_6.get_x(), mult_res_53.get_y() - 1.0, 0])
            res_14[1].move_to([div_7.get_x(), mult_res_53.get_y() - 1.0, 0])
            self.play(Write(res_14))

        with self.voiceover(text="Now, bring down the two to make one hundred and forty-two.") as tracker:
            arrow_down = Arrow(start=div_2.get_bottom(), end=[div_2.get_x(), res_14.get_y(), 0], buff=0.1, color=Brand.AUXILIARY)
            res_2_down = MathTex("2").scale(digits_scale).move_to([div_2.get_x(), res_14.get_y(), 0])
            self.play(Create(arrow_down))
            self.play(TransformFromCopy(div_2, res_2_down))
            self.play(FadeOut(arrow_down))
            curr_142 = VGroup(res_14, res_2_down)

        with self.voiceover(text="How many fifty-threes go into one hundred and forty-two? Let's estimate.") as tracker:
            self.play(Indicate(d_53, color=Brand.ACTIVE), Indicate(curr_142, color=Brand.ACTIVE))
            side_calc_pos = [3, 1, 0]
            side_est_1 = MathTex("53", "\\times", "2", "=", "106").scale(note_scale).move_to(side_calc_pos).set_color(Brand.AUXILIARY)
            side_est_2 = MathTex("53", "\\times", "3", "=", "159").scale(note_scale).next_to(side_est_1, DOWN).set_color(Brand.AUXILIARY)
            cross = Cross(side_est_2).scale(0.8)

        with self.voiceover(text="Fifty times two is one hundred.") as tracker:
            self.play(Write(side_est_1))

        with self.voiceover(text="Fifty times three is one hundred and fifty, which is too high. So it must be two.") as tracker:
            self.play(Write(side_est_2))
            self.play(Create(cross))

        with self.voiceover(text="We write the two above the line. Two times fifty-three is one hundred and six.") as tracker:
            ans_2 = MathTex("2").scale(digits_scale).next_to(ans_1, RIGHT, buff=0.3)
            ans_2.set_x(div_2.get_x())
            self.play(Write(ans_2))
            
            mult_res_106 = MathTex("1", "0", "6").scale(digits_scale)
            mult_res_106[0].move_to([res_14[0].get_x(), res_14.get_y() - 1.0, 0])
            mult_res_106[1].move_to([res_14[1].get_x(), res_14.get_y() - 1.0, 0])
            mult_res_106[2].move_to([res_2_down.get_x(), res_14.get_y() - 1.0, 0])
            minus_sign_2 = MathTex("-").scale(digits_scale).next_to(mult_res_106, LEFT, buff=0.2)
            line_sub_2 = Line(
                start=mult_res_106.get_corner(DL) + DOWN * 0.1 + LEFT * 0.2,
                end=mult_res_106.get_corner(DR) + DOWN * 0.1 + RIGHT * 0.2
            )
            self.play(
                Write(mult_res_106),
                Write(minus_sign_2),
                Create(line_sub_2),
                FadeOut(side_est_1), FadeOut(side_est_2), FadeOut(cross)
            )

        with self.voiceover(text="Subtracting one hundred and six from one hundred and forty-two leaves a remainder of thirty-six. So the answer is twelve remainder thirty-six.") as tracker:
            res_36 = MathTex("3", "6").scale(digits_scale)
            res_36[0].move_to([mult_res_106[1].get_x(), mult_res_106.get_y() - 1.0, 0])
            res_36[1].move_to([mult_res_106[2].get_x(), mult_res_106.get_y() - 1.0, 0])
            self.play(Write(res_36))
            rem_text = MathTex("r", "36").scale(digits_scale).next_to(ans_2, RIGHT, buff=0.3)
            self.play(Write(rem_text[0]), TransformFromCopy(res_36, rem_text[1]))

        with self.voiceover(text="Now we must interpret this answer. The twelve represents full coaches.") as tracker:
            t_full = Text("12 Full Coaches").scale(0.8).move_to([3, 0, 0])
            self.play(Write(t_full))
            self.play(Indicate(VGroup(ans_1, ans_2), color=Brand.ACTIVE))

        with self.voiceover(text="The remainder of thirty-six represents thirty-six people still waiting. We need another coach for them.") as tracker:
            t_rem = Text("36 People Left").scale(0.8).next_to(t_full, DOWN, buff=0.5)
            self.play(Write(t_rem))
            self.play(Indicate(rem_text, color=Brand.ACTIVE))
            t_plus1 = Text("+1 Coach").scale(0.8).next_to(t_rem, DOWN, buff=0.2).set_color(Brand.ACTIVE)
            self.play(Write(t_plus1))

        with self.voiceover(text="So, we round up to thirteen coaches in total.") as tracker:
            line_total = Line(start=t_plus1.get_left(), end=t_plus1.get_right()).next_to(t_plus1, DOWN)
            t_total = Text("13 Coaches Total").scale(1.0).next_to(line_total, DOWN).set_color(Brand.ANSWER)
            self.play(Create(line_total), Write(t_total))
            self.wait(1)

    def slide_09_free_entry(self):
        with self.voiceover(text="Finally, let's look at the entry costs. One adult gets in free for every fifteen children.") as tracker:
            text_scale = 0.8
            math_scale = 1.0
            t_children = Text("613 Children").scale(text_scale).to_edge(UP).shift(LEFT * 2)
            t_rule = Text("1 Free Adult / 15 Children").scale(text_scale).next_to(t_children, DOWN)
            self.play(Write(t_children))
            self.play(Write(t_rule))

        with self.voiceover(text="We need to find out how many adults must pay. We divide the number of children, six hundred and thirteen, by fifteen.") as tracker:
            eq_div = MathTex("613", "\\div", "15").scale(math_scale).shift(UP * 0.5)
            self.play(Write(eq_div))

        with self.voiceover(text="We know that two times fifteen is thirty, so four times fifteen is sixty.") as tracker:
            est_1 = MathTex("2", "\\times", "15", "=", "30").scale(text_scale).set_color(Brand.AUXILIARY)
            est_2 = MathTex("4", "\\times", "15", "=", "60").scale(text_scale).set_color(Brand.AUXILIARY)
            est_1.next_to(eq_div, DOWN, buff=1.0).shift(LEFT * 2)
            est_2.next_to(est_1, DOWN, buff=0.3)
            self.play(Write(est_1))
            self.play(Write(est_2))

        with self.voiceover(text="Therefore, forty times fifteen is six hundred.") as tracker:
            est_3 = MathTex("40", "\\times", "15", "=", "600").scale(text_scale).set_color(Brand.ACTIVE)
            est_3.next_to(est_2, DOWN, buff=0.3)
            self.play(Write(est_3))

        with self.voiceover(text="We have six hundred and thirteen children, so we have forty groups of fifteen, with thirteen children left over.") as tracker:
            sub_eq = MathTex("613", "-", "600", "=", "13").scale(math_scale)
            sub_eq.next_to(eq_div, DOWN, buff=1.0).shift(RIGHT * 2)
            sub_eq[2].set_color(Brand.ACTIVE)
            self.play(Write(sub_eq))

        with self.voiceover(text="Since we get one free adult for each full group of fifteen, forty adults get in for free.") as tracker:
            t_free = Text("40 Free Adults").scale(text_scale).set_color(Brand.ANSWER)
            t_free.next_to(sub_eq, DOWN, buff=0.5)
            self.play(Indicate(est_3[0], color=Brand.ANSWER))
            self.play(Write(t_free))

        with self.voiceover(text="The question asks how many adults must pay. There are fifty-nine adults in total.") as tracker:
            group_part1 = VGroup(eq_div, est_1, est_2, est_3, sub_eq, t_children, t_rule)
            self.play(
                FadeOut(group_part1),
                t_free.animate.to_edge(UP).shift(LEFT * 2)
            )
            t_total_adults = Text("Total Adults: 59").scale(text_scale).next_to(t_free, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(Write(t_total_adults))

        with self.voiceover(text="We subtract the forty free places from fifty-nine, which tells us that nineteen adults must pay to get in.") as tracker:
            final_calc = MathTex("59", "-", "40", "=", "19").scale(math_scale).move_to(ORIGIN)
            final_calc[2].set_color(Brand.ANSWER)
            final_calc[4].set_color(Brand.ANSWER)
            self.play(Write(final_calc))
            t_paying = Text("19 Paying Adults").scale(1.2).set_color(Brand.ANSWER).next_to(final_calc, DOWN, buff=0.5)
            self.play(Write(t_paying))
            self.play(Indicate(t_paying, color=Brand.ACTIVE))

    def slide_10_summary(self):
        with self.voiceover(text="To summarize, solving real-life problems is about more than just calculation.") as tracker:
            title = Text("Summary").scale(1.2).to_edge(UP)
            self.play(Write(title))
            
        bullets = VGroup(
            Text("• Understand the context"),
            Text("• Choose your method"),
            Text("• Interpret the answer"),
            Text("• Check your results")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8)
        
        with self.voiceover(text="It requires reading the context carefully to understand what is being asked.") as tracker:
            self.play(FadeIn(bullets[0], shift=RIGHT))

        with self.voiceover(text="You need to choose an appropriate method—whether that's long multiplication or division.") as tracker:
            self.play(FadeIn(bullets[1], shift=RIGHT))

        with self.voiceover(text="And crucially, you must interpret your answers back into the context of the problem, especially when dealing with remainders.") as tracker:
            self.play(FadeIn(bullets[2], shift=RIGHT))

        with self.voiceover(text="Always take a moment to check if your answer is reasonable.") as tracker:
            self.play(FadeIn(bullets[3], shift=RIGHT))
                
        self.wait(1)
