from manim import *
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from animations.styles import Brand

class BoxMultiplication(Scene):
    def construct(self):
        # Apply Branding
        Brand.set_default_theme(self)

        # Configuration
        digits_scale = 1.0
        header_scale = 1.2
        result_scale = 1.2
        
        # Grid Parameters
        # Columns: [Header, 200, 30, 5]
        # Rows: [Header, 20, 4]
        
        col_x = [-6, -3.5, -1, 1] # Shifted LEFT
        row_y = [2, 0, -2]       # Y coords for rows
        
        h_lines_y = [1, -1]      # Y coords for horizontal separators
        v_lines_x = [-4.5]       # Shifted LEFT
        
        # --- 1. Introduction ---
        problem = MathTex("235", "\\times", "24").scale(1.5).move_to([0, 3, 0])
        self.play(Write(problem))
        self.wait(1)
        
        self.play(problem.animate.scale(0.7).to_corner(UL))
        
        # --- 2. Setup Grid Headers ---
        
        # Top Headers (200, 30, 5)
        h_200 = MathTex("200").scale(header_scale).move_to([col_x[1], row_y[0], 0])
        h_30 = MathTex("30").scale(header_scale).move_to([col_x[2], row_y[0], 0])
        h_5 = MathTex("5").scale(header_scale).move_to([col_x[3], row_y[0], 0])
        
        # Side Headers (20, 4)
        h_20 = MathTex("20").scale(header_scale).move_to([col_x[0], row_y[1], 0])
        h_4 = MathTex("4").scale(header_scale).move_to([col_x[0], row_y[2], 0])
        
        # Multiplication sign
        mult_sign = MathTex("\\times").scale(header_scale).move_to([col_x[0], row_y[0], 0])
        
        # Draw Lines
        # Horizontal lines
        line_h1 = Line(start=[-7, h_lines_y[0], 0], end=[2, h_lines_y[0], 0])
        line_h2 = Line(start=[-7, h_lines_y[1], 0], end=[2, h_lines_y[1], 0])
        
        # Vertical line
        line_v1 = Line(start=[v_lines_x[0], 3, 0], end=[v_lines_x[0], -3, 0])
        
        grid_group = VGroup(line_h1, line_h2, line_v1)
        
        # Animate decomposition
        # 235 -> 200, 30, 5
        self.play(
            ReplacementTransform(problem[0][0].copy(), h_200), # 2 -> 200 (visual approximation)
            ReplacementTransform(problem[0][1].copy(), h_30),  # 3 -> 30
            ReplacementTransform(problem[0][2].copy(), h_5)    # 5 -> 5
        )
        
        # 24 -> 20, 4
        self.play(
            ReplacementTransform(problem[2][0].copy(), h_20),  # 2 -> 20
            ReplacementTransform(problem[2][1].copy(), h_4)    # 4 -> 4
        )
        
        self.play(Create(grid_group), Write(mult_sign))
        self.wait(0.5)
        
        # --- 3. Calculations ---
        
        # Helper to create and animate cell calculation
        def animate_cell(row_header, col_header, result_val, pos_idx_x, pos_idx_y):
            pos = [col_x[pos_idx_x], row_y[pos_idx_y], 0]
            result_mob = MathTex(str(result_val)).scale(digits_scale).move_to(pos)
            
            # Highlight headers
            self.play(
                Indicate(row_header, color=Brand.ACTIVE), 
                Indicate(col_header, color=Brand.ACTIVE),
                run_time=1
            )
            
            # Show result
            self.play(Write(result_mob))
            return result_mob

        # Row 1 (x20)
        c_20_200 = animate_cell(h_20, h_200, "4000", 1, 1)
        self.wait(0.5)
        
        c_20_30 = animate_cell(h_20, h_30, "600", 2, 1)
        self.wait(0.5)
        
        c_20_5 = animate_cell(h_20, h_5, "100", 3, 1)
        self.wait(0.5)
        
        # Row 2 (x4)
        c_4_200 = animate_cell(h_4, h_200, "800", 1, 2)
        self.wait(0.5)
        
        c_4_30 = animate_cell(h_4, h_30, "120", 2, 2)
        self.wait(0.5)
        
        c_4_5 = animate_cell(h_4, h_5, "20", 3, 2)
        self.wait(1)
        
        # --- 4. Summation ---
        
        # We need to sum the rows.
        # Shift grid slightly left to make room or just overlay
        # Let's fade out the grid lines and headers slightly to focus on sums
        
        # Row 1 Sum
        # 4000 + 600 + 100 = 4700
        row1_group = VGroup(c_20_200, c_20_30, c_20_5)
        row1_sum_text = MathTex("4000", "+", "600", "+", "100", "=", "4700").scale(0.8)
        row1_sum_text.to_edge(RIGHT).shift(UP * 1)
        
        self.play(TransformFromCopy(row1_group, row1_sum_text[:5]))
        self.play(Write(row1_sum_text[5:]))
        self.play(row1_sum_text[6].animate.set_color(Brand.ACTIVE))
        
        # Row 2 Sum
        # 800 + 120 + 20 = 940
        row2_group = VGroup(c_4_200, c_4_30, c_4_5)
        row2_sum_text = MathTex("800", "+", "120", "+", "20", "=", "940").scale(0.8)
        row2_sum_text.next_to(row1_sum_text, DOWN, aligned_edge=RIGHT)
        
        self.play(TransformFromCopy(row2_group, row2_sum_text[:5]))
        self.play(Write(row2_sum_text[5:]))
        self.play(row2_sum_text[6].animate.set_color(Brand.ACTIVE))
        
        self.wait(1)
        
        # Final Sum
        # 4700 + 940 = 5640
        line_sum = Line(start=row2_sum_text.get_left(), end=row2_sum_text.get_right()).next_to(row2_sum_text, DOWN)
        final_sum_text = MathTex("5640").scale(1.2).set_color(Brand.ANSWER)
        final_sum_text.next_to(line_sum, DOWN, aligned_edge=RIGHT)
        
        # Addition symbol
        plus_sign = MathTex("+").next_to(row2_sum_text, LEFT)
        
        self.play(Create(line_sum), Write(plus_sign))
        
        # Explicitly set z_index to ensure visibility
        final_sum_text.set_z_index(10)
        
        # Simple Write animation to guarantee visibility
        self.play(Write(final_sum_text))
        
        self.wait(2)
