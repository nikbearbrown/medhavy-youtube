"""vox_scenes.py — Why the Average Particle Stops Behaving Classically
(vox-ehrenfest-double-well, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = narrow packet (follows classical force, trustworthy average);
           CRIMSON = wide packet (split, stranded expectation value).
Exclusions: no Ehrenfest-equation derivation, no Heisenberg-picture algebra,
            no V''' error-term math.
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
        title = Text("Why the Average Particle", font=DISPLAY, color=INK, font_size=46)
        sub = Text("Stops Behaving Classically", font=SERIF, color=CRIMSON, font_size=40, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.5 + DOWN * 0.65, RIGHT * 5.5 + DOWN * 0.65,
                    color=TEAL, stroke_width=2.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: Ehrenfest theorem ──────────────────────────────────────
class B02_EhrenfestStatement(Scene):
    def construct(self):
        total = _dur("B02", 12.0)
        eyebrow = LabelChip("Ehrenfest's theorem", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_class = VGroup(
            LabelChip("classical particle", accent=SLATE, size=22),
            Text("position follows velocity", font=MONO, color=SLATE, font_size=26),
            Text("velocity changes by force", font=MONO, color=SLATE, font_size=26),
        )
        col_class.arrange(DOWN, buff=0.35)
        col_class.move_to(LEFT * 3.0 + DOWN * 0.2)

        col_qm = VGroup(
            LabelChip("wave packet", accent=TEAL, size=22),
            Text("average position follows", font=MONO, color=TEAL, font_size=26),
            Text("average velocity", font=MONO, color=TEAL, font_size=26),
            Text("average velocity changes by", font=MONO, color=TEAL, font_size=26),
            Text("average force", font=MONO, color=TEAL, font_size=26),
        )
        col_qm.arrange(DOWN, buff=0.25)
        col_qm.move_to(RIGHT * 3.0 + DOWN * 0.1)

        div = Line(UP * 1.2, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_class[0]), FadeIn(col_qm[0]), run_time=0.6)
        self.play(FadeIn(col_class[1]), FadeIn(col_qm[1]), run_time=0.5)
        self.play(FadeIn(col_class[2]), FadeIn(col_qm[2]), run_time=0.5)
        self.play(FadeIn(col_qm[3]), FadeIn(col_qm[4]), run_time=0.5)
        self.wait(total - 4.5)


# ── B03 — Cold open: narrow packet in double well ────────────────────────────
class B03_NarrowPacket(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("narrow packet", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Double-well schematic (two minima)
        well_lbl = Text("double well potential", font=SERIF, color=SLATE,
                        font_size=24, slant=ITALIC)
        well_lbl.move_to(UP * 1.6)

        left_min = LabelChip("left minimum", accent=TEAL, size=20)
        left_min.move_to(LEFT * 3.5 + UP * 0.3)

        right_min = LabelChip("right minimum", accent=TEAL, size=20)
        right_min.move_to(RIGHT * 3.5 + UP * 0.3)

        center_hill = Text("central hill", font=SERIF, color=SLATE,
                           font_size=22, slant=ITALIC)
        center_hill.move_to(ORIGIN + UP * 0.3)

        arrow_down = Arrow(LEFT * 3.5 + UP * 0.0, LEFT * 3.5 + DOWN * 0.8,
                           color=TEAL, stroke_width=2.5, buff=0.1)

        result = VGroup(
            LabelChip("result: narrow packet", accent=TEAL, size=22),
            Text("rolls to one minimum", font=MONO, color=TEAL, font_size=26),
            Text("average = actual location", font=MONO, color=TEAL, font_size=26),
        )
        result.arrange(DOWN, buff=0.3)
        result.move_to(DOWN * 1.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(well_lbl, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(left_min), FadeIn(right_min), FadeIn(center_hill), run_time=0.6)
        self.play(GrowArrow(arrow_down), run_time=0.5)
        self.play(FadeIn(result[0]), run_time=0.5)
        self.play(FadeIn(result[1]), FadeIn(result[2]), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("Wide packet splits into two lobes.", font=DISPLAY, color=INK, font_size=34)
        q2 = Text("Average position stalls at the hilltop", font=DISPLAY, color=CRIMSON, font_size=34)
        q3 = Text("where the particle is never found.", font=SERIF, color=INK, font_size=30, slant=ITALIC)
        q4 = Text("What went wrong?", font=DISPLAY, color=TEAL, font_size=38)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 4.5 + DOWN * 0.55, RIGHT * 4.5 + DOWN * 0.55,
                    color=SLATE, stroke_width=2.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), FadeIn(q3, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q4, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)


# ── B05 — THE PROBLEM: naive average tracks peak ─────────────────────────────
class B05_NaiveAverage(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE READING", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_expect = VGroup(
            LabelChip("expected behavior", accent=SLATE, size=22),
            Text("average should track", font=MONO, color=SLATE, font_size=26),
            Text("largest probability peak", font=MONO, color=SLATE, font_size=26),
            Text("or split 50/50 between lobes", font=SERIF, color=SLATE, font_size=24, slant=ITALIC),
        )
        col_expect.arrange(DOWN, buff=0.32)
        col_expect.move_to(LEFT * 2.6 + DOWN * 0.2)

        col_actual = VGroup(
            LabelChip("what actually happens", accent=CRIMSON, size=22),
            Text("average stalls at center", font=MONO, color=CRIMSON, font_size=26),
            Text("probability at center = 0", font=MONO, color=CRIMSON, font_size=26),
            Text("average lies about location", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
        )
        col_actual.arrange(DOWN, buff=0.32)
        col_actual.move_to(RIGHT * 2.6 + DOWN * 0.2)

        div = Line(UP * 1.0, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_expect[0]), FadeIn(col_actual[0]), run_time=0.6)
        self.play(FadeIn(col_expect[1]), FadeIn(col_actual[1]), run_time=0.5)
        self.play(FadeIn(col_expect[2]), FadeIn(col_actual[2]), run_time=0.5)
        self.play(FadeIn(col_expect[3]), FadeIn(col_actual[3]), run_time=0.6)
        self.wait(total - 4.5)


# ── B06 — MECHANISM: narrow packet, average force = force at average ──────────
class B06_NarrowMechanism(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("NARROW PACKET", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        head = Text("Ehrenfest:  average force  =  <-dV/dx>", font=MONO,
                    color=INK, font_size=26)
        head.move_to(UP * 1.6)
        rule_h = Line(LEFT * 5.0 + UP * 1.15, RIGHT * 5.0 + UP * 1.15,
                      color=SLATE, stroke_width=1.5)

        narrow_lbl = LabelChip("narrow packet: force barely varies across it", accent=TEAL, size=22)
        narrow_lbl.move_to(UP * 0.4)

        arrow_eq = Text("average force  ~  force at average position", font=MONO,
                        color=TEAL, font_size=26)
        arrow_eq.move_to(DOWN * 0.3)

        conclusion = VGroup(
            Text("classical mechanics applies", font=DISPLAY, color=TEAL, font_size=26),
            Text("average = where the particle actually is", font=SERIF,
                 color=TEAL, font_size=24, slant=ITALIC),
        )
        conclusion.arrange(DOWN, buff=0.25)
        conclusion.move_to(DOWN * 1.3)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(head, shift=DOWN * 0.1), run_time=0.6)
        self.play(Create(rule_h), run_time=0.4)
        self.play(FadeIn(narrow_lbl), run_time=0.6)
        self.play(FadeIn(arrow_eq, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(conclusion, shift=DOWN * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B07 — MECHANISM: wide packet, opposing forces ────────────────────────────
class B07_WideMechanism(Scene):
    def construct(self):
        total = _dur("B07", 12.0)
        eyebrow = LabelChip("WIDE PACKET", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two lobes pushing in opposite directions
        lobe_left = LabelChip("left lobe", accent=CRIMSON, size=22)
        lobe_left.move_to(LEFT * 3.5 + UP * 0.5)

        arr_right = Arrow(LEFT * 3.5 + UP * 0.1, LEFT * 1.5 + UP * 0.1,
                          color=TEAL, stroke_width=2.5, buff=0.1)
        force_left_lbl = Text("force points right", font=SERIF, color=TEAL,
                              font_size=22, slant=ITALIC)
        force_left_lbl.move_to(LEFT * 3.5 + DOWN * 0.15)

        lobe_right = LabelChip("right lobe", accent=CRIMSON, size=22)
        lobe_right.move_to(RIGHT * 3.5 + UP * 0.5)

        arr_left = Arrow(RIGHT * 3.5 + UP * 0.1, RIGHT * 1.5 + UP * 0.1,
                         color=TEAL, stroke_width=2.5, buff=0.1)
        force_right_lbl = Text("force points left", font=SERIF, color=TEAL,
                               font_size=22, slant=ITALIC)
        force_right_lbl.move_to(RIGHT * 3.5 + DOWN * 0.15)

        result = VGroup(
            Text("average of two opposite forces  ~  zero", font=MONO,
                 color=CRIMSON, font_size=26),
            Text("average position stalls at center", font=DISPLAY,
                 color=CRIMSON, font_size=26),
        )
        result.arrange(DOWN, buff=0.3)
        result.move_to(DOWN * 1.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(lobe_left), FadeIn(lobe_right), run_time=0.6)
        self.play(GrowArrow(arr_right), FadeIn(force_left_lbl), run_time=0.6)
        self.play(GrowArrow(arr_left), FadeIn(force_right_lbl), run_time=0.6)
        self.play(FadeIn(result, shift=DOWN * 0.1), run_time=0.7)
        self.wait(total - 4.5)


# ── B08 — MECHANISM: average is math, not location ───────────────────────────
class B08_AverageMath(Scene):
    def construct(self):
        total = _dur("B08", 12.0)
        eyebrow = LabelChip("average is a number, not a location", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_narrow = VGroup(
            LabelChip("narrow distribution", accent=TEAL, size=22),
            Text("one peak at x=x0", font=MONO, color=TEAL, font_size=26),
            Text("average ~ x0", font=MONO, color=TEAL, font_size=26),
            Text("average = where particle is", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
        )
        col_narrow.arrange(DOWN, buff=0.3)
        col_narrow.move_to(LEFT * 2.8 + DOWN * 0.2)

        col_wide = VGroup(
            LabelChip("wide split distribution", accent=CRIMSON, size=22),
            Text("two peaks at x=-a, x=+a", font=MONO, color=CRIMSON, font_size=26),
            Text("average = 0  (between peaks)", font=MONO, color=CRIMSON, font_size=26),
            Text("probability at x=0  =  0", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
        )
        col_wide.arrange(DOWN, buff=0.3)
        col_wide.move_to(RIGHT * 2.8 + DOWN * 0.2)

        div = Line(UP * 1.2, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_narrow[0]), FadeIn(col_wide[0]), run_time=0.6)
        self.play(FadeIn(col_narrow[1]), FadeIn(col_wide[1]), run_time=0.5)
        self.play(FadeIn(col_narrow[2]), FadeIn(col_wide[2]), run_time=0.5)
        self.play(FadeIn(col_narrow[3]), FadeIn(col_wide[3]), run_time=0.6)
        self.wait(total - 4.5)


# ── B09 — Implication: quantum != guaranteed classical path ───────────────────
class B09_Implication(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        myth = VGroup(
            LabelChip("common myth", accent=CRIMSON, size=22),
            Text("quantum particles follow classical paths", font=MONO,
                 color=CRIMSON, font_size=26),
            Text("described by Ehrenfest", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
        )
        myth.arrange(DOWN, buff=0.32)
        myth.move_to(LEFT * 2.6 + UP * 0.3)

        truth = VGroup(
            LabelChip("the truth", accent=TEAL, size=22),
            Text("NARROW packets follow classical paths", font=MONO,
                 color=TEAL, font_size=26),
            Text("wide packets do not have to", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
        )
        truth.arrange(DOWN, buff=0.32)
        truth.move_to(RIGHT * 2.6 + UP * 0.3)

        div = Line(UP * 1.2, DOWN * 1.6, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        note = SerifLabel("when the average lies, quantum reality has diverged from classical", accent=TEAL, size=24)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(myth[0]), FadeIn(truth[0]), run_time=0.6)
        self.play(FadeIn(myth[1]), FadeIn(truth[1]), run_time=0.5)
        self.play(FadeIn(myth[2]), FadeIn(truth[2]), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B10 — THE EXAMPLE: narrow vs wide starting packet ─────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        header = Text("Physicist studies two packets in a double well", font=DISPLAY,
                      color=INK, font_size=26)
        header.move_to(UP * 1.8)
        rule_top = Line(LEFT * 5.5 + UP * 1.4, RIGHT * 5.5 + UP * 1.4,
                        color=SLATE, stroke_width=1.5)

        row1 = VGroup(
            LabelChip("narrow start", accent=TEAL, size=20),
            Text("average rolls to left minimum", font=MONO, color=TEAL, font_size=24),
            Text("-> average tells truth", font=SERIF, color=TEAL, font_size=22, slant=ITALIC),
        )
        row1.arrange(RIGHT, buff=0.4)
        row1.move_to(UP * 0.6)

        row2 = VGroup(
            LabelChip("wide start", accent=CRIMSON, size=20),
            Text("average stalls at center hilltop", font=MONO, color=CRIMSON, font_size=24),
            Text("-> average is stranded", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC),
        )
        row2.arrange(RIGHT, buff=0.4)
        row2.move_to(DOWN * 0.1)

        footer = SerifLabel("both averages are correct — only one describes where the particle is", accent=TEAL, size=23)
        footer.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(header), Create(rule_top), run_time=0.6)
        self.play(FadeIn(row1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(row2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("Average force is not force at average position.", font=MONO,
                     color=INK, font_size=24)
        line1.move_to(UP * 0.9)
        line2 = Text("Wide packet: lobes push opposite ways.", font=MONO,
                     color=CRIMSON, font_size=24)
        line2.move_to(UP * 0.2)
        line3 = Text("Average stalls where the particle never is.", font=DISPLAY,
                     color=CRIMSON, font_size=24)
        line3.move_to(DOWN * 0.5)
        sub = Text("The average is real. The particle is not there.", font=SERIF,
                   color=INK, font_size=24, slant=ITALIC)
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
