"""vox_scenes.py — Measuring spin in one direction destroys what you knew about another
(vox-spin-measurement, slate cut, 16:9).
Color law: TEAL=known/definite spin; CRIMSON=scrambled/indefinite; GOLD=measurement axis.
Exclusions: no Pauli algebra derivation; no entanglement; no Bell inequalities.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _dur(bid, fallback=8.0):
    return DUR.get(bid, fallback)


def _bloch_sphere(center=ORIGIN, radius=1.8):
    """Draw a simplified Bloch sphere: circle + axes."""
    circ = Circle(radius=radius, color=SLATE, stroke_width=1.2, fill_opacity=0)
    circ.move_to(center)
    # z-axis (vertical)
    z_ax = Line(center + DOWN * radius, center + UP * (radius + 0.3),
                color=INK, stroke_width=1.2)
    # x-axis (horizontal)
    x_ax = Line(center + LEFT * (radius + 0.3), center + RIGHT * (radius + 0.3),
                color=INK, stroke_width=1.2)
    # Equator line (slightly tilted to look 3D)
    eq_pts = []
    for angle in np.linspace(0, 2 * np.pi, 80):
        x = center[0] + radius * np.cos(angle)
        y = center[1] + 0.3 * np.sin(angle)  # small y offset gives 3D illusion
        eq_pts.append(RIGHT * x + UP * y)
    eq = VMobject(color=SLATE, stroke_width=0.8, stroke_opacity=0.5)
    eq.set_points_as_corners(eq_pts)
    return VGroup(circ, z_ax, x_ax, eq)


def _bloch_vector(center, end_point, color=TEAL, stroke_width=3.0):
    """Arrow from center to end_point on Bloch sphere."""
    arr = Arrow(center, end_point, buff=0, stroke_width=stroke_width, color=color,
                max_tip_length_to_length_ratio=0.18)
    return arr


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Measuring spin in one\ndirection destroys what\nyou knew about another",
                        font=SERIF, color=INK, font_size=32, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B01") - 1.3)


# ── B02 CARD ──────────────────────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Measuring x destroys\nthe z information. Why?",
                        font=SERIF, color=INK, font_size=38, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — sigma_z and sigma_x matrices ───────────────────────────
class B03_PauliMatrices(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("The two operators: diagonal vs off-diagonal",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: sigma_z (diagonal)
        sz_box = Rectangle(width=3.0, height=1.8, color=TEAL, fill_opacity=0.07)
        sz_box.set_stroke(TEAL, width=1.5)
        sz_box.move_to(LEFT * 3.5 + UP * 1.2)
        sz_lbl = Text("σ_z =", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        sz_lbl.move_to(LEFT * 3.5 + UP * 2.2)
        sz_mat = Text("+1   0\n  0  −1", font=DISPLAY, color=TEAL, font_size=20)
        sz_mat.move_to(LEFT * 3.5 + UP * 1.2)
        self.play(Create(sz_box), FadeIn(sz_lbl), FadeIn(sz_mat), run_time=0.6)

        # State 3: sigma_x (off-diagonal)
        sx_box = Rectangle(width=3.0, height=1.8, color=CRIMSON, fill_opacity=0.07)
        sx_box.set_stroke(CRIMSON, width=1.5)
        sx_box.move_to(RIGHT * 3.5 + UP * 1.2)
        sx_lbl = Text("σ_x =", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC)
        sx_lbl.move_to(RIGHT * 3.5 + UP * 2.2)
        sx_mat = Text("0   +1\n+1   0", font=DISPLAY, color=CRIMSON, font_size=20)
        sx_mat.move_to(RIGHT * 3.5 + UP * 1.2)
        self.play(Create(sx_box), FadeIn(sx_lbl), FadeIn(sx_mat), run_time=0.6)

        # State 4: Eigenstates
        sep_line = Line(LEFT * 6.5 + UP * -0.3, RIGHT * 6.5 + UP * -0.3,
                        color=SLATE, stroke_width=0.8)
        self.play(Create(sep_line), run_time=0.4)
        zup_lbl = Text("|↑⟩ = (1,0)  eigenvalue +1 of σ_z",
                       font=DISPLAY, color=TEAL, font_size=18)
        zup_lbl.move_to(LEFT * 1.5 + UP * -1.0)
        self.play(FadeIn(zup_lbl), run_time=0.5)

        # State 5: x-eigenstate expressed in z-basis
        xup_lbl = Text("|+x⟩ = (1/√2)(|↑⟩ + |↓⟩)  eigenvalue +1 of σ_x",
                       font=DISPLAY, color=CRIMSON, font_size=17)
        xup_lbl.move_to(LEFT * 0.5 + UP * -2.0)
        self.play(FadeIn(xup_lbl), run_time=0.4)

        # State 6: Key insight highlight box
        insight_box = Rectangle(width=7.5, height=0.6, color=GOLD, fill_opacity=0.28)
        insight_box.set_stroke(GOLD, width=0)
        insight_box.move_to(UP * -3.0)
        xup_note = Text("x-eigenstate = SUPERPOSITION of z-eigenstates",
                        font=DISPLAY, color=INK, font_size=16, weight=BOLD)
        xup_note.move_to(UP * -3.0)
        self.play(FadeIn(insight_box), FadeIn(xup_note), run_time=0.5)

        self.wait(_dur("B03") - 3.4)


# ── B04 THE PROBLEM — superposition structure ────────────────────────────────
class B04_SuperpositionStructure(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("x-eigenstate is 50/50 in z-basis",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Step 1 — start in up_z
        step1_box = Rectangle(width=8.5, height=0.7, color=TEAL, fill_opacity=0.07)
        step1_box.set_stroke(TEAL, width=1.5)
        step1_box.move_to(UP * 2.1)
        step1_lbl = Text("Start: |↑_z⟩ = definite z-spin (+1)",
                         font=DISPLAY, color=TEAL, font_size=20)
        step1_lbl.move_to(UP * 2.1)
        self.play(Create(step1_box), FadeIn(step1_lbl), run_time=0.6)

        # State 3: Step 2 — measure x
        step2_box = Rectangle(width=8.5, height=0.7, color=CRIMSON, fill_opacity=0.07)
        step2_box.set_stroke(CRIMSON, width=1.5)
        step2_box.move_to(UP * 0.9)
        step2_lbl = Text("Measure x: collapse to |+x⟩ = (1/√2)|↑⟩ + (1/√2)|↓⟩",
                         font=DISPLAY, color=CRIMSON, font_size=18)
        step2_lbl.move_to(UP * 0.9)
        self.play(Create(step2_box), FadeIn(step2_lbl), run_time=0.5)

        # State 4: Step 3 — measure z again
        step3_box = Rectangle(width=8.5, height=0.7, color=CRIMSON, fill_opacity=0.07)
        step3_box.set_stroke(CRIMSON, width=1.5)
        step3_box.move_to(UP * -0.5)
        step3_lbl = Text("Measure z again: P(↑) = 1/2, P(↓) = 1/2  (random!)",
                         font=DISPLAY, color=CRIMSON, font_size=18)
        step3_lbl.move_to(UP * -0.5)
        self.play(Create(step3_box), FadeIn(step3_lbl), run_time=0.5)

        # State 5: The culprit box
        gold_bar = Rectangle(width=7.0, height=0.55, color=GOLD, fill_opacity=0.28)
        gold_bar.set_stroke(GOLD, width=0)
        gold_bar.move_to(UP * -2.0)
        culprit = Text("The x-collapse erased the z-information",
                       font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        culprit.move_to(UP * -2.0)
        self.play(FadeIn(gold_bar), FadeIn(culprit), run_time=0.5)

        self.wait(_dur("B04") - 2.6)


# ── B05 THE MECHANISM — commutator = non-zero ────────────────────────────────
class B05_Commutator(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("The commutator is the root cause",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Commutator equation
        comm_box = Rectangle(width=6.5, height=0.8, color=CRIMSON, fill_opacity=0.07)
        comm_box.set_stroke(CRIMSON, width=1.8)
        comm_box.move_to(UP * 1.8)
        comm_lbl = Text("[σ_x, σ_z] = σ_xσ_z − σ_zσ_x = −2iσ_y ≠ 0",
                        font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        comm_lbl.move_to(UP * 1.8)
        self.play(Create(comm_box), FadeIn(comm_lbl), run_time=0.6)

        # State 3: Consequence box
        cons_box = Rectangle(width=7.5, height=0.7, color=INK, fill_opacity=0.05)
        cons_box.set_stroke(INK, width=1.2)
        cons_box.move_to(UP * 0.5)
        cons_lbl = Text("Non-zero commutator → no shared eigenbasis",
                        font=DISPLAY, color=INK, font_size=22)
        cons_lbl.move_to(UP * 0.5)
        self.play(Create(cons_box), FadeIn(cons_lbl), run_time=0.6)

        # State 4: Consequence implication
        impl_box = Rectangle(width=7.5, height=0.7, color=TEAL, fill_opacity=0.07)
        impl_box.set_stroke(TEAL, width=1.5)
        impl_box.move_to(UP * -0.8)
        impl_lbl = Text("Definite x-spin → indefinite z-spin  (and vice versa)",
                        font=DISPLAY, color=TEAL, font_size=22)
        impl_lbl.move_to(UP * -0.8)
        self.play(Create(impl_box), FadeIn(impl_lbl), run_time=0.5)

        # State 5: Contrast with commuting operators
        comm2_box = Rectangle(width=7.5, height=0.65, color=SLATE, fill_opacity=0.06)
        comm2_box.set_stroke(SLATE, width=1.2)
        comm2_box.move_to(UP * -2.3)
        comm2_lbl = Text("Compare: commuting operators DO share eigenstates",
                         font=DISPLAY, color=SLATE, font_size=19)
        comm2_lbl.move_to(UP * -2.3)
        self.play(Create(comm2_box), FadeIn(comm2_lbl), run_time=0.5)

        self.wait(_dur("B05") - 2.7)


# ── B06 THE MECHANISM — Bloch sphere visualization ──────────────────────────
class B06_BlochSphere(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Bloch sphere: x-measurement pushes to equator",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        cx = LEFT * 1.5
        sphere_center = np.array([-1.5, 0, 0])
        sphere = _bloch_sphere(center=cx, radius=1.6)
        # Axis labels
        z_lbl = Text("z", font=SERIF, color=INK, font_size=18, slant=ITALIC)
        z_lbl.move_to(cx + UP * 2.0)
        x_lbl = Text("x", font=SERIF, color=INK, font_size=18, slant=ITALIC)
        x_lbl.move_to(cx + RIGHT * 1.9)

        self.play(Create(sphere), FadeIn(z_lbl), FadeIn(x_lbl), run_time=0.6)

        # State 2: Initial state — north pole
        north = cx + UP * 1.6
        state_dot0 = Dot(north, color=TEAL, radius=0.15)
        state_vec0 = _bloch_vector(cx, north, color=TEAL)
        state_lbl0 = Text("|↑_z⟩", font=SERIF, color=TEAL, font_size=20, slant=ITALIC)
        state_lbl0.move_to(north + RIGHT * 0.7 + UP * 0.2)
        self.play(FadeIn(state_dot0), Create(state_vec0), FadeIn(state_lbl0), run_time=0.6)

        # State 3: After x-measurement — equatorial point
        equator = cx + RIGHT * 1.6
        state_dot1 = Dot(equator, color=CRIMSON, radius=0.15)
        state_vec1 = _bloch_vector(cx, equator, color=CRIMSON)
        state_lbl1 = Text("|+x⟩", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        state_lbl1.move_to(equator + RIGHT * 0.7 + UP * 0.2)
        meas_note = Text("x-measurement\n→ equator", font=DISPLAY, color=CRIMSON, font_size=17)
        meas_note.move_to(RIGHT * 3.0 + UP * 1.5)
        self.play(
            Transform(state_dot0, state_dot1),
            Transform(state_vec0, state_vec1),
            FadeOut(state_lbl0), FadeIn(state_lbl1),
            FadeIn(meas_note),
            run_time=0.8,
        )

        # State 4: z-axis distance annotation
        z_dist_lbl = Text("Equatorial: equidistant\nfrom N and S poles",
                          font=DISPLAY, color=INK, font_size=17)
        z_dist_lbl.move_to(RIGHT * 3.0 + UP * -0.5)
        z_dist_box = Rectangle(width=3.5, height=1.0, color=SLATE, fill_opacity=0.07)
        z_dist_box.set_stroke(SLATE, width=1.0)
        z_dist_box.move_to(RIGHT * 3.0 + UP * -0.5)
        self.play(Create(z_dist_box), FadeIn(z_dist_lbl), run_time=0.5)

        # State 5: Arrow from equatorial to "50/50 z"
        prob_lbl = Text("z-measurement: 50/50", font=DISPLAY, color=CRIMSON,
                        font_size=18, weight=BOLD)
        prob_lbl.move_to(RIGHT * 3.0 + UP * -2.0)
        prob_box = Rectangle(width=3.5, height=0.6, color=CRIMSON, fill_opacity=0.08)
        prob_box.set_stroke(CRIMSON, width=1.5)
        prob_box.move_to(RIGHT * 3.0 + UP * -2.0)
        self.play(Create(prob_box), FadeIn(prob_lbl), run_time=0.5)

        self.wait(_dur("B06") - 3.5)


# ── B07 THE IMPLICATION — no shared eigenbasis ───────────────────────────────
class B07_NoSharedBasis(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Eigenbases rotated 90° relative to each other",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: z-eigenbasis on left
        z_box = Rectangle(width=4.0, height=2.2, color=TEAL, fill_opacity=0.07)
        z_box.set_stroke(TEAL, width=1.5)
        z_box.move_to(LEFT * 3.2 + UP * 0.8)
        z_title = Text("σ_z eigenbasis", font=DISPLAY, color=TEAL, font_size=19, weight=BOLD)
        z_title.move_to(LEFT * 3.2 + UP * 1.9)
        z_e1 = Text("|↑⟩ = (1, 0)", font=DISPLAY, color=TEAL, font_size=18)
        z_e1.move_to(LEFT * 3.2 + UP * 1.1)
        z_e2 = Text("|↓⟩ = (0, 1)", font=DISPLAY, color=TEAL, font_size=18)
        z_e2.move_to(LEFT * 3.2 + UP * 0.4)
        self.play(Create(z_box), FadeIn(z_title), FadeIn(z_e1), FadeIn(z_e2), run_time=0.6)

        # State 3: x-eigenbasis on right
        x_box = Rectangle(width=4.5, height=2.2, color=CRIMSON, fill_opacity=0.07)
        x_box.set_stroke(CRIMSON, width=1.5)
        x_box.move_to(RIGHT * 3.2 + UP * 0.8)
        x_title = Text("σ_x eigenbasis", font=DISPLAY, color=CRIMSON, font_size=19, weight=BOLD)
        x_title.move_to(RIGHT * 3.2 + UP * 1.9)
        x_e1 = Text("|+x⟩ = (1/√2)(|↑⟩+|↓⟩)", font=DISPLAY, color=CRIMSON, font_size=16)
        x_e1.move_to(RIGHT * 3.2 + UP * 1.1)
        x_e2 = Text("|−x⟩ = (1/√2)(|↑⟩−|↓⟩)", font=DISPLAY, color=CRIMSON, font_size=16)
        x_e2.move_to(RIGHT * 3.2 + UP * 0.4)
        self.play(Create(x_box), FadeIn(x_title), FadeIn(x_e1), FadeIn(x_e2), run_time=0.6)

        # State 4: Rotation arrow between bases
        rot_arrow = CurvedArrow(LEFT * 1.5 + UP * 0.8, RIGHT * 1.5 + UP * 0.8,
                                angle=np.pi / 3, color=SLATE, stroke_width=1.8)
        rot_lbl = Text("90° rotation\nin state space", font=DISPLAY, color=SLATE, font_size=16)
        rot_lbl.move_to(UP * 1.4)
        self.play(Create(rot_arrow), FadeIn(rot_lbl), run_time=0.5)

        # State 5: Conclusion
        concl_bar = Rectangle(width=9.0, height=0.6, color=GOLD, fill_opacity=0.28)
        concl_bar.set_stroke(GOLD, width=0)
        concl_bar.move_to(UP * -2.2)
        concl_lbl = Text("Definite in one basis = maximally uncertain in the other",
                         font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        concl_lbl.move_to(UP * -2.2)
        self.play(FadeIn(concl_bar), FadeIn(concl_lbl), run_time=0.5)

        self.wait(_dur("B07") - 2.7)


# ── B08 THE IMPLICATION — QKD application ────────────────────────────────────
class B08_QKDApplication(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Non-commutativity secures quantum cryptography",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Alice sends
        alice_box = Rectangle(width=5.0, height=0.7, color=TEAL, fill_opacity=0.07)
        alice_box.set_stroke(TEAL, width=1.5)
        alice_box.move_to(UP * 2.0)
        alice_lbl = Text("Alice: sends photons with definite z-polarization",
                         font=DISPLAY, color=TEAL, font_size=19)
        alice_lbl.move_to(UP * 2.0)
        self.play(Create(alice_box), FadeIn(alice_lbl), run_time=0.5)

        # State 3: Eavesdropper measures in wrong basis
        eve_box = Rectangle(width=5.0, height=0.7, color=CRIMSON, fill_opacity=0.07)
        eve_box.set_stroke(CRIMSON, width=1.5)
        eve_box.move_to(UP * 0.7)
        eve_lbl = Text("Eve: measures in x-basis, collapses state to ±x",
                       font=DISPLAY, color=CRIMSON, font_size=19)
        eve_lbl.move_to(UP * 0.7)
        self.play(Create(eve_box), FadeIn(eve_lbl), run_time=0.5)

        # State 4: Bob detects errors
        bob_box = Rectangle(width=5.0, height=0.7, color=SLATE, fill_opacity=0.07)
        bob_box.set_stroke(SLATE, width=1.5)
        bob_box.move_to(UP * -0.6)
        bob_lbl = Text("Bob: z-measurement now 50/50 — errors detected",
                       font=DISPLAY, color=SLATE, font_size=19)
        bob_lbl.move_to(UP * -0.6)
        self.play(Create(bob_box), FadeIn(bob_lbl), run_time=0.5)

        # State 5: Conclusion
        qkd_bar = Rectangle(width=8.0, height=0.55, color=GOLD, fill_opacity=0.28)
        qkd_bar.set_stroke(GOLD, width=0)
        qkd_bar.move_to(UP * -2.0)
        qkd_lbl = Text("Non-commutativity makes eavesdropping detectable",
                       font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        qkd_lbl.move_to(UP * -2.0)
        self.play(FadeIn(qkd_bar), FadeIn(qkd_lbl), run_time=0.5)

        self.wait(_dur("B08") - 2.5)


# ── B09 THE EXAMPLE — step-by-step probabilities ────────────────────────────
class B09_StepByStep(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Sequential measurements: all probabilities computed",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Step 1
        s1_box = Rectangle(width=8.5, height=0.65, color=TEAL, fill_opacity=0.07)
        s1_box.set_stroke(TEAL, width=1.5)
        s1_box.move_to(UP * 2.2)
        s1_lbl = Text("① Prepare |↑_z⟩: definite z-spin (+1), certain",
                      font=DISPLAY, color=TEAL, font_size=19)
        s1_lbl.move_to(UP * 2.2)
        self.play(Create(s1_box), FadeIn(s1_lbl), run_time=0.6)

        # State 3: Step 2
        s2_box = Rectangle(width=8.5, height=0.65, color=CRIMSON, fill_opacity=0.07)
        s2_box.set_stroke(CRIMSON, width=1.5)
        s2_box.move_to(UP * 1.0)
        s2_lbl = Text("② Measure x: P(+x) = 1/2, P(−x) = 1/2",
                      font=DISPLAY, color=CRIMSON, font_size=19)
        s2_lbl.move_to(UP * 1.0)
        self.play(Create(s2_box), FadeIn(s2_lbl), run_time=0.5)

        # State 4: Step 3
        s3_box = Rectangle(width=8.5, height=0.65, color=CRIMSON, fill_opacity=0.07)
        s3_box.set_stroke(CRIMSON, width=1.5)
        s3_box.move_to(UP * -0.2)
        s3_lbl = Text("③ Collapse to |+x⟩ = (1/√2)|↑⟩ + (1/√2)|↓⟩",
                      font=DISPLAY, color=CRIMSON, font_size=19)
        s3_lbl.move_to(UP * -0.2)
        self.play(Create(s3_box), FadeIn(s3_lbl), run_time=0.5)

        # State 5: Step 4 final measurement
        s4_box = Rectangle(width=8.5, height=0.65, color=CRIMSON, fill_opacity=0.07)
        s4_box.set_stroke(CRIMSON, width=1.5)
        s4_box.move_to(UP * -1.4)
        s4_lbl = Text("④ Measure z: P(↑) = 1/2, P(↓) = 1/2  (erased!)",
                      font=DISPLAY, color=CRIMSON, font_size=19, weight=BOLD)
        s4_lbl.move_to(UP * -1.4)
        self.play(Create(s4_box), FadeIn(s4_lbl), run_time=0.5)

        # Summary line
        summ_lbl = Text("Original z-information is irretrievably erased after step ②",
                        font=DISPLAY, color=INK, font_size=17)
        summ_lbl.move_to(UP * -2.8)
        self.play(FadeIn(summ_lbl), run_time=0.4)

        self.wait(_dur("B09") - 3.0)


# ── B10 CARD ──────────────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("[σₓ, σ_z] ≠ 0.\nNo shared eigenbasis.\nDefinite x = random z.",
                        font=SERIF, color=INK, font_size=34, line_spacing=1.25)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B10") - 1.3)
