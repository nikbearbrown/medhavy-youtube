import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np
import math

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ── B01: COLD OPEN — one vs many final states setup ──────────────────────────
class B01_OneVsMany(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        # Three horizontal "level" bars showing N=1, N=2, N=many
        n1_lbl = Text("1 final state:", font=DISPLAY, font_size=22, color=INK).move_to(LEFT * 4.5 + UP * 1.5)
        n2_lbl = Text("2 final states:", font=DISPLAY, font_size=22, color=INK).move_to(LEFT * 4.5 + UP * 0.0)
        nm_lbl = Text("continuum:", font=DISPLAY, font_size=22, color=INK).move_to(LEFT * 4.5 + DOWN * 1.5)
        # Arrows showing what happens
        osc1 = Text("oscillates back", font=SERIF, font_size=20, color=CRIMSON,
                    slant=ITALIC).move_to(RIGHT * 1.5 + UP * 1.5)
        osc2 = Text("partially damps", font=SERIF, font_size=20, color=TEAL,
                    slant=ITALIC).move_to(RIGHT * 1.5 + UP * 0.0)
        decay = Text("smooth decay", font=SERIF, font_size=20, color=TEAL,
                     slant=ITALIC).move_to(RIGHT * 1.5 + DOWN * 1.5)
        divider = Line(np.array([-1.0, 2.5, 0.0]), np.array([-1.0, -2.5, 0.0]),
                       color=INK, stroke_width=1.0)
        self.play(FadeIn(n1_lbl), FadeIn(n2_lbl), FadeIn(nm_lbl), Create(divider), run_time=0.4)
        self.play(FadeIn(osc1), run_time=dur * 0.30)
        self.play(FadeIn(osc2), run_time=dur * 0.25)
        self.play(FadeIn(decay), divider.animate.scale(0.95), run_time=dur * 0.45)


# ── B02: COLD OPEN — oscillation to exponential decay ────────────────────────
class B02_OscToDecay(Scene):
    def construct(self):
        dur = DUR.get("B02", 10.0)
        axes = Axes(x_range=[0, 8, 2], y_range=[0, 1.2, 0.5],
                    x_length=8.5, y_length=3.8,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        # Single-state Rabi oscillation
        osc_curve = axes.plot(lambda x: np.sin(2.0 * x) ** 2,
                              x_range=[0, 7.8], color=CRIMSON, stroke_width=2.5)
        # Exponential decay envelope
        decay_curve = axes.plot(lambda x: np.exp(-0.5 * x),
                                x_range=[0, 7.8], color=TEAL, stroke_width=3)
        x_lbl = Text("time", font=SERIF, font_size=18, color=INK, slant=ITALIC).next_to(axes, DOWN + RIGHT * 3, buff=0.1)
        y_lbl = Text("P(excited)", font=SERIF, font_size=18, color=INK, slant=ITALIC).next_to(axes, UP + LEFT * 2.5, buff=0.1)
        osc_lbl = Text("discrete: oscillates", font=SERIF, font_size=18,
                       color=CRIMSON, slant=ITALIC).move_to(np.array([2.0, 2.8, 0.0]))
        decay_lbl = Text("continuum: decays", font=SERIF, font_size=18,
                         color=TEAL, slant=ITALIC).move_to(np.array([4.5, 2.0, 0.0]))
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)
        self.play(Create(osc_curve), FadeIn(osc_lbl), run_time=dur * 0.45)
        self.play(Create(decay_curve), FadeIn(decay_lbl), run_time=dur * 0.55)


# ── B03: CARD — THE QUESTION (no scene needed) ────────────────────────────────


# ── B04: THE PROBLEM — single final state, coherent bounce ───────────────────
class B04_CoherentBounce(Scene):
    def construct(self):
        dur = DUR.get("B04", 11.0)
        title = Text("One final state: amplitude builds and returns", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        # Two boxes: initial state and one final state, with double arrow
        init_box = Rectangle(width=2.8, height=1.0, stroke_width=2, color=INK)
        init_box.set_fill(INK, opacity=0.12).move_to(LEFT * 3.5 + UP * 0.5)
        init_lbl = Text("|initial>", font=MONO, font_size=22, color=INK).move_to(LEFT * 3.5 + UP * 0.5)
        final_box = Rectangle(width=2.8, height=1.0, stroke_width=2, color=CRIMSON)
        final_box.set_fill(CRIMSON, opacity=0.12).move_to(RIGHT * 3.5 + UP * 0.5)
        final_lbl = Text("|final>", font=MONO, font_size=22, color=CRIMSON).move_to(RIGHT * 3.5 + UP * 0.5)
        fwd_arrow = Arrow(np.array([-2.0, 0.85, 0.0]), np.array([2.0, 0.85, 0.0]),
                          buff=0.1, color=CRIMSON, stroke_width=2)
        bwd_arrow = Arrow(np.array([2.0, 0.15, 0.0]), np.array([-2.0, 0.15, 0.0]),
                          buff=0.1, color=CRIMSON, stroke_width=2)
        bounce_lbl = Text("amplitude returns: population bounces forever", font=SERIF,
                          font_size=19, color=CRIMSON, slant=ITALIC).move_to(DOWN * 1.5)
        self.play(FadeIn(title), FadeIn(init_box), FadeIn(init_lbl), run_time=0.3)
        self.play(FadeIn(final_box), FadeIn(final_lbl), Create(fwd_arrow), run_time=dur * 0.40)
        self.play(Create(bwd_arrow), run_time=dur * 0.30)
        self.play(FadeIn(bounce_lbl), fwd_arrow.animate.scale(1.02), run_time=dur * 0.30)


# ── B05: THE PROBLEM — many states, dephasing amplitudes ─────────────────────
class B05_Dephasing(Scene):
    def construct(self):
        dur = DUR.get("B05", 11.0)
        title = Text("Many final states: each oscillates at a different frequency", font=DISPLAY,
                     font_size=20, color=INK).move_to(UP * 3.0)
        # Show 5 sinusoidal amplitude lines at different frequencies
        axes = Axes(x_range=[0, 4, 1], y_range=[-1.2, 1.2, 0.5],
                    x_length=7.5, y_length=3.2,
                    axis_config={"color": INK, "stroke_width": 1.0},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.3)
        colors = [TEAL, CRIMSON, SLATE, TEAL, CRIMSON]
        curves = VGroup()
        for i, freq in enumerate([1.8, 2.2, 2.6, 3.0, 3.4]):
            c = axes.plot(lambda x, f=freq: 0.18 * np.sin(f * x),
                          x_range=[0, 3.8], color=colors[i % len(colors)], stroke_width=2)
            curves.add(c)
        cancel_lbl = Text("they cancel each other — except at t=0", font=SERIF,
                          font_size=19, color=CRIMSON, slant=ITALIC).move_to(DOWN * 2.5)
        self.play(FadeIn(title), Create(axes), run_time=0.4)
        self.play(Create(curves), run_time=dur * 0.55)
        self.play(FadeIn(cancel_lbl), curves.animate.set_stroke(width=1.5), run_time=dur * 0.45)


# ── B06: THE MECHANISM — only initial slope survives ─────────────────────────
class B06_InitialSlope(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 1.2, 0.5],
                    x_length=7.5, y_length=3.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        # Sum of many oscillations → straight line (linear rise)
        linear = axes.plot(lambda x: 0.18 * x, x_range=[0, 4.8],
                           color=TEAL, stroke_width=3.5)
        # Wobble lines (individual)
        wobbles = VGroup()
        for i, freq in enumerate([2.5, 3.5, 4.5, 5.5]):
            c = axes.plot(lambda x, f=freq: 0.18 * x + 0.08 * np.sin(f * x) / max(0.1, x * 0.3),
                          x_range=[0.1, 4.8], color=CRIMSON, stroke_width=1.2, stroke_opacity=0.5)
            wobbles.add(c)
        x_lbl = Text("time", font=SERIF, font_size=18, color=INK, slant=ITALIC).next_to(axes, DOWN + RIGHT * 3, buff=0.1)
        y_lbl = Text("total P(excited)", font=SERIF, font_size=18, color=INK, slant=ITALIC).next_to(axes, UP + LEFT * 2.0, buff=0.1)
        slope_lbl = Text("slope = constant rate W", font=SERIF, font_size=19,
                         color=TEAL, slant=ITALIC).move_to(np.array([2.0, 2.8, 0.0]))
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(wobbles), run_time=dur * 0.35)
        self.play(Create(linear), FadeIn(slope_lbl), wobbles.animate.set_stroke(opacity=0.2), run_time=dur * 0.65)


# ── B07: THE MECHANISM — Fermi's golden rule formula ─────────────────────────
class B07_GoldenRule(Scene):
    def construct(self):
        dur = DUR.get("B07", 11.0)
        title = Text("Fermi's Golden Rule", font=DISPLAY, font_size=32, color=INK).move_to(UP * 3.0)
        formula = Text("W = (2*pi / h-bar) * |V_fi|^2 * rho(E)",
                       font=MONO, font_size=24, color=TEAL).move_to(UP * 1.7)
        box = Rectangle(width=9.5, height=0.9, stroke_width=2, color=TEAL)
        box.set_fill(TEAL, opacity=0.08).move_to(UP * 1.7)
        vfi_lbl = Text("|V_fi|^2 : matrix element — how hard the drive couples states", font=SERIF,
                       font_size=18, color=INK, slant=ITALIC).move_to(UP * 0.5)
        rho_lbl = Text("rho(E)  : density of final states at the transition energy", font=SERIF,
                       font_size=18, color=INK, slant=ITALIC).move_to(DOWN * 0.3)
        const_lbl = Text("W is constant → exponential decay", font=DISPLAY, font_size=22,
                         color=TEAL).move_to(DOWN * 1.5)
        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(box), FadeIn(formula), run_time=dur * 0.30)
        self.play(FadeIn(vfi_lbl), run_time=dur * 0.25)
        self.play(FadeIn(rho_lbl), run_time=dur * 0.20)
        self.play(FadeIn(const_lbl), box.animate.scale(1.01), run_time=dur * 0.25)


