"""vox_scenes.py — Why Matter Has Structure: Pauli as a Fact About Determinants
(vox-slater-zero, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL-ai slots.
Color law: TEAL = distinct orbitals (different columns, nonzero determinant, state exists)
           CRIMSON = identical orbitals (duplicate columns, determinant collapses to zero)
Exclusions: no N-particle expansion, no Hartree-Fock detour, no periodic-table filling rules.
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
        title = Text("Why Matter Has Structure:", font=DISPLAY, color=INK, font_size=40)
        sub = Text("Pauli as a Fact About Determinants",
                   font=SERIF, color=TEAL, font_size=38, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.5 + DOWN * 0.7, RIGHT * 5.5 + DOWN * 0.7,
                    color=CRIMSON, stroke_width=2.5)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: Pauli's postulate ───────────────────────────────────────
class B02_PauliPostulate(Scene):
    def construct(self):
        total = _dur("B02", 13.0)
        eyebrow = LabelChip("Pauli, 1925 — a postulate", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        rule_box = Rectangle(width=9.5, height=0.85, color=CRIMSON, stroke_width=2.5)
        rule_box.set_fill(GROUND, opacity=0.0)
        rule_box.move_to(UP * 1.4)
        rule_text = Text("no two electrons can share the same quantum numbers",
                         font=DISPLAY, color=CRIMSON, font_size=28)
        rule_text.move_to(UP * 1.4)

        context = Text("no derivation. explained the periodic table. kept it.",
                       font=MONO, color=SLATE, font_size=26)
        context.move_to(UP * 0.3)

        nobel = Text("Nobel Prize 1945 — partly for this rule",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        nobel.move_to(DOWN * 0.7)

        question = Text("but IS it a postulate, or a theorem?",
                        font=DISPLAY, color=TEAL, font_size=28)
        question.move_to(DOWN * 1.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(rule_text), Create(rule_box), run_time=0.8)
        self.play(FadeIn(context), run_time=0.6)
        self.play(FadeIn(nobel), run_time=0.5)
        self.play(FadeIn(question), run_time=0.6)
        self.wait(total - 4.5)


# ── B03 — Cold open: Slater's determinant ────────────────────────────────────
class B03_SlaterDeterminant(Scene):
    def construct(self):
        total = _dur("B03", 13.0)
        eyebrow = LabelChip("Slater, 1929 — a theorem", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        insight = Text("Write the 2-electron wave function as a grid:",
                       font=MONO, color=SLATE, font_size=26)
        insight.move_to(UP * 1.8)

        # 2x2 grid diagram (abstract)
        # Draw cells
        cell_w, cell_h = 2.2, 0.9
        cells = []
        labels = [["phi_a(r1)", "phi_b(r1)"],
                  ["phi_a(r2)", "phi_b(r2)"]]
        for row in range(2):
            for col in range(2):
                x = -1.2 + col * cell_w
                y = 0.4 - row * cell_h
                rect = Rectangle(width=cell_w - 0.1, height=cell_h - 0.1,
                                  color=TEAL, stroke_width=1.8)
                rect.set_fill(GROUND, opacity=0.0)
                rect.move_to(np.array([x, y, 0]))
                lbl = Text(labels[row][col], font=MONO, color=TEAL, font_size=22)
                lbl.move_to(np.array([x, y, 0]))
                cells.append(VGroup(rect, lbl))

        row_lbl1 = Text("particle 1", font=MONO, color=SLATE, font_size=20)
        row_lbl1.move_to(LEFT * 3.8 + UP * 0.4)
        row_lbl2 = Text("particle 2", font=MONO, color=SLATE, font_size=20)
        row_lbl2.move_to(LEFT * 3.8 + DOWN * 0.5)
        col_lbl1 = Text("orbital A", font=MONO, color=SLATE, font_size=20)
        col_lbl1.move_to(UP * 1.25 + LEFT * 1.2)
        col_lbl2 = Text("orbital B", font=MONO, color=SLATE, font_size=20)
        col_lbl2.move_to(UP * 1.25 + RIGHT * 1.0)

        det_label = Text("this grid is a determinant", font=DISPLAY, color=TEAL, font_size=26)
        det_label.move_to(DOWN * 1.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(insight), run_time=0.6)
        for cell in cells:
            self.play(FadeIn(cell), run_time=0.3)
        self.play(FadeIn(row_lbl1), FadeIn(row_lbl2),
                  FadeIn(col_lbl1), FadeIn(col_lbl2), run_time=0.5)
        self.play(FadeIn(det_label), run_time=0.5)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 12.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.to_corner(UL, buff=0.6)
        q = Text("Does a two-identical-column determinant", font=DISPLAY, color=INK, font_size=34)
        q2 = Text("really enforce the Pauli exclusion principle?", font=DISPLAY, color=CRIMSON, font_size=34)
        content = VGroup(q, q2)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        content.move_to(ORIGIN)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 2.5)


# ── B05 — Problem: antisymmetry is the real requirement ──────────────────────
class B05_Antisymmetry(Scene):
    def construct(self):
        total = _dur("B05", 14.0)
        eyebrow = LabelChip("the real requirement", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        req = Text("swap two electrons -> wave function flips sign",
                   font=DISPLAY, color=TEAL, font_size=30)
        req.move_to(UP * 1.5)

        box = Rectangle(width=9.0, height=0.85, color=TEAL, stroke_width=2.5)
        box.set_fill(GROUND, opacity=0.0)
        box.move_to(UP * 1.5)

        det_prop = Text("a determinant: swap rows -> sign flips",
                        font=MONO, color=TEAL, font_size=28)
        det_prop.move_to(UP * 0.4)

        consequence = Text("antisymmetry is built into the matrix structure",
                           font=MONO, color=TEAL, font_size=26)
        consequence.move_to(DOWN * 0.5)

        note = Text("exclusion principle follows — it is a corollary, not an axiom",
                    font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        note.move_to(DOWN * 1.6)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(req), Create(box), run_time=0.8)
        self.play(FadeIn(det_prop), run_time=0.6)
        self.play(FadeIn(consequence), run_time=0.5)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(total - 4.5)


# ── B06 — Mechanism: two-by-two, distinct orbitals ───────────────────────────
class B06_DistinctOrbitals(Scene):
    def construct(self):
        total = _dur("B06", 16.0)
        eyebrow = LabelChip("distinct orbitals: state exists", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        cell_w, cell_h = 2.2, 0.9
        cells = []
        labels = [["phi_a(r1)", "phi_b(r1)"],
                  ["phi_a(r2)", "phi_b(r2)"]]
        for row in range(2):
            for col in range(2):
                x = -1.2 + col * cell_w
                y = 0.6 - row * cell_h
                rect = Rectangle(width=cell_w - 0.1, height=cell_h - 0.1,
                                  color=TEAL, stroke_width=2.0)
                rect.set_fill(GROUND, opacity=0.0)
                rect.move_to(np.array([x, y, 0]))
                lbl = Text(labels[row][col], font=MONO, color=TEAL, font_size=22)
                lbl.move_to(np.array([x, y, 0]))
                cells.append(VGroup(rect, lbl))

        col_a = Text("orbital A", font=MONO, color=TEAL, font_size=20)
        col_a.move_to(UP * 1.5 + LEFT * 1.2)
        col_b = Text("orbital B", font=MONO, color=TEAL, font_size=20)
        col_b.move_to(UP * 1.5 + RIGHT * 1.0)

        divider_label = Text("columns differ:", font=MONO, color=SLATE, font_size=24)
        divider_label.move_to(RIGHT * 4.2 + UP * 0.6)
        det_nonzero = Text("det = NONZERO", font=DISPLAY, color=TEAL, font_size=30)
        det_nonzero.move_to(RIGHT * 4.2 + DOWN * 0.2)

        state_exists = Text("state exists", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        state_exists.move_to(DOWN * 2.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        for cell in cells:
            self.play(FadeIn(cell), run_time=0.32)
        self.play(FadeIn(col_a), FadeIn(col_b), run_time=0.5)
        self.play(FadeIn(divider_label), FadeIn(det_nonzero), run_time=0.6)
        self.play(FadeIn(state_exists), run_time=0.5)
        self.wait(total - 5.0)


# ── B07 — Mechanism: duplicate columns collapse to zero ──────────────────────
class B07_DuplicateCollapse(Scene):
    def construct(self):
        total = _dur("B07", 15.0)
        eyebrow = LabelChip("identical orbitals: determinant = 0", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Grid with identical columns
        cell_w, cell_h = 2.2, 0.9
        cells_start = []
        labels_same = [["phi_a(r1)", "phi_a(r1)"],
                       ["phi_a(r2)", "phi_a(r2)"]]
        for row in range(2):
            for col in range(2):
                x = -1.2 + col * cell_w
                y = 0.6 - row * cell_h
                rect = Rectangle(width=cell_w - 0.1, height=cell_h - 0.1,
                                  color=CRIMSON, stroke_width=2.0)
                rect.set_fill(GROUND, opacity=0.0)
                rect.move_to(np.array([x, y, 0]))
                lbl = Text(labels_same[row][col], font=MONO, color=CRIMSON, font_size=22)
                lbl.move_to(np.array([x, y, 0]))
                cells_start.append(VGroup(rect, lbl))

        col_a1 = Text("orbital A", font=MONO, color=CRIMSON, font_size=20)
        col_a1.move_to(UP * 1.5 + LEFT * 1.2)
        col_a2 = Text("orbital A", font=MONO, color=CRIMSON, font_size=20)
        col_a2.move_to(UP * 1.5 + RIGHT * 1.0)
        same_label = Text("(same!)", font=MONO, color=CRIMSON, font_size=20)
        same_label.move_to(UP * 1.5 + RIGHT * 2.8)

        result = Text("det = 0", font=DISPLAY, color=CRIMSON, font_size=46)
        result.move_to(RIGHT * 4.5 + UP * 0.3)

        zero_box = Rectangle(width=3.0, height=1.2, color=CRIMSON, stroke_width=3.0)
        zero_box.set_fill(GROUND, opacity=0.0)
        zero_box.move_to(RIGHT * 4.5 + UP * 0.3)

        note = Text("identically zero. everywhere. the state does not exist.",
                    font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        note.move_to(DOWN * 2.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        for cell in cells_start:
            self.play(FadeIn(cell), run_time=0.3)
        self.play(FadeIn(col_a1), FadeIn(col_a2), FadeIn(same_label), run_time=0.5)
        self.play(FadeIn(result), Create(zero_box), run_time=0.8)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(total - 5.0)


# ── B08 — Implication: no chemistry without it ───────────────────────────────
class B08_NoChemistry(Scene):
    def construct(self):
        total = _dur("B08", 15.0)
        eyebrow = LabelChip("what it prevents", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        without = Text("without exclusion:", font=MONO, color=CRIMSON, font_size=28)
        without.move_to(UP * 1.8)

        collapse = Text("every electron collapses to the lowest orbital",
                        font=DISPLAY, color=CRIMSON, font_size=28)
        collapse.move_to(UP * 0.9)

        result = Text("all atoms: hydrogen-sized spheres. no elements.",
                      font=MONO, color=CRIMSON, font_size=26)
        result.move_to(UP * 0.0)

        rule_line = Line(LEFT * 5.0 + DOWN * 0.5, RIGHT * 5.0 + DOWN * 0.5,
                         color=TEAL, stroke_width=1.5)

        with_excl = Text("with exclusion:", font=MONO, color=TEAL, font_size=28)
        with_excl.move_to(DOWN * 1.0)

        chem = Text("orbitals fill in order. distinct shells. chemistry.",
                    font=DISPLAY, color=TEAL, font_size=26)
        chem.move_to(DOWN * 1.9)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(without), run_time=0.5)
        self.play(FadeIn(collapse), run_time=0.6)
        self.play(FadeIn(result), run_time=0.5)
        self.play(Create(rule_line), run_time=0.4)
        self.play(FadeIn(with_excl), run_time=0.4)
        self.play(FadeIn(chem), run_time=0.6)
        self.wait(total - 4.5)


# ── B09 — THE EXAMPLE (illustrative): helium 1s^2 ────────────────────────────
class B09_Example(Scene):
    def construct(self):
        total = _dur("B09", 18.0)
        eyebrow = LabelChip("illustrative example", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        title = Text("A student writes the helium 1s^2 Slater determinant",
                     font=DISPLAY, color=INK, font_size=26)
        title.move_to(UP * 2.4)

        steps = [
            ("both electrons:", "in the 1s orbital (same quantum numbers)", CRIMSON),
            ("constructs grid:", "column 1 = phi_1s(r), column 2 = phi_1s(r)", CRIMSON),
            ("two identical columns:", "determinant is identically zero", CRIMSON),
            ("conclusion:", "state doesn't exist — not forbidden, just zero", TEAL),
            ("Pauli exclusion:", "is a theorem, not a postulate", TEAL),
        ]
        step_mobs = []
        for i, (label, text, color) in enumerate(steps):
            l_mob = Text(label, font=MONO, color=SLATE, font_size=21)
            t_mob = Text(text, font=MONO, color=color, font_size=21)
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
        total = _dur("B10", 14.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.6)

        q_row = Text("Q: Does a two-identical-column determinant enforce Pauli exclusion?",
                     font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        q_row.move_to(UP * 1.8)

        rule = Line(LEFT * 5.5 + UP * 1.15, RIGHT * 5.5 + UP * 1.15,
                    color=TEAL, stroke_width=1.5)

        a_row = Text("A: Yes. Identical columns make the determinant identically zero.",
                     font=DISPLAY, color=INK, font_size=26)
        a_sub = Text("Pauli exclusion is a theorem, not a postulate.",
                     font=SERIF, color=TEAL, font_size=30, slant=ITALIC)
        a_group = VGroup(a_row, a_sub)
        a_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        a_group.move_to(DOWN * 0.3)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q_row), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(a_row, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(a_sub, shift=UP * 0.1), run_time=0.7)
        self.wait(total - 4.0)
