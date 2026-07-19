"""vox_scenes.py — Why the Electron Can't Be a Tiny Spinning Ball
(vox-spin-speed-limit, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL-ai slots.
Color law: TEAL = intrinsic spin (actual quantum property, no spinning object)
           CRIMSON = the classical spinning ball picture (fails at 170c)
Exclusions: no moment-of-inertia derivation on screen, no Dirac-equation math,
            no g-factor discussion.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

def _dur(bid, fallback=9.0):
    return DUR.get(bid, fallback)


# ── B01 — Title card ─────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        total = _dur("B01", 10.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        title = Text("Why the Electron Can't Be", font=DISPLAY, color=INK, font_size=44)
        sub = Text("a Tiny Spinning Ball", font=SERIF, color=CRIMSON, font_size=44, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.5 + DOWN * 0.6, RIGHT * 5.5 + DOWN * 0.6,
                    color=TEAL, stroke_width=2.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: spin is real ────────────────────────────────────────────
class B02_SpinIsReal(Scene):
    def construct(self):
        total = _dur("B02", 13.0)
        eyebrow = LabelChip("spin is real angular momentum", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        fact1 = Text("deflects atoms in a magnetic field", font=MONO, color=TEAL, font_size=26)
        fact1.move_to(UP * 1.6)
        fact2 = Text("produces two spots in Stern-Gerlach", font=MONO, color=TEAL, font_size=26)
        fact2.move_to(UP * 0.7)
        fact3 = Text("is conserved in reactions", font=MONO, color=TEAL, font_size=26)
        fact3.move_to(DOWN * 0.2)

        value = Text("value: hbar / 2  (exactly)", font=DISPLAY, color=TEAL, font_size=36)
        value.move_to(DOWN * 1.4)

        note = Text("this is measured. it is real.", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        note.move_to(DOWN * 2.5)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(fact1), run_time=0.5)
        self.play(FadeIn(fact2), run_time=0.5)
        self.play(FadeIn(fact3), run_time=0.5)
        self.play(FadeIn(value), run_time=0.7)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(total - 4.0)


# ── B03 — Cold open: the spinning ball picture ───────────────────────────────
class B03_SpinningBallPicture(Scene):
    def construct(self):
        total = _dur("B03", 12.0)
        eyebrow = LabelChip("the natural picture", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Draw a spinning sphere
        circle = Circle(radius=1.4, color=CRIMSON, stroke_width=3.0)
        circle.set_fill(GROUND, opacity=0.0)
        circle.move_to(LEFT * 3.0)

        # Equator line
        equator = Ellipse(width=2.8, height=0.7, color=CRIMSON, stroke_width=2.0)
        equator.set_fill(GROUND, opacity=0.0)
        equator.move_to(LEFT * 3.0)

        # Spin axis arrow
        axis = Arrow(LEFT * 3.0 + DOWN * 1.8, LEFT * 3.0 + UP * 1.8,
                     color=CRIMSON, stroke_width=2.5,
                     max_tip_length_to_length_ratio=0.12)

        ball_label = Text("electron?", font=MONO, color=CRIMSON, font_size=24)
        ball_label.move_to(LEFT * 3.0 + DOWN * 2.5)

        q_line1 = Text("if rotation gives hbar/2,", font=DISPLAY, color=INK, font_size=28)
        q_line2 = Text("how fast is the surface?", font=DISPLAY, color=INK, font_size=28)
        question = VGroup(q_line1, q_line2)
        question.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        question.move_to(RIGHT * 2.2 + UP * 0.9)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(Create(circle), Create(equator), run_time=0.7)
        self.play(Create(axis), run_time=0.5)
        self.play(circle.animate.rotate(0.4), equator.animate.rotate(0.4), run_time=0.8)
        self.play(FadeIn(ball_label), run_time=0.4)
        self.play(FadeIn(question), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 12.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.to_corner(UL, buff=0.6)
        q = Text("If spin is physical rotation,", font=DISPLAY, color=INK, font_size=38)
        q2 = Text("how fast must the electron's surface move?", font=DISPLAY, color=CRIMSON, font_size=36)
        content = VGroup(q, q2)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        content.move_to(ORIGIN)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 2.5)


# ── B05 — Problem: use the largest plausible radius ──────────────────────────
class B05_ClassicalRadius(Scene):
    def construct(self):
        total = _dur("B05", 14.0)
        eyebrow = LabelChip("generous assumption", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        setup = Text("to be generous, use the classical electron radius:",
                     font=MONO, color=SLATE, font_size=26)
        setup.move_to(UP * 1.8)

        radius = Text("r = 2.82 x 10^-15 m", font=DISPLAY, color=CRIMSON, font_size=38)
        radius.move_to(UP * 0.8)

        caveat = Text("experiments say electron is smaller than 10^-18 m",
                      font=MONO, color=SLATE, font_size=24)
        caveat.move_to(DOWN * 0.2)

        worse = Text("a smaller radius makes the answer worse, not better",
                     font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        worse.move_to(DOWN * 1.3)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(setup), run_time=0.6)
        self.play(FadeIn(radius), run_time=0.7)
        self.play(FadeIn(caveat), run_time=0.5)
        self.play(FadeIn(worse), run_time=0.6)
        self.wait(total - 3.8)


# ── B06 — Mechanism: the calculation gives 170c ──────────────────────────────
class B06_Calculation170c(Scene):
    def construct(self):
        total = _dur("B06", 16.0)
        eyebrow = LabelChip("the calculation", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        start = Text("L = (2/5) m r^2 * omega = hbar/2",
                     font=MONO, color=SLATE, font_size=28)
        start.move_to(UP * 1.8)

        result_label = Text("equatorial speed:", font=MONO, color=SLATE, font_size=28)
        result_label.move_to(UP * 0.7)

        speed = Text("~170 x c", font=DISPLAY, color=CRIMSON, font_size=52)
        speed.move_to(DOWN * 0.3)

        box = Rectangle(width=5.5, height=1.1, color=CRIMSON, stroke_width=3.0)
        box.set_fill(GROUND, opacity=0.0)
        box.move_to(DOWN * 0.3)

        note = Text("two full orders of magnitude past the speed of light",
                    font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        note.move_to(DOWN * 1.7)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(start), run_time=0.6)
        self.play(FadeIn(result_label), run_time=0.5)
        self.play(FadeIn(speed), Create(box), run_time=0.8)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(total - 4.0)


# ── B07 — Mechanism: smaller radius makes it worse ───────────────────────────
class B07_SmallerWorse(Scene):
    def construct(self):
        total = _dur("B07", 14.0)
        eyebrow = LabelChip("the radius problem", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_a = Text("r = 2.82 x 10^-15 m", font=MONO, color=CRIMSON, font_size=26)
        col_a.move_to(LEFT * 2.5 + UP * 1.5)
        speed_a = Text("~170c", font=DISPLAY, color=CRIMSON, font_size=34)
        speed_a.move_to(LEFT * 4.5 + UP * 0.4)

        arrow_down = Arrow(LEFT * 2.5 + UP * 1.2, LEFT * 2.5 + DOWN * 0.1,
                          color=CRIMSON, stroke_width=2.0,
                          max_tip_length_to_length_ratio=0.18)

        col_b = Text("r < 10^-18 m  (measured)", font=MONO, color=CRIMSON, font_size=26)
        col_b.move_to(RIGHT * 2.0 + UP * 1.5)
        speed_b = Text(">> 170c", font=DISPLAY, color=CRIMSON, font_size=34)
        speed_b.move_to(RIGHT * 2.0 + UP * 0.4)

        conclusion = Text("every bound on electron size makes this worse",
                          font=MONO, color=SLATE, font_size=24)
        conclusion.move_to(DOWN * 1.5)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(col_a), run_time=0.5)
        self.play(Create(arrow_down), run_time=0.4)
        self.play(FadeIn(speed_a), run_time=0.5)
        self.play(FadeIn(col_b), FadeIn(speed_b), run_time=0.7)
        self.play(FadeIn(conclusion), run_time=0.6)
        self.wait(total - 4.0)


# ── B08 — Implication: spin is intrinsic ─────────────────────────────────────
class B08_SpinIntrinsic(Scene):
    def construct(self):
        total = _dur("B08", 15.0)
        eyebrow = LabelChip("what spin actually is", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        line1 = Text("spin is INTRINSIC", font=DISPLAY, color=TEAL, font_size=40)
        line1.move_to(UP * 1.5)

        line2 = Text("a built-in property, not rotation through space",
                     font=MONO, color=TEAL, font_size=26)
        line2.move_to(UP * 0.5)

        rule_line = Line(LEFT * 5.0 + UP * 0.0, RIGHT * 5.0 + UP * 0.0,
                         color=TEAL, stroke_width=1.5)

        line3 = Text("algebra of angular momentum: yes", font=MONO, color=TEAL, font_size=26)
        line3.move_to(DOWN * 0.7)

        line4 = Text("physical motion underneath: none", font=MONO, color=TEAL, font_size=26)
        line4.move_to(DOWN * 1.55)

        line5 = Text("Dirac (1928): spin-1/2 falls out of relativistic quantum mechanics",
                     font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        line5.move_to(DOWN * 2.5)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.7)
        self.play(FadeIn(line2), run_time=0.6)
        self.play(Create(rule_line), run_time=0.4)
        self.play(FadeIn(line3), run_time=0.5)
        self.play(FadeIn(line4), run_time=0.5)
        self.play(FadeIn(line5), run_time=0.5)
        self.wait(total - 4.2)


# ── B09 — THE EXAMPLE (illustrative): student calculation ────────────────────
class B09_Example(Scene):
    def construct(self):
        total = _dur("B09", 18.0)
        eyebrow = LabelChip("illustrative example", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        title = Text("A student explains spin to a skeptical friend",
                     font=DISPLAY, color=INK, font_size=28)
        title.move_to(UP * 2.4)

        steps = [
            ("1.", "starts with spinning ball picture", CRIMSON),
            ("2.", "friend asks: how fast is the surface?", INK),
            ("3.", "writes L = (2/5) m r^2 omega = hbar/2", CRIMSON),
            ("4.", "gets: v = 170c", CRIMSON),
            ("5.", "crosses out ball. writes: internal quantum number", TEAL),
        ]
        step_mobs = []
        for i, (num, text, color) in enumerate(steps):
            n_mob = Text(num, font=MONO, color=SLATE, font_size=23)
            t_mob = Text(text, font=MONO, color=color, font_size=23)
            row = VGroup(n_mob, t_mob)
            row.arrange(RIGHT, buff=0.28)
            row.move_to(UP * (1.0 - i * 0.72))
            step_mobs.append(row)

        note = Text("(illustrative)", font=MONO, color=SLATE, font_size=20)
        note.move_to(DOWN * 2.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(title), run_time=0.7)
        for mob in step_mobs:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(total - 5.5)


# ── B10 — RECAP endcard ──────────────────────────────────────────────────────
class B10_Endcard(Scene):
    def construct(self):
        total = _dur("B10", 14.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.6)

        q_row = Text("Q: If spin is physical rotation, how fast must the electron's surface move?",
                     font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        q_row.move_to(UP * 1.8)

        rule = Line(LEFT * 5.5 + UP * 1.15, RIGHT * 5.5 + UP * 1.15,
                    color=TEAL, stroke_width=1.5)

        a_row = Text("A: About 170 times the speed of light.", font=DISPLAY, color=INK, font_size=28)
        a_sub = Text("Spin is angular momentum with no spinning object underneath.",
                     font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        a_group = VGroup(a_row, a_sub)
        a_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        a_group.move_to(DOWN * 0.3)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q_row), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(a_row, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(a_sub, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)
