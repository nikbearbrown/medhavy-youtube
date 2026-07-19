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


# ── B01: COLD OPEN — resonant drive setup ────────────────────────────────────
class B01_ResonantDrive(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        atom_lbl = Text("atom", font=DISPLAY, font_size=36, color=TEAL).move_to(LEFT * 3.5 + UP * 0.5)
        g_lbl = Text("|g>  ground", font=MONO, font_size=22, color=INK).move_to(LEFT * 3.5 + DOWN * 0.3)
        e_lbl = Text("|e>  excited", font=MONO, font_size=22, color=TEAL).move_to(LEFT * 3.5 + DOWN * 1.1)
        arrow = Arrow(np.array([0.0, 0.5, 0.0]), np.array([2.0, 0.5, 0.0]),
                      buff=0.1, color=INK, stroke_width=2)
        laser_lbl = Text("resonant laser", font=SERIF, font_size=20, color=INK,
                         slant=ITALIC).move_to(np.array([1.0, 1.1, 0.0]))
        question = Text("P(excited) = ?", font=MONO, font_size=32, color=TEAL).move_to(RIGHT * 3.5 + UP * 1.5)
        divider = Line(np.array([0.0, 2.5, 0.0]), np.array([0.0, -1.8, 0.0]),
                       color=INK, stroke_width=1.0)
        self.play(FadeIn(atom_lbl), FadeIn(g_lbl), FadeIn(e_lbl), Create(divider), run_time=0.4)
        self.play(Create(arrow), FadeIn(laser_lbl), run_time=dur * 0.45)
        self.play(FadeIn(question), divider.animate.scale(0.95), run_time=dur * 0.55)


# ── B02: COLD OPEN — PT formula predicts 247% ────────────────────────────────
class B02_PT247(Scene):
    def construct(self):
        dur = DUR.get("B02", 10.0)
        title = Text("First-order perturbation theory:", font=DISPLAY, font_size=26,
                     color=INK).move_to(UP * 2.8)
        pt_formula = Text("P = (Omega * t / 2)^2", font=MONO, font_size=30, color=CRIMSON).move_to(UP * 1.6)
        box = Rectangle(width=7.5, height=1.0, stroke_width=2, color=CRIMSON)
        box.set_fill(CRIMSON, opacity=0.08).move_to(UP * 1.6)
        at_pi = Text("at the pi-pulse (Omega*t = pi):", font=SERIF, font_size=20,
                     color=INK, slant=ITALIC).move_to(UP * 0.4)
        result = Text("P = (pi/2)^2 = 2.47", font=MONO, font_size=32, color=CRIMSON).move_to(DOWN * 0.6)
        impossible = Text("247% — impossible.", font=DISPLAY, font_size=28,
                          color=CRIMSON).move_to(DOWN * 1.9)
        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(box), FadeIn(pt_formula), run_time=dur * 0.30)
        self.play(FadeIn(at_pi), run_time=dur * 0.25)
        self.play(FadeIn(result), run_time=dur * 0.25)
        self.play(FadeIn(impossible), box.animate.scale(1.02), run_time=dur * 0.20)


# ── B03: CARD — THE QUESTION (no scene needed) ────────────────────────────────


