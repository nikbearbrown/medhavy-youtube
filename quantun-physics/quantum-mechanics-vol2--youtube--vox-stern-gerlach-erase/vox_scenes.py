"""vox_scenes.py — Why Measuring Sideways Erases What You Knew
(vox-stern-gerlach-erase, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = definite spin-up (first selection);
           CRIMSON = 50/50 split (result after intermediate x-measurement).
Exclusions: no commutator algebra, no Bloch-sphere formalism,
            hidden-variable as one-line contrast only.
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
        title = Text("Why Measuring Sideways", font=DISPLAY, color=INK, font_size=46)
        sub = Text("Erases What You Knew", font=SERIF, color=CRIMSON, font_size=40, slant=ITALIC)
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


# ── B02 — Cold open: first SG selects spin-up ───────────────────────────────
class B02_FirstSG(Scene):
    def construct(self):
        total = _dur("B02", 12.0)
        eyebrow = LabelChip("stage 1: up-down magnet", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Beam entering
        beam_in = Arrow(LEFT * 6.0 + UP * 0.0, LEFT * 3.5 + UP * 0.0,
                        color=SLATE, stroke_width=2.5, buff=0.1)
        in_lbl = Text("mixed beam", font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        in_lbl.move_to(LEFT * 5.5 + UP * 0.4)

        # Magnet box
        magnet = Rectangle(width=1.2, height=1.6).set_fill(SLATE, 0.15).set_stroke(SLATE, 2.0)
        magnet.move_to(LEFT * 2.8)
        mag_lbl = Text("SG_z", font=MONO, color=SLATE, font_size=22)
        mag_lbl.next_to(magnet, UP, buff=0.1)

        # Output beams
        out_up = Arrow(LEFT * 2.2 + UP * 0.0, LEFT * 0.5 + UP * 0.5,
                       color=TEAL, stroke_width=2.5, buff=0.1)
        up_lbl = LabelChip("spin-up  selected", accent=TEAL, size=20)
        up_lbl.move_to(RIGHT * 0.4 + UP * 0.7)

        out_dn = Arrow(LEFT * 2.2 + UP * 0.0, LEFT * 0.5 + DOWN * 0.5,
                       color=CRIMSON, stroke_width=2.5, buff=0.1)
        dn_lbl = LabelChip("spin-down  blocked", accent=CRIMSON, size=20)
        dn_lbl.move_to(RIGHT * 0.4 + DOWN * 0.7)

        result = Text("output: pure spin-up beam", font=MONO, color=TEAL, font_size=26)
        result.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(GrowArrow(beam_in), FadeIn(in_lbl), run_time=0.5)
        self.play(FadeIn(magnet), FadeIn(mag_lbl), run_time=0.5)
        self.play(GrowArrow(out_up), FadeIn(up_lbl), run_time=0.5)
        self.play(GrowArrow(out_dn), FadeIn(dn_lbl), run_time=0.5)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B03 — Cold open: sideways SG selects spin-left ──────────────────────────
class B03_SidewaysSG(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("stage 2: sideways magnet", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        in_lbl = LabelChip("pure spin-up beam enters", accent=TEAL, size=22)
        in_lbl.move_to(UP * 1.3 + LEFT * 2.5)

        mag2 = Rectangle(width=1.2, height=1.6).set_fill(SLATE, 0.15).set_stroke(SLATE, 2.0)
        mag2.move_to(ORIGIN + UP * 0.2)
        mag2_lbl = Text("SG_x", font=MONO, color=SLATE, font_size=22)
        mag2_lbl.next_to(mag2, UP, buff=0.1)

        out_left = Arrow(RIGHT * 0.6 + UP * 0.2, RIGHT * 2.5 + UP * 0.8,
                         color=TEAL, stroke_width=2.5, buff=0.1)
        left_lbl = LabelChip("spin-left  selected", accent=TEAL, size=20)
        left_lbl.move_to(RIGHT * 3.8 + UP * 1.0)

        out_right = Arrow(RIGHT * 0.6 + UP * 0.2, RIGHT * 2.5 + DOWN * 0.4,
                          color=CRIMSON, stroke_width=2.5, buff=0.1)
        right_lbl = LabelChip("spin-right  blocked", accent=CRIMSON, size=20)
        right_lbl.move_to(RIGHT * 3.8 + DOWN * 0.6)

        result = Text("output: pure spin-left beam", font=MONO, color=TEAL, font_size=26)
        result.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(in_lbl, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(mag2), FadeIn(mag2_lbl), run_time=0.5)
        self.play(GrowArrow(out_left), FadeIn(left_lbl), run_time=0.5)
        self.play(GrowArrow(out_right), FadeIn(right_lbl), run_time=0.5)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("Spin-up was definite after the first magnet.", font=DISPLAY,
                  color=INK, font_size=32)
        q2 = Text("The sideways magnet only sorted left/right.", font=DISPLAY,
                  color=SLATE, font_size=32)
        q3 = Text("Final up-down test gives 50/50", font=DISPLAY, color=CRIMSON, font_size=34)
        q4 = Text("instead of 100% up. Why?", font=SERIF, color=INK, font_size=32, slant=ITALIC)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        content.move_to(ORIGIN)
        rule = Line(LEFT * 4.5 + DOWN * 0.6, RIGHT * 4.5 + DOWN * 0.6,
                    color=SLATE, stroke_width=2.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(q3, shift=DOWN * 0.1), FadeIn(q4, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.wait(total - 4.0)


# ── B05 — THE PROBLEM: hidden-variable reading ───────────────────────────────
class B05_HiddenVariable(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE READING", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_hv = VGroup(
            LabelChip("hidden-variable model", accent=SLATE, size=22),
            Text("atoms carry pre-set up/down value", font=MONO, color=SLATE, font_size=24),
            Text("AND pre-set left/right value", font=MONO, color=SLATE, font_size=24),
            Text("like a coin with two faces", font=SERIF, color=SLATE, font_size=22, slant=ITALIC),
            Text("sideways magnet reads left/right", font=MONO, color=SLATE, font_size=24),
            Text("up/down face untouched", font=SERIF, color=SLATE, font_size=22, slant=ITALIC),
        )
        col_hv.arrange(DOWN, buff=0.25)
        col_hv.move_to(LEFT * 1.5 + DOWN * 0.0)

        prediction = LabelChip("prediction: final SG still all spin-up", accent=CRIMSON, size=22)
        prediction.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(col_hv[0]), run_time=0.5)
        self.play(FadeIn(col_hv[1]), FadeIn(col_hv[2]), run_time=0.6)
        self.play(FadeIn(col_hv[3]), run_time=0.5)
        self.play(FadeIn(col_hv[4]), FadeIn(col_hv[5]), run_time=0.6)
        self.play(FadeIn(prediction, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B06 — MECHANISM: up = superposition of left+right ────────────────────────
class B06_UpSuperposition(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("THE MECHANISM", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        heading = Text("Spin-up is a superposition:", font=DISPLAY, color=INK, font_size=30)
        heading.move_to(UP * 1.6)
        rule_h = Line(LEFT * 5.0 + UP * 1.15, RIGHT * 5.0 + UP * 1.15,
                      color=SLATE, stroke_width=1.5)

        eq = Text("|up>  =  (|left> + |right>) / sqrt(2)", font=MONO,
                  color=TEAL, font_size=32)
        eq.move_to(UP * 0.4)

        consequence = Text("sideways magnet selects |left>", font=MONO,
                           color=CRIMSON, font_size=28)
        consequence.move_to(DOWN * 0.5)

        note = SerifLabel("left and right are not separate from up and down", accent=TEAL, size=26)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(heading, shift=DOWN * 0.1), run_time=0.6)
        self.play(Create(rule_h), run_time=0.4)
        self.play(FadeIn(eq, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(consequence, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B07 — MECHANISM: left = superposition of up+down ─────────────────────────
class B07_LeftSuperposition(Scene):
    def construct(self):
        total = _dur("B07", 12.0)
        eyebrow = LabelChip("spin-left has no definite z-spin", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        eq = Text("|left>  =  (|up> + |down>) / sqrt(2)", font=MONO,
                  color=CRIMSON, font_size=32)
        eq.move_to(UP * 1.0)

        rule_m = Line(LEFT * 5.0 + UP * 0.4, RIGHT * 5.0 + UP * 0.4,
                      color=SLATE, stroke_width=1.5)

        consequence1 = Text("P(up) = 1/2  when measured along z", font=MONO,
                            color=CRIMSON, font_size=28)
        consequence1.move_to(DOWN * 0.1)

        consequence2 = Text("P(down) = 1/2  when measured along z", font=MONO,
                            color=CRIMSON, font_size=28)
        consequence2.move_to(DOWN * 0.8)

        note = Text("no z-information was erased — there was none to preserve",
                    font=SERIF, color=INK, font_size=24, slant=ITALIC)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(eq, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule_m), run_time=0.4)
        self.play(FadeIn(consequence1, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(consequence2, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B08 — MECHANISM: non-commuting operators share no state ──────────────────
class B08_NonCommuting(Scene):
    def construct(self):
        total = _dur("B08", 12.0)
        eyebrow = LabelChip("non-commuting operators", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_z = VGroup(
            LabelChip("S_z eigenstates", accent=TEAL, size=22),
            Text("|up> and |down>", font=MONO, color=TEAL, font_size=28),
            Text("definite z-spin", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
        )
        col_z.arrange(DOWN, buff=0.3)
        col_z.move_to(LEFT * 2.8 + DOWN * 0.2)

        col_x = VGroup(
            LabelChip("S_x eigenstates", accent=CRIMSON, size=22),
            Text("|left> and |right>", font=MONO, color=CRIMSON, font_size=28),
            Text("definite x-spin", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
        )
        col_x.arrange(DOWN, buff=0.3)
        col_x.move_to(RIGHT * 2.8 + DOWN * 0.2)

        div = Line(UP * 0.8, DOWN * 1.8, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        note = Text("S_x and S_z share no eigenstate — definite x always means indefinite z",
                    font=SERIF, color=INK, font_size=23, slant=ITALIC)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_z[0]), FadeIn(col_x[0]), run_time=0.6)
        self.play(FadeIn(col_z[1]), FadeIn(col_x[1]), run_time=0.6)
        self.play(FadeIn(col_z[2]), FadeIn(col_x[2]), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B09 — Implication: quantum info not stored, structurally erased ───────────
class B09_Implication(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        myth = VGroup(
            LabelChip("common phrase", accent=CRIMSON, size=22),
            Text("measurement disturbed the z-spin", font=MONO, color=CRIMSON, font_size=26),
            Text("by jostling the atom", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
        )
        myth.arrange(DOWN, buff=0.3)
        myth.move_to(LEFT * 2.8 + DOWN * 0.0)

        truth = VGroup(
            LabelChip("the truth", accent=TEAL, size=22),
            Text("spin-left has no z-spin to disturb", font=MONO, color=TEAL, font_size=26),
            Text("the state has no definite z", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
        )
        truth.arrange(DOWN, buff=0.3)
        truth.move_to(RIGHT * 2.8 + DOWN * 0.0)

        div = Line(UP * 0.8, DOWN * 1.8, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        note = SerifLabel("selecting a definite axis erases the other — not by disturbance but by definition", accent=TEAL, size=23)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(myth[0]), FadeIn(truth[0]), run_time=0.6)
        self.play(FadeIn(myth[1]), FadeIn(truth[1]), run_time=0.5)
        self.play(FadeIn(myth[2]), FadeIn(truth[2]), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B10 — THE EXAMPLE: with/without blocking ─────────────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        header = Text("Three-stage Stern-Gerlach experiment", font=DISPLAY,
                      color=INK, font_size=26)
        header.move_to(UP * 1.8)
        rule_top = Line(LEFT * 5.5 + UP * 1.4, RIGHT * 5.5 + UP * 1.4,
                        color=SLATE, stroke_width=1.5)

        row1 = VGroup(
            LabelChip("block spin-right", accent=CRIMSON, size=20),
            Text("final SG_z gives 50/50", font=MONO, color=CRIMSON, font_size=24),
        )
        row1.arrange(RIGHT, buff=0.5)
        row1.move_to(UP * 0.6)

        row2 = VGroup(
            LabelChip("block neither output", accent=TEAL, size=20),
            Text("final SG_z gives 100% up", font=MONO, color=TEAL, font_size=24),
        )
        row2.arrange(RIGHT, buff=0.5)
        row2.move_to(DOWN * 0.1)

        footer = SerifLabel("selecting one path collapses the state — passing both paths preserves it", accent=TEAL, size=23)
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
        line1 = Text("Spin-up  =  superposition of left + right.", font=MONO,
                     color=TEAL, font_size=24)
        line1.move_to(UP * 0.9)
        line2 = Text("Selecting left ->  no definite up/down.", font=MONO,
                     color=CRIMSON, font_size=24)
        line2.move_to(UP * 0.2)
        line3 = Text("Non-commuting operators share no eigenstate.", font=DISPLAY,
                     color=INK, font_size=24)
        line3.move_to(DOWN * 0.5)
        sub = Text("Not disturbed — structurally erased.", font=SERIF,
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
