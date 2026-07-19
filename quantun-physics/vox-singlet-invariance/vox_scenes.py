"""vox_scenes.py — Why Entangled Spins Disagree on Every Axis
(vox-singlet-invariance, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL-ai slots.
Color law: TEAL = the singlet state (rotationally invariant, perfect anti-correlation)
           CRIMSON = the triplet (not rotationally invariant, anti-correlation fails off-axis)
Exclusions: no ladder construction, no CHSH/Bell derivation, no triplet algebra.
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
        title = Text("Why Entangled Spins", font=DISPLAY, color=INK, font_size=46)
        sub = Text("Disagree on Every Axis", font=SERIF, color=TEAL, font_size=46, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.5 + DOWN * 0.65, RIGHT * 5.5 + DOWN * 0.65,
                    color=CRIMSON, stroke_width=2.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: singlet has total spin zero ──────────────────────────────
class B02_SingletZeroSpin(Scene):
    def construct(self):
        total = _dur("B02", 14.0)
        eyebrow = LabelChip("the singlet state", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        state = Text("(up-down  -  down-up) / sqrt(2)", font=MONO, color=TEAL, font_size=32)
        state.move_to(UP * 1.5)

        box = Rectangle(width=8.5, height=0.85, color=TEAL, stroke_width=2.5)
        box.set_fill(GROUND, opacity=0.0)
        box.move_to(UP * 1.5)

        prop1 = Text("total angular momentum: exactly zero", font=DISPLAY, color=TEAL, font_size=30)
        prop1.move_to(UP * 0.3)

        prop2 = Text("no preferred direction, no axis", font=MONO, color=TEAL, font_size=26)
        prop2.move_to(DOWN * 0.6)

        prop3 = Text("the unique two-spin state with J = 0", font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        prop3.move_to(DOWN * 1.6)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(state), Create(box), run_time=0.8)
        self.play(FadeIn(prop1), run_time=0.6)
        self.play(FadeIn(prop2), run_time=0.5)
        self.play(FadeIn(prop3), run_time=0.5)
        self.wait(total - 4.0)


# ── B03 — Cold open: the anti-correlation on different axes ───────────────────
class B03_AntiCorrelation(Scene):
    def construct(self):
        total = _dur("B03", 13.0)
        eyebrow = LabelChip("what you observe", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two axis rows
        row_z = Text("measure along z:", font=MONO, color=SLATE, font_size=26)
        row_z.move_to(UP * 1.6 + LEFT * 2.0)
        result_z = Text("particle 1: UP  ->  particle 2: DOWN", font=DISPLAY, color=TEAL, font_size=26)
        result_z.move_to(UP * 0.7)

        row_x = Text("measure along x:", font=MONO, color=SLATE, font_size=26)
        row_x.move_to(UP * 0.0 + LEFT * 2.0)
        result_x = Text("particle 1: RIGHT  ->  particle 2: LEFT", font=DISPLAY, color=TEAL, font_size=26)
        result_x.move_to(DOWN * 0.9)

        always = Text("always opposite — every axis, every time",
                      font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        always.move_to(DOWN * 2.2)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(row_z), run_time=0.5)
        self.play(FadeIn(result_z), run_time=0.6)
        self.play(FadeIn(row_x), run_time=0.5)
        self.play(FadeIn(result_x), run_time=0.6)
        self.play(FadeIn(always), run_time=0.6)
        self.wait(total - 4.0)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 12.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.to_corner(UL, buff=0.6)
        q = Text("Why does the singlet give perfect anti-correlation",
                 font=DISPLAY, color=INK, font_size=34)
        q2 = Text("on every measurement axis?", font=DISPLAY, color=TEAL, font_size=36)
        content = VGroup(q, q2)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        content.move_to(ORIGIN)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 2.5)


# ── B05 — Problem: why z-axis alone is not enough ────────────────────────────
class B05_WhyNotJustZ(Scene):
    def construct(self):
        total = _dur("B05", 14.0)
        eyebrow = LabelChip("the naive expectation", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        singlet_form = Text("singlet: up-down  -  down-up",
                            font=MONO, color=TEAL, font_size=28)
        singlet_form.move_to(UP * 1.8)

        triplet_form = Text("triplet: up-down  +  down-up",
                            font=MONO, color=CRIMSON, font_size=28)
        triplet_form.move_to(UP * 0.9)

        same_pieces = Text("built from the same pieces — just a sign difference",
                           font=MONO, color=SLATE, font_size=24)
        same_pieces.move_to(UP * 0.0)

        rule_line = Line(LEFT * 5.0 + DOWN * 0.5, RIGHT * 5.0 + DOWN * 0.5,
                         color=SLATE, stroke_width=1.5)

        diff = Text("triplet does NOT give anti-correlation on x-axis",
                    font=DISPLAY, color=CRIMSON, font_size=26)
        diff.move_to(DOWN * 1.2)

        question = Text("the minus sign makes all the difference",
                        font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        question.move_to(DOWN * 2.2)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(singlet_form), run_time=0.6)
        self.play(FadeIn(triplet_form), run_time=0.6)
        self.play(FadeIn(same_pieces), run_time=0.5)
        self.play(Create(rule_line), run_time=0.4)
        self.play(FadeIn(diff), run_time=0.6)
        self.play(FadeIn(question), run_time=0.5)
        self.wait(total - 4.5)


# ── B06 — Mechanism: x-basis rewrite gives same form ─────────────────────────
class B06_XBasisRewrite(Scene):
    def construct(self):
        total = _dur("B06", 16.0)
        eyebrow = LabelChip("the calculation", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        step1 = Text("x-eigenstates: right = (up+down)/sqrt(2),  left = (up-down)/sqrt(2)",
                     font=MONO, color=SLATE, font_size=22)
        step1.move_to(UP * 2.0)

        step2 = Text("substitute into singlet. cross terms cancel.",
                     font=MONO, color=TEAL, font_size=26)
        step2.move_to(UP * 1.0)

        result_box = Rectangle(width=7.5, height=0.85, color=TEAL, stroke_width=2.5)
        result_box.set_fill(GROUND, opacity=0.0)
        result_box.move_to(UP * 0.0)
        result_text = Text("get: (right-left  -  left-right) / sqrt(2)",
                           font=DISPLAY, color=TEAL, font_size=30)
        result_text.move_to(UP * 0.0)

        same_form = Text("same form as in the z-basis", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        same_form.move_to(DOWN * 1.0)

        note = Text("the minus sign ensures the cross terms cancel in every basis",
                    font=MONO, color=SLATE, font_size=22)
        note.move_to(DOWN * 2.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(step1), run_time=0.6)
        self.play(FadeIn(step2), run_time=0.6)
        self.play(FadeIn(result_text), Create(result_box), run_time=0.8)
        self.play(FadeIn(same_form), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(total - 4.5)


# ── B07 — Mechanism: rotational invariance ───────────────────────────────────
class B07_RotationalInvariance(Scene):
    def construct(self):
        total = _dur("B07", 16.0)
        eyebrow = LabelChip("why it works", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        key = Text("total angular momentum = 0", font=DISPLAY, color=TEAL, font_size=38)
        key.move_to(UP * 1.5)

        rule_line = Line(LEFT * 5.0 + UP * 0.9, RIGHT * 5.0 + UP * 0.9,
                         color=TEAL, stroke_width=1.5)

        meaning = Text("rotationally invariant:", font=MONO, color=TEAL, font_size=28)
        meaning.move_to(UP * 0.2)

        desc = Text("the state looks the same in every basis",
                    font=DISPLAY, color=TEAL, font_size=30)
        desc.move_to(DOWN * 0.65)

        consequence = Text("whatever axis you measure — the singlet is still the same anti-correlated form",
                           font=MONO, color=SLATE, font_size=22)
        consequence.move_to(DOWN * 1.7)

        circle = Circle(radius=1.1, color=TEAL, stroke_width=2.0)
        circle.set_fill(GROUND, opacity=0.0)
        circle.move_to(RIGHT * 5.2 + DOWN * 0.2)
        dot = Dot(RIGHT * 5.2 + DOWN * 0.2, color=TEAL, radius=0.08)
        radius_line = Line(RIGHT * 5.2 + DOWN * 0.2, RIGHT * 6.3 + DOWN * 0.2,
                           color=TEAL, stroke_width=2.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(key), run_time=0.7)
        self.play(Create(rule_line), run_time=0.4)
        self.play(FadeIn(meaning), run_time=0.5)
        self.play(FadeIn(desc), run_time=0.6)
        self.play(Create(circle), Create(dot), Create(radius_line), run_time=0.6)
        self.play(Rotate(radius_line, angle=TAU, about_point=RIGHT * 5.2 + DOWN * 0.2), run_time=1.5)
        self.play(FadeIn(consequence), run_time=0.5)
        self.wait(total - 6.0)


# ── B08 — Implication: EPR argument ─────────────────────────────────────────
class B08_EPRArgument(Scene):
    def construct(self):
        total = _dur("B08", 15.0)
        eyebrow = LabelChip("the EPR argument", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        fact1 = Text("correlated on every axis simultaneously",
                     font=DISPLAY, color=TEAL, font_size=30)
        fact1.move_to(UP * 1.5)

        rule = Line(LEFT * 5.0 + UP * 0.9, RIGHT * 5.0 + UP * 0.9,
                    color=SLATE, stroke_width=1.5)

        fact2_label = Text("hidden instruction books:", font=MONO, color=CRIMSON, font_size=26)
        fact2_label.move_to(UP * 0.2 + LEFT * 1.5)
        fact2 = Text("ruled out by Bell inequalities", font=MONO, color=CRIMSON, font_size=26)
        fact2.move_to(DOWN * 0.55)

        fact3 = Text("the correlations are genuinely quantum",
                     font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        fact3.move_to(DOWN * 1.7)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(fact1), run_time=0.7)
        self.play(Create(rule), run_time=0.4)
        self.play(FadeIn(fact2_label), run_time=0.5)
        self.play(FadeIn(fact2), run_time=0.5)
        self.play(FadeIn(fact3), run_time=0.6)
        self.wait(total - 3.8)


# ── B09 — THE EXAMPLE (illustrative): student measures three axes ─────────────
class B09_Example(Scene):
    def construct(self):
        total = _dur("B09", 20.0)
        eyebrow = LabelChip("illustrative example", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        title = Text("A student measures two singlet particles on three axes",
                     font=DISPLAY, color=INK, font_size=26)
        title.move_to(UP * 2.4)

        steps = [
            ("z-axis:", "particle 1 up -> particle 2 down", TEAL),
            ("x-axis:", "particle 1 right -> particle 2 left", TEAL),
            ("45 deg:", "particle 1 + -> particle 2 -", TEAL),
            ("rewrites singlet in each basis:", "always same anti-correlated form", TEAL),
            ("conclusion:", "the axis does not matter. J=0.", TEAL),
        ]
        step_mobs = []
        for i, (label, text, color) in enumerate(steps):
            l_mob = Text(label, font=MONO, color=SLATE, font_size=22)
            t_mob = Text(text, font=MONO, color=color, font_size=22)
            row = VGroup(l_mob, t_mob)
            row.arrange(RIGHT, buff=0.28)
            row.move_to(UP * (1.2 - i * 0.72))
            step_mobs.append(row)

        note = Text("(illustrative)", font=MONO, color=SLATE, font_size=20)
        note.move_to(DOWN * 2.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(title), run_time=0.7)
        for mob in step_mobs:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.48)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(total - 5.5)


# ── B10 — RECAP endcard ──────────────────────────────────────────────────────
class B10_Endcard(Scene):
    def construct(self):
        total = _dur("B10", 15.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.6)

        q_row = Text("Q: Why does the singlet give anti-correlation on every axis?",
                     font=SERIF, color=SLATE, font_size=24, slant=ITALIC)
        q_row.move_to(UP * 1.8)

        rule = Line(LEFT * 5.0 + UP * 1.15, RIGHT * 5.0 + UP * 1.15,
                    color=TEAL, stroke_width=1.5)

        a_row = Text("A: Total angular momentum zero means the same form on every axis.",
                     font=DISPLAY, color=INK, font_size=26)
        a_sub = Text("Rotational invariance forces perfect anti-correlation everywhere.",
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