# ── B04: THE PROBLEM — PT assumption breakdown ───────────────────────────────
class B04_PTAssumption(Scene):
    def construct(self):
        dur = DUR.get("B04", 11.0)
        title = Text("PT assumption: ground state never empties", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Show population bar diagram: ground filling "stays full"
        g_bar_bg = Rectangle(width=3.5, height=1.0, stroke_width=1.5, color=INK)
        g_bar_bg.set_fill(GROUND, opacity=1.0).move_to(LEFT * 2.5 + UP * 0.5)
        g_bar_fill = Rectangle(width=3.5, height=1.0, stroke_width=0)
        g_bar_fill.set_fill(INK, opacity=0.5).move_to(LEFT * 2.5 + UP * 0.5)
        g_lbl = Text("|g> population", font=SERIF, font_size=18, color=INK,
                     slant=ITALIC).move_to(LEFT * 2.5 + UP * 1.9)
        assume_lbl = Text("PT assumes: c_g = 1 always", font=MONO, font_size=20,
                          color=CRIMSON).move_to(LEFT * 2.5 + DOWN * 0.6)
        e_bar_bg = Rectangle(width=3.5, height=1.0, stroke_width=1.5, color=INK)
        e_bar_bg.set_fill(GROUND, opacity=1.0).move_to(RIGHT * 2.5 + UP * 0.5)
        e_bar_empty = Rectangle(width=3.5, height=0.1, stroke_width=0)
        e_bar_empty.set_fill(TEAL, opacity=0.6).move_to(RIGHT * 2.5 + UP * 0.05)
        e_lbl = Text("|e> population", font=SERIF, font_size=18, color=TEAL,
                     slant=ITALIC).move_to(RIGHT * 2.5 + UP * 1.9)
        mistake_lbl = Text("keeps draining |g> even after it empied", font=SERIF,
                           font_size=18, color=CRIMSON, slant=ITALIC).move_to(DOWN * 2.0)
        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(g_bar_bg), FadeIn(g_bar_fill), FadeIn(g_lbl),
                  FadeIn(e_bar_bg), FadeIn(e_bar_empty), FadeIn(e_lbl), run_time=dur * 0.40)
        self.play(FadeIn(assume_lbl), run_time=dur * 0.30)
        self.play(FadeIn(mistake_lbl), g_bar_fill.animate.scale(1.02), run_time=dur * 0.30)


# ── B05: THE PROBLEM — parabola climbs past P=1 ──────────────────────────────
class B05_ParabolaClimbs(Scene):
    def construct(self):
        dur = DUR.get("B05", 10.0)
        axes = Axes(x_range=[0, 3.5, 1], y_range=[0, 3.0, 1],
                    x_length=7.0, y_length=4.2,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        parabola = axes.plot(lambda x: (x / 2) ** 2, x_range=[0, 3.4], color=CRIMSON, stroke_width=3.5)
        ceiling = DashedLine(np.array([-3.5, 0.2, 0.0]), np.array([3.5, 0.2, 0.0]),
                             color=TEAL, stroke_width=2, dash_length=0.25)
        ceiling_lbl = Text("P = 1  (ceiling)", font=SERIF, font_size=18, color=TEAL,
                           slant=ITALIC).move_to(np.array([3.2, 0.55, 0.0]))
        x_lbl = Text("Omega * t", font=SERIF, font_size=18, color=INK,
                     slant=ITALIC).next_to(axes, DOWN + RIGHT * 2, buff=0.1)
        y_lbl = Text("P(excited)", font=SERIF, font_size=18, color=INK,
                     slant=ITALIC).next_to(axes, UP + LEFT * 2.5, buff=0.1)
        pt_lbl = Text("PT: (Omega*t/2)^2", font=MONO, font_size=18, color=CRIMSON).move_to(np.array([1.5, 3.2, 0.0]))
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(parabola), run_time=dur * 0.50)
        self.play(Create(ceiling), FadeIn(ceiling_lbl), FadeIn(pt_lbl), run_time=dur * 0.50)


# ── B06: THE MECHANISM — exact Rabi sine ─────────────────────────────────────
class B06_RabiSine(Scene):
    def construct(self):
        dur = DUR.get("B06", 12.0)
        axes = Axes(x_range=[0, 3.5, 1], y_range=[0, 1.3, 0.5],
                    x_length=7.0, y_length=4.2,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        rabi_sine = axes.plot(lambda x: np.sin(x / 2) ** 2, x_range=[0, 3.4],
                              color=TEAL, stroke_width=3.5)
        ceiling = DashedLine(np.array([-2.8, 3.15, 0.0]), np.array([2.5, 3.15, 0.0]),
                             color=TEAL, stroke_width=1.5, dash_length=0.2)
        x_lbl = Text("Omega * t", font=SERIF, font_size=18, color=INK,
                     slant=ITALIC).next_to(axes, DOWN + RIGHT * 2, buff=0.1)
        y_lbl = Text("P(excited)", font=SERIF, font_size=18, color=INK,
                     slant=ITALIC).next_to(axes, UP + LEFT * 2.5, buff=0.1)
        rabi_lbl = Text("Rabi: sin^2(Omega*t/2)", font=MONO, font_size=18,
                        color=TEAL).move_to(np.array([1.5, 2.8, 0.0]))
        p1_lbl = Text("P = 1", font=SERIF, font_size=18, color=TEAL,
                      slant=ITALIC).move_to(np.array([3.1, 3.15, 0.0]))
        flip_lbl = Text("atom fully flips — then flips back", font=DISPLAY, font_size=20,
                        color=TEAL).move_to(DOWN * 2.7)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(rabi_sine), run_time=dur * 0.50)
        self.play(Create(ceiling), FadeIn(p1_lbl), FadeIn(rabi_lbl), run_time=dur * 0.25)
        self.play(FadeIn(flip_lbl), rabi_sine.animate.set_stroke(width=4.5), run_time=dur * 0.25)


