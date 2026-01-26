from manim import *
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from animations.styles import Brand
from manim_voiceover import VoiceoverScene
from animations.voxcpm_service import VoxCPMService

class Lesson012Complete(VoiceoverScene):
    def construct(self):
        Brand.set_default_theme(self)
        self.set_speech_service(VoxCPMService(
            checkpoint_dir="/home/leo/code/udemy-course-gcse-maths/checkpoints/myvoice/step_0002000",
            base_model_path="/home/leo/code/udemy-course-gcse-maths/models/VoxCPM1.5"
        ))
        
        # --- Slide 1: Introduction ---
        self.slide_01_introduction()
        self.clear_screen()
        
        # --- Slide 2: Decimal Notation ---
        self.slide_02_decimal_notation()
        self.clear_screen()
        
        # --- Slide 3: Decimal Places ---
        self.slide_03_decimal_places()
        self.clear_screen()
        
        # --- Slide 4: Rounding Rules ---
        self.slide_04_rounding_rules()
        self.clear_screen()
        
        # --- Slide 5: Rounding Examples ---
        self.slide_05_rounding_examples()
        self.clear_screen()
        
        # --- Slide 6: Multiplication Method ---
        self.slide_06_multiplication_method()
        self.clear_screen()
        
        # --- Slide 7: Multiplication Example ---
        self.slide_07_multiplication_example()
        self.clear_screen()
        
        # --- Slide 8: Dividing by a Decimal ---
        self.slide_08_division_concept()
        self.clear_screen()
        
        # --- Slide 9: Division Example A ---
        self.slide_09_division_example_a()
        self.clear_screen()
        
        # --- Slide 10: Division Example B ---
        self.slide_10_division_example_b()
        self.clear_screen()
        
        # --- Slide 11: Summary ---
        self.slide_11_summary()
        self.wait(2)

    def clear_screen(self):
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(0.5)

    def slide_01_introduction(self):
        with self.voiceover(text="Welcome to this lesson on multiplication and division with decimals. In this session, we will learn how to multiply two decimal numbers together.") as tracker:
            title = Text("Multiplication and Division").scale(1.2).to_edge(UP)
            subtitle = Text("with Decimals").scale(1.0).next_to(title, DOWN)
            underline = Line(LEFT, RIGHT).next_to(subtitle, DOWN).scale(2)
            
            self.play(Write(title), Write(subtitle), Create(underline))

        objectives = VGroup(
            Text("Objectives:").scale(0.8).set_color(Brand.ACTIVE),
            Text("• Multiply decimal by decimal").scale(0.7),
            Text("• Divide by a decimal").scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT).shift(LEFT * 3)

        with self.voiceover(text="We will also look at how to divide by a decimal number by transforming the calculation into one involving integers.") as tracker:
            self.play(Write(objectives))

        terms = VGroup(
            Text("Key Terms:").scale(0.8).set_color(Brand.ACTIVE),
            Text("• Decimal Place").scale(0.7),
            Text("• Decimal Point").scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 3)
        terms.match_y(objectives)

        with self.voiceover(text="We'll start by reviewing some key terms: the decimal point and decimal places.") as tracker:
            self.play(Write(terms))
        
        self.wait(1)

    def slide_02_decimal_notation(self):
        with self.voiceover(text="The number system is extended by using decimal numbers to represent fractions. The decimal point separates the whole-number part from the fractional part.") as tracker:
            title = Text("Decimal Notation").scale(1.0).to_edge(UP)
            self.play(Write(title))
            
            # Start number further up
            number = MathTex("2", "5", ".", "3", "7", "4").scale(2).shift(UP * 2)
            self.play(Write(number))

        # Create table structure
        # Columns: Tens, Units, |, Tenths, Hundredths, Thousandths
        headers = VGroup(
            Text("Tens").scale(0.6),
            Text("Units").scale(0.6),
            Text("|").scale(0.6),
            Text("Tenths").scale(0.6),
            Text("Hundredths").scale(0.6),
            Text("Thousandths").scale(0.6)
        )
        
        # Adjust header spacing
        headers[0].move_to(LEFT * 4)
        headers[1].next_to(headers[0], RIGHT, buff=1.0)
        headers[2].next_to(headers[1], RIGHT, buff=0.5) # The pipe
        headers[3].next_to(headers[2], RIGHT, buff=0.5)
        headers[4].next_to(headers[3], RIGHT, buff=1.0)
        headers[5].next_to(headers[4], RIGHT, buff=1.0)
        
        headers.move_to(DOWN * 0.5) # Center the table vertically slightly down
        
        # Values row
        values = VGroup(
            MathTex("10").scale(0.8),
            MathTex("1").scale(0.8),
            Text("|").scale(0.6),
            MathTex("1/10").scale(0.8),
            MathTex("1/100").scale(0.8),
            MathTex("1/1000").scale(0.8)
        )
        
        for i in range(6):
            values[i].next_to(headers[i], DOWN, buff=0.5)
            # Align centers
            values[i].match_x(headers[i])
            
        table_group = VGroup(headers, values)

        with self.voiceover(text="Take the number 25.374, for example. To the left of the decimal point, we have 2 Tens and 5 Units.") as tracker:
            self.play(FadeIn(table_group))
            
            # Move 2 (Tens) and 5 (Units)
            # number indices: 0->2, 1->5, 2->., 3->3, 4->7, 5->4
            
            target_2 = number[0].copy()
            target_5 = number[1].copy()
            
            # Define targets in table
            pos_2 = values[0].get_center() + DOWN * 1.0
            pos_5 = values[1].get_center() + DOWN * 1.0
            
            self.play(
                number[0].animate.move_to(pos_2),
                number[1].animate.move_to(pos_5),
                Indicate(headers[0], color=Brand.ACTIVE),
                Indicate(headers[1], color=Brand.ACTIVE)
            )

        with self.voiceover(text="To the right, we have 3 Tenths, 7 Hundredths, and 4 Thousandths.") as tracker:
            # Move decimal point, 3, 7, 4
            
            pos_dot = values[2].get_center() + DOWN * 1.0
            pos_3 = values[3].get_center() + DOWN * 1.0
            pos_7 = values[4].get_center() + DOWN * 1.0
            pos_4 = values[5].get_center() + DOWN * 1.0
            
            self.play(
                number[2].animate.move_to(pos_dot),
                number[3].animate.move_to(pos_3),
                number[4].animate.move_to(pos_7),
                number[5].animate.move_to(pos_4),
                Indicate(headers[3], color=Brand.ACTIVE),
                Indicate(headers[4], color=Brand.ACTIVE),
                Indicate(headers[5], color=Brand.ACTIVE)
            )

        with self.voiceover(text="We use this every day with money. £36.67 is simply 3 tens, 6 units, 6 tenths—which are 10 pence coins—and 7 hundredths—which are pennies.") as tracker:
            # Shift everything up a bit to make room or clear
            everything = VGroup(title, table_group, number)
            self.play(everything.animate.scale(0.7).to_edge(UP))
            
            money = MathTex("\\pounds 36.67").scale(1.5).move_to(DOWN * 2)
            breakdown = MathTex("30 + 6 + 0.6 + 0.07").scale(1.0).next_to(money, DOWN)
            self.play(Write(money))
            self.play(Write(breakdown))
            self.wait(1)

    def slide_03_decimal_places(self):
        with self.voiceover(text="When we talk about 'decimal places,' we are referring to the positions of the digits to the right of the decimal point.") as tracker:
            title = Text("Decimal Places (dp)").scale(1.0).to_edge(UP)
            self.play(Write(title))

        # Example 1
        ex1_num = MathTex("79", ".", "4").scale(1.5).shift(UP * 1 + LEFT * 3)
        ex1_label = Text("1 decimal place").scale(0.6).next_to(ex1_num, RIGHT, buff=1)
        
        with self.voiceover(text="For instance, 79.4 has one digit after the point, so it has one decimal place.") as tracker:
            self.play(Write(ex1_num))
            self.play(Indicate(ex1_num[2], color=Brand.ACTIVE))
            self.play(Write(ex1_label))

        # Example 2
        ex2_num = MathTex("6", ".", "8", "3").scale(1.5).next_to(ex1_num, DOWN, buff=1.5, aligned_edge=LEFT)
        ex2_label = Text("2 decimal places").scale(0.6).next_to(ex2_num, RIGHT, buff=1)
        
        with self.voiceover(text="6.83 has two digits after the point, so it has two decimal places.") as tracker:
            self.play(Write(ex2_num))
            self.play(Indicate(ex2_num[2:], color=Brand.ACTIVE))
            self.play(Write(ex2_label))

        # Example 3
        ex3_num = MathTex("0", ".", "5", "2", "6").scale(1.5).next_to(ex2_num, DOWN, buff=1.5, aligned_edge=LEFT)
        ex3_label = Text("3 decimal places").scale(0.6).next_to(ex3_num, RIGHT, buff=1)
        
        with self.voiceover(text="And 0.526 has three decimal places. Knowing this is crucial for rounding and for checking our answers in multiplication.") as tracker:
            self.play(Write(ex3_num))
            self.play(Indicate(ex3_num[2:], color=Brand.ACTIVE))
            self.play(Write(ex3_label))

    def slide_04_rounding_rules(self):
        with self.voiceover(text="Often, you will need to round a decimal number to a specific number of decimal places.") as tracker:
            title = Text("Rounding Decimals").scale(1.0).to_edge(UP)
            self.play(Write(title))

        steps = VGroup(
            Text("1. Count to required decimal place"),
            Text("2. Look at the NEXT digit"),
            Text("3. If < 5: Remove unwanted digits"),
            Text("4. If ≥ 5: Add 1 to previous digit, then remove")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8)

        with self.voiceover(text="Here is the method: Start at the decimal point and count along to the required number of places. Then, look at the very next digit—the first one you are going to remove.") as tracker:
            self.play(Write(steps[0]))
            self.play(Write(steps[1]))

        with self.voiceover(text="If that digit is less than 5, you simply remove it and all following digits.") as tracker:
            self.play(Write(steps[2]))

        with self.voiceover(text="If that digit is 5 or more, you must round up. Add 1 to the digit in the previous decimal place, and then remove the unwanted digits.") as tracker:
            self.play(Write(steps[3]))

    def slide_05_rounding_examples(self):
        title = Text("Rounding Examples").scale(1.0).to_edge(UP)
        self.add(title)

        # Example A: 5.852 (2 dp)
        with self.voiceover(text="Let's practice this with some examples. First, round 5.852 to 2 decimal places.") as tracker:
            e1_text = MathTex("5.852").scale(1.5).shift(UP * 2 + LEFT * 2)
            e1_req = Text("(to 2 dp)").scale(0.6).next_to(e1_text, RIGHT)
            self.play(Write(e1_text), Write(e1_req))

        with self.voiceover(text="The second decimal digit is 5. The next digit is 2, which is less than 5. So, we leave it as 5.85.") as tracker:
            # Highlight 2nd dp (5) and decider (2)
            # 5 . 8 5 2
            # 0 1 2 3 4 (indices roughly)
            self.play(Indicate(e1_text[0][3], color=Brand.ACTIVE)) # The '5'
            self.play(Circumscribe(e1_text[0][4], color=Brand.AUXILIARY)) # The '2'
            
            e1_ans = MathTex("\\rightarrow 5.85").scale(1.5).next_to(e1_req, RIGHT).set_color(Brand.ANSWER)
            self.play(Write(e1_ans))

        # Example B: 7.156 (2 dp)
        with self.voiceover(text="Second, round 7.156 to 2 decimal places.") as tracker:
            e2_text = MathTex("7.156").scale(1.5).next_to(e1_text, DOWN, buff=1, aligned_edge=LEFT)
            e2_req = Text("(to 2 dp)").scale(0.6).next_to(e2_text, RIGHT)
            self.play(Write(e2_text), Write(e2_req))

        with self.voiceover(text="The second digit is 5, but the next digit is 6. Since 6 is 5 or more, we round up the 5 to a 6. The answer is 7.16.") as tracker:
            self.play(Indicate(e2_text[0][3], color=Brand.ACTIVE)) # The '5'
            self.play(Circumscribe(e2_text[0][4], color=Brand.AUXILIARY)) # The '6'
            e2_ans = MathTex("\\rightarrow 7.16").scale(1.5).next_to(e2_req, RIGHT).set_color(Brand.ANSWER)
            self.play(Write(e2_ans))

        # Example C: 0.274 (1 dp)
        with self.voiceover(text="Third, round 0.274 to 1 decimal place.") as tracker:
            e3_text = MathTex("0.274").scale(1.5).next_to(e2_text, DOWN, buff=1, aligned_edge=LEFT)
            e3_req = Text("(to 1 dp)").scale(0.6).next_to(e3_text, RIGHT)
            self.play(Write(e3_text), Write(e3_req))

        with self.voiceover(text="The first digit is 2. The next is 7, which is high enough to round up. So, 0.2 becomes 0.3.") as tracker:
            self.play(Indicate(e3_text[0][2], color=Brand.ACTIVE)) # The '2'
            self.play(Circumscribe(e3_text[0][3], color=Brand.AUXILIARY)) # The '7'
            e3_ans = MathTex("\\rightarrow 0.3").scale(1.5).next_to(e3_req, RIGHT).set_color(Brand.ANSWER)
            self.play(Write(e3_ans))

        # Example D: 15.3518 (1 dp)
        with self.voiceover(text="Finally, 15.3518 to 1 decimal place. The next digit is 5, so we round up the 3 to a 4. The result is 15.4.") as tracker:
            e4_text = MathTex("15.3518").scale(1.5).next_to(e3_text, DOWN, buff=1, aligned_edge=LEFT)
            e4_req = Text("(to 1 dp)").scale(0.6).next_to(e4_text, RIGHT)
            self.play(Write(e4_text), Write(e4_req))
            
            self.play(Indicate(e4_text[0][3], color=Brand.ACTIVE)) # The '3'
            self.play(Circumscribe(e4_text[0][4], color=Brand.AUXILIARY)) # The '5'
            
            e4_ans = MathTex("\\rightarrow 15.4").scale(1.5).next_to(e4_req, RIGHT).set_color(Brand.ANSWER)
            self.play(Write(e4_ans))
            self.wait(1)

    def slide_06_multiplication_method(self):
        with self.voiceover(text="Now, let's look at multiplying two decimal numbers. The easiest way to do this is to temporarily forget about the decimal points.") as tracker:
            title = Text("Multiplying Decimals").scale(1.0).to_edge(UP)
            self.play(Write(title))

        steps = VGroup(
            Text("1. Multiply by powers of 10 to make integers"),
            Text("2. Multiply the integers"),
            Text("3. Multiply the powers of 10 used"),
            Text("4. Divide result by total power of 10")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8)

        with self.voiceover(text="First, multiply each decimal by a power of 10—like 10, 100, or 1000—to turn them into whole numbers.") as tracker:
            self.play(Write(steps[0]))

        with self.voiceover(text="Second, multiply those whole numbers together.") as tracker:
            self.play(Write(steps[1]))

        with self.voiceover(text="Third, multiply the powers of 10 you used in step one.") as tracker:
            self.play(Write(steps[2]))

        with self.voiceover(text="Finally, divide your result by that combined power of 10 to put the decimal point back in the correct place.") as tracker:
            self.play(Write(steps[3]))

    def slide_07_multiplication_example(self):
        with self.voiceover(text="Let's calculate 3.42 multiplied by 2.7.") as tracker:
            title = Text("Example: 3.42 × 2.7").scale(1.0).to_edge(UP)
            self.play(Write(title))
            
            problem = MathTex("3.42", "\\times", "2.7").scale(1.5).shift(UP * 2)
            self.play(Write(problem))

        with self.voiceover(text="First, we make them whole numbers. 3.42 has two decimal places, so we multiply by 100 to get 342.") as tracker:
            arrow1 = Arrow(start=problem[0].get_bottom(), end=problem[0].get_bottom() + DOWN * 1.5, color=Brand.AUXILIARY)
            t1 = MathTex("\\times 100").scale(0.8).next_to(arrow1, RIGHT)
            n1 = MathTex("342").scale(1.5).next_to(arrow1, DOWN)
            self.play(Create(arrow1), Write(t1))
            self.play(Write(n1))

        with self.voiceover(text="2.7 has one decimal place, so we multiply by 10 to get 27.") as tracker:
            arrow2 = Arrow(start=problem[2].get_bottom(), end=problem[2].get_bottom() + DOWN * 1.5, color=Brand.AUXILIARY)
            t2 = MathTex("\\times 10").scale(0.8).next_to(arrow2, RIGHT)
            n2 = MathTex("27").scale(1.5).next_to(arrow2, DOWN)
            self.play(Create(arrow2), Write(t2))
            self.play(Write(n2))

        with self.voiceover(text="Now we calculate 342 times 27. Using long multiplication, we get 9,234.") as tracker:
            mult_sym = MathTex("\\times").scale(1.5).move_to((n1.get_center() + n2.get_center()) / 2)
            eq_line = Line(start=n1.get_left() + DOWN * 0.5, end=n2.get_right() + DOWN * 0.5)
            
            # Show the result directly to save time, as long mult was covered in prev lesson
            res_int = MathTex("9234").scale(1.5).next_to(eq_line, DOWN)
            
            self.play(Write(mult_sym))
            self.play(Create(eq_line))
            self.play(Write(res_int))

        with self.voiceover(text="We multiplied by 100 and then by 10. 100 times 10 is 1,000.") as tracker:
            total_pow = MathTex("100 \\times 10 = 1000").scale(1.0).to_edge(RIGHT).shift(UP * 2)
            self.play(Write(total_pow))

        with self.voiceover(text="So, we must divide our answer, 9,234, by 1,000. This moves the decimal point three places to the left.") as tracker:
            final_step = MathTex("9234", "\\div", "1000", "=", "9.234").scale(1.5).move_to(DOWN * 2)
            final_step[4].set_color(Brand.ANSWER)
            
            arrow_back = Arrow(start=res_int.get_bottom(), end=final_step.get_top())
            t_back = MathTex("\\div 1000").scale(0.8).next_to(arrow_back, RIGHT)
            
            self.play(Create(arrow_back), Write(t_back))
            self.play(Write(final_step))

        with self.voiceover(text="The final answer is 9.234.") as tracker:
            self.play(Circumscribe(final_step[4], color=Brand.ANSWER))
            self.wait(1)

    def slide_08_division_concept(self):
        with self.voiceover(text="Dividing by a decimal number can be tricky. The best strategy is to change the problem so you are dividing by a whole number instead.") as tracker:
            title = Text("Dividing by a Decimal").scale(1.0).to_edge(UP)
            self.play(Write(title))
            
            # Visual representation: Fraction
            frac = MathTex("\\frac{A}{B}").scale(2)
            self.play(Write(frac))

        with self.voiceover(text="Look at the divisor—the number you are dividing by. Decide what you need to multiply it by to make it a whole number.") as tracker:
            arrow = Arrow(start=frac.get_bottom() + DOWN * 0.5, end=frac[0][2].get_bottom(), color=Brand.ACTIVE)
            label = Text("Divisor must be integer").scale(0.6).next_to(arrow, DOWN).set_color(Brand.ACTIVE)
            self.play(Create(arrow), Write(label))

        with self.voiceover(text="Then, multiply BOTH parts of the division by that same amount. This keeps the answer the same, but makes the calculation much easier.") as tracker:
            trans = MathTex("= \\frac{A \\times 10}{B \\times 10}").scale(2).next_to(frac, RIGHT)
            self.play(Write(trans))
            self.wait(1)

    def slide_09_division_example_a(self):
        with self.voiceover(text="Let's try 42 divided by 0.2.") as tracker:
            title = Text("Example: 42 ÷ 0.2").scale(1.0).to_edge(UP)
            self.play(Write(title))
            
            prob = MathTex("42", "\\div", "0.2").scale(1.5).shift(UP * 1)
            self.play(Write(prob))

        with self.voiceover(text="We are dividing by 0.2. To make 0.2 a whole number, we need to multiply it by 10.") as tracker:
            self.play(Indicate(prob[2], color=Brand.ACTIVE))
            
        with self.voiceover(text="So, we must also multiply 42 by 10.") as tracker:
            # Transformation animation
            arrow = Arrow(DOWN, UP).scale(0.5).rotate(-PI/2)
            
            p1 = MathTex("42", "\\times", "10", "=", "420").scale(1.0).move_to([-3, -1, 0])
            p2 = MathTex("0.2", "\\times", "10", "=", "2").scale(1.0).move_to([3, -1, 0])
            
            self.play(Write(p1))
            self.play(Write(p2))

        with self.voiceover(text="The calculation changes from 42 divided by 0.2... to 420 divided by 2.") as tracker:
            new_prob = MathTex("420", "\\div", "2").scale(1.5).next_to(prob, DOWN, buff=3)
            self.play(Write(new_prob))

        with self.voiceover(text="420 divided by 2 is easy: it is 210.") as tracker:
            eq = MathTex("=").scale(1.5).next_to(new_prob, RIGHT)
            ans = MathTex("210").scale(1.5).next_to(eq, RIGHT).set_color(Brand.ANSWER)
            self.play(Write(eq), Write(ans))

        with self.voiceover(text="So, 42 divided by 0.2 is 210.") as tracker:
            self.play(Circumscribe(ans, color=Brand.ANSWER))
            self.wait(1)

    def slide_10_division_example_b(self):
        with self.voiceover(text="Now a harder one: 19.8 divided by 0.55.") as tracker:
            title = Text("Example: 19.8 ÷ 0.55").scale(1.0).to_edge(UP)
            self.play(Write(title))
            
            prob = MathTex("19.8", "\\div", "0.55").scale(1.5).shift(UP * 2)
            self.play(Write(prob))

        with self.voiceover(text="The divisor is 0.55. To make this a whole number, we need to multiply by 100.") as tracker:
            self.play(Indicate(prob[2], color=Brand.ACTIVE))

        with self.voiceover(text="So we multiply 19.8 by 100 as well, which gives us 1,980.") as tracker:
            # Transformation
            t_steps = VGroup(
                MathTex("19.8 \\times 100 = 1980"),
                MathTex("0.55 \\times 100 = 55")
            ).arrange(DOWN, aligned_edge=LEFT).move_to(LEFT * 3)
            self.play(Write(t_steps))
            
            new_prob = MathTex("1980 \\div 55").scale(1.5).next_to(prob, DOWN, buff=2)
            self.play(Write(new_prob))

        with self.voiceover(text="Our new problem is 1,980 divided by 55. We can use long division or repeated subtraction here.") as tracker:
            # Simplified subtraction display
            # 1980
            # -1100 (20 x 55)
            # = 880
            # - 440 (8 x 55)
            # = 440
            # - 440 (8 x 55)
            # = 0
            
            start_num = MathTex("1980").scale(1.0).shift(RIGHT * 2 + UP * 0.5)
            self.play(Write(start_num))

        with self.voiceover(text="20 times 55 is 1,100. Subtracting that from 1,980 leaves 880.") as tracker:
            sub1 = MathTex("- 1100").scale(1.0).next_to(start_num, DOWN, aligned_edge=RIGHT)
            note1 = Text("(20 x 55)").scale(0.5).next_to(sub1, LEFT, buff=0.5).set_color(Brand.AUXILIARY)
            line1 = Line(sub1.get_left(), sub1.get_right()).next_to(sub1, DOWN)
            rem1 = MathTex("880").scale(1.0).next_to(line1, DOWN, aligned_edge=RIGHT)
            
            self.play(Write(sub1), Write(note1))
            self.play(Create(line1))
            self.play(Write(rem1))

        with self.voiceover(text="8 times 55 is 440. We can subtract that twice to clear the remaining 880.") as tracker:
            sub2 = MathTex("- 880").scale(1.0).next_to(rem1, DOWN, aligned_edge=RIGHT)
            note2 = Text("(16 x 55)").scale(0.5).next_to(sub2, LEFT, buff=0.5).set_color(Brand.AUXILIARY)
            line2 = Line(sub2.get_left(), sub2.get_right()).next_to(sub2, DOWN)
            rem2 = MathTex("0").scale(1.0).next_to(line2, DOWN, aligned_edge=RIGHT)
            
            self.play(Write(sub2), Write(note2))
            self.play(Create(line2))
            self.play(Write(rem2))

        with self.voiceover(text="20 plus 8 plus 8 equals 36. So, 19.8 divided by 0.55 is 36.") as tracker:
            final_ans = MathTex("= 36").scale(1.5).next_to(new_prob, RIGHT).set_color(Brand.ANSWER)
            self.play(Write(final_ans))
            self.wait(1)

    def slide_11_summary(self):
        with self.voiceover(text="To summarize, we've seen that decimals are just another way to represent fractions.") as tracker:
            title = Text("Summary").scale(1.2).to_edge(UP)
            self.play(Write(title))
            
        bullets = VGroup(
            Text("• Decimals represent fractions"),
            Text("• Rounding: Check the NEXT digit"),
            Text("• Multiplication: Treat as integers first"),
            Text("• Division: Make divisor a whole number")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8)

        with self.voiceover(text="When rounding, always look at the digit immediately to the right of your target place.") as tracker:
            self.play(FadeIn(bullets[0], shift=RIGHT))
            self.play(FadeIn(bullets[1], shift=RIGHT))

        with self.voiceover(text="For multiplication, treat them as whole numbers first, then put the decimal point back at the end.") as tracker:
            self.play(FadeIn(bullets[2], shift=RIGHT))

        with self.voiceover(text="And for division, always adjust the problem so you are dividing by a whole number.") as tracker:
            self.play(FadeIn(bullets[3], shift=RIGHT))

        with self.voiceover(text="With these methods, you can handle any decimal calculation with confidence.") as tracker:
            self.wait(2)
