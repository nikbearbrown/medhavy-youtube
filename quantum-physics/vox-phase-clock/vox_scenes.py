"""vox_scenes.py — Why a 'Stationary' State Is Secretly Spinning
(vox-phase-clock, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = single energy eigenstate (clock hand turning, shadow frozen)
           CRIMSON = two-eigenstate superposition (beat between phases, moving shadow)
Exclusions: no time-evolution-operator derivation, no spectral-theorem formalism,
            no Bohr-frequency algebra.
"""
import sys, json, pathlib, numpy as np
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
        title = Text("Why a 'Stationary' State", font=DISPLAY, color=INK, font_size=44)
        sub = Text("Is Secretly Spinning", font=SERIF, color=TEAL, font_size=44, slant=ITALIC)
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


# ── B02 — Cold open: single eigenstate, nothing changes ──────────────────────
class B02_SingleEigenstate(Scene):
    def construct(self):
        total = _dur("B02", 15.0)
        eyebrow = LabelChip("energy eigenstate", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left column: clock in complex plane
        circle = Circle(radius=1.4, color=TEAL, stroke_width=1.5)
        circle.move_to(LEFT * 3.5 + UP * 0.3)
        hand = Arrow(LEFT * 3.5 + UP * 0.3, LEFT * 3.5 + UP * 0.3 + RIGHT * 1.4,
                     buff=0.0, color=TEAL, stroke_width=3.0,
                     max_tip_length_to_length_ratio=0.25)
        clock_lbl = Text("phase rotating", font=MONO, color=TEAL, font_size=22)
        clock_lbl.move_to(LEFT * 3.5 + DOWN * 1.5)

        # Right column: probability flat line
        flat_line = Line(RIGHT * 1.5 + DOWN * 0.3, RIGHT * 5.0 + DOWN * 0.3,
                         color=TEAL, stroke_width=2.5)
        flat_lbl = Text("|psi|^2  = constant", font=DISPLAY, color=TEAL, font_size=26)
        flat_lbl.move_to(RIGHT * 3.2 + UP * 0.5)
        flat_note = Text("nothing measurable\nchanges", font=MONO, color=TEAL, font_size=22)
        flat_note.move_to(RIGHT * 3.2 + DOWN * 1.3)

        vs = Text("but", font=DISPLAY, color=SLATE, font_size=30)
        vs.move_to(ORIGIN + UP * 0.3)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(circle), FadeIn(hand), run_time=0.8)
        self.play(FadeIn(clock_lbl), run_time=0.5)
        self.play(FadeIn(vs), run_time=0.4)
        self.play(Create(flat_line), run_time=0.7)
        self.play(FadeIn(flat_lbl), run_time=0.5)
        self.play(FadeIn(flat_note), run_time=0.5)
        self.wait(total - 4.5)


