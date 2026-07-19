"""vox_scenes.py — Why an Electron Needs Two Full Turns to Come Back
(vox-spin-720, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL-ai slots.
Color law: TEAL = spinor (spin-1/2, needs 720 deg); CRIMSON = ordinary vector (returns at 360).
Exclusions: no SU(2)/SO(3) group theory, no Pauli-exponential derivation, no interferometer optics.
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


# -- B01 — Title card -----------------------------------------------------------
class B01_TitleCard(Scene):
    def construct(self):
        total = _dur("B01", 10.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        title = Text("Why an Electron Needs", font=DISPLAY, color=INK, font_size=46)
        sub = Text("Two Full Turns to Come Back", font=SERIF, color=TEAL, font_size=40, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.0 + DOWN * 0.5, RIGHT * 5.0 + DOWN * 0.5,
                    color=TEAL, stroke_width=2.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# -- B02 — 360 vs normal vector ------------------------------------------------
class B02_NormalVsSpinor(Scene):
    def construct(self):
        total = _dur("B02", 11.0)
        eyebrow = LabelChip("360 degrees", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left column: ordinary vector
        col_vec = VGroup(
            LabelChip("ordinary vector", accent=CRIMSON, size=22),
            Text("rotate 360 deg", font=MONO, color=CRIMSON, font_size=28),
            Text("returns IDENTICAL", font=DISPLAY, color=CRIMSON, font_size=28),
        )
        col_vec.arrange(DOWN, buff=0.38)
        col_vec.move_to(LEFT * 3.2 + DOWN * 0.2)

        # Right column: spin state
        col_spin = VGroup(
            LabelChip("spin-1/2 state", accent=TEAL, size=22),
            Text("rotate 360 deg", font=MONO, color=TEAL, font_size=28),
            Text("returns as  -|psi>", font=DISPLAY, color=TEAL, font_size=28),
        )
        col_spin.arrange(DOWN, buff=0.38)
        col_spin.move_to(RIGHT * 3.2 + DOWN * 0.2)

        div = Line(UP * 1.5 + ORIGIN, DOWN * 1.8 + ORIGIN, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        note = Text("expectations unchanged — state itself is not", font=SERIF,
                    color=INK, font_size=24, slant=ITALIC)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_vec[0]), FadeIn(col_spin[0]), run_time=0.6)
        self.play(FadeIn(col_vec[1]), FadeIn(col_spin[1]), run_time=0.6)
        self.play(FadeIn(col_vec[2]), FadeIn(col_spin[2]), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# -- B03 — Neutron interferometry confirms sign flip ---------------------------
class B03_NeutronInterferometry(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("neutron interferometry", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two-path beam diagram (schematic)
        beam_lbl = Text("beam", font=MONO, color=INK, font_size=24)
        beam_lbl.move_to(LEFT * 4.8 + UP * 0.0)

        path_top = Line(LEFT * 4.0 + UP * 0.6, RIGHT * 2.5 + UP * 0.6,
                        color=TEAL, stroke_width=2.0)
        path_bot = Line(LEFT * 4.0 + DOWN * 0.6, RIGHT * 2.5 + DOWN * 0.6,
                        color=SLATE, stroke_width=2.0)

        rot_lbl = Text("rotation applied here", font=SERIF, color=TEAL,
                       font_size=22, slant=ITALIC)
        rot_lbl.move_to(LEFT * 0.5 + UP * 1.2)

        result_360 = VGroup(
            LabelChip("at 360 deg", accent=CRIMSON, size=22),
            Text("destructive interference", font=MONO, color=CRIMSON, font_size=24),
            Text("pi phase shift detected", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC),
        )
        result_360.arrange(DOWN, buff=0.28)
        result_360.move_to(RIGHT * 3.8 + UP * 0.5)

        result_720 = VGroup(
            LabelChip("at 720 deg", accent=TEAL, size=22),
            Text("constructive interference", font=MONO, color=TEAL, font_size=24),
            Text("state restored", font=SERIF, color=TEAL, font_size=22, slant=ITALIC),
        )
        result_720.arrange(DOWN, buff=0.28)
        result_720.move_to(RIGHT * 3.8 + DOWN * 0.9)

        rule_sep = Line(RIGHT * 2.5 + UP * 1.5, RIGHT * 2.5 + DOWN * 1.5,
                        color=SLATE, stroke_width=1.2)

        source = Text("Rauch et al. 1975; Werner et al. 1975", font=SERIF,
                      color=SLATE, font_size=20, slant=ITALIC)
        source.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(beam_lbl), Create(path_top), Create(path_bot), run_time=0.6)
        self.play(Create(rule_sep), run_time=0.4)
        self.play(FadeIn(rot_lbl), run_time=0.5)
        self.play(FadeIn(result_360[0]), FadeIn(result_720[0]), run_time=0.6)
        self.play(FadeIn(result_360[1]), FadeIn(result_720[1]), run_time=0.6)
        self.play(FadeIn(result_360[2]), FadeIn(result_720[2]), run_time=0.6)
        self.play(FadeIn(source, shift=UP * 0.05), run_time=0.5)
        self.wait(total - 5.5)


# -- B04 — THE QUESTION card ---------------------------------------------------
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("360-degree rotation flips the sign.", font=DISPLAY, color=INK, font_size=34)
        q2 = Text("Probabilities don't change.", font=DISPLAY, color=SLATE, font_size=34)
        q3 = Text("The flip is invisible — but interferometry detects it.", font=SERIF,
                  color=CRIMSON, font_size=30, slant=ITALIC)
        q4 = Text("How?", font=DISPLAY, color=TEAL, font_size=42)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        content.move_to(ORIGIN).shift(DOWN * 0.2)
        rule = Line(LEFT * 4.5 + DOWN * 0.55, RIGHT * 4.5 + DOWN * 0.55,
                    color=SLATE, stroke_width=2.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q3, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q4, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# -- B05 — THE PROBLEM: naive "must be artifact" model -------------------------
class B05_NaiveArtifact(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE READING", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_arg = VGroup(
            LabelChip("classical logic", accent=SLATE, size=22),
            Text("360 deg = full rotation", font=MONO, color=SLATE, font_size=28),
            Text("should return any state", font=SERIF, color=SLATE, font_size=26, slant=ITALIC),
            Text("minus sign is invisible", font=SERIF, color=SLATE, font_size=26, slant=ITALIC),
        )
        col_arg.arrange(DOWN, buff=0.35)
        col_arg.move_to(LEFT * 2.8 + DOWN * 0.2)

        col_concl = VGroup(
            LabelChip("naive conclusion", accent=CRIMSON, size=22),
            Text("must be a bookkeeping", font=MONO, color=CRIMSON, font_size=28),
            Text("artifact", font=MONO, color=CRIMSON, font_size=28),
            Text("no physical meaning", font=DISPLAY, color=CRIMSON, font_size=26),
        )
        col_concl.arrange(DOWN, buff=0.35)
        col_concl.move_to(RIGHT * 2.8 + DOWN * 0.2)

        div = Line(UP * 1.5 + ORIGIN, DOWN * 2.2 + ORIGIN, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_arg[0]), FadeIn(col_concl[0]), run_time=0.6)
        self.play(FadeIn(col_arg[1]), FadeIn(col_concl[1]), run_time=0.6)
        self.play(FadeIn(col_arg[2]), FadeIn(col_concl[2]), run_time=0.6)
        self.play(FadeIn(col_arg[3]), FadeIn(col_concl[3]), run_time=0.7)
        self.wait(total - 4.5)


# -- B06 — MECHANISM: half-angle in Bloch state --------------------------------
class B06_HalfAngleState(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("THE MECHANISM", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        heading = Text("Bloch sphere state formula:", font=DISPLAY, color=INK, font_size=30)
        heading.move_to(UP * 1.7)

        rule_h = Line(LEFT * 5.0 + UP * 1.2, RIGHT * 5.0 + UP * 1.2,
                      color=SLATE, stroke_width=1.5)

        state_eq = Text("|psi> = cos(theta/2)|up> + exp(i*phi)*sin(theta/2)|down>",
                        font=MONO, color=TEAL, font_size=26)
        state_eq.move_to(UP * 0.5)

        half_note = Text("angles theta and phi appear HALVED", font=SERIF,
                         color=TEAL, font_size=26, slant=ITALIC)
        half_note.move_to(DOWN * 0.25)

        contrast = Text("a classical direction: uses theta, not theta/2", font=SERIF,
                        color=CRIMSON, font_size=24, slant=ITALIC)
        contrast.move_to(DOWN * 0.85)

        note = SerifLabel("this half-angle is the source of the sign flip", accent=TEAL, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(heading), run_time=0.6)
        self.play(Create(rule_h), run_time=0.4)
        self.play(FadeIn(state_eq, shift=DOWN * 0.1), run_time=0.8)
        self.play(FadeIn(half_note, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(contrast, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# -- B07 — MECHANISM: 360 rotation advances half-angle by pi → sign flip ------
class B07_SignFlipMechanism(Scene):
    def construct(self):
        total = _dur("B07", 11.0)
        eyebrow = LabelChip("sign flip", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        step1 = Text("physical rotation: theta -> theta + 2*pi", font=MONO,
                     color=INK, font_size=26)
        step1.move_to(UP * 1.2)

        rule1 = Line(LEFT * 5.0 + UP * 0.7, RIGHT * 5.0 + UP * 0.7,
                     color=SLATE, stroke_width=1.0)

        step2 = Text("half-angle: theta/2 -> theta/2 + pi", font=MONO,
                     color=TEAL, font_size=26)
        step2.move_to(UP * 0.2)

        step3 = Text("cos(theta/2 + pi) = -cos(theta/2)", font=MONO,
                     color=TEAL, font_size=26)
        step3.move_to(DOWN * 0.4)

        rule2 = Line(LEFT * 5.0 + DOWN * 0.9, RIGHT * 5.0 + DOWN * 0.9,
                     color=SLATE, stroke_width=1.0)

        result = Text("|psi> -> -|psi>   after ONE full turn", font=DISPLAY,
                      color=CRIMSON, font_size=28)
        result.move_to(DOWN * 1.4)

        note = Text("only at 720 deg does theta/2 advance by 2*pi -> full return",
                    font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        note.to_edge(DOWN, buff=0.75)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(step1, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule1), run_time=0.4)
        self.play(FadeIn(step2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(step3, shift=DOWN * 0.1), run_time=0.6)
        self.play(Create(rule2), run_time=0.4)
        self.play(FadeIn(result, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(total - 5.5)


# -- B08 — MECHANISM: sign flip invisible alone, real in interference ----------
class B08_InvisibleButReal(Scene):
    def construct(self):
        total = _dur("B08", 11.0)
        eyebrow = LabelChip("invisible alone, real in interference", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left panel: alone — undetectable
        col_alone = VGroup(
            LabelChip("single beam", accent=SLATE, size=22),
            Text("-|psi>  vs  |psi>", font=MONO, color=SLATE, font_size=26),
            Text("|amplitude|^2 unchanged", font=MONO, color=SLATE, font_size=24),
            Text("all probabilities same", font=SERIF, color=SLATE, font_size=22, slant=ITALIC),
            Text("INVISIBLE", font=DISPLAY, color=SLATE, font_size=28),
        )
        col_alone.arrange(DOWN, buff=0.3)
        col_alone.move_to(LEFT * 3.0 + DOWN * 0.1)

        # Right panel: interference — detectable
        col_interf = VGroup(
            LabelChip("interference", accent=TEAL, size=22),
            Text("-|psi> vs ref. |psi>", font=MONO, color=TEAL, font_size=26),
            Text("pi phase shift", font=MONO, color=CRIMSON, font_size=24),
            Text("destructive minimum", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC),
            Text("DETECTABLE", font=DISPLAY, color=TEAL, font_size=28),
        )
        col_interf.arrange(DOWN, buff=0.3)
        col_interf.move_to(RIGHT * 3.0 + DOWN * 0.1)

        div = Line(UP * 1.8 + ORIGIN, DOWN * 2.2 + ORIGIN, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_alone[0]), FadeIn(col_interf[0]), run_time=0.6)
        self.play(FadeIn(col_alone[1]), FadeIn(col_interf[1]), run_time=0.6)
        self.play(FadeIn(col_alone[2]), FadeIn(col_interf[2]), run_time=0.6)
        self.play(FadeIn(col_alone[3]), FadeIn(col_interf[3]), run_time=0.6)
        self.play(FadeIn(col_alone[4]), FadeIn(col_interf[4]), run_time=0.7)
        self.wait(total - 5.0)


# -- B09 — Implication: SU(2) double-covers SO(3) ------------------------------
class B09_SU2DoubleCover(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left: ordinary rotations
        col_so3 = VGroup(
            LabelChip("ordinary rotations", accent=CRIMSON, size=22),
            Text("vectors, directions", font=MONO, color=CRIMSON, font_size=26),
            Text("SO(3)", font=DISPLAY, color=CRIMSON, font_size=30),
            Text("one loop closes at 360", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC),
        )
        col_so3.arrange(DOWN, buff=0.35)
        col_so3.move_to(LEFT * 3.0 + DOWN * 0.2)

        # Right: spin states
        col_su2 = VGroup(
            LabelChip("spin-1/2 states", accent=TEAL, size=22),
            Text("spinors", font=MONO, color=TEAL, font_size=26),
            Text("SU(2)", font=DISPLAY, color=TEAL, font_size=30),
            Text("two loops needed: 720", font=SERIF, color=TEAL, font_size=22, slant=ITALIC),
        )
        col_su2.arrange(DOWN, buff=0.35)
        col_su2.move_to(RIGHT * 3.0 + DOWN * 0.2)

        div = Line(UP * 1.5 + ORIGIN, DOWN * 2.0 + ORIGIN, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        note = Text("SU(2) wraps twice around SO(3)", font=DISPLAY,
                    color=INK, font_size=24)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_so3[0]), FadeIn(col_su2[0]), run_time=0.6)
        self.play(FadeIn(col_so3[1]), FadeIn(col_su2[1]), run_time=0.6)
        self.play(FadeIn(col_so3[2]), FadeIn(col_su2[2]), run_time=0.6)
        self.play(FadeIn(col_so3[3]), FadeIn(col_su2[3]), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# -- B10 — THE EXAMPLE: student in interferometry thought experiment -----------
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        header = Text("Interferometry thought experiment", font=DISPLAY,
                      color=INK, font_size=28)
        header.move_to(UP * 1.8)
        rule_top = Line(LEFT * 5.5 + UP * 1.4, RIGHT * 5.5 + UP * 1.4,
                        color=SLATE, stroke_width=1.5)

        step1 = Text("1. split beam: path A (rotated), path B (ref.)",
                     font=MONO, color=INK, font_size=24)
        step1.move_to(UP * 0.75 + LEFT * 0.3)

        step2 = Text("2. rotate path A spins by 360 deg", font=MONO,
                     color=TEAL, font_size=24)
        step2.move_to(UP * 0.1 + LEFT * 0.3)

        step3 = Text("3. interfere the two paths", font=MONO, color=INK, font_size=24)
        step3.move_to(DOWN * 0.55 + LEFT * 0.3)

        result = Text("RESULT: destructive minimum", font=DISPLAY,
                      color=CRIMSON, font_size=26)
        result.move_to(DOWN * 1.2)

        footer = Text("sign was waiting to be measured — not just bookkeeping",
                      font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        footer.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(header), Create(rule_top), run_time=0.6)
        self.play(FadeIn(step1), run_time=0.6)
        self.play(FadeIn(step2), run_time=0.6)
        self.play(FadeIn(step3), run_time=0.6)
        self.play(FadeIn(result, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.5)


# -- B11 — RECAP endcard -------------------------------------------------------
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("Half-angle in state  ->  360 deg flips sign.", font=MONO,
                     color=TEAL, font_size=24)
        line1.move_to(UP * 0.9)
        line2 = Text("Sign invisible alone  ->  real in interference.", font=MONO,
                     color=CRIMSON, font_size=24)
        line2.move_to(UP * 0.2)
        line3 = Text("720 deg restores the state.", font=MONO, color=INK, font_size=24)
        line3.move_to(DOWN * 0.5)
        line4 = Text("Spin lives in SU(2), which wraps twice around SO(3).", font=DISPLAY,
                     color=TEAL, font_size=24)
        line4.move_to(DOWN * 1.2)
        sub = Text("The sign was real — interferometry proved it.", font=SERIF,
                   color=INK, font_size=24, slant=ITALIC)
        sub.to_edge(DOWN, buff=0.9)

        end_box = Rectangle(width=0.6, height=0.6).set_fill(SLATE, 0.8).set_stroke(SLATE, 2.0)
        end_box.to_corner(DR, buff=0.6)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line3, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(line4, shift=DOWN * 0.1), run_time=0.6)
        self.play(GrowFromCenter(end_box), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
        self.wait(total - 4.8)