# ── B07: THE MECHANISM — compare parabola and sine ───────────────────────────
class B07_CompareTwo(Scene):
    def construct(self):
        dur = DUR.get("B07", 11.0)
        axes = Axes(x_range=[0, 3.5, 1], y_range=[0, 3.0, 1],
                    x_length=7.5, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    x_axis_config={"include_numbers": False},
                    y_axis_config={"include_numbers": False},
                    tips=False)
        axes.move_to(DOWN * 0.1)
        parabola = axes.plot(lambda x: (x / 2) ** 2, x_range=[0, 3.4],
                             color=CRIMSON, stroke_width=3)
        rabi_sine = axes.plot(lambda x: np.sin(x / 2) ** 2, x_range=[0, 3.4],
                              color=TEAL, stroke_width=3)
        ceiling = DashedLine(np.array([-3.75, 0.2, 0.0]), np.array([3.75, 0.2, 0.0]),
                             color=SLATE, stroke_width=1.5, dash_length=0.2)
        ceiling_lbl = Text("P = 1", font=SERIF, font_size=16, color=SLATE,
                           slant=ITALIC).move_to(np.array([3.5, 0.5, 0.0]))
        x_lbl = Text("Omega * t", font=SERIF, font_size=18, color=INK,
                     slant=ITALIC).next_to(axes, DOWN + RIGHT * 2, buff=0.1)
        agree_lbl = Text("agree: Omega*t << 1", font=SERIF, font_size=18,
                         color=INK, slant=ITALIC).move_to(np.array([-2.0, 2.8, 0.0]))
        diverge_lbl = Text("diverge: Omega*t ~ pi", font=SERIF, font_size=18,
                           color=CRIMSON, slant=ITALIC).move_to(np.array([2.0, 2.8, 0.0]))
        pt_tag = Text("PT", font=MONO, font_size=16, color=CRIMSON).move_to(np.array([2.0, 1.8, 0.0]))
        rabi_tag = Text("Rabi", font=MONO, font_size=16, color=TEAL).move_to(np.array([2.3, 1.0, 0.0]))
        self.play(Create(axes), FadeIn(x_lbl), run_time=0.4)
        self.play(Create(parabola), Create(rabi_sine), run_time=dur * 0.45)
        self.play(Create(ceiling), FadeIn(ceiling_lbl), FadeIn(pt_tag), FadeIn(rabi_tag), run_time=dur * 0.25)
        self.play(FadeIn(agree_lbl), FadeIn(diverge_lbl), run_time=dur * 0.30)