# ── B03 — Cold open: two energies beat into visible change ───────────────────
class B03_TwoEnergiesBeat(Scene):
    def construct(self):
        total = _dur("B03", 14.0)
        eyebrow = LabelChip("superposition of two energies", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two clock circles
        c1 = Circle(radius=1.0, color=TEAL, stroke_width=1.5)
        c1.move_to(LEFT * 4.0 + UP * 0.5)
        h1 = Arrow(LEFT * 4.0 + UP * 0.5, LEFT * 4.0 + UP * 0.5 + RIGHT * 1.0,
                   buff=0.0, color=TEAL, stroke_width=2.5,
                   max_tip_length_to_length_ratio=0.3)
        lbl1 = Text("E1", font=MONO, color=TEAL, font_size=22)
        lbl1.move_to(LEFT * 4.0 + DOWN * 0.8)

        c2 = Circle(radius=1.0, color=CRIMSON, stroke_width=1.5)
        c2.move_to(LEFT * 1.0 + UP * 0.5)
        h2 = Arrow(LEFT * 1.0 + UP * 0.5, LEFT * 1.0 + UP * 0.5 + UP * 1.0,
                   buff=0.0, color=CRIMSON, stroke_width=2.5,
                   max_tip_length_to_length_ratio=0.3)
        lbl2 = Text("E2 (faster)", font=MONO, color=CRIMSON, font_size=22)
        lbl2.move_to(LEFT * 1.0 + DOWN * 0.8)

        sloshing = Text("probability density sloshes", font=DISPLAY, color=CRIMSON, font_size=26)
        sloshing.move_to(RIGHT * 3.8 + UP * 1.2)
        sloshing_note = Text("beat = E2 - E1", font=MONO, color=CRIMSON, font_size=22)
        sloshing_note.move_to(RIGHT * 3.8 + UP * 0.3)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(c1), FadeIn(h1), FadeIn(lbl1), run_time=0.7)
        self.play(FadeIn(c2), FadeIn(h2), FadeIn(lbl2), run_time=0.7)
        self.play(FadeIn(sloshing), FadeIn(sloshing_note), run_time=0.6)
        self.wait(total - 3.8)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 14.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.to_corner(UL, buff=0.6)
        q = Text("If the phase spins,", font=DISPLAY, color=INK, font_size=44)
        q2 = Text("why does nothing change?", font=DISPLAY, color=CRIMSON, font_size=44)
        ask = Text("What does invisible spinning mean?", font=SERIF, color=INK, font_size=30, slant=ITALIC)
        content = VGroup(q, q2, ask)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(ask), run_time=0.7)
        self.wait(total - 3.2)


# ── B05 — The Problem: global phase is invisible ─────────────────────────────
class B05_GlobalPhase(Scene):
    def construct(self):
        total = _dur("B05", 17.0)
        eyebrow = LabelChip("global phase", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        rule1 = Text("amplitude psi: complex number", font=MONO, color=SLATE, font_size=26)
        rule1.move_to(UP * 1.8)

        rule2 = Text("probability = |psi|^2 = psi* x psi", font=MONO, color=SLATE, font_size=26)
        rule2.move_to(UP * 1.0)

        key = Text("e^(i x theta) x psi -> |e^(i x theta) x psi|^2 = |psi|^2",
                   font=DISPLAY, color=TEAL, font_size=28)
        key.move_to(ORIGIN)

        result = Text("global phase cancels. every time. always.",
                      font=SERIF, color=TEAL, font_size=30, slant=ITALIC)
        result.move_to(DOWN * 1.4)

        note = Text("rotating the whole state by the same angle changes nothing measurable",
                    font=MONO, color=SLATE, font_size=22)
        note.move_to(DOWN * 2.5)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(rule1), run_time=0.6)
        self.play(FadeIn(rule2), run_time=0.6)
        self.play(FadeIn(key), run_time=0.7)
        self.play(FadeIn(result), run_time=0.6)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(total - 4.0)


