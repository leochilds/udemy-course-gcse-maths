from manim import *
import sys
import os

# Ensure we can import from the root animations directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from animations.styles import Brand
from manim_voiceover import VoiceoverScene
from animations.voxcpm_service import VoxCPMService

class Lesson010Introduction(VoiceoverScene):
    def construct(self):
        Brand.set_default_theme(self)
        self.set_speech_service(VoxCPMService(
            checkpoint_dir="/home/leo/code/udemy-course-gcse-maths/checkpoints/myvoice/step_0002000",
            base_model_path="/home/leo/code/udemy-course-gcse-maths/models/VoxCPM1.5"
        ))

        # --- Slide 1: Welcome ---
        self.slide_01_welcome()
        self.clear_screen()
        
        # --- Slide 2: What You Will Learn ---
        self.slide_02_learning_objectives()
        self.clear_screen()
        
        # --- Slide 3: Prerequisites ---
        self.slide_03_prerequisites()
        self.clear_screen()
        
        # --- Slide 4: Real-World Applications ---
        self.slide_04_applications()
        self.clear_screen()
        
        # --- Slide 5: Summary ---
        self.slide_05_summary()
        self.wait(2)

    def clear_screen(self):
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(0.5)

    def slide_01_welcome(self):
        with self.voiceover(text="Welcome to the first section of your GCSE Maths course: Number. This section covers the fundamental building blocks of mathematics. Whether you're managing household finances, planning a project, or just want to feel more confident with figures, the skills we will cover here are essential. In this brief introduction, we'll outline what you can expect to learn and why these skills are so valuable.") as tracker:
            title = Text("Section 1: Basic Number Skills").scale(1.2).to_edge(UP)
            underline = Line(LEFT, RIGHT).next_to(title, DOWN).scale(2)
            
            self.play(Write(title), Create(underline))
            
            subtitle1 = Text("Foundation of all mathematics").scale(0.8)
            subtitle2 = Text("Essential for daily life and work").scale(0.8)
            
            group = VGroup(subtitle1, subtitle2).arrange(DOWN, buff=0.8)
            
            self.play(FadeIn(subtitle1, shift=UP))
            self.play(FadeIn(subtitle2, shift=UP))
            # Wait for narration to complete
            self.wait(1)

    def slide_02_learning_objectives(self):
        with self.voiceover(text="In this section, we will guide you through several key topics. We'll start by ensuring you are comfortable calculating with both whole numbers—which we call integers—and decimals. We will look at how to round numbers, which is a crucial skill for estimation. You'll explore the properties of numbers, including factors, multiples, and prime numbers, as well as squares and cubes. We will also cover how to find the Lowest Common Multiple and Highest Common Factor, and finally, we'll master the rules for working with negative numbers.") as tracker:
            title = Text("What You Will Learn").scale(1.2).to_edge(UP)
            self.play(Write(title))
            
            bullets = VGroup(
                Text("• Calculations: Integers and decimals"),
                Text("• Rounding: Significant figures and estimation"),
                Text("• Properties of Numbers: Multiples, factors, primes"),
                Text("• Advanced Tools: LCM and HCF"),
                Text("• Negative Numbers: Rules and calculations")
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).scale(0.7)
            
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT))
                self.wait(0.2)
            
            self.wait(1)

    def slide_03_prerequisites(self):
        with self.voiceover(text="Before we begin, it's helpful to know where we're starting from. You should already be familiar with the four basic operations: addition, subtraction, multiplication, and division using integers. You should also have some recognition of what multiples, factors, and prime numbers are, even if you need a refresher. Familiarity with the order of operations—often remembered by the acronym BIDMAS or BODMAS—will also be beneficial, along with the ability to substitute numbers into simple algebraic expressions. If any of these sound daunting, don't worry; we will build up your understanding as we go.") as tracker:
            title = Text("Prerequisites").scale(1.2).to_edge(UP)
            self.play(Write(title))
            
            bullets = VGroup(
                Text("• Basic Arithmetic: +, -, ×, ÷"),
                Text("• Knowledge of: Multiples, factors, primes"),
                Text("• Order of Operations: BIDMAS/BODMAS"),
                Text("• Algebra: Substituting values")
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).scale(0.7)
            
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT))
                self.wait(0.2)
                
            self.wait(1)

    def slide_04_applications(self):
        with self.voiceover(text="Mathematics isn't just about exams; it's a vital tool for the workplace and daily life. Consider a cashier who needs to give the correct change, or a delivery driver planning the most efficient route to save fuel and time. Pilots use maths to calculate fuel requirements and navigation, while doctors must calculate precise medicine dosages based on a patient's age and weight. One of the most important skills you'll develop is knowing when an estimation is sufficient and when an exact answer is required.") as tracker:
            title = Text("Real-World Applications").scale(1.2).to_edge(UP)
            self.play(Write(title))
            
            # Use a grid layout for applications
            
            # Everyday Math
            t_everyday = Text("Everyday Math").scale(0.9).set_color(Brand.ACTIVE)
            sub_everyday = Text("Cashiers, Delivery Drivers").scale(0.6)
            g_everyday = VGroup(t_everyday, sub_everyday).arrange(DOWN)
            
            # Technical Math
            t_tech = Text("Technical Math").scale(0.9).set_color(Brand.ACTIVE)
            sub_tech = Text("Pilots, Doctors").scale(0.6)
            g_tech = VGroup(t_tech, sub_tech).arrange(DOWN)
            
            # Key Skill
            t_skill = Text("Key Skill").scale(0.9).set_color(Brand.ANSWER)
            sub_skill = Text("Estimation vs. Exact Calculation").scale(0.6)
            g_skill = VGroup(t_skill, sub_skill).arrange(DOWN)
            
            # Position groups
            g_everyday.move_to([-4, 1, 0])
            g_tech.move_to([4, 1, 0])
            g_skill.move_to([0, -2, 0])
            
            self.play(Write(g_everyday))
            self.wait(0.5)
            self.play(Write(g_tech))
            self.wait(0.5)
            self.play(Write(g_skill))
            self.wait(1)

    def slide_05_summary(self):
        with self.voiceover(text="To summarize, this section is designed to make you competent and confident in basic number skills. We will focus not just on the abstract rules, but on how to apply them to identify and solve problems in real-life situations. This preparation is key for the world of work and for the rest of your mathematical journey. When you are ready, move on to the next lesson, where we will start applying these skills to solve real-life problems.") as tracker:
            title = Text("Summary").scale(1.2).to_edge(UP)
            self.play(Write(title))
            
            bullets = VGroup(
                Text("• Goal: Competence in basic number skills"),
                Text("• Focus: Real-life situations and problem solving"),
                Text("• Next Step: Lesson 1.1 - Solving Real-Life Problems")
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).scale(0.7)
            
            # Highlight the next step
            bullets[-1].set_color(Brand.ACTIVE)
            
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT))
                self.wait(0.2)
                
            self.wait(1)
