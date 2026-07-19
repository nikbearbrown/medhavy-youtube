"""vox_scenes.py — Why Every Qubit Lives on a Globe
(vox-bloch-sphere-qubit, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = state arrow (qubit Bloch vector);
           CRIMSON = analyzer arrow (measurement direction).
Exclusions: no half-angle proof, no gate operations, no density matrix.
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
        title = Text("Why Every Qubit", font=DISPLAY, color=INK, font_size=54)
        sub = Text("Lives on a Globe", font=SERIF, color=TEAL, font_size=46, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.0 + DOWN * 0.55, RIGHT * 5.0 + DOWN * 0.55,
                    color=TEAL, stroke_width=2.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: qubit state ────────────────────────────────────────────
class B02_QubitState(Scene):
    def construct(self):
        total = _dur("B02", 12.0)
        eyebrow = LabelChip("QUBIT", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_classic = VGroup(
            LabelChip("classical bit", accent=SLATE, size=22),
            Text("0  or  1", font=MONO, color=SLATE, font_size=36),
            Text("exactly one value", font=SERIF, color=SLATE, font_size=24, slant=ITALIC),
        )
        col_classic.arrange(DOWN, buff=0.4)
        col_classic.move_to(LEFT * 3.0 + DOWN * 0.2)

        col_qubit = VGroup(
            LabelChip("quantum bit", accent=TEAL, size=22),
            Text("a|0> + b|1>", font=MONO, color=TEAL, font_size=34),
            Text("a, b complex numbers", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
        )
        col_qubit.arrange(DOWN, buff=0.4)
        col_qubit.move_to(RIGHT * 3.0 + DOWN * 0.2)

        div = Line(UP * 1.2, DOWN * 1.8, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_classic[0]), FadeIn(col_qubit[0]), run_time=0.6)
        self.play(FadeIn(col_classic[1]), FadeIn(col_qubit[1]), run_time=0.6)
        self.play(FadeIn(col_classic[2]), FadeIn(col_qubit[2]), run_time=0.6)
        self.wait(total - 4.0)


# ── B03 — Cold open: Born rule & normalization ───────────────────────────────
class B03_BornNorm(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("Born rule", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        rule1 = Text("P(0)  =  |a|^2", font=MONO, color=TEAL, font_size=32)
        rule1.move_to(UP * 0.9)

        rule2 = Text("P(1)  =  |b|^2", font=MONO, color=CRIMSON, font_size=32)
        rule2.move_to(UP * 0.15)

        sep = Line(LEFT * 4.5 + DOWN * 0.35, RIGHT * 4.5 + DOWN * 0.35,
                   color=SLATE, stroke_width=1.5)

        norm = Text("|a|^2  +  |b|^2  =  1", font=MONO, color=INK, font_size=34)
        norm.move_to(DOWN * 1.0)

        note = SerifLabel("probabilities always sum to one", accent=TEAL, size=26)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(rule1, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(rule2, shift=DOWN * 0.1), run_time=0.6)
        self.play(Create(sep), run_time=0.4)
        self.play(FadeIn(norm, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("A qubit needs four real parameters.", font=DISPLAY, color=INK, font_size=34)
        q2 = Text("Yet it maps to a sphere —", font=DISPLAY, color=CRIMSON, font_size=34)
        q3 = Text("which is two-dimensional.", font=SERIF, color=INK, font_size=30, slant=ITALIC)
        q4 = Text("Where do the extras go?", font=DISPLAY, color=TEAL, font_size=38)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 4.5 + DOWN * 0.5, RIGHT * 4.5 + DOWN * 0.5,
                    color=SLATE, stroke_width=2.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), FadeIn(q3, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q4, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)


# ── B05 — THE PROBLEM: 4 params needed ──────────────────────────────────────
class B05_FourParams(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE COUNT", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_count = VGroup(
            LabelChip("two complex numbers", accent=SLATE, size=22),
            Text("a  =  re(a) + i·im(a)", font=MONO, color=SLATE, font_size=26),
            Text("b  =  re(b) + i·im(b)", font=MONO, color=SLATE, font_size=26),
            Text("total: 4 real parameters", font=DISPLAY, color=SLATE, font_size=28),
        )
        col_count.arrange(DOWN, buff=0.32)
        col_count.move_to(LEFT * 2.5 + DOWN * 0.1)

        col_sphere = VGroup(
            LabelChip("but a sphere needs", accent=CRIMSON, size=22),
            Text("latitude  (1 number)", font=MONO, color=CRIMSON, font_size=26),
            Text("longitude  (1 number)", font=MONO, color=CRIMSON, font_size=26),
            Text("total: 2 real parameters", font=DISPLAY, color=CRIMSON, font_size=28),
        )
        col_sphere.arrange(DOWN, buff=0.32)
        col_sphere.move_to(RIGHT * 2.5 + DOWN * 0.1)

        div = Line(UP * 1.2, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_count[0]), FadeIn(col_sphere[0]), run_time=0.6)
        self.play(FadeIn(col_count[1]), FadeIn(col_sphere[1]), run_time=0.6)
        self.play(FadeIn(col_count[2]), FadeIn(col_sphere[2]), run_time=0.6)
        self.play(FadeIn(col_count[3]), FadeIn(col_sphere[3]), run_time=0.6)
        self.wait(total - 4.5)


# ── B06 — MECHANISM: normalization removes 1 ────────────────────────────────
class B06_NormalizationRemoves1(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("CONSTRAINT 1: NORMALIZATION", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        start = Text("start:  4 real parameters", font=MONO, color=SLATE, font_size=30)
        start.move_to(UP * 1.2)

        constraint = Text("|a|^2 + |b|^2 = 1  (one equation)", font=MONO,
                          color=CRIMSON, font_size=28)
        constraint.move_to(UP * 0.3)

        result = Text("removes 1 parameter  ->  3 remain", font=DISPLAY,
                      color=TEAL, font_size=30)
        result.move_to(DOWN * 0.6)

        sep1 = Line(LEFT * 5.5 + UP * 0.75, RIGHT * 5.5 + UP * 0.75,
                    color=SLATE, stroke_width=1.0)
        sep2 = Line(LEFT * 5.5 + DOWN * 0.1, RIGHT * 5.5 + DOWN * 0.1,
                    color=SLATE, stroke_width=1.0)

        note = SerifLabel("normalization constrains the radius, not the direction", accent=TEAL, size=24)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(start, shift=DOWN * 0.1), run_time=0.6)
        self.play(Create(sep1), run_time=0.4)
        self.play(FadeIn(constraint, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(sep2), run_time=0.4)
        self.play(FadeIn(result, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B07 — MECHANISM: global phase removes 1 ─────────────────────────────────
class B07_GlobalPhaseRemoves1(Scene):
    def construct(self):
        total = _dur("B07", 12.0)
        eyebrow = LabelChip("CONSTRAINT 2: GLOBAL PHASE", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        start = Text("3 parameters remain", font=MONO, color=SLATE, font_size=30)
        start.move_to(UP * 1.2)

        constraint = Text("e^(i*phi) * |psi>  gives same probabilities", font=MONO,
                          color=CRIMSON, font_size=26)
        constraint.move_to(UP * 0.3)

        result = Text("removes 1 more  ->  2 remain", font=DISPLAY,
                      color=TEAL, font_size=30)
        result.move_to(DOWN * 0.55)

        final = Text("2 real parameters  =  a point on a sphere", font=DISPLAY,
                     color=TEAL, font_size=28)
        final.move_to(DOWN * 1.3)

        sep1 = Line(LEFT * 5.5 + UP * 0.75, RIGHT * 5.5 + UP * 0.75,
                    color=SLATE, stroke_width=1.0)
        sep2 = Line(LEFT * 5.5 + DOWN * 0.1, RIGHT * 5.5 + DOWN * 0.1,
                    color=SLATE, stroke_width=1.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(start, shift=DOWN * 0.1), run_time=0.6)
        self.play(Create(sep1), run_time=0.4)
        self.play(FadeIn(constraint, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(sep2), run_time=0.4)
        self.play(FadeIn(result, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(final, shift=DOWN * 0.1), run_time=0.6)
        self.wait(total - 5.5)


# ── B08 — MECHANISM: theta and phi on the sphere ────────────────────────────
class B08_SphereCoords(Scene):
    def construct(self):
        total = _dur("B08", 12.0)
        eyebrow = LabelChip("THE BLOCH SPHERE", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Vertical axis (left side only, kept short so text on right stays clear)
        axis = Line(DOWN * 1.5, UP * 1.5, color=SLATE, stroke_width=2.0)
        axis.move_to(LEFT * 5.0)
        north_lbl = Text("|up>", font=MONO, color=TEAL, font_size=24)
        north_lbl.move_to(LEFT * 5.0 + UP * 1.9)
        south_lbl = Text("|down>", font=MONO, color=CRIMSON, font_size=24)
        south_lbl.move_to(LEFT * 5.0 + DOWN * 1.9)

        # Table of points — all well to the right of the axis
        header = LabelChip("sphere positions", accent=SLATE, size=22)
        header.move_to(RIGHT * 1.5 + UP * 1.5)

        row1 = Text("north pole  theta=0      ->  |up>", font=MONO, color=TEAL, font_size=22)
        row1.move_to(RIGHT * 1.5 + UP * 0.7)
        row2 = Text("south pole  theta=pi     ->  |down>", font=MONO, color=CRIMSON, font_size=22)
        row2.move_to(RIGHT * 1.5 + DOWN * 0.0)
        row3 = Text("equator     theta=pi/2   ->  equal mix", font=MONO, color=INK, font_size=22)
        row3.move_to(RIGHT * 1.5 + DOWN * 0.7)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(axis), FadeIn(north_lbl), FadeIn(south_lbl), run_time=0.6)
        self.play(FadeIn(header), run_time=0.5)
        self.play(FadeIn(row1, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(row2, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(row3, shift=DOWN * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B09 — Implication: P(up) = cos^2(gamma/2) geometry ──────────────────────
class B09_BornRuleGeometry(Scene):
    def construct(self):
        total = _dur("B09", 12.0)
        eyebrow = LabelChip("BORN RULE AS GEOMETRY", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        formula = Text("P(+)  =  cos^2 (gamma / 2)", font=MONO, color=TEAL, font_size=34)
        formula.move_to(UP * 1.2)

        rule_f = Line(LEFT * 4.5 + UP * 0.75, RIGHT * 4.5 + UP * 0.75,
                      color=TEAL, stroke_width=1.5)

        col_gamma = VGroup(
            LabelChip("angle gamma", accent=SLATE, size=22),
            Text("0   (parallel)", font=MONO, color=SLATE, font_size=26),
            Text("90  (perpendicular)", font=MONO, color=SLATE, font_size=26),
            Text("180 (antiparallel)", font=MONO, color=SLATE, font_size=26),
        )
        col_gamma.arrange(DOWN, buff=0.3)
        col_gamma.move_to(LEFT * 2.8 + DOWN * 0.55)

        col_prob = VGroup(
            LabelChip("P(+)", accent=TEAL, size=22),
            Text("1.00  (certain)", font=MONO, color=TEAL, font_size=26),
            Text("0.50", font=MONO, color=INK, font_size=26),
            Text("0.00  (never)", font=MONO, color=CRIMSON, font_size=26),
        )
        col_prob.arrange(DOWN, buff=0.3)
        col_prob.move_to(RIGHT * 2.8 + DOWN * 0.55)

        div = Line(UP * 0.35, DOWN * 2.2, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN + DOWN * 0.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(formula, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule_f), run_time=0.4)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_gamma[0]), FadeIn(col_prob[0]), run_time=0.6)
        self.play(FadeIn(col_gamma[1]), FadeIn(col_prob[1]), run_time=0.6)
        self.play(FadeIn(col_gamma[2]), FadeIn(col_prob[2]), run_time=0.6)
        self.play(FadeIn(col_gamma[3]), FadeIn(col_prob[3]), run_time=0.6)
        self.wait(total - 6.0)


# ── B10 — THE EXAMPLE: theta=60, 1000 shots ─────────────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        header = Text("Measuring a qubit at theta = 60 deg", font=DISPLAY,
                      color=INK, font_size=28)
        header.move_to(UP * 1.8)
        rule_top = Line(LEFT * 5.5 + UP * 1.4, RIGHT * 5.5 + UP * 1.4,
                        color=SLATE, stroke_width=1.5)

        step1 = Text("state at theta = 60 deg from north pole", font=MONO,
                     color=TEAL, font_size=24)
        step1.move_to(UP * 0.75 + LEFT * 0.4)

        step2 = Text("measure along z  ->  gamma = 60 deg", font=MONO, color=INK, font_size=24)
        step2.move_to(UP * 0.15)

        step3 = Text("P(up) = cos^2(30 deg) = 3/4 = 0.75", font=MONO, color=TEAL, font_size=24)
        step3.move_to(DOWN * 0.45)

        step4 = Text("run 1000 copies  ->  ~750 up,  ~250 down", font=MONO,
                     color=CRIMSON, font_size=24)
        step4.move_to(DOWN * 1.05)

        footer = SerifLabel("the sphere predicts the count — no fitting required", accent=TEAL, size=24)
        footer.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(header), Create(rule_top), run_time=0.6)
        self.play(FadeIn(step1, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(step2, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(step3, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(step4, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.5)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("4 params - normalization - global phase = 2.", font=MONO,
                     color=TEAL, font_size=24)
        line1.move_to(UP * 0.9)
        line2 = Text("2 real parameters  =  a sphere.", font=MONO,
                     color=TEAL, font_size=26)
        line2.move_to(UP * 0.2)
        line3 = Text("P(+) = cos^2(gamma/2)  —  pure geometry.", font=DISPLAY,
                     color=INK, font_size=26)
        line3.move_to(DOWN * 0.5)
        sub = Text("Every qubit lives on a globe.", font=SERIF,
                   color=INK, font_size=26, slant=ITALIC)
        sub.to_edge(DOWN, buff=0.9)

        end_box = Rectangle(width=0.6, height=0.6).set_fill(SLATE, 0.8).set_stroke(SLATE, 2.0)
        end_box.to_corner(DR, buff=0.6)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line3, shift=DOWN * 0.1), run_time=0.6)
        self.play(GrowFromCenter(end_box), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
        self.wait(total - 4.8)
