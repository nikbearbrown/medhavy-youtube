"""vox_scenes.py — Square the integral, spin it into polar coordinates
(vox-gaussian-polar, slate cut, 16:9).
Color law: TEAL=1D bell curve / x-direction; CRIMSON=2D surface / r-direction;
           GOLD=polar grid / rotation highlight fill; SLATE=axes/structure.
Exclusions: no error function, no Gamma function, no residues, no moment-generating
            function formalism. Squaring trick + polar rotation only.
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


def _axes_xy(x_length=8.0, y_length=3.0, color=SLATE):
    ax = Axes(
        x_range=(-3.5, 3.5, 1), y_range=(0, 1.2, 0.5),
        x_length=x_length, y_length=y_length,
        axis_config={"color": color, "stroke_width": 1.2, "include_tip": False,
                     "include_ticks": False},
    )
    return ax


def _gaussian(x_vals):
    return np.exp(-x_vals ** 2)


def _bell_curve(ax, color=TEAL, stroke_width=2.5, n_pts=200, fill=True):
    x_vals = np.linspace(-3.5, 3.5, n_pts)
    y_vals = _gaussian(x_vals)
    pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_vals)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners(pts)
    if fill:
        # Build a filled region under the curve
        fill_pts = list(pts) + [ax.c2p(3.5, 0), ax.c2p(-3.5, 0)]
        region = Polygon(*fill_pts, color=color, fill_opacity=0.18, stroke_width=0)
        return VGroup(curve, region)
    return curve


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("You can't integrate e^(-x2) directly.\nSquare it. Rotate.",
                        font=SERIF, color=INK, font_size=26, line_spacing=1.3)
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
        headline = Text("How do you compute\nint e^{-x2} dx\nwhen it has no antiderivative?",
                        font=SERIF, color=INK, font_size=28, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — 1D bell curve ──────────────────────────────────────────
class B03_BellCurveProblem(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("I = int e^{-x2} dx: finite area, no closed form",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Axes
        ax = _axes_xy()
        ax.move_to(UP * 0.2)
        x_lbl = Text("x", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        x_lbl.move_to(ax.c2p(4.0, 0.0))
        self.play(Create(ax), FadeIn(x_lbl), run_time=0.4)

        # State 3: Bell curve with fill
        bell = _bell_curve(ax, color=TEAL, fill=True)
        self.play(Create(bell), run_time=0.7)

        # State 4: I label
        i_box = Rectangle(width=3.8, height=0.65, color=TEAL, fill_opacity=0.08)
        i_box.set_stroke(TEAL, width=1.5)
        i_box.move_to(RIGHT * 3.5 + UP * 2.5)
        i_lbl = Text("I = int e^{-x2} dx", font=DISPLAY, color=TEAL, font_size=20)
        i_lbl.move_to(RIGHT * 3.5 + UP * 2.5)
        self.play(Create(i_box), FadeIn(i_lbl), run_time=0.4)

        # State 5: "no elementary antiderivative" note
        note_box = Rectangle(width=6.0, height=0.6, color=SLATE, fill_opacity=0.07)
        note_box.set_stroke(SLATE, width=1.2)
        note_box.move_to(DOWN * 2.2)
        note_lbl = Text("no elementary antiderivative", font=DISPLAY, color=SLATE, font_size=19)
        note_lbl.move_to(DOWN * 2.2)
        self.play(Create(note_box), FadeIn(note_lbl), run_time=0.4)

        self.wait(_dur("B03") - 2.4)


# ── B04 THE PROBLEM — squaring trick ─────────────────────────────────────────
class B04_SquaringTrick(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Multiply I by itself using a fresh variable y",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: I squared product form
        prod_box = Rectangle(width=9.0, height=0.75, color=TEAL, fill_opacity=0.07)
        prod_box.set_stroke(TEAL, width=1.8)
        prod_box.move_to(UP * 2.2)
        prod_lbl = Text("I2 = (int e^{-x2} dx)(int e^{-y2} dy)",
                        font=DISPLAY, color=TEAL, font_size=21)
        prod_lbl.move_to(UP * 2.2)
        self.play(Create(prod_box), FadeIn(prod_lbl), run_time=0.6)

        # State 3: Arrow and "independent variables" label
        arrow = Arrow(UP * 1.6, UP * 0.9, buff=0, color=INK, stroke_width=2.0,
                      max_tip_length_to_length_ratio=0.2)
        indep_lbl = Text("x and y are independent", font=DISPLAY, color=SLATE, font_size=18)
        indep_lbl.move_to(RIGHT * 3.0 + UP * 1.3)
        self.play(Create(arrow), FadeIn(indep_lbl), run_time=0.4)

        # State 4: Double integral form
        dbl_box = Rectangle(width=9.0, height=0.75, color=CRIMSON, fill_opacity=0.07)
        dbl_box.set_stroke(CRIMSON, width=1.8)
        dbl_box.move_to(UP * 0.3)
        dbl_lbl = Text("I2 = int int e^{-(x2+y2)} dx dy",
                       font=DISPLAY, color=CRIMSON, font_size=21)
        dbl_lbl.move_to(UP * 0.3)
        self.play(Create(dbl_box), FadeIn(dbl_lbl), run_time=0.6)

        # State 5: Insight bar — x2+y2 is distance from origin
        insight_bar = Rectangle(width=9.5, height=0.6, color=GOLD, fill_opacity=0.22)
        insight_bar.set_stroke(GOLD, width=0)
        insight_bar.move_to(DOWN * 1.8)
        insight_lbl = Text("exponent x2+y2 = distance from origin squared",
                           font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        insight_lbl.move_to(DOWN * 1.8)
        self.play(FadeIn(insight_bar), FadeIn(insight_lbl), run_time=0.4)

        self.wait(_dur("B04") - 2.7)


# ── B05 THE MECHANISM — polar substitution ───────────────────────────────────
class B05_PolarSubstitution(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("x2+y2 = r2: switch to polar coordinates",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Cartesian circle (left panel)
        cart_rect = Rectangle(width=4.5, height=3.4, color=SLATE, fill_opacity=0.05)
        cart_rect.set_stroke(SLATE, width=1.2)
        cart_rect.move_to(LEFT * 3.0 + UP * 0.5)
        cart_lbl = Text("Cartesian", font=DISPLAY, color=SLATE, font_size=17, weight=BOLD)
        cart_lbl.move_to(LEFT * 3.0 + UP * 2.0)
        cart_circle = Circle(radius=0.9, color=SLATE, stroke_width=1.5, fill_opacity=0)
        cart_circle.move_to(LEFT * 3.0 + UP * 0.4)
        r_lbl = Text("x2+y2 = r2", font=DISPLAY, color=SLATE, font_size=16)
        r_lbl.move_to(LEFT * 3.0 + DOWN * 0.8)
        self.play(Create(cart_rect), FadeIn(cart_lbl), Create(cart_circle), FadeIn(r_lbl), run_time=0.5)

        # State 3: Polar fan (right panel)
        polar_rect = Rectangle(width=4.5, height=3.4, color=GOLD, fill_opacity=0.07)
        polar_rect.set_stroke(GOLD, width=1.5)
        polar_rect.move_to(RIGHT * 3.0 + UP * 0.5)
        polar_lbl = Text("Polar", font=DISPLAY, color=SLATE, font_size=17, weight=BOLD)
        polar_lbl.move_to(RIGHT * 3.0 + UP * 2.0)
        # Draw simple polar grid: arc and radial line
        polar_arc = Arc(radius=0.9, start_angle=0, angle=PI / 3,
                        color=GOLD, stroke_width=2.0)
        polar_arc.move_to(RIGHT * 3.0 + UP * 0.4)
        polar_radial = Line(RIGHT * 3.0 + UP * 0.4, RIGHT * 3.0 + UP * 0.4 + RIGHT * 0.9,
                            color=CRIMSON, stroke_width=2.0)
        r_polar_lbl = Text("r", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        r_polar_lbl.move_to(RIGHT * 3.5 + UP * 0.55)
        theta_lbl = Text("theta", font=SERIF, color=SLATE, font_size=16, slant=ITALIC)
        theta_lbl.move_to(RIGHT * 3.0 + UP * 1.0)
        self.play(Create(polar_rect), FadeIn(polar_lbl), Create(polar_arc),
                  Create(polar_radial), FadeIn(r_polar_lbl), FadeIn(theta_lbl), run_time=0.6)

        # State 4: Arrow between panels
        arrow_mid = Arrow(LEFT * 0.8 + UP * 0.5, RIGHT * 0.8 + UP * 0.5,
                          buff=0, color=INK, stroke_width=2.0,
                          max_tip_length_to_length_ratio=0.2)
        sub_lbl = Text("x = r cos(theta)\ny = r sin(theta)", font=DISPLAY, color=INK, font_size=15)
        sub_lbl.move_to(UP * 1.2)
        self.play(Create(arrow_mid), FadeIn(sub_lbl), run_time=0.4)

        # State 5: Area element
        area_bar = Rectangle(width=9.5, height=0.65, color=CRIMSON, fill_opacity=0.09)
        area_bar.set_stroke(CRIMSON, width=1.8)
        area_bar.move_to(DOWN * 2.2)
        area_lbl = Text("area element: dx dy = r dr d(theta)", font=DISPLAY, color=CRIMSON, font_size=20)
        area_lbl.move_to(DOWN * 2.2)
        self.play(Create(area_bar), FadeIn(area_lbl), run_time=0.4)

        self.wait(_dur("B05") - 2.9)


# ── B06 THE MECHANISM — computing I^2 = pi ───────────────────────────────────
class B06_ComputingISquared(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Polar form factors: theta integral * r integral",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Polar integral form
        step1_box = Rectangle(width=9.5, height=0.75, color=CRIMSON, fill_opacity=0.07)
        step1_box.set_stroke(CRIMSON, width=1.8)
        step1_box.move_to(UP * 2.2)
        step1_lbl = Text("I2 = (int_0^{2pi} d(theta)) * (int_0^inf e^{-r2} r dr)",
                         font=DISPLAY, color=CRIMSON, font_size=20)
        step1_lbl.move_to(UP * 2.2)
        self.play(Create(step1_box), FadeIn(step1_lbl), run_time=0.5)

        # State 3: Theta integral = 2pi
        th_box = Rectangle(width=5.5, height=0.65, color=SLATE, fill_opacity=0.07)
        th_box.set_stroke(SLATE, width=1.2)
        th_box.move_to(LEFT * 2.5 + UP * 1.0)
        th_lbl = Text("theta integral = 2*pi", font=DISPLAY, color=SLATE, font_size=19)
        th_lbl.move_to(LEFT * 2.5 + UP * 1.0)
        self.play(Create(th_box), FadeIn(th_lbl), run_time=0.4)

        # State 4: r integral with substitution
        r_box = Rectangle(width=7.5, height=0.65, color=CRIMSON, fill_opacity=0.07)
        r_box.set_stroke(CRIMSON, width=1.5)
        r_box.move_to(UP * 0.0)
        r_lbl = Text("u = r2: int_0^inf e^{-r2} r dr = (1/2) int_0^inf e^{-u} du = 1/2",
                     font=DISPLAY, color=CRIMSON, font_size=17)
        r_lbl.move_to(UP * 0.0)
        self.play(Create(r_box), FadeIn(r_lbl), run_time=0.5)

        # State 5: I^2 = pi result
        pi_box = Rectangle(width=6.0, height=0.8, color=TEAL, fill_opacity=0.1)
        pi_box.set_stroke(TEAL, width=2.0)
        pi_box.move_to(DOWN * 1.4)
        pi_lbl = Text("I2 = 2*pi * (1/2) = pi", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        pi_lbl.move_to(DOWN * 1.4)
        self.play(Create(pi_box), FadeIn(pi_lbl), run_time=0.5)

        # State 6: Final I = sqrt(pi)
        final_box = Rectangle(width=5.0, height=0.85, color=GOLD, fill_opacity=0.25)
        final_box.set_stroke(GOLD, width=0)
        final_box.move_to(DOWN * 2.7)
        final_lbl = Text("I = sqrt(pi)", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        final_lbl.move_to(DOWN * 2.7)
        self.play(FadeIn(final_box), FadeIn(final_lbl), run_time=0.5)

        self.wait(_dur("B06") - 3.3)


# ── B07 THE IMPLICATION — QM normalization ────────────────────────────────────
class B07_QMNormalization(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("sqrt(pi) underlies every Gaussian wavefunction",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: QM Gaussian wavefunction
        psi_box = Rectangle(width=9.5, height=0.8, color=TEAL, fill_opacity=0.07)
        psi_box.set_stroke(TEAL, width=1.8)
        psi_box.move_to(UP * 2.1)
        psi_lbl = Text("psi(x) = (2*pi*sigma2)^{-1/4} * exp(-x2 / 4*sigma2)",
                       font=DISPLAY, color=TEAL, font_size=19)
        psi_lbl.move_to(UP * 2.1)
        self.play(Create(psi_box), FadeIn(psi_lbl), run_time=0.6)

        # State 3: Normalization integral
        norm_box = Rectangle(width=9.5, height=0.75, color=CRIMSON, fill_opacity=0.07)
        norm_box.set_stroke(CRIMSON, width=1.5)
        norm_box.move_to(UP * 0.8)
        norm_lbl = Text("int |psi|2 dx = 1   uses sqrt(pi) from Gaussian integral",
                        font=DISPLAY, color=CRIMSON, font_size=19)
        norm_lbl.move_to(UP * 0.8)
        self.play(Create(norm_box), FadeIn(norm_lbl), run_time=0.5)

        # State 4: Arrow to the prefactor
        arrow_pf = Arrow(UP * 0.2, UP * 1.5, buff=0.05, color=INK, stroke_width=1.8,
                         max_tip_length_to_length_ratio=0.18)
        arrow_pf.move_to(LEFT * 4.0 + UP * 0.85)
        pf_note = Text("normalization prefactor\ncomes from sqrt(pi)",
                       font=DISPLAY, color=SLATE, font_size=16)
        pf_note.move_to(LEFT * 1.5 + DOWN * 0.3)
        self.play(Create(arrow_pf), FadeIn(pf_note), run_time=0.4)

        # State 5: Connection bar
        conn_bar = Rectangle(width=9.5, height=0.6, color=GOLD, fill_opacity=0.22)
        conn_bar.set_stroke(GOLD, width=0)
        conn_bar.move_to(DOWN * 2.3)
        conn_lbl = Text("Every QM Gaussian normalization traces back to int e^{-x2} dx = sqrt(pi)",
                        font=DISPLAY, color=INK, font_size=17, weight=BOLD)
        conn_lbl.move_to(DOWN * 2.3)
        self.play(FadeIn(conn_bar), FadeIn(conn_lbl), run_time=0.4)

        self.wait(_dur("B07") - 2.9)


# ── B08 THE IMPLICATION — Gaussian moments trick ─────────────────────────────
class B08_GaussianMoments(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Every Gaussian moment uses the same integral",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Parametrized integral I(a)
        ia_box = Rectangle(width=8.5, height=0.75, color=TEAL, fill_opacity=0.07)
        ia_box.set_stroke(TEAL, width=1.8)
        ia_box.move_to(UP * 2.1)
        ia_lbl = Text("I(a) = int e^{-a*x2} dx = sqrt(pi / a)",
                      font=DISPLAY, color=TEAL, font_size=21)
        ia_lbl.move_to(UP * 2.1)
        self.play(Create(ia_box), FadeIn(ia_lbl), run_time=0.6)

        # State 3: Derivative trick
        diff_box = Rectangle(width=8.5, height=0.75, color=CRIMSON, fill_opacity=0.07)
        diff_box.set_stroke(CRIMSON, width=1.5)
        diff_box.move_to(UP * 0.8)
        diff_lbl = Text("-dI/da = int x2 * e^{-a*x2} dx = (sqrt(pi)/2) * a^{-3/2}",
                        font=DISPLAY, color=CRIMSON, font_size=18)
        diff_lbl.move_to(UP * 0.8)
        self.play(Create(diff_box), FadeIn(diff_lbl), run_time=0.5)

        # State 4: At a=1 result
        at1_box = Rectangle(width=6.5, height=0.65, color=TEAL, fill_opacity=0.07)
        at1_box.set_stroke(TEAL, width=1.5)
        at1_box.move_to(DOWN * 0.5)
        at1_lbl = Text("a = 1: int x2 e^{-x2} dx = sqrt(pi) / 2",
                       font=DISPLAY, color=TEAL, font_size=19)
        at1_lbl.move_to(DOWN * 0.5)
        self.play(Create(at1_box), FadeIn(at1_lbl), run_time=0.4)

        # State 5: Key takeaway
        key_bar = Rectangle(width=9.5, height=0.6, color=SLATE, fill_opacity=0.08)
        key_bar.set_stroke(SLATE, width=1.2)
        key_bar.move_to(DOWN * 2.1)
        key_lbl = Text("Differentiate once: x2 moment. Twice: x4 moment. All reduce to sqrt(pi).",
                       font=DISPLAY, color=SLATE, font_size=17)
        key_lbl.move_to(DOWN * 2.1)
        self.play(Create(key_bar), FadeIn(key_lbl), run_time=0.4)

        self.wait(_dur("B08") - 2.8)


# ── B09 THE EXAMPLE — concrete normalization check ───────────────────────────
class B09_NormalizationCheck(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Check: normalized Gaussian integrates to 1",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: The probability density
        pd_box = Rectangle(width=7.5, height=0.75, color=TEAL, fill_opacity=0.07)
        pd_box.set_stroke(TEAL, width=1.8)
        pd_box.move_to(UP * 2.1)
        pd_lbl = Text("p(x) = (1/sqrt(pi)) * e^{-x2}",
                      font=DISPLAY, color=TEAL, font_size=22)
        pd_lbl.move_to(UP * 2.1)
        self.play(Create(pd_box), FadeIn(pd_lbl), run_time=0.5)

        # State 3: Apply the integral
        apply_box = Rectangle(width=9.5, height=0.75, color=CRIMSON, fill_opacity=0.07)
        apply_box.set_stroke(CRIMSON, width=1.5)
        apply_box.move_to(UP * 0.7)
        apply_lbl = Text("int p(x) dx = (1/sqrt(pi)) * int e^{-x2} dx = (1/sqrt(pi)) * sqrt(pi)",
                         font=DISPLAY, color=CRIMSON, font_size=18)
        apply_lbl.move_to(UP * 0.7)
        self.play(Create(apply_box), FadeIn(apply_lbl), run_time=0.5)

        # State 4: = 1 result
        result_box = Rectangle(width=4.5, height=0.85, color=TEAL, fill_opacity=0.1)
        result_box.set_stroke(TEAL, width=2.0)
        result_box.move_to(DOWN * 0.6)
        result_lbl = Text("= 1", font=DISPLAY, color=TEAL, font_size=26, weight=BOLD)
        result_lbl.move_to(DOWN * 0.6)
        self.play(Create(result_box), FadeIn(result_lbl), run_time=0.4)

        # State 5: Normalization confirmed bar (GOLD fill, INK text)
        conf_bar = Rectangle(width=7.5, height=0.65, color=GOLD, fill_opacity=0.25)
        conf_bar.set_stroke(GOLD, width=0)
        conf_bar.move_to(DOWN * 2.2)
        conf_lbl = Text("Normalization confirmed: probability sums to 1",
                        font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        conf_lbl.move_to(DOWN * 2.2)
        self.play(FadeIn(conf_bar), FadeIn(conf_lbl), run_time=0.4)

        self.wait(_dur("B09") - 2.7)


# ── B10 CARD ──────────────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Square it: I2 = int int e^{-r2} dA.\nSwitch to polar: r dr d(theta).\nI2 = pi  ->  I = sqrt(pi).",
                        font=SERIF, color=INK, font_size=24, line_spacing=1.3)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B10") - 1.3)
