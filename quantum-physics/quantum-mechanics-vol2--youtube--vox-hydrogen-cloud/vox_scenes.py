"""vox_scenes.py — Why the Electron Has No Orbit, Only a Cloud
(vox-hydrogen-cloud, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = wave-mechanics prediction (P(r) curve, two distinct radii)
           CRIMSON = Bohr orbit at single radius (the wrong model being displaced)
Exclusions: no radial-equation/Laguerre derivation, no SO(4) symmetry, no normalization algebra.
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
        total = _dur("B01", 9.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        title = Text("Why the Electron Has No Orbit,", font=DISPLAY, color=INK, font_size=42)
        sub = Text("Only a Cloud", font=SERIF, color=TEAL, font_size=44, slant=ITALIC)
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


# ── B02 — Cold open: Bohr model, single radius ───────────────────────────────
class B02_BohrOrbit(Scene):
    def construct(self):
        total = _dur("B02", 15.0)
        eyebrow = LabelChip("Bohr 1913", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Proton dot
        proton = Dot(radius=0.12, color=CRIMSON)
        proton.move_to(ORIGIN)
        proton_lbl = Text("proton", font=MONO, color=CRIMSON, font_size=20)
        proton_lbl.next_to(proton, DOWN, buff=0.12)

        # Orbit circle at radius a0 (represented at r=2 units on screen)
        orbit = Circle(radius=2.0, color=CRIMSON, stroke_width=1.5)
        orbit.move_to(ORIGIN)

        # Electron dot on orbit
        elec = Dot(radius=0.10, color=CRIMSON)
        elec.move_to(RIGHT * 2.0)
        elec_lbl = Text("electron", font=MONO, color=CRIMSON, font_size=20)
        elec_lbl.next_to(elec, UR, buff=0.08)

        # Labels
        a0_lbl = Text("Bohr radius", font=DISPLAY, color=CRIMSON, font_size=24)
        a0_lbl.move_to(RIGHT * 3.8 + UP * 0.5)

        same = Text("most-likely = average = a0", font=MONO, color=CRIMSON, font_size=24)
        same.move_to(DOWN * 2.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(proton), FadeIn(proton_lbl), run_time=0.5)
        self.play(Create(orbit), run_time=0.8)
        self.play(FadeIn(elec), FadeIn(elec_lbl), run_time=0.5)
        self.play(FadeIn(a0_lbl), run_time=0.5)
        self.play(FadeIn(same), run_time=0.6)
        self.wait(total - 4.0)


# ── B03 — Cold open: wave mechanics gives two different radii ─────────────────
class B03_WaveMechanics(Scene):
    def construct(self):
        total = _dur("B03", 14.0)
        eyebrow = LabelChip("Schrodinger 1926", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Sketch of P(r): peak at a0, mean further right
        # Use line segments to approximate the curve shape (no numpy plotting needed)
        axes_x = Line(LEFT * 4.5 + DOWN * 1.5, RIGHT * 4.5 + DOWN * 1.5,
                      color=SLATE, stroke_width=1.5)
        axes_y = Line(LEFT * 4.5 + DOWN * 1.5, LEFT * 4.5 + UP * 1.8,
                      color=SLATE, stroke_width=1.5)

        # Approximate P(r) ~ r^2 exp(-2r) as a sequence of short line segments
        pts = []
        for i in range(60):
            r = i * 0.12
            p = r * r * np.exp(-2.0 * r / 1.8)
            x = -4.0 + r * 1.5
            y = -1.5 + p * 5.5
            pts.append([x, y, 0])

        curve = VMobject()
        curve.set_points_as_corners(pts)
        curve.set_stroke(color=TEAL, width=2.5)
        curve.set_fill(opacity=0.0)

        peak_line = Line(LEFT * 2.3 + DOWN * 1.5, LEFT * 2.3 + UP * 0.8,
                         color=TEAL, stroke_width=1.8)
        mean_line = Line(LEFT * 1.2 + DOWN * 1.5, LEFT * 1.2 + UP * 0.5,
                         color=TEAL, stroke_width=1.8, stroke_opacity=0.7)

        peak_lbl = Text("peak = a0", font=MONO, color=TEAL, font_size=20)
        peak_lbl.move_to(LEFT * 2.3 + UP * 1.1)
        mean_lbl = Text("mean = 3a0/2", font=MONO, color=TEAL, font_size=20)
        mean_lbl.move_to(LEFT * 1.2 + UP * 0.85)

        x_lbl = Text("r", font=MONO, color=SLATE, font_size=22)
        x_lbl.next_to(axes_x, RIGHT, buff=0.15)
        y_lbl = Text("P(r)", font=MONO, color=SLATE, font_size=22)
        y_lbl.next_to(axes_y, UP, buff=0.12)

        different = Text("two different numbers!", font=DISPLAY, color=TEAL, font_size=26)
        different.move_to(RIGHT * 2.5 + UP * 1.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(Create(axes_x), Create(axes_y), run_time=0.6)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(curve), run_time=1.0)
        self.play(Create(peak_line), Create(mean_line), run_time=0.6)
        self.play(FadeIn(peak_lbl), FadeIn(mean_lbl), run_time=0.5)
        self.play(FadeIn(different), run_time=0.5)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 14.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.to_corner(UL, buff=0.6)
        q = Text("Why do most-likely and", font=DISPLAY, color=INK, font_size=44)
        q2 = Text("average radius disagree?", font=DISPLAY, color=CRIMSON, font_size=44)
        ask = Text("Two numbers, one electron.", font=SERIF, color=INK, font_size=34, slant=ITALIC)
        content = VGroup(q, q2, ask)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(ask), run_time=0.7)
        self.wait(total - 3.2)


# ── B05 — The Problem: classical orbit gives one answer ──────────────────────
class B05_ClassicalOrbit(Scene):
    def construct(self):
        total = _dur("B05", 16.0)
        eyebrow = LabelChip("what an orbit would give", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two "measurements" from an orbit — both the same
        meas_lbl = Text("1000 measurements of orbit radius:", font=MONO, color=SLATE, font_size=26)
        meas_lbl.move_to(UP * 1.8)

        val1 = Text("most common:   r0", font=DISPLAY, color=CRIMSON, font_size=36)
        val2 = Text("average:   r0", font=DISPLAY, color=CRIMSON, font_size=36)
        vals = VGroup(val1, val2)
        vals.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        vals.move_to(ORIGIN + UP * 0.3)

        result = Text("same number. always.", font=SERIF, color=CRIMSON, font_size=32, slant=ITALIC)
        result.move_to(DOWN * 2.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(meas_lbl), run_time=0.6)
        self.play(FadeIn(val1, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(val2, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(result), run_time=0.7)
        self.wait(total - 3.5)


# ── B06 — The Problem: the r-squared shell factor ────────────────────────────
class B06_ShellFactor(Scene):
    def construct(self):
        total = _dur("B06", 18.0)
        eyebrow = LabelChip("the shell volume trick", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left: density |psi|^2 — peaks at nucleus
        col_psi = Text("|psi|^2 at a point:", font=MONO, color=SLATE, font_size=26)
        col_psi.move_to(LEFT * 3.5 + UP * 1.8)
        psi_lbl = Text("largest at r = 0", font=DISPLAY, color=CRIMSON, font_size=28)
        psi_lbl.move_to(LEFT * 3.5 + UP * 0.7)
        psi_note = Text("(density, not\nprobability)", font=MONO, color=SLATE, font_size=22)
        psi_note.move_to(LEFT * 3.5 + DOWN * 0.2)

        # Right: P(r) = r^2 |R|^2 — shell volume matters
        col_pr = Text("P(r) in a shell:", font=MONO, color=SLATE, font_size=26)
        col_pr.move_to(RIGHT * 3.5 + UP * 1.8)
        pr_lbl = Text("r^2 x |psi|^2", font=DISPLAY, color=TEAL, font_size=28)
        pr_lbl.move_to(RIGHT * 3.5 + UP * 0.7)
        pr_note = Text("small shell at r~0\nkills the peak", font=MONO, color=TEAL, font_size=22)
        pr_note.move_to(RIGHT * 3.5 + DOWN * 0.2)

        vs = Text("vs", font=DISPLAY, color=SLATE, font_size=32)
        vs.move_to(ORIGIN + UP * 1.2)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(col_psi), FadeIn(col_pr), run_time=0.6)
        self.play(FadeIn(vs), run_time=0.4)
        self.play(FadeIn(psi_lbl), FadeIn(pr_lbl), run_time=0.6)
        self.play(FadeIn(psi_note), FadeIn(pr_note), run_time=0.6)
        self.wait(total - 3.5)


# ── B07 — The Mechanism: P(r) has a peak and a long tail ─────────────────────
class B07_PrCurve(Scene):
    def construct(self):
        total = _dur("B07", 20.0)
        eyebrow = LabelChip("radial probability P(r)", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        axes_x = Line(LEFT * 5.0 + DOWN * 1.8, RIGHT * 4.5 + DOWN * 1.8,
                      color=SLATE, stroke_width=1.5)
        axes_y = Line(LEFT * 5.0 + DOWN * 1.8, LEFT * 5.0 + UP * 2.2,
                      color=SLATE, stroke_width=1.5)
        x_lbl = Text("r", font=MONO, color=SLATE, font_size=22)
        x_lbl.next_to(axes_x, RIGHT, buff=0.15)
        y_lbl = Text("P(r)", font=MONO, color=SLATE, font_size=22)
        y_lbl.next_to(axes_y, UP, buff=0.12)

        # P(r) curve approximation
        pts = []
        for i in range(80):
            r = i * 0.10
            p = r * r * np.exp(-2.0 * r / 1.5)
            x = -4.5 + r * 1.8
            y = -1.8 + p * 7.0
            pts.append([x, y, 0])

        curve = VMobject()
        curve.set_points_as_corners(pts)
        curve.set_stroke(color=TEAL, width=3.0)
        curve.set_fill(opacity=0.0)

        # Tail annotation
        tail_lbl = Text("long tail ->", font=MONO, color=TEAL, font_size=22)
        tail_lbl.move_to(RIGHT * 2.0 + DOWN * 0.5)

        zero_note = Text("P(0) = 0", font=MONO, color=TEAL, font_size=20)
        zero_note.move_to(LEFT * 3.5 + DOWN * 0.5)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(Create(axes_x), Create(axes_y), run_time=0.6)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(curve), run_time=1.2)
        self.play(FadeIn(zero_note), run_time=0.5)
        self.play(FadeIn(tail_lbl), run_time=0.5)
        self.wait(total - 4.5)


# ── B08 — The Mechanism: peak at a0, mean at 3a0/2 ──────────────────────────
class B08_PeakVsMean(Scene):
    def construct(self):
        total = _dur("B08", 19.0)
        eyebrow = LabelChip("two markers, one distribution", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        axes_x = Line(LEFT * 5.0 + DOWN * 1.8, RIGHT * 4.5 + DOWN * 1.8,
                      color=SLATE, stroke_width=1.5)
        axes_y = Line(LEFT * 5.0 + DOWN * 1.8, LEFT * 5.0 + UP * 2.2,
                      color=SLATE, stroke_width=1.5)

        pts = []
        for i in range(80):
            r = i * 0.10
            p = r * r * np.exp(-2.0 * r / 1.5)
            x = -4.5 + r * 1.8
            y = -1.8 + p * 7.0
            pts.append([x, y, 0])

        curve = VMobject()
        curve.set_points_as_corners(pts)
        curve.set_stroke(color=TEAL, width=2.5)
        curve.set_fill(opacity=0.0)

        # Peak line at a0: r=1.5 in our parameter => x = -4.5 + 1.5*1.8 = -1.8
        peak_x = -4.5 + 1.5 * 1.8  # ~ -1.8
        peak_line = Line([peak_x, -1.8, 0], [peak_x, 1.5, 0],
                         color=TEAL, stroke_width=2.5)
        peak_lbl = Text("most-likely: a0", font=DISPLAY, color=TEAL, font_size=24)
        peak_lbl.move_to([peak_x, 1.85, 0])

        # Mean line at 3a0/2 = 1.5*a0: r = 1.5*1.5 = 2.25 => x = -4.5 + 2.25*1.8 = -0.45
        mean_x = -4.5 + 2.25 * 1.8  # ~ -0.45
        mean_line = Line([mean_x, -1.8, 0], [mean_x, 1.0, 0],
                         color=SLATE, stroke_width=2.0)
        mean_lbl = Text("mean: 3a0/2", font=DISPLAY, color=SLATE, font_size=24)
        mean_lbl.move_to([mean_x + 1.0, 1.3, 0])

        note = Text("tail pulls average past the peak",
                    font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        note.move_to(DOWN * 2.8)

        x_lbl = Text("r", font=MONO, color=SLATE, font_size=22)
        x_lbl.next_to(axes_x, RIGHT, buff=0.15)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(Create(axes_x), Create(axes_y), FadeIn(x_lbl), run_time=0.6)
        self.play(Create(curve), run_time=1.0)
        self.play(Create(peak_line), run_time=0.6)
        self.play(FadeIn(peak_lbl), run_time=0.5)
        self.play(Create(mean_line), run_time=0.6)
        self.play(FadeIn(mean_lbl), run_time=0.5)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(total - 5.5)


# ── B09 — The Implication: two numbers means a cloud ─────────────────────────
class B09_TwoMeansCloud(Scene):
    def construct(self):
        total = _dur("B09", 17.0)
        eyebrow = LabelChip("the fingerprint of wave mechanics", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_bohr = Text("Bohr orbit:", font=MONO, color=CRIMSON, font_size=26)
        b1 = Text("one radius", font=DISPLAY, color=CRIMSON, font_size=34)
        b2 = Text("a path, not a cloud", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        bohr_grp = VGroup(col_bohr, b1, b2)
        bohr_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        bohr_grp.move_to(LEFT * 3.2 + UP * 0.4)

        vs = Text("vs", font=DISPLAY, color=SLATE, font_size=32)
        vs.move_to(ORIGIN)

        col_qm = Text("wave mechanics:", font=MONO, color=TEAL, font_size=26)
        q1 = Text("two radii", font=DISPLAY, color=TEAL, font_size=34)
        q2 = Text("a cloud, not a path", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        qm_grp = VGroup(col_qm, q1, q2)
        qm_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        qm_grp.move_to(RIGHT * 3.0 + UP * 0.4)

        note = Text("not a measurement limit. that is what the state is.",
                    font=MONO, color=TEAL, font_size=22)
        note.move_to(DOWN * 2.4)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(bohr_grp), run_time=0.8)
        self.play(FadeIn(vs), run_time=0.4)
        self.play(FadeIn(qm_grp), run_time=0.8)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(total - 3.5)


# ── B10 — THE EXAMPLE (illustrative): 1000 measurements ──────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 22.0)
        eyebrow = LabelChip("illustrative example", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        title = Text("A student measures the 1s electron position 1000 times",
                     font=DISPLAY, color=INK, font_size=28)
        title.move_to(UP * 2.3)

        result1 = Text("most common result:   ~1 Bohr radius (a0)",
                       font=MONO, color=TEAL, font_size=28)
        result1.move_to(UP * 1.0)

        result2 = Text("average of all 1000:   ~1.5 Bohr radii (3a0/2)",
                       font=MONO, color=TEAL, font_size=28)
        result2.move_to(UP * 0.2)

        diff = Text("0.5 a0 gap — not measurement error, not a quantum blur",
                    font=SERIF, color=INK, font_size=24, slant=ITALIC)
        diff.move_to(DOWN * 0.8)

        control = Text("same experiment on a Bohr orbit: both give the same r",
                       font=MONO, color=CRIMSON, font_size=24)
        control.move_to(DOWN * 1.9)

        note = Text("(illustrative)", font=MONO, color=SLATE, font_size=20)
        note.move_to(DOWN * 2.7)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(result1), run_time=0.6)
        self.play(FadeIn(result2), run_time=0.6)
        self.play(FadeIn(diff), run_time=0.6)
        self.play(FadeIn(control), run_time=0.6)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(total - 5.0)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 16.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.6)

        q_row = Text("Q: Why do most-likely and average radius disagree?",
                     font=SERIF, color=SLATE, font_size=26, slant=ITALIC)
        q_row.move_to(UP * 1.7)

        rule = Line(LEFT * 5.0 + UP * 1.05, RIGHT * 5.0 + UP * 1.05,
                    color=TEAL, stroke_width=1.5)

        a_row = Text("A: P(r) is right-skewed — peak at a0, mean at 3a0/2.",
                     font=DISPLAY, color=INK, font_size=30)
        a_sub = Text("Two radii where an orbit gives one. That is the cloud.",
                     font=SERIF, color=TEAL, font_size=27, slant=ITALIC)
        a_group = VGroup(a_row, a_sub)
        a_group.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        a_group.move_to(DOWN * 0.3)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q_row), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(a_row, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(a_sub, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)
