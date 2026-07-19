"""vox_scenes.py — Why One Minus Sign Lights Up the Whole Galaxy
(vox-21cm-singlet, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = singlet (minus sign, J=0, lower energy);
           CRIMSON = triplet (plus sign, J=1, higher energy, decays).
Exclusions: no CG-ladder construction, no hyperfine-Hamiltonian derivation,
            no full triplet enumeration.
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
        title = Text("Why One Minus Sign", font=DISPLAY, color=INK, font_size=50)
        sub = Text("Lights Up the Whole Galaxy", font=SERIF, color=TEAL, font_size=40, slant=ITALIC)
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


# ── B02 — Cold open: 21-cm in radio astronomy ────────────────────────────────
class B02_RadioAstronomy(Scene):
    def construct(self):
        total = _dur("B02", 12.0)
        eyebrow = LabelChip("21-CM LINE", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        freq_lbl = Text("frequency:", font=SERIF, color=INK, font_size=28, slant=ITALIC)
        freq_val = Text("1420 MHz", font=MONO, color=CRIMSON, font_size=38)
        freq_lbl.move_to(LEFT * 3.5 + UP * 1.2)
        freq_val.move_to(RIGHT * 1.0 + UP * 1.2)

        wave_lbl = Text("wavelength:", font=SERIF, color=INK, font_size=28, slant=ITALIC)
        wave_val = Text("21 cm", font=MONO, color=TEAL, font_size=38)
        wave_lbl.move_to(LEFT * 3.5 + UP * 0.3)
        wave_val.move_to(RIGHT * 1.0 + UP * 0.3)

        use_lbl = Text("maps spiral arms, passes through dust", font=SERIF,
                       color=INK, font_size=26, slant=ITALIC)
        use_lbl.move_to(DOWN * 0.7)

        voyager = Text("engraved on Voyager's golden record", font=SERIF,
                       color=SLATE, font_size=24, slant=ITALIC)
        voyager.move_to(DOWN * 1.4)

        rule = Line(LEFT * 5.5 + UP * 1.75, RIGHT * 5.5 + UP * 1.75,
                    color=SLATE, stroke_width=1.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(rule), run_time=0.4)
        self.play(FadeIn(freq_lbl), FadeIn(freq_val, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(wave_lbl), FadeIn(wave_val, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(use_lbl, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(voyager, shift=DOWN * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B03 — Cold open: triplet vs singlet setup ─────────────────────────────────
class B03_TripletSingletSetup(Scene):
    def construct(self):
        total = _dur("B03", 11.0)
        eyebrow = LabelChip("hydrogen ground state", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left: triplet
        trip_chip = LabelChip("triplet  (parallel)", accent=CRIMSON, size=22)
        trip_state = Text("(|up-dn> + |dn-up|) / sqrt(2)", font=MONO, color=CRIMSON, font_size=26)
        trip_lbl = Text("spins parallel", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        trip_col = VGroup(trip_chip, trip_state, trip_lbl)
        trip_col.arrange(DOWN, buff=0.35)
        trip_col.move_to(LEFT * 3.0 + DOWN * 0.2)

        # Right: singlet
        sing_chip = LabelChip("singlet  (antiparallel)", accent=TEAL, size=22)
        sing_state = Text("(|up-dn> - |dn-up|) / sqrt(2)", font=MONO, color=TEAL, font_size=26)
        sing_lbl = Text("spins antiparallel", font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        sing_col = VGroup(sing_chip, sing_state, sing_lbl)
        sing_col.arrange(DOWN, buff=0.35)
        sing_col.move_to(RIGHT * 3.0 + DOWN * 0.2)

        div = Line(UP * 0.8, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        sign_note = Text("only difference:  +  vs  -", font=DISPLAY, color=INK, font_size=28)
        sign_note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(trip_chip), FadeIn(sing_chip), run_time=0.6)
        self.play(FadeIn(trip_state), FadeIn(sing_state), run_time=0.7)
        self.play(FadeIn(trip_lbl), FadeIn(sing_lbl), run_time=0.6)
        self.play(FadeIn(sign_note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("The triplet and singlet differ by one sign.", font=DISPLAY, color=INK, font_size=34)
        q2 = Text("That sign changes the energy", font=DISPLAY, color=CRIMSON, font_size=34)
        q3 = Text("and produces the 21-cm photon.", font=SERIF, color=INK, font_size=30, slant=ITALIC)
        q4 = Text("Why?", font=DISPLAY, color=TEAL, font_size=42)
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


# ── B05 — THE PROBLEM: signs shouldn't matter ────────────────────────────────
class B05_NaiveSigns(Scene):
    def construct(self):
        total = _dur("B05", 12.0)
        eyebrow = LabelChip("NAIVE READING", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_same = VGroup(
            LabelChip("both states", accent=SLATE, size=22),
            Text("one spin up, one spin down", font=MONO, color=SLATE, font_size=26),
            Text("both normalized", font=SERIF, color=SLATE, font_size=24, slant=ITALIC),
            Text("same ingredients", font=SERIF, color=SLATE, font_size=24, slant=ITALIC),
        )
        col_same.arrange(DOWN, buff=0.32)
        col_same.move_to(LEFT * 2.6 + DOWN * 0.2)

        col_pred = VGroup(
            LabelChip("naive prediction", accent=CRIMSON, size=22),
            Text("behavior should be identical", font=MONO, color=CRIMSON, font_size=26),
            Text("or differ by an irrelevant phase", font=SERIF, color=CRIMSON, font_size=24,
                 slant=ITALIC),
            Text("sign rarely matters physically", font=SERIF, color=CRIMSON, font_size=24,
                 slant=ITALIC),
        )
        col_pred.arrange(DOWN, buff=0.32)
        col_pred.move_to(RIGHT * 2.6 + DOWN * 0.2)

        div = Line(UP * 1.0, DOWN * 2.2, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_same[0]), FadeIn(col_pred[0]), run_time=0.6)
        self.play(FadeIn(col_same[1]), FadeIn(col_pred[1]), run_time=0.6)
        self.play(FadeIn(col_same[2]), FadeIn(col_pred[2]), run_time=0.6)
        self.play(FadeIn(col_same[3]), FadeIn(col_pred[3]), run_time=0.6)
        self.wait(total - 4.5)


# ── B06 — MECHANISM: plus → J=1, minus → J=0 ────────────────────────────────
class B06_SignDeterminesJ(Scene):
    def construct(self):
        total = _dur("B06", 12.0)
        eyebrow = LabelChip("THE MECHANISM", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Plus state row
        plus_lbl = Text("+  :", font=DISPLAY, color=CRIMSON, font_size=34)
        plus_state = Text("(|up-dn> + |dn-up|) / sqrt(2)", font=MONO, color=CRIMSON, font_size=26)
        plus_j = LabelChip("total spin  J = 1", accent=CRIMSON, size=22)
        plus_row = VGroup(plus_lbl, plus_state, plus_j)
        plus_row.arrange(RIGHT, buff=0.4)
        plus_row.move_to(UP * 0.8)

        sep = Line(LEFT * 5.5 + UP * 0.15, RIGHT * 5.5 + UP * 0.15,
                   color=SLATE, stroke_width=1.0)

        # Minus state row
        minus_lbl = Text("-  :", font=DISPLAY, color=TEAL, font_size=34)
        minus_state = Text("(|up-dn> - |dn-up|) / sqrt(2)", font=MONO, color=TEAL, font_size=26)
        minus_j = LabelChip("total spin  J = 0", accent=TEAL, size=22)
        minus_row = VGroup(minus_lbl, minus_state, minus_j)
        minus_row.arrange(RIGHT, buff=0.4)
        minus_row.move_to(DOWN * 0.4)

        note = SerifLabel("same ingredients — the sign decides the spin", accent=SLATE, size=26)
        note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(plus_lbl), FadeIn(plus_state), run_time=0.7)
        self.play(GrowFromCenter(plus_j), run_time=0.5)
        self.play(Create(sep), run_time=0.4)
        self.play(FadeIn(minus_lbl), FadeIn(minus_state), run_time=0.7)
        self.play(GrowFromCenter(minus_j), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 5.0)


# ── B07 — MECHANISM: why sign determines J ───────────────────────────────────
class B07_WhySignDeterminesJ(Scene):
    def construct(self):
        total = _dur("B07", 12.0)
        eyebrow = LabelChip("operator action", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        header = Text("Total-spin operator acts on the states:", font=DISPLAY,
                      color=INK, font_size=28)
        header.move_to(UP * 1.6)
        rule_h = Line(LEFT * 5.0 + UP * 1.15, RIGHT * 5.0 + UP * 1.15,
                      color=SLATE, stroke_width=1.5)

        plus_row = VGroup(
            Text("PLUS state:", font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC),
            Text("exchange terms ADD UP  ->  J = 1", font=MONO, color=CRIMSON, font_size=26),
        )
        plus_row.arrange(RIGHT, buff=0.5)
        plus_row.move_to(UP * 0.4)

        minus_row = VGroup(
            Text("MINUS state:", font=SERIF, color=TEAL, font_size=26, slant=ITALIC),
            Text("exchange terms CANCEL  ->  J = 0", font=MONO, color=TEAL, font_size=26),
        )
        minus_row.arrange(RIGHT, buff=0.5)
        minus_row.move_to(DOWN * 0.4)

        concl = Text("The sign controls cancellation — the cancellation controls the spin.",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        concl.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(header, shift=DOWN * 0.1), run_time=0.6)
        self.play(Create(rule_h), run_time=0.4)
        self.play(FadeIn(plus_row, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(minus_row, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(concl, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B08 — MECHANISM: hyperfine energy levels ─────────────────────────────────
class B08_HyperfineEnergy(Scene):
    def construct(self):
        total = _dur("B08", 12.0)
        eyebrow = LabelChip("hyperfine energy", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Energy level diagram
        # Triplet (high) level
        trip_line = Line(LEFT * 2.5 + UP * 1.2, RIGHT * 2.5 + UP * 1.2,
                         color=CRIMSON, stroke_width=3.0)
        trip_chip = LabelChip("triplet  J=1  (higher energy)", accent=CRIMSON, size=22)
        trip_chip.next_to(trip_line, RIGHT, buff=0.3)

        # Singlet (low) level
        sing_line = Line(LEFT * 2.5 + DOWN * 0.8, RIGHT * 2.5 + DOWN * 0.8,
                         color=TEAL, stroke_width=3.0)
        sing_chip = LabelChip("singlet  J=0  (lower energy)", accent=TEAL, size=22)
        sing_chip.next_to(sing_line, RIGHT, buff=0.3)

        # Arrow showing photon emission
        photon_arr = Arrow(LEFT * 3.0 + UP * 1.1, LEFT * 3.0 + DOWN * 0.7,
                           color=INK, buff=0.1, stroke_width=2.5)
        photon_lbl = Text("21-cm photon", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        photon_lbl.next_to(photon_arr, LEFT, buff=0.25)

        gap_note = Text("gap = 5.87 x 10^-6 eV = 1420 MHz", font=MONO,
                        color=SLATE, font_size=24)
        gap_note.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(trip_line), FadeIn(trip_chip), run_time=0.7)
        self.play(Create(sing_line), FadeIn(sing_chip), run_time=0.7)
        self.play(GrowArrow(photon_arr), FadeIn(photon_lbl), run_time=0.7)
        self.play(FadeIn(gap_note, shift=UP * 0.1), run_time=0.6)
        self.wait(total - 4.5)


# ── B09 — Implication: tiny gap = long wavelength, penetrates dust ────────────
class B09_TinyGapLongWave(Scene):
    def construct(self):
        total = _dur("B09", 11.0)
        eyebrow = LabelChip("THE IMPLICATION", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        col_gap = VGroup(
            LabelChip("tiny energy gap", accent=SLATE, size=22),
            Text("5.87 x 10^-6 eV", font=MONO, color=SLATE, font_size=28),
            Text("long wavelength", font=SERIF, color=SLATE, font_size=24, slant=ITALIC),
            Text("21 cm radio wave", font=MONO, color=SLATE, font_size=28),
        )
        col_gap.arrange(DOWN, buff=0.3)
        col_gap.move_to(LEFT * 2.8 + DOWN * 0.1)

        col_result = VGroup(
            LabelChip("consequence", accent=TEAL, size=22),
            Text("passes through dust clouds", font=MONO, color=TEAL, font_size=26),
            Text("hydrogen is everywhere", font=SERIF, color=TEAL, font_size=24, slant=ITALIC),
            Text("the galaxy lights up", font=DISPLAY, color=TEAL, font_size=28),
        )
        col_result.arrange(DOWN, buff=0.3)
        col_result.move_to(RIGHT * 2.8 + DOWN * 0.1)

        div = Line(UP * 1.0, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_gap[0]), FadeIn(col_result[0]), run_time=0.6)
        self.play(FadeIn(col_gap[1]), FadeIn(col_result[1]), run_time=0.6)
        self.play(FadeIn(col_gap[2]), FadeIn(col_result[2]), run_time=0.6)
        self.play(FadeIn(col_gap[3]), FadeIn(col_result[3]), run_time=0.6)
        self.wait(total - 4.5)


# ── B10 — THE EXAMPLE: radio astronomer maps spiral arm ──────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 14.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        header = Text("Mapping the Milky Way at 21 cm", font=DISPLAY, color=INK, font_size=28)
        header.move_to(UP * 1.8)
        rule_top = Line(LEFT * 5.5 + UP * 1.4, RIGHT * 5.5 + UP * 1.4,
                        color=SLATE, stroke_width=1.5)

        step1 = Text("1. tune to 1420 MHz", font=MONO, color=TEAL, font_size=26)
        step1.move_to(UP * 0.75 + LEFT * 1.0)

        step2 = Text("2. detect peak: neutral hydrogen at a velocity", font=MONO,
                     color=INK, font_size=26)
        step2.move_to(UP * 0.15 + LEFT * 0.0)

        step3 = Text("3. map the spiral arm in a week", font=MONO, color=TEAL, font_size=26)
        step3.move_to(DOWN * 0.45 + LEFT * 0.5)

        step4 = Text("4. dust was invisible to optical — 21 cm passed right through",
                     font=MONO, color=CRIMSON, font_size=24)
        step4.move_to(DOWN * 1.05 + LEFT * 0.0)

        footer = SerifLabel("billions of triplet-to-singlet flips per second per cloud",
                            accent=TEAL, size=24)
        footer.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(header), Create(rule_top), run_time=0.6)
        self.play(FadeIn(step1, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(step2, shift=DOWN * 0.1), run_time=0.6)
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
        line1 = Text("Triplet  ( + ) :  J = 1  ->  higher energy.", font=MONO,
                     color=CRIMSON, font_size=26)
        line1.move_to(UP * 0.9)
        line2 = Text("Singlet  ( - ) :  J = 0  ->  lower energy.", font=MONO,
                     color=TEAL, font_size=26)
        line2.move_to(UP * 0.2)
        line3 = Text("The gap = one 21-cm photon.", font=DISPLAY, color=INK, font_size=28)
        line3.move_to(DOWN * 0.5)
        sub = Text("One minus sign — and the galaxy lights up.", font=SERIF,
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
