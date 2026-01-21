from manim import *
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from animations.styles import Brand

class ThemeParkDivision(Scene):
    def construct(self):
        # Apply Branding
        Brand.set_default_theme(self)

        # Configuration
        digits_scale = 1.2
        note_scale = 0.8
        
        # Positioning
        start_x = -2.0
        start_y = 2.0
        
        # --- Visual Elements ---
        
        # Divisor: 53
        d_53 = MathTex("5", "3").scale(digits_scale).move_to([-3, 2, 0])
        
        # Dividend digits: 672
        # Position them first to define the "bus stop" size
        div_6 = MathTex("6").scale(digits_scale).next_to(d_53, RIGHT, buff=0.5)
        div_7 = MathTex("7").scale(digits_scale).next_to(div_6, RIGHT, buff=0.3)
        div_2 = MathTex("2").scale(digits_scale).next_to(div_7, RIGHT, buff=0.3)
        
        dividend_group = VGroup(div_6, div_7, div_2)

        # Custom Bus Stop / Division Bracket
        # Points relative to the digits
        p_bottom_left = div_6.get_corner(DL) + LEFT * 0.2 + DOWN * 0.1
        p_top_left = div_6.get_corner(UL) + LEFT * 0.2 + UP * 0.1
        p_top_right = div_2.get_corner(UR) + RIGHT * 0.1 + UP * 0.1

        # Curve for the vertical part ')'
        # We use an arc or a bezier curve. A simple cubic bezier is flexible.
        # Start at top left, curve down to bottom left.
        # However, typically drawn bottom-to-top or top-to-bottom.
        # Let's draw the vertical curve then horizontal line.
        
        # Adjusted curve to be a standard ')' shape
        # Start at top, curve down and right
        bus_stop_curve = ArcBetweenPoints(
            start=p_top_left,
            end=p_bottom_left,
            angle=-TAU/4 # Curve outwards to the left
        )
        
        bus_stop_line = Line(p_top_left, p_top_right)
        
        bus_stop = VGroup(bus_stop_curve, bus_stop_line)
        
        # Setup animation
        self.play(Write(d_53), Create(bus_stop), Write(dividend_group))
        self.wait(1)
        
        # --- Step 1: 67 / 53 ---
        
        # Highlight 67
        self.play(
            Indicate(d_53, color=Brand.ACTIVE),
            Indicate(VGroup(div_6, div_7), color=Brand.ACTIVE)
        )
        
        # Answer is 1
        ans_1 = MathTex("1").scale(digits_scale).next_to(div_7, UP, buff=0.3)
        # Align 1 over the 7 (since we are dividing into 67)
        ans_1.set_x(div_7.get_x())
        
        self.play(Write(ans_1))
        self.wait(0.5)
        
        # Multiply: 1 * 53 = 53
        mult_res_53 = MathTex("5", "3").scale(digits_scale)
        mult_res_53[0].move_to([div_6.get_x(), div_6.get_y() - 1.0, 0])
        mult_res_53[1].move_to([div_7.get_x(), div_7.get_y() - 1.0, 0])
        
        minus_sign_1 = MathTex("-").scale(digits_scale).next_to(mult_res_53, LEFT, buff=0.2)
        line_sub_1 = Line(
            start=mult_res_53.get_corner(DL) + DOWN * 0.1 + LEFT * 0.2,
            end=mult_res_53.get_corner(DR) + DOWN * 0.1 + RIGHT * 0.2
        )
        
        self.play(
            Write(mult_res_53),
            Write(minus_sign_1),
            Create(line_sub_1)
        )
        self.wait(0.5)
        
        # Subtract: 67 - 53 = 14
        res_14 = MathTex("1", "4").scale(digits_scale)
        res_14[0].move_to([div_6.get_x(), mult_res_53.get_y() - 1.0, 0])
        res_14[1].move_to([div_7.get_x(), mult_res_53.get_y() - 1.0, 0])
        
        self.play(Write(res_14))
        self.wait(1)
        
        # --- Step 2: Bring down 2 ---
        
        # Arrow or just move copy
        arrow_down = Arrow(
            start=div_2.get_bottom(),
            end=[div_2.get_x(), res_14.get_y(), 0],
            buff=0.1,
            color=Brand.AUXILIARY
        )
        
        res_2_down = MathTex("2").scale(digits_scale).move_to([div_2.get_x(), res_14.get_y(), 0])
        
        self.play(Create(arrow_down))
        self.play(TransformFromCopy(div_2, res_2_down))
        self.play(FadeOut(arrow_down))
        self.wait(0.5)
        
        # Current number: 142
        curr_142 = VGroup(res_14, res_2_down)
        
        # --- Step 3: 142 / 53 ---
        
        self.play(
            Indicate(d_53, color=Brand.ACTIVE),
            Indicate(curr_142, color=Brand.ACTIVE)
        )
        
        # Side estimation
        side_calc_pos = [3, 1, 0]
        side_est_1 = MathTex("53", "\\times", "2", "=", "106").scale(note_scale).move_to(side_calc_pos).set_color(Brand.AUXILIARY)
        side_est_2 = MathTex("53", "\\times", "3", "=", "159").scale(note_scale).next_to(side_est_1, DOWN).set_color(Brand.AUXILIARY)
        cross = Cross(side_est_2).scale(0.8)
        
        self.play(Write(side_est_1))
        self.wait(0.5)
        self.play(Write(side_est_2))
        self.wait(0.5)
        self.play(Create(cross))
        self.wait(0.5)
        
        # Use 2
        ans_2 = MathTex("2").scale(digits_scale).next_to(ans_1, RIGHT, buff=0.3)
        ans_2.set_x(div_2.get_x())
        
        self.play(Write(ans_2))
        
        # Multiply: 2 * 53 = 106
        mult_res_106 = MathTex("1", "0", "6").scale(digits_scale)
        # Alignment needs care. 1 under 1, 0 under 4, 6 under 2
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
            FadeOut(side_est_1),
            FadeOut(side_est_2),
            FadeOut(cross)
        )
        
        # Subtract: 142 - 106 = 36
        res_36 = MathTex("3", "6").scale(digits_scale)
        # 3 under 0, 6 under 6. (Since 142 - 106 = 36)
        
        res_36[0].move_to([mult_res_106[1].get_x(), mult_res_106.get_y() - 1.0, 0])
        res_36[1].move_to([mult_res_106[2].get_x(), mult_res_106.get_y() - 1.0, 0])
        
        self.play(Write(res_36))
        self.wait(1)
        
        # Remainder indication
        rem_text = MathTex("r", "36").scale(digits_scale).next_to(ans_2, RIGHT, buff=0.3)
        self.play(Write(rem_text[0]), TransformFromCopy(res_36, rem_text[1]))
        
        self.wait(1)
        
        # --- Step 4: Interpretation ---
        
        t_full = Text("12 Full Coaches").scale(0.8).move_to([3, 0, 0])
        t_rem = Text("36 People Left").scale(0.8).next_to(t_full, DOWN, buff=0.5)
        t_plus1 = Text("+1 Coach").scale(0.8).next_to(t_rem, DOWN, buff=0.2).set_color(Brand.ACTIVE)
        
        line_total = Line(start=t_plus1.get_left(), end=t_plus1.get_right()).next_to(t_plus1, DOWN)
        t_total = Text("13 Coaches Total").scale(1.0).next_to(line_total, DOWN).set_color(Brand.ANSWER)
        
        self.play(Write(t_full))
        self.play(Indicate(VGroup(ans_1, ans_2), color=Brand.ACTIVE))
        self.wait(0.5)
        
        self.play(Write(t_rem))
        self.play(Indicate(rem_text, color=Brand.ACTIVE))
        self.wait(0.5)
        
        self.play(Write(t_plus1))
        self.wait(0.5)
        
        self.play(Create(line_total), Write(t_total))
        self.wait(3)
