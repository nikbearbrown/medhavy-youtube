"""vox_scenes.py — Fill in the comb: how a sum becomes an integral
(vox-fourier-continuum, slate cut, 16:9).
Color law: TEAL=discrete modes/bound states; CRIMSON=continuum/free states;
           GOLD=envelope highlight; SLATE=axes/structure.
Exclusions: no delta-k bookkeeping derivation; keep to the visual densifying limit.
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


def _k_axis(x_length=10.0, color=SLATE):
    ax = Axes(
        x_range=(0, 10, 2), y_range=(0, 1.2, 0.5),
        x_length=x_length, y_length=2.8,
        axis_config={"color": color, "stroke_width": 1.2, "include_tip": False,
                     "include_ticks": False},
    )
    return ax


def _gaussian_envelope(k_vals, k0=5.0, sigma=2.5):
    return np.exp(-((k_vals - k0) ** 2) / (2 * sigma ** 2))


def _comb_bars(ax, n_bars, k_max=9.5, color=TEAL, bar_width=0.12, opacity=0.7):
    """Draw n_bars vertical bars at evenly spaced k values. Returns VGroup."""
    k_vals = np.linspace(0.5, k_max, n_bars)
    heights = _gaussian_envelope(k_vals)
    bars = VGroup()
    for k, h in zip(k_vals, heights):
        bar = Rectangle(
            width=bar_width, height=h * 2.0 + 0.001,
            color=color, fill_opacity=opacity,
        )
        bar.set_stroke(color, width=0.8)
        bar.move_to(ax.c2p(k, h * 0.5))
        bars.add(bar)
    return bars


def _continuum_curve(ax, color=CRIMSON, stroke_width=2.5, n_pts=200):
    k_vals = np.linspace(0, 10, n_pts)
    y_vals = _gaussian_envelope(k_vals)
    pts = [ax.c2p(k, y) for k, y in zip(k_vals, y_vals)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners(pts)
    return curve


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Stretch a box to infinity\nand the discrete spectrum\nmelts into a continuous one.",
                        font=SERIF, color=INK, font_size=28, line_spacing=1.2)
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
        headline = Text("How does a discrete\nspectrum become\na continuous one?",
                        font=SERIF, color=INK, font_size=34, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — discrete comb at L ─────────────────────────────────────
class B03_DiscreteComb(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Box of length L: discrete wavenumber comb",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Axes
        ax = _k_axis()
        ax.move_to(UP * 0.3)
        k_lbl = Text("k", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        k_lbl.move_to(ax.c2p(10.5, 0.0))
        self.play(Create(ax), FadeIn(k_lbl), run_time=0.4)

        # State 3: Sparse comb (6 bars)
        comb6 = _comb_bars(ax, 6, color=TEAL, bar_width=0.18)
        spacing_box = Rectangle(width=4.0, height=0.55, color=TEAL, fill_opacity=0.07)
        spacing_box.set_stroke(TEAL, width=1.2)
        spacing_box.move_to(UP * -1.2)
        spacing_lbl = Text("spacing Δk = π/L", font=DISPLAY, color=TEAL, font_size=19)
        spacing_lbl.move_to(UP * -1.2)
        self.play(Create(comb6), Create(spacing_box), FadeIn(spacing_lbl), run_time=0.6)

        # State 4: Box diagram
        box_rect = Rectangle(width=1.8, height=0.9, color=SLATE, fill_opacity=0.06)
        box_rect.set_stroke(SLATE, width=1.5)
        box_rect.move_to(LEFT * 4.5 + UP * -2.5)
        box_lbl = Text("L", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        box_lbl.move_to(LEFT * 4.5 + DOWN * 3.0)
        self.play(Create(box_rect), FadeIn(box_lbl), run_time=0.4)

        # State 5: Envelope curve
        env = _continuum_curve(ax, color=GOLD, stroke_width=1.5)
        env_lbl = Text("envelope: same at any L", font=DISPLAY, color=SLATE, font_size=16)
        env_lbl.move_to(UP * 1.8)
        self.play(Create(env), FadeIn(env_lbl), run_time=0.5)

        self.wait(_dur("B03") - 2.4)


# ── B04 THE PROBLEM — doubling L ─────────────────────────────────────────────
class B04_DoublingL(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Double the box: spacing halves, comb fills in",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        ax = _k_axis()
        ax.move_to(UP * 0.3)
        env = _continuum_curve(ax, color=GOLD, stroke_width=1.5)
        self.play(Create(ax), Create(env), run_time=0.4)

        # State 2: 6 bars (L)
        comb6 = _comb_bars(ax, 6, color=TEAL, bar_width=0.18, opacity=0.5)
        sp_lbl1 = Text("L: Δk = π/L", font=DISPLAY, color=TEAL, font_size=18)
        sp_lbl1.move_to(RIGHT * 4.0 + DOWN * 1.5)
        self.play(Create(comb6), FadeIn(sp_lbl1), run_time=0.5)

        # State 3: 12 bars (2L)
        comb12 = _comb_bars(ax, 12, color=TEAL, bar_width=0.12, opacity=0.7)
        sp_lbl2 = Text("2L: Δk = π/2L (half spacing)", font=DISPLAY, color=TEAL, font_size=18)
        sp_lbl2.move_to(RIGHT * 4.0 + DOWN * 2.2)
        self.play(Transform(comb6, comb12), FadeOut(sp_lbl1), FadeIn(sp_lbl2), run_time=0.7)

        # State 4: Comb and envelope comparison box
        compare_box = Rectangle(width=5.5, height=0.6, color=SLATE, fill_opacity=0.07)
        compare_box.set_stroke(SLATE, width=1.2)
        compare_box.move_to(DOWN * 3.0)
        compare_lbl = Text("More teeth, same envelope — keep going",
                           font=DISPLAY, color=SLATE, font_size=19)
        compare_lbl.move_to(DOWN * 3.0)
        self.play(Create(compare_box), FadeIn(compare_lbl), run_time=0.4)

        # State 5: 24 bars (4L) — move label to different y to avoid overlap
        comb24 = _comb_bars(ax, 24, color=TEAL, bar_width=0.08, opacity=0.8)
        sp_lbl3 = Text("4L: Δk = π/4L (denser)", font=DISPLAY, color=TEAL, font_size=18)
        sp_lbl3.move_to(RIGHT * 4.0 + DOWN * 2.8)
        self.play(Transform(comb6, comb24), FadeOut(sp_lbl2), FadeIn(sp_lbl3), run_time=0.7)

        self.wait(_dur("B04") - 3.2)


# ── B05 THE MECHANISM — comb densifying to continuum ─────────────────────────
class B05_CombDensifying(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("As L grows, comb fills in toward the envelope",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        ax = _k_axis()
        ax.move_to(UP * 0.3)
        env = _continuum_curve(ax, color=GOLD, stroke_width=1.5)
        self.play(Create(ax), Create(env), run_time=0.4)

        # State 2: 8 bars
        comb8 = _comb_bars(ax, 8, color=TEAL, bar_width=0.15, opacity=0.7)
        n_lbl = Text("L: 8 modes", font=DISPLAY, color=TEAL, font_size=17)
        n_lbl.move_to(DOWN * 1.5 + LEFT * 3.0)
        self.play(Create(comb8), FadeIn(n_lbl), run_time=0.5)

        # State 3: 20 bars
        comb20 = _comb_bars(ax, 20, color=TEAL, bar_width=0.10, opacity=0.75)
        n_lbl2 = Text("2.5L: 20 modes", font=DISPLAY, color=TEAL, font_size=17)
        n_lbl2.move_to(DOWN * 2.0 + LEFT * 3.0)
        self.play(Transform(comb8, comb20), FadeOut(n_lbl), FadeIn(n_lbl2), run_time=0.6)

        # State 4: 50 bars — near continuum
        comb50 = _comb_bars(ax, 50, color=TEAL, bar_width=0.06, opacity=0.8)
        n_lbl3 = Text("6L: 50 modes (near continuum)", font=DISPLAY, color=TEAL, font_size=17)
        n_lbl3.move_to(DOWN * 2.5 + LEFT * 2.0)
        self.play(Transform(comb8, comb50), FadeOut(n_lbl2), FadeIn(n_lbl3), run_time=0.7)

        # State 5: Conclusion bar
        concl_bar = Rectangle(width=9.5, height=0.6, color=GOLD, fill_opacity=0.2)
        concl_bar.set_stroke(GOLD, width=0)
        concl_bar.move_to(DOWN * 2.8)
        concl_lbl = Text("Limit L → ∞: discrete sum → continuous integral",
                         font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        concl_lbl.move_to(DOWN * 2.8)
        self.play(FadeIn(concl_bar), FadeIn(concl_lbl), run_time=0.4)

        self.wait(_dur("B05") - 3.1)


# ── B06 THE MECHANISM — sum to integral formula ───────────────────────────────
class B06_SumToIntegral(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("The limit makes the sum an integral",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Discrete sum
        sum_box = Rectangle(width=7.5, height=0.85, color=TEAL, fill_opacity=0.07)
        sum_box.set_stroke(TEAL, width=1.8)
        sum_box.move_to(UP * 2.1)
        sum_lbl = Text("f(x) = Σₙ cₙ e^{ikₙx}   (discrete, spacing Δk = π/L)",
                       font=DISPLAY, color=TEAL, font_size=21)
        sum_lbl.move_to(UP * 2.1)
        self.play(Create(sum_box), FadeIn(sum_lbl), run_time=0.6)

        # State 3: Arrow
        arr = Arrow(UP * 1.4, UP * 0.5, buff=0, color=INK, stroke_width=2.0,
                    max_tip_length_to_length_ratio=0.2)
        limit_lbl = Text("L → ∞,  Δk → 0", font=DISPLAY, color=INK, font_size=18)
        limit_lbl.move_to(RIGHT * 2.5 + UP * 0.95)
        self.play(Create(arr), FadeIn(limit_lbl), run_time=0.4)

        # State 4: Integral form
        int_box = Rectangle(width=7.5, height=0.85, color=CRIMSON, fill_opacity=0.07)
        int_box.set_stroke(CRIMSON, width=1.8)
        int_box.move_to(UP * -0.1)
        int_lbl = Text("f(x) = (1/2π) ∫ φ(k) e^{ikx} dk   (Fourier transform)",
                       font=DISPLAY, color=CRIMSON, font_size=21)
        int_lbl.move_to(UP * -0.1)
        self.play(Create(int_box), FadeIn(int_lbl), run_time=0.6)

        # State 5: QM connection
        qm_bar = Rectangle(width=9.5, height=0.6, color=SLATE, fill_opacity=0.06)
        qm_bar.set_stroke(SLATE, width=1.0)
        qm_bar.move_to(DOWN * 2.0)
        qm_lbl = Text("Same construction — just the box size parameter changes",
                      font=DISPLAY, color=SLATE, font_size=19)
        qm_lbl.move_to(DOWN * 2.0)
        self.play(Create(qm_bar), FadeIn(qm_lbl), run_time=0.5)

        self.wait(_dur("B06") - 2.7)


# ── B07 THE IMPLICATION — bound vs free spectrum ─────────────────────────────
class B07_BoundVsFree(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Discrete bound states, continuous free states",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Bound state panel (left)
        bound_box = Rectangle(width=4.5, height=3.0, color=TEAL, fill_opacity=0.06)
        bound_box.set_stroke(TEAL, width=1.5)
        bound_box.move_to(LEFT * 3.0 + UP * 0.6)
        bound_title = Text("BOUND", font=DISPLAY, color=TEAL, font_size=18, weight=BOLD)
        bound_title.move_to(LEFT * 3.0 + UP * 2.0)
        bound_e1 = Text("Box / finite well", font=DISPLAY, color=TEAL, font_size=16)
        bound_e1.move_to(LEFT * 3.0 + UP * 1.2)
        bound_e2 = Text("Discrete E₁, E₂, E₃ ...", font=DISPLAY, color=TEAL, font_size=16)
        bound_e2.move_to(LEFT * 3.0 + UP * 0.5)
        bound_e3 = Text("Fourier SERIES", font=DISPLAY, color=TEAL, font_size=16, weight=BOLD)
        bound_e3.move_to(LEFT * 3.0 + DOWN * 0.2)
        self.play(Create(bound_box), FadeIn(bound_title), FadeIn(bound_e1),
                  FadeIn(bound_e2), FadeIn(bound_e3), run_time=0.6)

        # State 3: Free state panel (right)
        free_box = Rectangle(width=4.5, height=3.0, color=CRIMSON, fill_opacity=0.06)
        free_box.set_stroke(CRIMSON, width=1.5)
        free_box.move_to(RIGHT * 3.0 + UP * 0.6)
        free_title = Text("FREE", font=DISPLAY, color=CRIMSON, font_size=18, weight=BOLD)
        free_title.move_to(RIGHT * 3.0 + UP * 2.0)
        free_e1 = Text("Open space (L → ∞)", font=DISPLAY, color=CRIMSON, font_size=16)
        free_e1.move_to(RIGHT * 3.0 + UP * 1.2)
        free_e2 = Text("Continuous E(k) for all k", font=DISPLAY, color=CRIMSON, font_size=16)
        free_e2.move_to(RIGHT * 3.0 + UP * 0.5)
        free_e3 = Text("Fourier TRANSFORM", font=DISPLAY, color=CRIMSON, font_size=16, weight=BOLD)
        free_e3.move_to(RIGHT * 3.0 + DOWN * 0.2)
        self.play(Create(free_box), FadeIn(free_title), FadeIn(free_e1),
                  FadeIn(free_e2), FadeIn(free_e3), run_time=0.6)

        # State 4: Connecting arrow
        conn_arr = Arrow(LEFT * 0.8 + UP * 0.6, RIGHT * 0.8 + UP * 0.6,
                         buff=0, color=SLATE, stroke_width=2.0,
                         max_tip_length_to_length_ratio=0.15)
        conn_lbl = Text("L→∞", font=DISPLAY, color=SLATE, font_size=18)
        conn_lbl.move_to(UP * 1.0)
        self.play(Create(conn_arr), FadeIn(conn_lbl), run_time=0.4)

        # State 5: Key takeaway
        key_bar = Rectangle(width=9.5, height=0.55, color=GOLD, fill_opacity=0.2)
        key_bar.set_stroke(GOLD, width=0)
        key_bar.move_to(DOWN * 2.5)
        key_lbl = Text("Bound = discrete = series. Free = continuous = transform.",
                       font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        key_lbl.move_to(DOWN * 2.5)
        self.play(FadeIn(key_bar), FadeIn(key_lbl), run_time=0.5)

        self.wait(_dur("B07") - 2.7)


# ── B08 THE IMPLICATION — why QM switches from sums to integrals ─────────────
class B08_SwitchReason(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Series and transform: one construction, two limits",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Timeline bar
        timeline_box = Rectangle(width=11.0, height=0.5, color=SLATE, fill_opacity=0.08)
        timeline_box.set_stroke(SLATE, width=1.2)
        timeline_box.move_to(UP * 1.5)
        self.play(Create(timeline_box), run_time=0.4)

        series_lbl = Text("Fourier Series (small L, discrete)", font=DISPLAY, color=TEAL, font_size=17)
        series_lbl.move_to(LEFT * 3.5 + UP * 1.5)
        transform_lbl = Text("Fourier Transform (L→∞, continuous)", font=DISPLAY, color=CRIMSON, font_size=17)
        transform_lbl.move_to(RIGHT * 2.8 + UP * 1.5)
        arrow_timeline = Arrow(LEFT * 1.0 + UP * 1.5, RIGHT * 0.8 + UP * 1.5,
                               buff=0, color=INK, stroke_width=2.0,
                               max_tip_length_to_length_ratio=0.2)
        arr_lbl = Text("L↑", font=DISPLAY, color=INK, font_size=16)
        arr_lbl.move_to(UP * 2.0)
        self.play(FadeIn(series_lbl), FadeIn(transform_lbl), Create(arrow_timeline), FadeIn(arr_lbl), run_time=0.6)

        # State 3: QM textbook note
        tb_box = Rectangle(width=9.5, height=0.7, color=INK, fill_opacity=0.05)
        tb_box.set_stroke(INK, width=1.2)
        tb_box.move_to(UP * 0.0)
        tb_lbl = Text("Every QM text switches from Σ to ∫ when leaving the box.",
                      font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        tb_lbl.move_to(UP * 0.0)
        self.play(Create(tb_box), FadeIn(tb_lbl), run_time=0.5)

        # State 4: Explanation line
        why_lbl = Text("Why? Not a convention — it's the L → ∞ limit.",
                       font=DISPLAY, color=SLATE, font_size=18)
        why_lbl.move_to(UP * -0.9)
        self.play(FadeIn(why_lbl), run_time=0.4)

        # State 5: Bottom bar
        bot_bar = Rectangle(width=9.5, height=0.55, color=SLATE, fill_opacity=0.06)
        bot_bar.set_stroke(SLATE, width=1.0)
        bot_bar.move_to(DOWN * 2.2)
        bot_lbl = Text("Same Fourier mathematics at both ends — just a different box size",
                       font=DISPLAY, color=SLATE, font_size=17)
        bot_lbl.move_to(DOWN * 2.2)
        self.play(Create(bot_bar), FadeIn(bot_lbl), run_time=0.5)

        self.wait(_dur("B08") - 2.9)


# ── B09 THE EXAMPLE — numerical density table ─────────────────────────────────
class B09_DensityTable(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Mode spacing shrinks as box grows",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Header
        hdr_box = Rectangle(width=8.5, height=0.6, color=SLATE, fill_opacity=0.12)
        hdr_box.set_stroke(SLATE, width=1.2)
        hdr_box.move_to(UP * 2.1)
        hdr_lbl = Text("Box length L          Mode spacing Δk", font=DISPLAY, color=SLATE, font_size=20)
        hdr_lbl.move_to(UP * 2.1)
        self.play(Create(hdr_box), FadeIn(hdr_lbl), run_time=0.4)

        # State 3: Rows 1 and 2
        rows_data = [
            ("L = 1 m", "Δk = π/m = 3.14 / m", TEAL),
            ("L = 10 m", "Δk = 0.31 / m", TEAL),
            ("L = 1000 m", "Δk = 0.003 / m", TEAL),
            ("L → ∞", "Δk → 0  (continuum)", CRIMSON),
        ]
        row_y = [1.2, 0.3, -0.6, -1.5]

        row1_box = Rectangle(width=8.5, height=0.6, color=rows_data[0][2], fill_opacity=0.07)
        row1_box.set_stroke(rows_data[0][2], width=1.2)
        row1_box.move_to(UP * row_y[0])
        row1_lbl = Text(f"{rows_data[0][0]}       {rows_data[0][1]}", font=DISPLAY,
                        color=rows_data[0][2], font_size=19)
        row1_lbl.move_to(UP * row_y[0])
        row2_box = Rectangle(width=8.5, height=0.6, color=rows_data[1][2], fill_opacity=0.07)
        row2_box.set_stroke(rows_data[1][2], width=1.2)
        row2_box.move_to(UP * row_y[1])
        row2_lbl = Text(f"{rows_data[1][0]}      {rows_data[1][1]}", font=DISPLAY,
                        color=rows_data[1][2], font_size=19)
        row2_lbl.move_to(UP * row_y[1])
        self.play(Create(row1_box), FadeIn(row1_lbl), Create(row2_box), FadeIn(row2_lbl), run_time=0.6)

        # State 4: Row 3
        row3_box = Rectangle(width=8.5, height=0.6, color=rows_data[2][2], fill_opacity=0.07)
        row3_box.set_stroke(rows_data[2][2], width=1.2)
        row3_box.move_to(UP * row_y[2])
        row3_lbl = Text(f"{rows_data[2][0]}   {rows_data[2][1]}", font=DISPLAY,
                        color=rows_data[2][2], font_size=19)
        row3_lbl.move_to(UP * row_y[2])
        self.play(Create(row3_box), FadeIn(row3_lbl), run_time=0.4)

        # State 5: Continuum row (highlighted)
        row4_box = Rectangle(width=8.5, height=0.65, color=CRIMSON, fill_opacity=0.12)
        row4_box.set_stroke(CRIMSON, width=2.0)
        row4_box.move_to(UP * row_y[3])
        row4_lbl = Text(f"{rows_data[3][0]}           {rows_data[3][1]}", font=DISPLAY,
                        color=CRIMSON, font_size=19, weight=BOLD)
        row4_lbl.move_to(UP * row_y[3])
        self.play(Create(row4_box), FadeIn(row4_lbl), run_time=0.5)

        self.wait(_dur("B09") - 2.8)


# ── B10 CARD ──────────────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Small box: discrete.\nBig box: dense.\nInfinite box: continuous.",
                        font=SERIF, color=INK, font_size=34, line_spacing=1.25)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B10") - 1.3)