# ── B08: THE IMPLICATION — exponential lifetime ───────────────────────────────
class B08_ExponentialLifetime(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 1.1, 0.5],
                    x_length=7.5, y_length=3.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        exp_curve = axes.plot(lambda x: np.exp(-x), x_range=[0, 4.8],
                              color=TEAL, stroke_width=3.5)
        tau_line = DashedLine(np.array([-3.75, 0.0, 0.0]), np.array([-3.75 + 7.5 / 5, 0.0, 0.0]),
                              color=INK, stroke_width=1.5, dash_length=0.2)
        # Vertical tau marker
        tau_vline = DashedLine(np.array([-3.75 + 7.5 / 5, -1.75, 0.0]),
                               np.array([-3.75 + 7.5 / 5, 0.0, 0.0]),
                               color=SLATE, stroke_width=1.5, dash_length=0.2)
        tau_lbl = Text("tau = 1/W", font=MONO, font_size=20, color=TEAL).move_to(np.array([0.0, 2.8, 0.0]))
        formula_lbl = Text("P(t) = exp(-t/tau)", font=MONO, font_size=24, color=TEAL).move_to(np.array([1.5, 2.0, 0.0]))
        no_memory_lbl = Text("atom has no memory of when it was excited", font=SERIF,
                             font_size=18, color=INK, slant=ITALIC).move_to(DOWN * 2.2)
        x_lbl = Text("time", font=SERIF, font_size=18, color=INK, slant=ITALIC).next_to(axes, DOWN + RIGHT * 3, buff=0.1)
        y_lbl = Text("P(excited)", font=SERIF, font_size=18, color=INK, slant=ITALIC).next_to(axes, UP + LEFT * 2.0, buff=0.1)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)
        self.play(Create(exp_curve), run_time=dur * 0.35)
        self.play(Create(tau_vline), FadeIn(tau_lbl), FadeIn(formula_lbl), run_time=dur * 0.35)
        self.play(FadeIn(no_memory_lbl), exp_curve.animate.set_stroke(width=4.5), run_time=dur * 0.30)


