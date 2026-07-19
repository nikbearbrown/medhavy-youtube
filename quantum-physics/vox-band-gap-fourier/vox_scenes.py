"""vox_scenes.py — The band gap width is just one Fourier coefficient
(vox-band-gap-fourier, slate cut, 16:9).
Color law: TEAL=allowed bands; CRIMSON=forbidden gap; GOLD=zone boundary marker.
Exclusions: no Bloch theorem derivation; no tight-binding; first zone only.
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


# Dispersion curve parameters
K_MAX = 4.0       # x-axis range: -K_MAX to K_MAX in units of pi/a
E_MAX = 5.0       # y-axis range: 0 to E_MAX (arbitrary units)
K_ZONE = 1.0      # zone boundary at k = pi/a (normalized to 1)
AX_W = 9.0
AX_H = 5.0
AX_CX = 0.0
AX_CY = -0.5


def _k_to_x(k):
    """Convert k (in units where zone boundary = 1) to screen x."""
    return AX_CX + (k / K_MAX) * (AX_W / 2)


def _e_to_y(e):
    """Convert energy to screen y."""
    return AX_CY - AX_H / 2 + (e / E_MAX) * AX_H


def _axis_frame():
    """Draw k-axis and E-axis."""
    bottom = AX_CY - AX_H / 2
    left = AX_CX - AX_W / 2
    right = AX_CX + AX_W / 2
    hline = Line(RIGHT * left + UP * bottom, RIGHT * right + UP * bottom,
                 color=INK, stroke_width=1.2)
    vline = Line(RIGHT * AX_CX + UP * bottom,
                 RIGHT * AX_CX + UP * (AX_CY + AX_H / 2 + 0.3),
                 color=INK, stroke_width=1.2)
    k_lbl = Text("k", font=SERIF, color=INK, font_size=20, slant=ITALIC)
    k_lbl.move_to(RIGHT * (right + 0.3) + UP * bottom)
    e_lbl = Text("E", font=SERIF, color=INK, font_size=20, slant=ITALIC)
    e_lbl.move_to(RIGHT * AX_CX + UP * (AX_CY + AX_H / 2 + 0.5))
    return VGroup(hline, vline, k_lbl, e_lbl)


def _free_electron_parabola(k_shift=0, color=TEAL, n_pts=120):
    """Free electron parabola centered at k_shift (in units of zone boundary)."""
    k_vals = np.linspace(-K_MAX, K_MAX, n_pts)
    e_vals = (k_vals - k_shift) ** 2  # E ∝ (k - G)^2
    pts = []
    for k, e in zip(k_vals, e_vals):
        if 0 <= e <= E_MAX:
            pts.append(RIGHT * _k_to_x(k) + UP * _e_to_y(e))
    if len(pts) < 2:
        return None
    poly = VMobject(color=color, stroke_width=2.2)
    poly.set_points_as_corners(pts)
    return poly


def _zone_boundary_line():
    """Vertical dashed line at k = ±1 (zone boundary)."""
    bottom = AX_CY - AX_H / 2
    top = AX_CY + AX_H / 2
    x_pos = _k_to_x(K_ZONE)
    x_neg = _k_to_x(-K_ZONE)
    line_pos = DashedLine(RIGHT * x_pos + UP * bottom, RIGHT * x_pos + UP * top,
                          color=GOLD, stroke_width=1.5, dash_length=0.15)
    line_neg = DashedLine(RIGHT * x_neg + UP * bottom, RIGHT * x_neg + UP * top,
                          color=GOLD, stroke_width=1.5, dash_length=0.15)
    return VGroup(line_pos, line_neg)


def _band_with_gap(V1=0.5, n_pts=200):
    """
    Dispersion curve with a gap at k=+/-pi/a.
    Near zone boundary k=1, E± = k^2 ± |V1|.
    Returns (lower_band, upper_band, gap_rect).
    """
    k_vals = np.linspace(-K_MAX, K_MAX, n_pts)
    # Free energy of two parabolas
    e1 = k_vals ** 2
    e2 = (k_vals - 2 * K_ZONE) ** 2
    # At zone boundary, mix both: E± = (e1+e2)/2 ± sqrt(((e1-e2)/2)^2 + V1^2)
    avg = (e1 + e2) / 2
    half_diff = (e1 - e2) / 2
    delta = np.sqrt(half_diff ** 2 + V1 ** 2)
    e_lower = avg - delta
    e_upper = avg + delta

    # Build lower band points (right side, k near zone boundary zone)
    lower_pts_right = []
    upper_pts_right = []
    for k, el, eu in zip(k_vals, e_lower, e_upper):
        if k > 0 and 0 <= el <= E_MAX:
            lower_pts_right.append(RIGHT * _k_to_x(k) + UP * _e_to_y(el))
        if k > 0 and 0 <= eu <= E_MAX:
            upper_pts_right.append(RIGHT * _k_to_x(k) + UP * _e_to_y(eu))

    lower_pts_left = []
    upper_pts_left = []
    for k, el, eu in zip(k_vals, e_lower, e_upper):
        if k < 0 and 0 <= el <= E_MAX:
            lower_pts_left.append(RIGHT * _k_to_x(k) + UP * _e_to_y(el))
        if k < 0 and 0 <= eu <= E_MAX:
            upper_pts_left.append(RIGHT * _k_to_x(k) + UP * _e_to_y(eu))

    def _make_curve(pts, color, sw=2.2):
        if len(pts) < 2:
            return VMobject()
        p = VMobject(color=color, stroke_width=sw)
        p.set_points_as_corners(pts)
        return p

    lower_r = _make_curve(lower_pts_right, TEAL)
    lower_l = _make_curve(lower_pts_left, TEAL)
    upper_r = _make_curve(upper_pts_right, TEAL)
    upper_l = _make_curve(upper_pts_left, TEAL)
    lower_band = VGroup(lower_r, lower_l)
    upper_band = VGroup(upper_r, upper_l)

    # Gap rectangle
    e_lower_at_zone = float(K_ZONE ** 2 - V1)
    e_upper_at_zone = float(K_ZONE ** 2 + V1)
    y_bottom = _e_to_y(max(0, e_lower_at_zone))
    y_top = _e_to_y(min(E_MAX, e_upper_at_zone))
    x_left = _k_to_x(0.5)
    x_right = _k_to_x(1.5)
    gap_h = y_top - y_bottom
    gap_w = x_right - x_left
    if gap_h > 0.01:
        gap_rect = Rectangle(width=gap_w * 2, height=gap_h, color=CRIMSON, fill_opacity=0.35)
        gap_rect.set_stroke(CRIMSON, width=0)
        gap_rect.move_to(RIGHT * AX_CX + UP * (y_bottom + gap_h / 2))
    else:
        gap_rect = VMobject()

    return lower_band, upper_band, gap_rect


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("The band gap width is\njust one Fourier coefficient",
                        font=SERIF, color=INK, font_size=36, line_spacing=1.2)
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
        eyebrow.move_to(UP * 2.2)
        headline = Text("The band gap should depend\non the whole lattice.\nIt only needs one number.\nWhy?",
                        font=SERIF, color=INK, font_size=26, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — free electron parabola and zone crossing ────────────────
class B03_FreeElectronParabola(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        # State 1: Axes
        axes = _axis_frame()
        title = Text("Free electron dispersion: parabola",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), Create(axes), run_time=0.6)

        # State 2: First parabola centered at k=0
        p1 = _free_electron_parabola(k_shift=0, color=TEAL)
        self.play(Create(p1), run_time=0.6)

        # State 3: Second parabola shifted by 2 (= 2 zone boundary units = G1)
        p2 = _free_electron_parabola(k_shift=2, color=SLATE)
        p2_neg = _free_electron_parabola(k_shift=-2, color=SLATE)
        zone_label = Text("Zone boundary k=π/a", font=DISPLAY, color=SLATE, font_size=17)
        zone_label.move_to(UP * 3.0 + RIGHT * 3.0)
        self.play(Create(p2), Create(p2_neg), FadeIn(zone_label), run_time=0.7)

        # State 4: Zone boundary lines
        zone_lines = _zone_boundary_line()
        self.play(Create(zone_lines), run_time=0.5)

        # State 5: Crossing dot — highlight the degeneracy
        k_zone_x = _k_to_x(K_ZONE)
        e_at_zone = K_ZONE ** 2
        e_y = _e_to_y(e_at_zone)
        cross_dot = Dot(RIGHT * k_zone_x + UP * e_y, color=CRIMSON, radius=0.15)
        cross_lbl = Text("Degeneracy", font=DISPLAY, color=CRIMSON, font_size=18)
        cross_lbl.move_to(RIGHT * (k_zone_x + 1.2) + UP * (e_y + 0.3))
        self.play(FadeIn(cross_dot), FadeIn(cross_lbl), run_time=0.5)

        self.wait(_dur("B03") - 2.9)


# ── B04 THE PROBLEM — Fourier expansion of V(x) ──────────────────────────────
class B04_FourierPotential(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Periodic potential has a Fourier series",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Show V(x) as a cosine wave (potential in real space)
        x_vals = np.linspace(-5.0, 5.0, 300)
        y_pot = 0.6 * np.cos(2 * np.pi * x_vals / 1.0) + 0.15 * np.cos(4 * np.pi * x_vals / 1.0)
        pot_pts = [RIGHT * x + UP * (y - 1.8) for x, y in zip(x_vals, y_pot)]
        pot_wave = VMobject(color=SLATE, stroke_width=2.0)
        pot_wave.set_points_as_corners(pot_pts)
        pot_lbl = Text("V(x): periodic crystal potential", font=DISPLAY, color=SLATE, font_size=18)
        pot_lbl.move_to(UP * -1.0)
        self.play(Create(pot_wave), FadeIn(pot_lbl), run_time=0.7)

        # State 3: Fourier bar chart (coefficients V0, V1, V2...)
        bar_y_base = -2.5
        coeff_labels = ["V₀", "V₁", "V₂", "V₃"]
        coeff_heights = [0.3, 1.5, 0.4, 0.15]
        coeff_colors = [SLATE, TEAL, SLATE, SLATE]
        bars = VGroup()
        for i, (lbl, h, col) in enumerate(zip(coeff_labels, coeff_heights, coeff_colors)):
            x_pos = -3.0 + i * 2.0
            bar = Rectangle(width=0.9, height=h, color=col, fill_opacity=0.65)
            bar.set_stroke(col, width=0.8)
            bar.move_to(RIGHT * x_pos + UP * (bar_y_base + h / 2))
            bars.add(bar)
        self.play(Create(bars), run_time=0.6)

        # State 4: Labels for bars
        bar_lbls = VGroup()
        for i, (lbl, h) in enumerate(zip(coeff_labels, coeff_heights)):
            x_pos = -3.0 + i * 2.0
            t = Text(lbl, font=SERIF, color=INK, font_size=18, slant=ITALIC)
            t.move_to(RIGHT * x_pos + UP * (bar_y_base - 0.3))
            bar_lbls.add(t)
        self.play(FadeIn(bar_lbls), run_time=0.5)

        # State 5: Separator line between real-space potential and Fourier bars
        sep_line = Line(LEFT * 6.5 + UP * -0.3, RIGHT * 6.5 + UP * -0.3,
                        color=SLATE, stroke_width=0.8)
        real_lbl = Text("Real space V(x)", font=DISPLAY, color=SLATE, font_size=16)
        real_lbl.move_to(LEFT * 4.5 + UP * -0.1)
        freq_lbl = Text("Fourier coefficients Vₙ", font=DISPLAY, color=SLATE, font_size=16)
        freq_lbl.move_to(LEFT * 4.5 + UP * -2.2)
        self.play(Create(sep_line), FadeIn(real_lbl), FadeIn(freq_lbl), run_time=0.5)

        # State 6: Arrow pointing to V1 bar with highlight
        v1_bar_x = -3.0 + 1 * 2.0
        v1_bar_h = coeff_heights[1]
        highlight_box = Rectangle(width=1.1, height=v1_bar_h + 0.2, color=TEAL, fill_opacity=0.08)
        highlight_box.set_stroke(TEAL, width=2.0)
        highlight_box.move_to(RIGHT * v1_bar_x + UP * (bar_y_base + v1_bar_h / 2))
        v1_note = Text("V₁ = matches zone spacing", font=DISPLAY, color=TEAL, font_size=16)
        v1_note.move_to(RIGHT * 1.5 + UP * -1.8)
        self.play(Create(highlight_box), FadeIn(v1_note), run_time=0.5)

        self.wait(_dur("B04") - 2.8)


# ── B05 THE MECHANISM — scattering selection rule ─────────────────────────────
class B05_ScatteringRule(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("V₁ is the only coupling that matters",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Two momentum dots at zone boundary: k=+1 and k=-1
        k_pos_x = _k_to_x(K_ZONE)
        k_neg_x = _k_to_x(-K_ZONE)
        e_y = _e_to_y(K_ZONE ** 2)

        dot_pos = Dot(RIGHT * k_pos_x + UP * e_y, color=TEAL, radius=0.18)
        dot_neg = Dot(RIGHT * k_neg_x + UP * e_y, color=TEAL, radius=0.18)
        lbl_pos = Text("+π/a", font=DISPLAY, color=TEAL, font_size=18)
        lbl_pos.move_to(RIGHT * k_pos_x + UP * (e_y + 0.4))
        lbl_neg = Text("−π/a", font=DISPLAY, color=TEAL, font_size=18)
        lbl_neg.move_to(RIGHT * k_neg_x + UP * (e_y + 0.4))
        axis = _axis_frame()
        self.play(Create(axis), FadeIn(dot_pos), FadeIn(dot_neg),
                  FadeIn(lbl_pos), FadeIn(lbl_neg), run_time=0.7)

        # State 3: Arrow connecting +k to -k (scattering by G1 = 2pi/a)
        scatter_arrow = Arrow(RIGHT * k_pos_x + UP * e_y,
                              RIGHT * k_neg_x + UP * e_y,
                              buff=0.2, stroke_width=2.5, color=CRIMSON,
                              max_tip_length_to_length_ratio=0.15)
        scatter_lbl = Text("Scattering by G₁ = 2π/a", font=DISPLAY, color=CRIMSON, font_size=18)
        scatter_lbl.move_to(UP * (e_y + 1.0))
        self.play(Create(scatter_arrow), FadeIn(scatter_lbl), run_time=0.6)

        # State 4: Coupling box — only V1
        coup_box = Rectangle(width=4.5, height=0.7, color=TEAL, fill_opacity=0.08)
        coup_box.set_stroke(TEAL, width=1.8)
        coup_box.move_to(UP * 1.2)
        coup_lbl = Text("Coupling = V₁  (the matching Fourier term)",
                        font=DISPLAY, color=TEAL, font_size=20)
        coup_lbl.move_to(UP * 1.2)
        self.play(Create(coup_box), FadeIn(coup_lbl), run_time=0.6)

        # State 5: Other V terms zero note
        zero_box = Rectangle(width=5.5, height=0.6, color=SLATE, fill_opacity=0.06)
        zero_box.set_stroke(SLATE, width=1.2)
        zero_box.move_to(UP * -2.5)
        zero_lbl = Text("V₂, V₃, ... don't couple this pair — wrong spatial frequency",
                        font=DISPLAY, color=SLATE, font_size=17)
        zero_lbl.move_to(UP * -2.5)
        self.play(Create(zero_box), FadeIn(zero_lbl), run_time=0.5)

        self.wait(_dur("B05") - 2.9)


# ── B06 THE MECHANISM — 2x2 matrix and gap formula ──────────────────────────
class B06_Matrix2x2(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("2×2 matrix in the degenerate subspace",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Matrix display
        mat_box = Rectangle(width=5.5, height=2.0, color=INK, fill_opacity=0.04)
        mat_box.set_stroke(INK, width=1.2)
        mat_box.move_to(UP * 1.2)
        row1 = Text("E₀   V₁", font=SERIF, color=INK, font_size=28, slant=ITALIC)
        row1.move_to(UP * 1.6)
        row2 = Text("V₁   E₀", font=SERIF, color=INK, font_size=28, slant=ITALIC)
        row2.move_to(UP * 0.8)
        self.play(Create(mat_box), FadeIn(row1), FadeIn(row2), run_time=0.7)

        # State 3: Eigenvalues
        eig_box = Rectangle(width=5.5, height=0.75, color=TEAL, fill_opacity=0.08)
        eig_box.set_stroke(TEAL, width=1.8)
        eig_box.move_to(UP * -0.5)
        eig_lbl = Text("Eigenvalues: E₀ ± |V₁|",
                       font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        eig_lbl.move_to(UP * -0.5)
        self.play(Create(eig_box), FadeIn(eig_lbl), run_time=0.6)

        # State 4: Gap formula
        gap_box = Rectangle(width=4.0, height=0.75, color=CRIMSON, fill_opacity=0.08)
        gap_box.set_stroke(CRIMSON, width=1.8)
        gap_box.move_to(UP * -1.7)
        gap_lbl = Text("Gap = 2|V₁|", font=SERIF, color=CRIMSON, font_size=32, slant=ITALIC)
        gap_lbl.move_to(UP * -1.7)
        self.play(Create(gap_box), FadeIn(gap_lbl), run_time=0.6)

        # State 5: Gold summary bar
        gold_bar = Rectangle(width=6.5, height=0.55, color=GOLD, fill_opacity=0.28)
        gold_bar.set_stroke(GOLD, width=0)
        gold_bar.move_to(UP * -3.0)
        summ_lbl = Text("One coefficient. One gap. Linear algebra.",
                        font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        summ_lbl.move_to(UP * -3.0)
        self.play(FadeIn(gold_bar), FadeIn(summ_lbl), run_time=0.5)

        self.wait(_dur("B06") - 2.9)


# ── B07 THE IMPLICATION — dispersion curve with gap opening ───────────────────
class B07_GapOpening(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("The gap opens at the zone boundary",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        axes = _axis_frame()
        self.play(FadeIn(title), Create(axes), run_time=0.6)

        # State 2: Free parabola (no gap)
        p1 = _free_electron_parabola(k_shift=0, color=TEAL)
        p2 = _free_electron_parabola(k_shift=2, color=SLATE)
        self.play(Create(p1), Create(p2), run_time=0.6)

        # State 3: Zone boundary lines
        zone_lines = _zone_boundary_line()
        self.play(Create(zone_lines), run_time=0.4)

        # State 4: Bands with gap (V1=0.8)
        lower, upper, gap_rect = _band_with_gap(V1=0.8)
        self.play(
            Create(lower), Create(upper),
            run_time=0.8,
        )

        # State 5: Gap rectangle + label
        gap_lbl = Text("Gap = 2|V₁|", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        e_at_zone = K_ZONE ** 2
        gap_lbl.move_to(RIGHT * 2.5 + UP * _e_to_y(e_at_zone))
        self.play(FadeIn(gap_rect), FadeIn(gap_lbl), run_time=0.5)

        self.wait(_dur("B07") - 2.9)


# ── B08 THE IMPLICATION — higher zone boundaries ─────────────────────────────
class B08_HigherZones(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Each zone boundary has its own Fourier coefficient",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Zone label rows
        zone1_box = Rectangle(width=8.5, height=0.7, color=TEAL, fill_opacity=0.07)
        zone1_box.set_stroke(TEAL, width=1.5)
        zone1_box.move_to(UP * 2.0)
        zone1_lbl = Text("First zone boundary (k=π/a):   gap = 2|V₁|",
                         font=DISPLAY, color=TEAL, font_size=20)
        zone1_lbl.move_to(UP * 2.0)
        self.play(Create(zone1_box), FadeIn(zone1_lbl), run_time=0.6)

        # State 3: Second zone
        zone2_box = Rectangle(width=8.5, height=0.7, color=SLATE, fill_opacity=0.07)
        zone2_box.set_stroke(SLATE, width=1.2)
        zone2_box.move_to(UP * 0.8)
        zone2_lbl = Text("Second zone boundary (k=2π/a): gap = 2|V₂|",
                         font=DISPLAY, color=SLATE, font_size=20)
        zone2_lbl.move_to(UP * 0.8)
        self.play(Create(zone2_box), FadeIn(zone2_lbl), run_time=0.5)

        # State 4: Third zone
        zone3_box = Rectangle(width=8.5, height=0.7, color=SLATE, fill_opacity=0.06)
        zone3_box.set_stroke(SLATE, width=1.0)
        zone3_box.move_to(UP * -0.4)
        zone3_lbl = Text("Third zone boundary (k=3π/a):  gap = 2|V₃|",
                         font=DISPLAY, color=SLATE, font_size=20)
        zone3_lbl.move_to(UP * -0.4)
        self.play(Create(zone3_box), FadeIn(zone3_lbl), run_time=0.5)

        # State 5: Gold summary — each gap independent
        gold_bar = Rectangle(width=8.0, height=0.55, color=GOLD, fill_opacity=0.28)
        gold_bar.set_stroke(GOLD, width=0)
        gold_bar.move_to(UP * -2.0)
        indep_lbl = Text("Fourier selects the matching frequency — each gap independent",
                         font=DISPLAY, color=INK, font_size=18)
        indep_lbl.move_to(UP * -2.0)
        self.play(FadeIn(gold_bar), FadeIn(indep_lbl), run_time=0.5)

        self.wait(_dur("B08") - 2.6)


# ── B09 THE EXAMPLE — 0.3 nm crystal ─────────────────────────────────────────
class B09_NumericalExample(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Example: 1D crystal with a = 0.3 nm",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Given data
        given_box = Rectangle(width=7.0, height=0.7, color=INK, fill_opacity=0.05)
        given_box.set_stroke(INK, width=1.2)
        given_box.move_to(UP * 2.2)
        given_lbl = Text("a = 0.3 nm   |   V₁ = −0.4 eV",
                         font=DISPLAY, color=INK, font_size=22)
        given_lbl.move_to(UP * 2.2)
        self.play(Create(given_box), FadeIn(given_lbl), run_time=0.6)

        # State 3: Calculation
        calc_box = Rectangle(width=5.0, height=0.7, color=TEAL, fill_opacity=0.07)
        calc_box.set_stroke(TEAL, width=1.5)
        calc_box.move_to(UP * 0.9)
        calc_lbl = Text("Gap = 2 × |−0.4| = 0.8 eV", font=DISPLAY, color=TEAL, font_size=22)
        calc_lbl.move_to(UP * 0.9)
        self.play(Create(calc_box), FadeIn(calc_lbl), run_time=0.6)

        # State 4: No table lookup
        result_box = Rectangle(width=7.0, height=0.7, color=TEAL, fill_opacity=0.07)
        result_box.set_stroke(TEAL, width=1.8)
        result_box.move_to(UP * -0.5)
        result_lbl = Text("First band gap is 0.8 eV — no band theory book needed",
                          font=DISPLAY, color=INK, font_size=20)
        result_lbl.move_to(UP * -0.5)
        self.play(Create(result_box), FadeIn(result_lbl), run_time=0.5)

        # State 5: Second gap
        gap2_box = Rectangle(width=7.0, height=0.65, color=SLATE, fill_opacity=0.06)
        gap2_box.set_stroke(SLATE, width=1.2)
        gap2_box.move_to(UP * -1.8)
        gap2_lbl = Text("If V₂ = −0.1 eV: second gap = 0.2 eV  (independent)",
                        font=DISPLAY, color=SLATE, font_size=20)
        gap2_lbl.move_to(UP * -1.8)
        self.play(Create(gap2_box), FadeIn(gap2_lbl), run_time=0.5)

        self.wait(_dur("B09") - 2.7)


# ── B10 CARD ──────────────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Zone boundary degeneracy.\nMixed by V₁.\nGap = 2|V₁|.",
                        font=SERIF, color=INK, font_size=36, line_spacing=1.25)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B10") - 1.3)