# ── B06 — The Problem: clock hand spinning, shadow frozen ────────────────────
class B06_ClockShadow(Scene):
    def construct(self):
        total = _dur("B06", 17.0)
        eyebrow = LabelChip("the clock picture", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Complex-plane circle on left
        circ = Circle(radius=1.5, color=TEAL, stroke_width=1.5)
        circ.move_to(LEFT * 3.5 + UP * 0.2)
        hand = Arrow(LEFT * 3.5 + UP * 0.2, LEFT * 3.5 + UP * 0.2 + RIGHT * 1.5,
                     buff=0.0, color=TEAL, stroke_width=3.0,
                     max_tip_length_to_length_ratio=0.25)
        re_label = Text("Re", font=MONO, color=SLATE, font_size=20)
        re_label.move_to(LEFT * 1.8 + UP * 0.2)
        im_label = Text("Im", font=MONO, color=SLATE, font_size=20)
        im_label.move_to(LEFT * 3.5 + UP * 2.0)
        circ_lbl = Text("hand turns at E/h-bar", font=MONO, color=TEAL, font_size=20)
        circ_lbl.move_to(LEFT * 3.5 + DOWN * 2.0)

        # Shadow projection on right
        shadow_ax = Line(RIGHT * 0.5 + DOWN * 1.5, RIGHT * 5.5 + DOWN * 1.5,
                         color=SLATE, stroke_width=1.2)
        shadow_flat = Line(RIGHT * 0.5 + DOWN * 1.5, RIGHT * 5.5 + DOWN * 1.5,
                           color=TEAL, stroke_width=3.0)
        shadow_lbl = Text("|psi|^2  = flat", font=DISPLAY, color=TEAL, font_size=26)
        shadow_lbl.move_to(RIGHT * 3.0 + DOWN * 0.5)
        shadow_note = Text("shadow never moves", font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        shadow_note.move_to(RIGHT * 3.0 + UP * 0.5)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(circ), FadeIn(hand), run_time=0.7)
        self.play(FadeIn(re_label), FadeIn(im_label), FadeIn(circ_lbl), run_time=0.5)
        self.play(Create(shadow_ax), run_time=0.5)
        self.play(Create(shadow_flat), run_time=0.5)
        self.play(FadeIn(shadow_lbl), FadeIn(shadow_note), run_time=0.6)
        self.wait(total - 4.0)


# ── B07 — The Mechanism: two clocks, relative angle changes ──────────────────
class B07_TwoClocks(Scene):
    def construct(self):
        total = _dur("B07", 19.0)
        eyebrow = LabelChip("two energy levels", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Clock 1 (TEAL, slower)
        c1 = Circle(radius=1.1, color=TEAL, stroke_width=1.5)
        c1.move_to(LEFT * 3.5 + UP * 0.3)
        h1 = Arrow(LEFT * 3.5 + UP * 0.3, LEFT * 3.5 + UP * 0.3 + RIGHT * 1.1,
                   buff=0.0, color=TEAL, stroke_width=2.5,
                   max_tip_length_to_length_ratio=0.3)
        lbl1 = Text("E1 / h-bar", font=MONO, color=TEAL, font_size=20)
        lbl1.move_to(LEFT * 3.5 + DOWN * 1.6)

        # Clock 2 (CRIMSON, faster)
        c2 = Circle(radius=1.1, color=CRIMSON, stroke_width=1.5)
        c2.move_to(LEFT * 0.5 + UP * 0.3)
        h2 = Arrow(LEFT * 0.5 + UP * 0.3, LEFT * 0.5 + UP * 0.3 + UP * 1.1,
                   buff=0.0, color=CRIMSON, stroke_width=2.5,
                   max_tip_length_to_length_ratio=0.3)
        lbl2 = Text("E2 / h-bar (faster)", font=MONO, color=CRIMSON, font_size=20)
        lbl2.move_to(LEFT * 0.5 + DOWN * 1.6)

        # Angle between them
        angle_lbl = Text("relative angle changes with t", font=DISPLAY, color=CRIMSON, font_size=28)
        angle_lbl.move_to(RIGHT * 3.0 + UP * 0.6)

        visible = Text("relative phase IS observable", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        visible.move_to(RIGHT * 3.0 + DOWN * 0.3)

        key_note = Text("all dynamics live in relative phases", font=MONO, color=SLATE, font_size=22)
        key_note.move_to(DOWN * 2.5)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(c1), FadeIn(h1), FadeIn(lbl1), run_time=0.6)
        self.play(FadeIn(c2), FadeIn(h2), FadeIn(lbl2), run_time=0.6)
        self.play(FadeIn(angle_lbl), run_time=0.6)
        self.play(FadeIn(visible), run_time=0.6)
        self.play(FadeIn(key_note), run_time=0.5)
        self.wait(total - 4.0)


# ── B08 — The Mechanism: cross terms in probability ──────────────────────────
class B08_CrossTerms(Scene):
    def construct(self):
        total = _dur("B08", 19.0)
        eyebrow = LabelChip("how the beat becomes visible", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        step1 = Text("psi = c1 e^(-iE1t/h) |E1> + c2 e^(-iE2t/h) |E2>",
                     font=MONO, color=SLATE, font_size=24)
        step1.move_to(UP * 1.8)

        step2 = Text("|psi|^2 = |c1|^2 + |c2|^2 + cross terms", font=MONO, color=SLATE, font_size=24)
        step2.move_to(UP * 0.9)

        cross = Text("cross terms ~ cos((E2-E1) x t / h-bar)", font=DISPLAY, color=CRIMSON, font_size=30)
        cross.move_to(ORIGIN)

        result = Text("cross terms oscillate at the beat frequency", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        result.move_to(DOWN * 1.0)

        single_lbl = Text("single eigenstate: no cross terms, no beat, nothing changes",
                          font=MONO, color=TEAL, font_size=22)
        single_lbl.move_to(DOWN * 2.2)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(step1, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(step2, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(cross), run_time=0.7)
        self.play(FadeIn(result), run_time=0.6)
        self.play(FadeIn(single_lbl), run_time=0.5)
        self.wait(total - 4.2)


# ── B09 — The Implication: why "stationary" is accurate ─────────────────────
class B09_WhyStationary(Scene):
    def construct(self):
        total = _dur("B09", 17.0)
        eyebrow = LabelChip("the right word for the right reason", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_single = Text("single eigenstate:", font=MONO, color=TEAL, font_size=26)
        s1 = Text("phase spins at E/h-bar", font=DISPLAY, color=TEAL, font_size=30)
        s2 = Text("no other hand -> no relative phase", font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        s3 = Text("nothing measurable ever changes", font=DISPLAY, color=TEAL, font_size=26)
        s_grp = VGroup(col_single, s1, s2, s3)
        s_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        s_grp.move_to(LEFT * 0.5 + UP * 0.5)

        note = Text("stationary = spinning invisibly. both are true.",
                    font=SERIF, color=INK, font_size=28, slant=ITALIC)
        note.move_to(DOWN * 2.3)

        self.play(FadeIn(eyebrow), run_time=0.4)
        for mob in [col_single, s1, s2, s3]:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.55)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(total - 4.0)


# ── B10 — THE EXAMPLE (illustrative): particle in a box ─────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 22.0)
        eyebrow = LabelChip("illustrative example", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        title = Text("Particle in a box: ground and first excited state",
                     font=DISPLAY, color=INK, font_size=30)
        title.move_to(UP * 2.3)

        case1 = Text("CASE A: 50-50 superposition of E1 and E2",
                     font=MONO, color=CRIMSON, font_size=24)
        case1.move_to(UP * 1.2)
        c1_result = Text("probability density sloshes at (E2-E1)/h-bar",
                         font=DISPLAY, color=CRIMSON, font_size=26)
        c1_result.move_to(UP * 0.3)

        div = Line(LEFT * 5.5 + DOWN * 0.25, RIGHT * 5.5 + DOWN * 0.25,
                   color=SLATE, stroke_width=1.0)

        case2 = Text("CASE B: just the ground state E1 alone",
                     font=MONO, color=TEAL, font_size=24)
        case2.move_to(DOWN * 0.7)
        c2_result = Text("clock hand spins, shadow frozen, nothing observable moves",
                         font=DISPLAY, color=TEAL, font_size=26)
        c2_result.move_to(DOWN * 1.6)

        note = Text("(illustrative)", font=MONO, color=SLATE, font_size=20)
        note.move_to(DOWN * 2.7)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(case1), run_time=0.5)
        self.play(FadeIn(c1_result), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(case2), run_time=0.5)
        self.play(FadeIn(c2_result), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(total - 5.0)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 17.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.6)

        q_row = Text("Q: If the phase spins, why does nothing change?",
                     font=SERIF, color=SLATE, font_size=26, slant=ITALIC)
        q_row.move_to(UP * 1.7)

        rule = Line(LEFT * 5.0 + UP * 1.05, RIGHT * 5.0 + UP * 1.05,
                    color=TEAL, stroke_width=1.5)

        a_row = Text("A: Global phase cancels in |psi|^2 — invisible alone.", font=DISPLAY, color=INK, font_size=30)
        a_sub = Text("Relative phase between two energies beats and drives all dynamics.",
                     font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        a_group = VGroup(a_row, a_sub)
        a_group.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        a_group.move_to(DOWN * 0.4)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q_row), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(a_row, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(a_sub, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)
