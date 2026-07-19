"""vox_scenes.py — Why a Spin Flips Completely When You Whisper to It
(vox-rabi-oscillation, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = spin-up population; CRIMSON = spin-down population.
Exclusions: no eigenstate-expansion algebra, no interaction-picture, no pulse-area calculation.
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
        title = Text("Why a Spin Flips Completely", font=DISPLAY, color=INK, font_size=46)
        sub = Text("When You Whisper to It", font=SERIF, color=TEAL, font_size=40, slant=ITALIC)
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


# ── B02 — Cold open: NMR spin flip setup ─────────────────────────────────────
class B02_NMRSetup(Scene):
    def construct(self):
        total = _dur("B02", 11.0)
        eyebrow = LabelChip("NMR / MRI", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left: spin-up state
        col_up = VGroup(
            LabelChip("before pulse", accent=TEAL, size=22),
            Text("all spins: UP", font=MONO, color=TEAL, font_size=30),
            Text("P(up) = 1", font=MONO, color=TEAL, font_size=26),
        )
        col_up.arrange(DOWN, buff=0.4)
        col_up.move_to(LEFT * 3.2)

        # Right: spin-down state
        col_down = VGroup(
            LabelChip("after pi-pulse", accent=CRIMSON, size=22),
            Text("all spins: DOWN", font=MONO, color=CRIMSON, font_size=30),
            Text("P(up) = 0", font=MONO, color=CRIMSON, font_size=26),
        )
        col_down.arrange(DOWN, buff=0.4)
        col_down.move_to(RIGHT * 3.2)

        div = Line(UP * 1.5 + LEFT * 0.0, DOWN * 1.5, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        pulse_lbl = Text("resonant pulse", font=SERIF, color=SLATE, font_size=24, slant=ITALIC)
        pulse_lbl.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_up[0]), FadeIn(col_down[0]), run_time=0.6)
        self.play(FadeIn(col_up[1]), FadeIn(col_down[1]), run_time=0.6)
        self.play(FadeIn(col_up[2]), FadeIn(col_down[2]), run_time=0.6)
        self.play(FadeIn(pulse_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B03 — Cold open: sinusoidal population exchange ──────────────────────────
class B03_PopulationExchange(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("Rabi oscillation", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Population bars (static version of the slosh)
        bar_bg = Rectangle(width=8.0, height=0.8).set_stroke(SLATE, 1.0).set_fill(SLATE, 0.1)
        bar_bg.move_to(UP * 0.4)

        bar_up = Rectangle(width=8.0, height=0.8).set_stroke(TEAL, 0.0).set_fill(TEAL, 0.55)
        bar_up.move_to(UP * 0.4)
        bar_up_lbl = Text("P(up)", font=MONO, color=TEAL, font_size=26)
        bar_up_lbl.move_to(UP * 0.4 + LEFT * 4.5)

        bar_dn_bg = Rectangle(width=8.0, height=0.8).set_stroke(SLATE, 1.0).set_fill(SLATE, 0.1)
        bar_dn_bg.move_to(DOWN * 0.6)
        bar_dn = Rectangle(width=0.01, height=0.8).set_stroke(CRIMSON, 0.0).set_fill(CRIMSON, 0.55)
        bar_dn.move_to(DOWN * 0.6 + LEFT * 3.995)
        bar_dn_lbl = Text("P(down)", font=MONO, color=CRIMSON, font_size=26)
        bar_dn_lbl.move_to(DOWN * 0.6 + LEFT * 4.5)

        t_axis = Line(LEFT * 4.2 + DOWN * 1.6, RIGHT * 4.2 + DOWN * 1.6,
                      color=SLATE, stroke_width=1.5)
        t_lbl = Text("time", font=SERIF, color=SLATE, font_size=22)
        t_lbl.move_to(RIGHT * 3.8 + DOWN * 1.2)

        sum_note = Text("P(up) + P(down) = 1  always", font=MONO, color=INK, font_size=26)
        sum_note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(bar_bg), FadeIn(bar_dn_bg), run_time=0.5)
        self.play(FadeIn(bar_up_lbl), FadeIn(bar_dn_lbl), run_time=0.5)
        self.play(GrowFromEdge(bar_up, LEFT), run_time=0.8)
        self.play(GrowFromEdge(bar_dn, LEFT), run_time=0.8)
        self.play(Create(t_axis), FadeIn(t_lbl), run_time=0.5)
        self.play(FadeIn(sum_note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("A weak transverse field", font=DISPLAY, color=INK, font_size=36)
        q2 = Text("completely flips the spin.", font=DISPLAY, color=CRIMSON, font_size=36)
        q3 = Text("Small perturbation — maximum change.", font=SERIF,
                  color=INK, font_size=32, slant=ITALIC)
        q4 = Text("Why?", font=DISPLAY, color=TEAL, font_size=42)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 4.5 + DOWN * 0.5, RIGHT * 4.5 + DOWN * 0.5,
                    color=SLATE, stroke_width=2.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), FadeIn(q2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q3, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q4, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)


# ── B05 — THE PROBLEM: naive small-nudge model ────────────────────────────────
class B05_NaiveNudge(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE READING", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_small = VGroup(
            LabelChip("weak field", accent=SLATE, size=22),
            Text("small energy", font=MONO, color=SLATE, font_size=28),
            Text("small perturbation", font=SERIF, color=SLATE, font_size=26, slant=ITALIC),
            Text("small change to spin", font=SERIF, color=SLATE, font_size=26, slant=ITALIC),
        )
        col_small.arrange(DOWN, buff=0.35)
        col_small.move_to(LEFT * 2.5 + DOWN * 0.2)

        col_pred = VGroup(
            LabelChip("naive prediction", accent=CRIMSON, size=22),
            Text("spin wobbles slightly", font=MONO, color=CRIMSON, font_size=28),
            Text("P(up) dips to ~0.9", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC),
            Text("NOT zero", font=DISPLAY, color=CRIMSON, font_size=28),
        )
        col_pred.arrange(DOWN, buff=0.35)
        col_pred.move_to(RIGHT * 2.5 + DOWN * 0.2)

        div = Line(UP * 1.2, DOWN * 2.2, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_small[0]), FadeIn(col_pred[0]), run_time=0.6)
        self.play(FadeIn(col_small[1]), FadeIn(col_pred[1]), run_time=0.6)
        self.play(FadeIn(col_small[2]), FadeIn(col_pred[2]), run_time=0.6)
        self.play(FadeIn(col_small[3]), FadeIn(col_pred[3]), run_time=0.7)
        self.wait(total - 4.5)


# ── B06 — MECHANISM: field defines eigenstates = superpositions ───────────────
class B06_EigenstatesSuperpositions(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("THE MECHANISM", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        heading = Text("Transverse field eigenstates:", font=DISPLAY, color=INK, font_size=30)
        heading.move_to(UP * 1.5)

        rule_h = Line(LEFT * 5.0 + UP * 0.95, RIGHT * 5.0 + UP * 0.95,
                      color=SLATE, stroke_width=1.5)

        eig_plus = Text("|x+> = (|up> + |down>) / sqrt(2)", font=MONO, color=TEAL, font_size=28)
        eig_plus.move_to(UP * 0.3)

        eig_minus = Text("|x-> = (|up> - |down>) / sqrt(2)", font=MONO, color=TEAL, font_size=28)
        eig_minus.move_to(DOWN * 0.3)

        init_state = Text("initial |up> = (|x+> + |x->) / sqrt(2)", font=MONO,
                          color=INK, font_size=26)
        init_state.move_to(DOWN * 1.0)

        note = SerifLabel("spin-up is a mixture of BOTH eigenstates", accent=TEAL, size=26)
        note.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(heading), run_time=0.6)
        self.play(Create(rule_h), run_time=0.4)
        self.play(FadeIn(eig_plus, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(eig_minus, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(init_state), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B07 — MECHANISM: phases advance, beat grows ──────────────────────────────
class B07_PhaseBeat(Scene):
    def construct(self):
        total = _dur("B07", 11.0)
        eyebrow = LabelChip("phase beat", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two energy levels with phase clocks
        lbl_plus = LabelChip("|x+>  energy +E", accent=TEAL, size=22)
        lbl_plus.move_to(UP * 0.7 + LEFT * 2.0)

        lbl_minus = LabelChip("|x->  energy -E", accent=CRIMSON, size=22)
        lbl_minus.move_to(DOWN * 0.7 + LEFT * 2.0)

        phase_txt = Text("phases advance at different rates", font=SERIF,
                         color=INK, font_size=26, slant=ITALIC)
        phase_txt.move_to(RIGHT * 2.0 + DOWN * 0.5)

        beat_eq = Text("beat = (E+ - E-) / hbar = omega_0", font=MONO, color=TEAL, font_size=26)
        beat_eq.move_to(DOWN * 1.2)

        beat_note = Text("relative phase grows from 0 to pi over half period", font=SERIF,
                         color=TEAL, font_size=24, slant=ITALIC)
        beat_note.to_edge(DOWN, buff=0.85)

        sep_line = Line(LEFT * 5.5 + UP * 0.0, RIGHT * 5.5 + UP * 0.0,
                        color=SLATE, stroke_width=1.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(lbl_plus), run_time=0.6)
        self.play(FadeIn(lbl_minus), run_time=0.6)
        self.play(Create(sep_line), run_time=0.4)
        self.play(FadeIn(phase_txt), run_time=0.6)
        self.play(FadeIn(beat_eq, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(beat_note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B08 — MECHANISM: beat=pi → complete flip ─────────────────────────────────
class B08_BeatPiFlip(Scene):
    def construct(self):
        total = _dur("B08", 11.0)
        eyebrow = LabelChip("beat reaches pi", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Interference table
        col_label = VGroup(
            LabelChip("beat", accent=SLATE, size=22),
            Text("0", font=MONO, color=SLATE, font_size=26),
            Text("pi/2", font=MONO, color=SLATE, font_size=26),
            Text("pi", font=MONO, color=SLATE, font_size=26),
        )
        col_label.arrange(DOWN, buff=0.38)
        col_label.move_to(LEFT * 4.0)

        col_up = VGroup(
            LabelChip("P(up)", accent=TEAL, size=22),
            Text("1", font=MONO, color=TEAL, font_size=26),
            Text("1/2", font=MONO, color=TEAL, font_size=26),
            Text("0", font=MONO, color=TEAL, font_size=26),
        )
        col_up.arrange(DOWN, buff=0.38)
        col_up.move_to(LEFT * 0.5)

        col_dn = VGroup(
            LabelChip("P(down)", accent=CRIMSON, size=22),
            Text("0", font=MONO, color=CRIMSON, font_size=26),
            Text("1/2", font=MONO, color=CRIMSON, font_size=26),
            Text("1", font=MONO, color=CRIMSON, font_size=26),
        )
        col_dn.arrange(DOWN, buff=0.38)
        col_dn.move_to(RIGHT * 3.5)

        note = Text("complete flip: interference, not field strength", font=SERIF,
                    color=INK, font_size=24, slant=ITALIC)
        note.to_edge(DOWN, buff=0.85)

        # Table grid lines
        rule_hdr = Line(LEFT * 5.5 + UP * 0.55, RIGHT * 5.5 + UP * 0.55,
                        color=SLATE, stroke_width=1.5)
        div_v1 = Line(LEFT * 2.0 + UP * 1.2, LEFT * 2.0 + DOWN * 1.8,
                      color=SLATE, stroke_width=1.0)
        div_v2 = Line(RIGHT * 1.8 + UP * 1.2, RIGHT * 1.8 + DOWN * 1.8,
                      color=SLATE, stroke_width=1.0)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(rule_hdr), Create(div_v1), Create(div_v2), run_time=0.5)
        self.play(FadeIn(col_label[0]), FadeIn(col_up[0]), FadeIn(col_dn[0]), run_time=0.6)
        self.play(FadeIn(col_label[1]), FadeIn(col_up[1]), FadeIn(col_dn[1]), run_time=0.6)
        self.play(FadeIn(col_label[2]), FadeIn(col_up[2]), FadeIn(col_dn[2]), run_time=0.6)
        self.play(FadeIn(col_label[3]), FadeIn(col_up[3]), FadeIn(col_dn[3]), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 5.5)


# ── B09 — Implication: Rabi frequency = energy gap ───────────────────────────
class B09_RabiFrequency(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        eq = Text("omega_Rabi = energy_gap / hbar", font=MONO, color=TEAL, font_size=34)
        eq.move_to(UP * 1.0)

        rule_eq = Line(LEFT * 4.5 + UP * 0.4, RIGHT * 4.5 + UP * 0.4,
                       color=TEAL, stroke_width=1.5)

        col_weak = VGroup(
            LabelChip("weaker field", accent=SLATE, size=22),
            Text("smaller gap", font=MONO, color=SLATE, font_size=26),
            Text("slower oscillation", font=SERIF, color=SLATE, font_size=24, slant=ITALIC),
        )
        col_weak.arrange(DOWN, buff=0.35)
        col_weak.move_to(LEFT * 2.8 + DOWN * 0.8)

        col_amp = VGroup(
            LabelChip("amplitude = 100%", accent=TEAL, size=22),
            Text("always", font=MONO, color=TEAL, font_size=28),
            Text("field strength sets rate", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
        )
        col_amp.arrange(DOWN, buff=0.35)
        col_amp.move_to(RIGHT * 2.8 + DOWN * 0.8)

        div = Line(UP * 0.2, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN + DOWN * 0.9)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(eq, shift=DOWN * 0.1), run_time=0.8)
        self.play(Create(rule_eq), run_time=0.4)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_weak[0]), FadeIn(col_amp[0]), run_time=0.6)
        self.play(FadeIn(col_weak[1]), FadeIn(col_amp[1]), run_time=0.6)
        self.play(FadeIn(col_weak[2]), FadeIn(col_amp[2]), run_time=0.6)
        self.wait(total - 5.5)


# ── B10 — THE EXAMPLE: NMR pi-pulse ──────────────────────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 13.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        header = Text("NMR pi-pulse protocol", font=DISPLAY, color=INK, font_size=28)
        header.move_to(UP * 1.8)
        rule_top = Line(LEFT * 5.5 + UP * 1.4, RIGHT * 5.5 + UP * 1.4,
                        color=SLATE, stroke_width=1.5)

        step1 = VGroup(
            Text("1. spin starts UP  (P = 1)", font=MONO, color=TEAL, font_size=26),
        )
        step1.move_to(UP * 0.7)

        step2 = VGroup(
            Text("2. apply pulse for half-period", font=MONO, color=INK, font_size=26),
            Text("   beat reaches pi", font=MONO, color=INK, font_size=26),
        )
        step2.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        step2.move_to(DOWN * 0.05 + LEFT * 0.5)

        step3 = VGroup(
            Text("3. spin is now DOWN  (P = 0)", font=MONO, color=CRIMSON, font_size=26),
            Text("   complete inversion", font=MONO, color=CRIMSON, font_size=26),
        )
        step3.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        step3.move_to(DOWN * 1.1 + LEFT * 0.5)

        footer = Text("amplitude always 100% — the whisper was enough", font=SERIF,
                      color=TEAL, font_size=24, slant=ITALIC)
        footer.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(header), Create(rule_top), run_time=0.6)
        self.play(FadeIn(step1), run_time=0.6)
        self.play(FadeIn(step2), run_time=0.6)
        self.play(FadeIn(step3), run_time=0.7)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("Transverse field  defines  two eigenstates that beat.", font=MONO,
                     color=TEAL, font_size=24)
        line1.move_to(UP * 0.9)
        line2 = Text("Beat reaches pi  ->  complete flip.", font=MONO, color=CRIMSON, font_size=26)
        line2.move_to(UP * 0.2)
        line3 = Text("Rabi frequency = energy gap / hbar.", font=MONO, color=INK, font_size=24)
        line3.move_to(DOWN * 0.5)
        line4 = Text("Amplitude is always 100%. Field sets the rate.", font=DISPLAY,
                     color=TEAL, font_size=26)
        line4.move_to(DOWN * 1.2)
        sub = Text("The whisper was enough — the beat did the work.", font=SERIF,
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