# ── B09: THE IMPLICATION — density of states and Purcell ─────────────────────
class B09_DensityPurcell(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("More final states → faster decay", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        rho_lbl = Text("rho(E) increases => W increases => shorter lifetime", font=SERIF,
                       font_size=20, color=TEAL, slant=ITALIC).move_to(UP * 1.8)
        apps = [
            ("Free space", "rho_photon ~ omega^2 / c^3"),
            ("Purcell cavity", "rho_photon enhanced => faster decay"),
            ("Photonic crystal", "rho_photon suppressed => slower decay"),
        ]
        group = VGroup()
        for i, (name, desc) in enumerate(apps):
            box = Rectangle(width=10.5, height=1.0, stroke_width=0)
            box.set_fill(TEAL, opacity=0.08).move_to(np.array([0.0, 0.5 - i * 1.3, 0.0]))
            n_lbl = Text(name + ":", font=DISPLAY, font_size=19, color=TEAL).move_to(
                np.array([-3.2, 0.5 - i * 1.3, 0.0]))
            d_lbl = Text(desc, font=SERIF, font_size=17, color=INK, slant=ITALIC).move_to(
                np.array([2.0, 0.5 - i * 1.3, 0.0]))
            group.add(box, n_lbl, d_lbl)
        self.play(FadeIn(title), FadeIn(rho_lbl), run_time=0.4)
        self.play(FadeIn(group), run_time=dur * 0.60)
        self.play(group.animate.scale(1.01), run_time=dur * 0.40)


# ── B10: THE EXAMPLE — illustrative H 2p→1s ──────────────────────────────────
class B10_HydrogenExample(Scene):
    def construct(self):
        dur = DUR.get("B10", 13.0)
        title = Text("Illustrative: hydrogen 2p → 1s", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        subtitle = Text("(from chapter worked example, labeled illustrative)", font=SERIF,
                        font_size=17, color=INK, slant=ITALIC).move_to(UP * 2.4)
        params = [
            ("photon energy", "10.2 eV"),
            ("|r_fi|^2", "0.55 a_0^2"),
        ]
        param_group = VGroup()
        for i, (k, v) in enumerate(params):
            k_lbl = Text(k + ":", font=SERIF, font_size=21, color=INK,
                         slant=ITALIC).move_to(LEFT * 3.2 + UP * (0.9 - i * 0.85))
            v_lbl = Text(v, font=MONO, font_size=21, color=TEAL).move_to(
                RIGHT * 0.8 + UP * (0.9 - i * 0.85))
            param_group.add(k_lbl, v_lbl)
        rate_lbl = Text("W = 6 x 10^8 s^-1", font=MONO, font_size=24, color=TEAL).move_to(DOWN * 0.7)
        tau_lbl = Text("lifetime tau = 1.6 ns  (matches experiment)", font=MONO,
                       font_size=22, color=TEAL).move_to(DOWN * 1.5)
        highlight = Rectangle(width=9.0, height=0.65, stroke_width=0)
        highlight.set_fill(GOLD, opacity=0.30).move_to(DOWN * 1.5)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(FadeIn(param_group), run_time=dur * 0.30)
        self.play(FadeIn(rate_lbl), run_time=dur * 0.20)
        self.play(FadeIn(highlight), FadeIn(tau_lbl), run_time=dur * 0.25)
        self.wait(dur * 0.25)


# ── B11: RECAP — CARD beat — no scene needed ─────────────────────────────────
