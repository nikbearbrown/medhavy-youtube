"""vox_scenes.py — Why Two Electrons Avoid Each Other With No Force
(vox-exchange-avoidance, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. No STILL·ai slots.
Color law: TEAL = antisymmetric spatial state (parallel spins, node at coincidence, lower energy)
           CRIMSON = symmetric spatial state (opposite spins, enhanced overlap, higher energy)
Exclusions: no exchange-integral J/K formulas on screen, no Slater-determinant algebra,
            no spin-statistics-theorem proof.
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
        title = Text("Why Two Electrons Avoid", font=DISPLAY, color=INK, font_size=44)
        sub = Text("Each Other With No Force", font=SERIF, color=TEAL, font_size=40, slant=ITALIC)
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


# ── B02 — Cold open: oxygen is magnetic ──────────────────────────────────────
class B02_OxygenMagnetic(Scene):
    def construct(self):
        total = _dur("B02", 16.0)
        eyebrow = LabelChip("oxygen: 2 unpaired electrons", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two orbital boxes side by side
        box_w, box_h = 1.4, 1.0
        lbl_up = Text("2px", font=MONO, color=SLATE, font_size=24)
        lbl_mid = Text("2py", font=MONO, color=SLATE, font_size=24)
        lbl_dn = Text("2pz", font=MONO, color=SLATE, font_size=24)

        def orb_box(label, x_pos):
            box = Rectangle(width=box_w, height=box_h, color=SLATE, stroke_width=1.8)
            box.set_fill(GROUND, opacity=0.0)
            label.next_to(box, DOWN, buff=0.15)
            grp = VGroup(box, label)
            grp.move_to(x_pos)
            return grp

        orb1 = orb_box(lbl_up, LEFT * 2.5 + UP * 0.3)
        orb2 = orb_box(lbl_mid, ORIGIN + UP * 0.3)
        orb3 = orb_box(lbl_dn, RIGHT * 2.5 + UP * 0.3)

        # Arrows for parallel spins (all up, TEAL)
        def spin_arrow(orb, direction):
            tip = orb.get_center() + direction * 0.28
            base = orb.get_center() - direction * 0.28
            a = Arrow(base, tip, buff=0.0, color=TEAL,
                      stroke_width=3.0, max_tip_length_to_length_ratio=0.35)
            return a

        arrow1 = spin_arrow(orb1, UP)
        arrow2 = spin_arrow(orb2, UP)
        arrow3 = spin_arrow(orb3, UP)

        hunds_lbl = Text("Hund's rule: parallel spins fill first",
                         font=SERIF, color=INK, font_size=26, slant=ITALIC)
        hunds_lbl.move_to(DOWN * 2.2)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(orb1), FadeIn(orb2), FadeIn(orb3), run_time=0.8)
        self.play(FadeIn(arrow1), FadeIn(arrow2), FadeIn(arrow3), run_time=0.8)
        self.play(FadeIn(hunds_lbl), run_time=0.6)
        self.wait(total - 3.0)


# ── B03 — Cold open: no force in the equations ───────────────────────────────
class B03_NoForce(Scene):
    def construct(self):
        total = _dur("B03", 14.0)
        eyebrow = LabelChip("the Hamiltonian", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Show labeled terms as text blocks
        kinetic = Text("kinetic energy (electron 1)", font=MONO, color=SLATE, font_size=26)
        kinetic2 = Text("kinetic energy (electron 2)", font=MONO, color=SLATE, font_size=26)
        potential = Text("nuclear attraction (both)", font=MONO, color=SLATE, font_size=26)
        coulomb = Text("electron-electron repulsion", font=MONO, color=SLATE, font_size=26)
        nospin = Text("spin-spin force: ABSENT", font=DISPLAY, color=CRIMSON, font_size=30)

        terms = VGroup(kinetic, kinetic2, potential, coulomb)
        terms.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        terms.move_to(ORIGIN + UP * 0.4)
        nospin.move_to(DOWN * 2.1)

        self.play(FadeIn(eyebrow), run_time=0.4)
        for t in [kinetic, kinetic2, potential, coulomb]:
            self.play(FadeIn(t, shift=RIGHT * 0.15), run_time=0.5)
        self.play(FadeIn(nospin), run_time=0.7)
        self.wait(total - 4.0)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 15.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.to_corner(UL, buff=0.6)
        q = Text("Spin controls separation.", font=DISPLAY, color=INK, font_size=44)
        q2 = Text("No force does it.", font=DISPLAY, color=CRIMSON, font_size=44)
        ask = Text("Why?", font=SERIF, color=INK, font_size=48, slant=ITALIC)
        content = VGroup(q, q2, ask)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(ask), run_time=0.7)
        self.wait(total - 3.2)


# ── B05 — The Problem: magnetic repulsion too weak ───────────────────────────
class B05_MagneticTooWeak(Scene):
    def construct(self):
        total = _dur("B05", 17.0)
        eyebrow = LabelChip("naive guess", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        naive = Text("Maybe parallel spins repel like magnets?",
                     font=SERIF, color=INK, font_size=30, slant=ITALIC)
        naive.move_to(UP * 1.8)

        scale_lbl = Text("scale of electron magnetic-dipole interaction:",
                         font=MONO, color=SLATE, font_size=24)
        val_small = Text("~0.0001 eV", font=DISPLAY, color=CRIMSON, font_size=36)
        scale_lbl.move_to(UP * 0.4)
        val_small.move_to(DOWN * 0.35)

        vs_lbl = Text("scale of exchange splitting in helium:",
                      font=MONO, color=SLATE, font_size=24)
        val_big = Text("~0.80 eV  (10000x larger)", font=DISPLAY, color=TEAL, font_size=36)
        vs_lbl.move_to(DOWN * 1.3)
        val_big.move_to(DOWN * 2.1)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(naive), run_time=0.7)
        self.play(FadeIn(scale_lbl), run_time=0.5)
        self.play(FadeIn(val_small), run_time=0.6)
        self.play(FadeIn(vs_lbl), run_time=0.5)
        self.play(FadeIn(val_big), run_time=0.6)
        self.wait(total - 4.0)


# ── B06 — The Problem: indistinguishability ──────────────────────────────────
class B06_Indistinguishable(Scene):
    def construct(self):
        total = _dur("B06", 18.0)
        eyebrow = LabelChip("identical particles", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two overlapping circles (electron clouds)
        c1 = Circle(radius=1.2, color=TEAL, stroke_width=2.0)
        c1.set_fill(TEAL, opacity=0.15)
        c1.move_to(LEFT * 1.1)
        c2 = Circle(radius=1.2, color=CRIMSON, stroke_width=2.0)
        c2.set_fill(CRIMSON, opacity=0.15)
        c2.move_to(RIGHT * 1.1)

        lbl1 = Text("electron 1?", font=MONO, color=TEAL, font_size=24)
        lbl1.move_to(LEFT * 3.2 + UP * 0.0)
        lbl2 = Text("electron 2?", font=MONO, color=CRIMSON, font_size=24)
        lbl2.move_to(RIGHT * 3.2 + UP * 0.0)

        overlap_lbl = Text("no fact: which is which",
                           font=SERIF, color=INK, font_size=28, slant=ITALIC)
        overlap_lbl.move_to(DOWN * 2.2)

        combined = Text("one combined wavefunction",
                        font=DISPLAY, color=INK, font_size=30)
        combined.move_to(DOWN * 1.4)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(c1), FadeIn(c2), run_time=0.7)
        self.play(FadeIn(lbl1), FadeIn(lbl2), run_time=0.6)
        self.play(FadeIn(overlap_lbl), run_time=0.6)
        self.play(FadeIn(combined), run_time=0.6)
        self.wait(total - 3.5)


# ── B07 — The Mechanism: antisymmetry forces a node ──────────────────────────
class B07_AntisymmetryNode(Scene):
    def construct(self):
        total = _dur("B07", 20.0)
        eyebrow = LabelChip("antisymmetry requirement", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two rows: spin part + spatial part
        row_spin_par = Text("parallel spins   ->   spin part: SYMMETRIC",
                            font=MONO, color=INK, font_size=26)
        row_spatial_anti = Text("spatial part must be: ANTISYMMETRIC",
                                font=DISPLAY, color=TEAL, font_size=30)
        row_node = Text("antisymmetric f(r1, r2) = 0 when r1 = r2",
                        font=MONO, color=TEAL, font_size=26)

        arrow_down1 = Text("->", font=MONO, color=SLATE, font_size=30)
        arrow_down2 = Text("->", font=MONO, color=SLATE, font_size=30)

        col1 = VGroup(row_spin_par, arrow_down1, row_spatial_anti, arrow_down2, row_node)
        col1.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        col1.move_to(ORIGIN + UP * 0.3)

        note = Text("node: electrons can never coincide",
                    font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        note.move_to(DOWN * 2.4)

        self.play(FadeIn(eyebrow), run_time=0.4)
        for mob in [row_spin_par, arrow_down1, row_spatial_anti, arrow_down2, row_node]:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.55)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(total - 4.5)


# ── B08 — The Mechanism: joint probability map ───────────────────────────────
class B08_ProbabilityMap(Scene):
    def construct(self):
        total = _dur("B08", 20.0)
        eyebrow = LabelChip("joint probability: where are both electrons?", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Left panel: parallel spins (TEAL, node on diagonal)
        sq_size = 2.4
        left_sq = Square(side_length=sq_size, color=SLATE, stroke_width=1.5)
        left_sq.set_fill(GROUND, opacity=0.0)
        left_sq.move_to(LEFT * 3.2 + DOWN * 0.3)

        # Diagonal node line
        diag_node = Line(
            left_sq.get_corner(DL), left_sq.get_corner(UR),
            color=TEAL, stroke_width=2.5
        )

        left_title = Text("parallel spins", font=DISPLAY, color=TEAL, font_size=24)
        left_title.next_to(left_sq, UP, buff=0.2)
        node_lbl = Text("node: zero prob.", font=MONO, color=TEAL, font_size=20)
        node_lbl.next_to(left_sq, DOWN, buff=0.15)

        # Right panel: opposite spins (CRIMSON, enhanced diagonal)
        right_sq = Square(side_length=sq_size, color=SLATE, stroke_width=1.5)
        right_sq.set_fill(GROUND, opacity=0.0)
        right_sq.move_to(RIGHT * 3.2 + DOWN * 0.3)

        diag_high = Line(
            right_sq.get_corner(DL), right_sq.get_corner(UR),
            color=CRIMSON, stroke_width=4.5
        )

        right_title = Text("opposite spins", font=DISPLAY, color=CRIMSON, font_size=24)
        right_title.next_to(right_sq, UP, buff=0.2)
        pile_lbl = Text("pile-up: high prob.", font=MONO, color=CRIMSON, font_size=20)
        pile_lbl.next_to(right_sq, DOWN, buff=0.15)

        ax_lbl_l_x = Text("r1", font=MONO, color=SLATE, font_size=22)
        ax_lbl_l_y = Text("r2", font=MONO, color=SLATE, font_size=22)
        ax_lbl_l_x.next_to(left_sq, DOWN, buff=0.5)
        ax_lbl_l_y.next_to(left_sq, LEFT, buff=0.15)

        ax_lbl_r_x = Text("r1", font=MONO, color=SLATE, font_size=22)
        ax_lbl_r_y = Text("r2", font=MONO, color=SLATE, font_size=22)
        ax_lbl_r_x.next_to(right_sq, DOWN, buff=0.5)
        ax_lbl_r_y.next_to(right_sq, LEFT, buff=0.15)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(left_sq), FadeIn(right_sq), run_time=0.7)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.6)
        self.play(Create(diag_node), run_time=0.8)
        self.play(FadeIn(node_lbl), FadeIn(ax_lbl_l_x), FadeIn(ax_lbl_l_y), run_time=0.5)
        self.play(Create(diag_high), run_time=0.8)
        self.play(FadeIn(pile_lbl), FadeIn(ax_lbl_r_x), FadeIn(ax_lbl_r_y), run_time=0.5)
        self.wait(total - 5.5)


# ── B09 — The Mechanism: Coulomb consequence ─────────────────────────────────
class B09_CoulombConsequence(Scene):
    def construct(self):
        total = _dur("B09", 18.0)
        eyebrow = LabelChip("Coulomb repulsion depends on distance", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Chain of three labels
        step1 = Text("parallel spins  ->  antisymmetric spatial  ->  node at coincidence",
                     font=MONO, color=TEAL, font_size=24)
        step2 = Text("node  ->  electrons stay farther apart on average",
                     font=MONO, color=TEAL, font_size=24)
        step3 = Text("farther apart  ->  less Coulomb repulsion  ->  lower energy",
                     font=MONO, color=TEAL, font_size=24)

        vs_label = Text("vs", font=DISPLAY, color=SLATE, font_size=32)

        step4 = Text("opposite spins  ->  symmetric spatial  ->  pile-up at coincidence",
                     font=MONO, color=CRIMSON, font_size=24)
        step5 = Text("pile-up  ->  closer together  ->  more repulsion  ->  higher energy",
                     font=MONO, color=CRIMSON, font_size=24)

        teal_col = VGroup(step1, step2, step3)
        teal_col.arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        teal_col.move_to(UP * 1.5 + LEFT * 0.0)

        vs_label.move_to(ORIGIN + DOWN * 0.2)

        crim_col = VGroup(step4, step5)
        crim_col.arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        crim_col.move_to(DOWN * 1.5 + LEFT * 0.0)

        self.play(FadeIn(eyebrow), run_time=0.4)
        for mob in [step1, step2, step3]:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.55)
        self.play(FadeIn(vs_label), run_time=0.4)
        for mob in [step4, step5]:
            self.play(FadeIn(mob, shift=RIGHT * 0.1), run_time=0.55)
        self.wait(total - 4.5)


# ── B10 — The Implication: Hund's rule and oxygen ────────────────────────────
class B10_HundsRule(Scene):
    def construct(self):
        total = _dur("B10", 19.0)
        eyebrow = LabelChip("Hund's first rule", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        hunds = Text("Fill each orbital with one parallel-spin electron", font=SERIF,
                     color=INK, font_size=30, slant=ITALIC)
        hunds.move_to(UP * 2.0)

        # Oxygen filling: 3 orbitals, all spin-up (TEAL) then last one pairs
        box_labels = ["2px", "2py", "2pz"]
        orbs = []
        for i, lbl_txt in enumerate(box_labels):
            box = Rectangle(width=1.3, height=0.9, color=SLATE, stroke_width=1.5)
            box.set_fill(GROUND, opacity=0.0)
            lbl = Text(lbl_txt, font=MONO, color=SLATE, font_size=22)
            lbl.next_to(box, DOWN, buff=0.12)
            grp = VGroup(box, lbl)
            grp.move_to(LEFT * 2.0 + RIGHT * i * 2.0 + UP * 0.4)
            orbs.append(grp)

        arrows_teal = []
        for orb in orbs:
            arr = Arrow(orb.get_center() + DOWN * 0.22,
                        orb.get_center() + UP * 0.22,
                        buff=0.0, color=TEAL, stroke_width=3.0,
                        max_tip_length_to_length_ratio=0.35)
            arrows_teal.append(arr)

        reason = Text("exchange effect lowers energy  ->  oxygen is paramagnetic",
                      font=MONO, color=TEAL, font_size=24)
        reason.move_to(DOWN * 1.8)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(hunds), run_time=0.7)
        for o in orbs:
            self.play(FadeIn(o), run_time=0.4)
        for a in arrows_teal:
            self.play(FadeIn(a), run_time=0.4)
        self.play(FadeIn(reason), run_time=0.7)
        self.wait(total - 4.5)


# ── B11 — THE EXAMPLE (illustrative): 1D box ────────────────────────────────
class B11_Example(Scene):
    def construct(self):
        total = _dur("B11", 22.0)
        eyebrow = LabelChip("illustrative example", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        title = Text("Two electrons in a 1D box", font=DISPLAY, color=INK, font_size=34)
        title.move_to(UP * 2.3)

        # Left: parallel spins, TEAL
        left_lbl = Text("parallel spins", font=DISPLAY, color=TEAL, font_size=26)
        left_lbl.move_to(LEFT * 3.5 + UP * 1.2)

        # Box representing joint probability (schematic)
        left_box = Square(side_length=1.8, color=SLATE, stroke_width=1.5)
        left_box.set_fill(GROUND, opacity=0.0)
        left_box.move_to(LEFT * 3.5 + DOWN * 0.1)
        # Diagonal node
        l_node = Line(
            left_box.get_corner(DL), left_box.get_corner(UR),
            color=TEAL, stroke_width=2.5
        )
        left_note = Text("node on diagonal", font=MONO, color=TEAL, font_size=20)
        left_note.next_to(left_box, DOWN, buff=0.15)

        # Right: opposite spins, CRIMSON
        right_lbl = Text("opposite spins", font=DISPLAY, color=CRIMSON, font_size=26)
        right_lbl.move_to(RIGHT * 3.5 + UP * 1.2)

        right_box = Square(side_length=1.8, color=SLATE, stroke_width=1.5)
        right_box.set_fill(GROUND, opacity=0.0)
        right_box.move_to(RIGHT * 3.5 + DOWN * 0.1)
        r_diag = Line(
            right_box.get_corner(DL), right_box.get_corner(UR),
            color=CRIMSON, stroke_width=4.5
        )
        right_note = Text("pile-up on diagonal", font=MONO, color=CRIMSON, font_size=20)
        right_note.next_to(right_box, DOWN, buff=0.15)

        # Energy comparison
        energy_line = Text("energy difference in helium 1s2s: ~0.80 eV  (illustrative)",
                           font=MONO, color=SLATE, font_size=22)
        energy_line.move_to(DOWN * 2.4)

        self.play(FadeIn(eyebrow), run_time=0.4)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(left_lbl), FadeIn(right_lbl), run_time=0.6)
        self.play(FadeIn(left_box), FadeIn(right_box), run_time=0.6)
        self.play(Create(l_node), run_time=0.7)
        self.play(FadeIn(left_note), run_time=0.4)
        self.play(Create(r_diag), run_time=0.7)
        self.play(FadeIn(right_note), run_time=0.4)
        self.play(FadeIn(energy_line), run_time=0.6)
        self.wait(total - 6.5)


# ── B12 — RECAP endcard ──────────────────────────────────────────────────────
class B12_Endcard(Scene):
    def construct(self):
        total = _dur("B12", 18.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.6)

        q_row = Text("Q: Spin controls separation. No force does it. Why?",
                     font=SERIF, color=SLATE, font_size=26, slant=ITALIC)
        q_row.move_to(UP * 1.6)

        rule = Line(LEFT * 5.0 + UP * 0.95, RIGHT * 5.0 + UP * 0.95,
                    color=TEAL, stroke_width=1.5)

        a_row = Text("A: Antisymmetry carves a node at coincidence.",
                     font=DISPLAY, color=INK, font_size=32)
        a_sub = Text("Less Coulomb energy. No force needed.", font=SERIF,
                     color=TEAL, font_size=28, slant=ITALIC)
        a_group = VGroup(a_row, a_sub)
        a_group.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        a_group.move_to(DOWN * 0.4)

        kicker = Text("The exchange effect.", font=DISPLAY, color=CRIMSON, font_size=30)
        kicker.move_to(DOWN * 2.2)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(q_row), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(a_row, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(a_sub, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(kicker), run_time=0.6)
        self.wait(total - 4.2)