# ── B08: THE IMPLICATION — pi-pulse comparison ───────────────────────────────
class B08_PiPulse(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("At the pi-pulse (Omega*t = pi):", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 2.8)
        exact_lbl = Text("Rabi (exact):", font=DISPLAY, font_size=24,
                         color=TEAL).move_to(LEFT * 3.0 + UP * 1.2)
        exact_val = Text("P = 1.00  (100%)", font=MONO, font_size=26,
                         color=TEAL).move_to(LEFT * 3.0 + UP * 0.35)
        pt_lbl = Text("Perturbation theory:", font=DISPLAY, font_size=24,
                      color=CRIMSON).move_to(RIGHT * 2.8 + UP * 1.2)
        pt_val = Text("P = 2.47  (247%)", font=MONO, font_size=26,
                      color=CRIMSON).move_to(RIGHT * 2.8 + UP * 0.35)
        divider = Line(np.array([0.0, 1.8, 0.0]), np.array([0.0, -0.5, 0.0]),
                       color=INK, stroke_width=1.5)
        impossible_box = Rectangle(width=4.5, height=0.85, stroke_width=2, color=CRIMSON)
        impossible_box.set_fill(CRIMSON, opacity=0.10).move_to(RIGHT * 2.8 + UP * 0.35)
        note = Text("atom fully flips — PT missed the return", font=SERIF,
                    font_size=20, color=INK, slant=ITALIC).move_to(DOWN * 1.5)
        self.play(FadeIn(title), Create(divider), run_time=0.4)
        self.play(FadeIn(exact_lbl), FadeIn(exact_val), run_time=dur * 0.35)
        self.play(FadeIn(pt_lbl), FadeIn(impossible_box), FadeIn(pt_val), run_time=dur * 0.35)
        self.play(FadeIn(note), divider.animate.scale(0.95), run_time=dur * 0.30)


# ── B09: THE IMPLICATION — qubit / NMR relevance ─────────────────────────────
class B09_Applications(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("Every quantum control experiment is Rabi's apparatus", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.0)
        apps = [
            ("Superconducting qubit", "microwave pi-pulse"),
            ("Trapped ion gate", "Raman laser pair"),
            ("NMR pulse", "radio-frequency flip"),
            ("Atom in laser", "optical Rabi cycle"),
        ]
        group = VGroup()
        for i, (name, sub) in enumerate(apps):
            x = -3.5 + (i % 2) * 6.8
            y = 0.5 - (i // 2) * 2.2
            box = Rectangle(width=5.8, height=1.6, stroke_width=0)
            box.set_fill(TEAL, opacity=0.10).move_to(np.array([x, y, 0.0]))
            n_lbl = Text(name, font=DISPLAY, font_size=20, color=TEAL).move_to(np.array([x, y + 0.35, 0.0]))
            s_lbl = Text(sub, font=SERIF, font_size=17, color=INK, slant=ITALIC).move_to(np.array([x, y - 0.28, 0.0]))
            group.add(box, n_lbl, s_lbl)
        valid_lbl = Text("Valid when: Omega*t << 1", font=MONO, font_size=18,
                         color=CRIMSON).move_to(DOWN * 2.7)
        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(group), run_time=dur * 0.60)
        self.play(FadeIn(valid_lbl), group.animate.scale(1.01), run_time=dur * 0.40)


# ── B10: THE EXAMPLE — illustrative numbers ──────────────────────────────────
class B10_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B10", 13.0)
        title = Text("Illustrative: two-level atom", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        subtitle = Text("(labeled illustrative — from chapter worked example)", font=SERIF,
                        font_size=17, color=INK, slant=ITALIC).move_to(UP * 2.4)
        params = [
            ("h-bar omega_0", "2.00 eV  (transition energy)"),
            ("h-bar Omega", "0.010 eV  (Rabi coupling)"),
        ]
        param_group = VGroup()
        for i, (k, v) in enumerate(params):
            k_lbl = Text(k + ":", font=SERIF, font_size=21, color=INK,
                         slant=ITALIC).move_to(LEFT * 3.0 + UP * (0.9 - i * 0.85))
            v_lbl = Text(v, font=MONO, font_size=20, color=TEAL).move_to(
                RIGHT * 1.2 + UP * (0.9 - i * 0.85))
            param_group.add(k_lbl, v_lbl)
        result_pt = Text("PT at pi-pulse: 2.47  (impossible)", font=MONO, font_size=22,
                         color=CRIMSON).move_to(DOWN * 1.0)
        result_rabi = Text("Rabi at pi-pulse: 1.00  (correct)", font=MONO, font_size=22,
                           color=TEAL).move_to(DOWN * 1.8)
        highlight = Rectangle(width=8.5, height=0.65, stroke_width=0)
        highlight.set_fill(GOLD, opacity=0.30).move_to(DOWN * 1.8)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(FadeIn(param_group), run_time=dur * 0.30)
        self.play(FadeIn(result_pt), run_time=dur * 0.25)
        self.play(FadeIn(highlight), FadeIn(result_rabi), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B11: RECAP — CARD beat — no scene needed ─────────────────────────────────
