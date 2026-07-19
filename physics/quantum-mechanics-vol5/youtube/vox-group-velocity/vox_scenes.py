"""vox_scenes.py — A quantum matter wave has two speeds — and the one you can see is wrong
(vox-group-velocity, slate cut, 16:9).
Color law: TEAL=envelope/group velocity; CRIMSON=phase crests; GOLD=reference pin.
Exclusions: no relativistic case; no Schrödinger derivation.
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


def _wave_packet_points(x_vals, t, k0=2.5, dk=0.5, omega0=None, v_phase=1.0, v_group=2.0,
                         amplitude=1.5, sigma=1.8, y_center=0.0):
    """
    Generate wave packet y-values: Gaussian envelope * carrier wave.
    Envelope moves at v_group, carrier at v_phase.
    omega0 defaults to k0 * v_phase.
    """
    if omega0 is None:
        omega0 = k0 * v_phase
    # Envelope center position
    x_env = v_group * t
    # Carrier phase
    carrier = np.cos(k0 * x_vals - omega0 * t)
    # Gaussian envelope
    envelope = amplitude * np.exp(-((x_vals - x_env) ** 2) / (2 * sigma ** 2))
    y = envelope * carrier + y_center
    return y


def _wave_polyline(x_vals, y_vals, color=TEAL, stroke_width=2.5):
    """Convert x, y arrays to a Manim VMobject polyline."""
    pts = [RIGHT * x + UP * y for x, y in zip(x_vals, y_vals)]
    poly = VMobject(color=color, stroke_width=stroke_width)
    poly.set_points_as_corners(pts)
    return poly


def _envelope_line(x_vals, t, v_group=2.0, amplitude=1.5, sigma=1.8, y_center=0.0,
                   color=TEAL, stroke_width=1.5):
    """Upper envelope curve (positive Gaussian)."""
    x_env = v_group * t
    env = amplitude * np.exp(-((x_vals - x_env) ** 2) / (2 * sigma ** 2)) + y_center
    pts = [RIGHT * x + UP * y for x, y in zip(x_vals, env)]
    poly = VMobject(color=color, stroke_width=stroke_width, stroke_opacity=0.6)
    poly.set_points_as_corners(pts)
    return poly


def _make_packet_group(t, n_pts=200, x_left=-6.5, x_right=6.5, y_center=0.0,
                       k0=2.5, v_phase=1.0, v_group=2.0, amplitude=1.5, sigma=1.8):
    """Build wave packet VGroup: carrier (CRIMSON) + envelope outline (TEAL)."""
    x_vals = np.linspace(x_left, x_right, n_pts)
    y_vals = _wave_packet_points(x_vals, t, k0=k0, v_phase=v_phase, v_group=v_group,
                                  amplitude=amplitude, sigma=sigma, y_center=y_center)
    carrier = _wave_polyline(x_vals, y_vals, color=CRIMSON, stroke_width=2.0)
    env_up = _envelope_line(x_vals, t, v_group=v_group, amplitude=amplitude, sigma=sigma,
                            y_center=y_center, color=TEAL, stroke_width=2.0)
    x_env = v_group * t
    env_neg = amplitude * np.exp(-((x_vals - x_env) ** 2) / (2 * sigma ** 2))
    pts_down = [RIGHT * x + UP * (-ey + y_center) for x, ey in zip(x_vals, env_neg)]
    env_down = VMobject(color=TEAL, stroke_width=2.0, stroke_opacity=0.6)
    env_down.set_points_as_corners(pts_down)
    return VGroup(carrier, env_up, env_down)


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("A quantum matter wave\nhas two speeds — and the\none you can see is wrong",
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
        headline = Text("De Broglie wave crests\nmove at half the electron's\nspeed. Why?",
                        font=SERIF, color=INK, font_size=34, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — phase velocity = v/2 ───────────────────────────────────
class B03_PhaseVelocity(Scene):
    def construct(self):
        """Show the phase velocity formula chain: E = p^2/2m → omega/k = v/2."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        # State 1: Title
        title = Text("Phase velocity for a free electron",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Dispersion relation row
        disp_box = Rectangle(width=5.5, height=0.75, color=SLATE, fill_opacity=0.08)
        disp_box.set_stroke(SLATE, width=1.2)
        disp_box.move_to(UP * 2.0)
        disp_lbl = Text("ω = ℏk² / 2m", font=SERIF, color=INK, font_size=28, slant=ITALIC)
        disp_lbl.move_to(UP * 2.0)
        self.play(Create(disp_box), FadeIn(disp_lbl), run_time=0.6)

        # State 3: Phase velocity box
        vph_box = Rectangle(width=5.5, height=0.75, color=CRIMSON, fill_opacity=0.08)
        vph_box.set_stroke(CRIMSON, width=1.5)
        vph_box.move_to(UP * 0.8)
        vph_lbl = Text("v_ph = ω/k = ℏk/2m = p/2m = v/2",
                       font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        vph_lbl.move_to(UP * 0.8)
        self.play(Create(vph_box), FadeIn(vph_lbl), run_time=0.6)

        # State 4: Highlight arrow pointing to v/2
        highlight_arr = Arrow(LEFT * 1.5 + UP * -0.2, RIGHT * 0.5 + UP * -0.2,
                              buff=0.05, stroke_width=2.5, color=CRIMSON,
                              max_tip_length_to_length_ratio=0.20)
        crest_note = Text("Crests move at v/2", font=DISPLAY, color=CRIMSON, font_size=22,
                          weight=BOLD)
        crest_note.move_to(UP * -0.8)
        self.play(Create(highlight_arr), FadeIn(crest_note), run_time=0.5)

        # State 5: Gold bar — "NOT the particle"
        gold_bar = Rectangle(width=4.0, height=0.5, color=GOLD, fill_opacity=0.28)
        gold_bar.set_stroke(GOLD, width=0)
        gold_bar.move_to(UP * -1.8)
        not_particle_lbl = Text("Phase pattern — not the particle",
                                font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        not_particle_lbl.move_to(UP * -1.8)
        self.play(FadeIn(gold_bar), FadeIn(not_particle_lbl), run_time=0.5)

        self.wait(_dur("B03") - 2.7)


# ── B04 THE PROBLEM — plane wave, need a packet ──────────────────────────────
class B04_PlaneWaveProblem(Scene):
    def construct(self):
        """Plane wave vs localized packet setup."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("A plane wave has no position",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: A flat sinusoidal wave (no envelope) — plane wave
        x_vals = np.linspace(-6.0, 6.0, 300)
        y_plane = 1.2 * np.cos(2.5 * x_vals)
        plane_pts = [RIGHT * x + UP * (y + 1.0) for x, y in zip(x_vals, y_plane)]
        plane_wave = VMobject(color=CRIMSON, stroke_width=2.0)
        plane_wave.set_points_as_corners(plane_pts)
        plane_lbl = Text("Plane wave: uniform forever, no position",
                         font=DISPLAY, color=CRIMSON, font_size=19)
        plane_lbl.move_to(UP * -0.4)
        self.play(Create(plane_wave), FadeIn(plane_lbl), run_time=0.7)

        # State 3: Add packet envelope on lower half
        packet_grp = _make_packet_group(t=0, y_center=-1.8)
        packet_lbl = Text("Wave packet: localized, has position",
                          font=DISPLAY, color=TEAL, font_size=19)
        packet_lbl.move_to(UP * -3.0)
        self.play(Create(packet_grp), FadeIn(packet_lbl), run_time=0.7)

        # State 4: Axis line separating the two
        sep_line = Line(LEFT * 6.5, RIGHT * 6.5, color=SLATE, stroke_width=0.8)
        sep_line.move_to(UP * -0.1)
        self.play(Create(sep_line), run_time=0.4)

        # State 5: Bracket labels
        brace_plane = Rectangle(width=0.15, height=2.0, color=CRIMSON, fill_opacity=0.30)
        brace_plane.set_stroke(CRIMSON, width=0)
        brace_plane.move_to(LEFT * 6.8 + UP * 1.0)
        brace_packet = Rectangle(width=0.15, height=2.0, color=TEAL, fill_opacity=0.30)
        brace_packet.set_stroke(TEAL, width=0)
        brace_packet.move_to(LEFT * 6.8 + UP * -1.8)
        self.play(FadeIn(brace_plane), FadeIn(brace_packet), run_time=0.4)

        self.wait(_dur("B04") - 2.7)


# ── B05 THE MECHANISM — carrier + envelope split ─────────────────────────────
class B05_CarrierEnvelope(Scene):
    def construct(self):
        """Show carrier at v_phase, envelope at v_group, at two time snapshots."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Carrier + envelope: two speeds",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Packet at t=0
        t0 = 0.0
        grp0 = _make_packet_group(t0, amplitude=1.6)
        x_crest0 = -2.0  # crest position at t=0 (a local maximum)
        crest_dot0 = Dot(RIGHT * x_crest0, color=CRIMSON, radius=0.12)
        env_dot0 = Dot(RIGHT * (2.0 * t0), color=TEAL, radius=0.15)  # envelope peak
        t0_lbl = Text("t = 0", font=DISPLAY, color=INK, font_size=20)
        t0_lbl.move_to(LEFT * 5.5 + UP * 2.6)
        self.play(Create(grp0), FadeIn(crest_dot0), FadeIn(env_dot0), FadeIn(t0_lbl), run_time=0.7)

        # State 3: Speed labels
        v_phase_lbl = Text("Carrier crests: v/2 →", font=DISPLAY, color=CRIMSON, font_size=18)
        v_phase_lbl.move_to(RIGHT * 1.0 + UP * -2.1)
        v_group_lbl = Text("Envelope peak: v →", font=DISPLAY, color=TEAL, font_size=18)
        v_group_lbl.move_to(RIGHT * 1.0 + UP * -2.7)
        self.play(FadeIn(v_phase_lbl), FadeIn(v_group_lbl), run_time=0.5)

        # State 4: Packet at t=0.6 (time advanced, envelope moved more than crests)
        t1 = 0.6
        grp1 = _make_packet_group(t1, amplitude=1.6)
        x_crest1 = x_crest0 + 1.0 * t1  # carrier crest moved at v_phase=1.0
        crest_dot1 = Dot(RIGHT * x_crest1, color=CRIMSON, radius=0.12)
        env_dot1 = Dot(RIGHT * (2.0 * t1), color=TEAL, radius=0.15)
        t1_lbl = Text("t = 0.6", font=DISPLAY, color=INK, font_size=20)
        t1_lbl.move_to(LEFT * 5.5 + UP * 2.0)
        self.play(
            Transform(grp0, grp1),
            Transform(crest_dot0, crest_dot1),
            Transform(env_dot0, env_dot1),
            FadeOut(t0_lbl), FadeIn(t1_lbl),
            run_time=0.9,
        )

        # State 5: Lines showing distance traveled — placed left and right, below packet
        dist_env = Line(LEFT * 2.0 + UP * -1.8, LEFT * 2.0 + RIGHT * 2.0 * t1 + UP * -1.8,
                        color=TEAL, stroke_width=2.5)
        dist_crest = Line(RIGHT * 1.5 + UP * -1.8, RIGHT * 1.5 + RIGHT * 1.0 * t1 + UP * -1.8,
                          color=CRIMSON, stroke_width=2.5)
        dist_lbl = Text("Env traveled 2x crest distance",
                        font=DISPLAY, color=INK, font_size=18)
        dist_lbl.move_to(UP * -2.5)
        self.play(Create(dist_env), Create(dist_crest), FadeIn(dist_lbl), run_time=0.5)

        # State 6: Summary box
        summary_box = Rectangle(width=6.5, height=0.55, color=GOLD, fill_opacity=0.22)
        summary_box.set_stroke(GOLD, width=0)
        summary_box.move_to(UP * -3.3)
        summary_lbl = Text("Carrier at v_phase  |  Envelope at v_group",
                           font=DISPLAY, color=INK, font_size=17)
        summary_lbl.move_to(UP * -3.3)
        self.play(FadeIn(summary_box), FadeIn(summary_lbl), run_time=0.5)

        # State 7: Two arrows side-by-side — showing distance difference
        arr_phase = Arrow(LEFT * 5.0 + UP * -1.3, LEFT * 5.0 + RIGHT * 1.0 * t1 + UP * -1.3,
                          buff=0, stroke_width=2.5, color=CRIMSON,
                          max_tip_length_to_length_ratio=0.15)
        arr_group = Arrow(RIGHT * 3.0 + UP * -1.3, RIGHT * 3.0 + RIGHT * 2.0 * t1 + UP * -1.3,
                          buff=0, stroke_width=2.5, color=TEAL,
                          max_tip_length_to_length_ratio=0.15)
        self.play(Create(arr_phase), Create(arr_group), run_time=0.5)

        self.wait(_dur("B05") - 4.6)


# ── B06 THE MECHANISM — group velocity = v ───────────────────────────────────
class B06_GroupVelocity(Scene):
    def construct(self):
        """Show d-omega/dk = v formula and summary comparison."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Group velocity: the derivative of dispersion",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: dispersion relation
        disp_box = Rectangle(width=5.0, height=0.75, color=SLATE, fill_opacity=0.08)
        disp_box.set_stroke(SLATE, width=1.2)
        disp_box.move_to(UP * 2.0)
        disp_lbl = Text("ω = ℏk² / 2m", font=SERIF, color=INK, font_size=28, slant=ITALIC)
        disp_lbl.move_to(UP * 2.0)
        self.play(Create(disp_box), FadeIn(disp_lbl), run_time=0.6)

        # State 3: Group velocity derivation
        vg_box = Rectangle(width=6.5, height=0.75, color=TEAL, fill_opacity=0.08)
        vg_box.set_stroke(TEAL, width=1.8)
        vg_box.move_to(UP * 0.8)
        vg_lbl = Text("v_g = dω/dk = ℏk/m = p/m = v",
                      font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        vg_lbl.move_to(UP * 0.8)
        self.play(Create(vg_box), FadeIn(vg_lbl), run_time=0.6)

        # State 4: Phase velocity comparison row
        vph_box = Rectangle(width=4.5, height=0.65, color=CRIMSON, fill_opacity=0.08)
        vph_box.set_stroke(CRIMSON, width=1.5)
        vph_box.move_to(UP * -0.5)
        vph_lbl = Text("v_ph = ω/k = v/2  (crests)",
                       font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        vph_lbl.move_to(UP * -0.5)
        self.play(Create(vph_box), FadeIn(vph_lbl), run_time=0.5)

        # State 5: Gold comparison bar — "particle rides envelope"
        gold_bar = Rectangle(width=5.5, height=0.55, color=GOLD, fill_opacity=0.28)
        gold_bar.set_stroke(GOLD, width=0)
        gold_bar.move_to(UP * -1.8)
        particle_lbl = Text("Particle rides the envelope at v",
                            font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        particle_lbl.move_to(UP * -1.8)
        self.play(FadeIn(gold_bar), FadeIn(particle_lbl), run_time=0.5)

        self.wait(_dur("B06") - 2.7)


# ── B07 THE IMPLICATION — reference pin showing crests sliding back ───────────
class B07_ReferencePinSlip(Scene):
    def construct(self):
        """Envelope moves right, crests slide BACKWARD through the pin."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Pin the envelope — watch the crests slip",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Packet at t=0 with gold vertical reference line at envelope peak (x=0)
        t0 = 0.0
        grp0 = _make_packet_group(t0, amplitude=1.5, y_center=-0.3)
        ref_line = Line(UP * 2.0, DOWN * 2.0, color=GOLD, stroke_width=2.5)
        ref_line.move_to(RIGHT * 0.0)
        ref_lbl = Text("Pin", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        ref_lbl.move_to(RIGHT * 0.0 + UP * 2.4)
        self.play(Create(grp0), Create(ref_line), FadeIn(ref_lbl), run_time=0.7)

        # State 3: Add crest marker dot at a local crest
        crest_x0 = -1.26  # near the envelope center, a crest
        crest_dot = Dot(RIGHT * crest_x0 + UP * -0.3, color=CRIMSON, radius=0.14)
        crest_lbl = Text("crest", font=DISPLAY, color=CRIMSON, font_size=16)
        crest_lbl.move_to(RIGHT * crest_x0 + UP * 0.3)
        self.play(FadeIn(crest_dot), FadeIn(crest_lbl), run_time=0.5)

        # State 4: Advance time — envelope peak moves right past pin (pin stays at 0)
        # but crests only advance half as far
        t1 = 0.8
        grp1 = _make_packet_group(t1, amplitude=1.5, y_center=-0.3)
        # New crest position: moved at v_phase=1.0 per unit time
        crest_x1 = crest_x0 + 1.0 * t1
        crest_dot1 = Dot(RIGHT * crest_x1 + UP * -0.3, color=CRIMSON, radius=0.14)
        crest_lbl1 = Text("crest moved right", font=DISPLAY, color=CRIMSON, font_size=16)
        crest_lbl1.move_to(RIGHT * crest_x1 + UP * 0.3)
        env_note = Text("Envelope past pin →", font=DISPLAY, color=TEAL, font_size=18)
        env_note.move_to(RIGHT * 2.5 + UP * -2.3)
        self.play(
            Transform(grp0, grp1),
            Transform(crest_dot, crest_dot1),
            FadeOut(crest_lbl), FadeIn(crest_lbl1),
            FadeIn(env_note),
            run_time=0.9,
        )

        # State 5: Lag arrow showing crests fell behind envelope
        lag_arrow = Arrow(RIGHT * crest_x1 + UP * -1.6,
                          RIGHT * 2.0 * t1 + UP * -1.6,
                          buff=0.05, stroke_width=2.0, color=CRIMSON,
                          max_tip_length_to_length_ratio=0.15)
        lag_lbl = Text("Crests lag behind envelope",
                       font=DISPLAY, color=CRIMSON, font_size=18)
        lag_lbl.move_to(UP * -2.8)
        self.play(Create(lag_arrow), FadeIn(lag_lbl), run_time=0.5)

        # State 6: Box highlight — detector measures envelope, not crests
        det_box = Rectangle(width=5.5, height=0.6, color=TEAL, fill_opacity=0.09)
        det_box.set_stroke(TEAL, width=1.5)
        det_box.move_to(UP * -3.5)
        det_lbl = Text("Detector measures envelope arrival",
                       font=DISPLAY, color=TEAL, font_size=18)
        det_lbl.move_to(UP * -3.5)
        self.play(Create(det_box), FadeIn(det_lbl), run_time=0.5)

        self.wait(_dur("B07") - 4.1)


# ── B08 THE IMPLICATION — phase vs group summary comparison ───────────────────
class B08_PhaseVsGroup(Scene):
    def construct(self):
        """Two-row comparison: phase speed and group speed side by side."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Two velocities — one physical",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Phase row
        phase_box = Rectangle(width=9.0, height=1.1, color=CRIMSON, fill_opacity=0.07)
        phase_box.set_stroke(CRIMSON, width=1.5)
        phase_box.move_to(UP * 1.5)
        phase_lbl = Text("Phase velocity:  v/2   — moves the crest pattern",
                         font=DISPLAY, color=CRIMSON, font_size=21)
        phase_lbl.move_to(UP * 1.5)
        self.play(Create(phase_box), FadeIn(phase_lbl), run_time=0.6)

        # State 3: Group row
        group_box = Rectangle(width=9.0, height=1.1, color=TEAL, fill_opacity=0.07)
        group_box.set_stroke(TEAL, width=1.8)
        group_box.move_to(UP * 0.0)
        group_lbl = Text("Group velocity:   v     — moves the particle",
                         font=DISPLAY, color=TEAL, font_size=21)
        group_lbl.move_to(UP * 0.0)
        self.play(Create(group_box), FadeIn(group_lbl), run_time=0.6)

        # State 4: no-signal note
        nosig_box = Rectangle(width=7.5, height=0.7, color=SLATE, fill_opacity=0.07)
        nosig_box.set_stroke(SLATE, width=1.2)
        nosig_box.move_to(UP * -1.3)
        nosig_lbl = Text("Phase carries no signal, no energy, no particle",
                         font=DISPLAY, color=INK, font_size=20)
        nosig_lbl.move_to(UP * -1.3)
        self.play(Create(nosig_box), FadeIn(nosig_lbl), run_time=0.5)

        # State 5: Gold highlight row — "equal only in non-dispersive medium"
        eq_bar = Rectangle(width=7.5, height=0.55, color=GOLD, fill_opacity=0.28)
        eq_bar.set_stroke(GOLD, width=0)
        eq_bar.move_to(UP * -2.4)
        eq_lbl = Text("Equal only when ω ∝ k (non-dispersive)", font=DISPLAY, color=INK,
                      font_size=19)
        eq_lbl.move_to(UP * -2.4)
        self.play(FadeIn(eq_bar), FadeIn(eq_lbl), run_time=0.5)

        self.wait(_dur("B08") - 2.7)


# ── B09 THE EXAMPLE — 100V electron ──────────────────────────────────────────
class B09_Electron100V(Scene):
    def construct(self):
        """Numerical example: 100V electron, phase = v/2, group = v."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("100 V electron: two speeds in numbers",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Electron speed row
        v_box = Rectangle(width=7.0, height=0.75, color=INK, fill_opacity=0.06)
        v_box.set_stroke(INK, width=1.2)
        v_box.move_to(UP * 2.1)
        v_lbl = Text("Electron speed v ≈ 6 × 10⁶ m/s", font=DISPLAY, color=INK, font_size=22)
        v_lbl.move_to(UP * 2.1)
        self.play(Create(v_box), FadeIn(v_lbl), run_time=0.6)

        # State 3: Phase velocity row
        vph_box = Rectangle(width=7.0, height=0.75, color=CRIMSON, fill_opacity=0.07)
        vph_box.set_stroke(CRIMSON, width=1.5)
        vph_box.move_to(UP * 0.9)
        vph_lbl = Text("Crest speed v_ph = v/2 ≈ 3 × 10⁶ m/s",
                       font=DISPLAY, color=CRIMSON, font_size=22)
        vph_lbl.move_to(UP * 0.9)
        self.play(Create(vph_box), FadeIn(vph_lbl), run_time=0.5)

        # State 4: Group velocity row
        vg_box = Rectangle(width=7.0, height=0.75, color=TEAL, fill_opacity=0.07)
        vg_box.set_stroke(TEAL, width=1.8)
        vg_box.move_to(UP * -0.4)
        vg_lbl = Text("Envelope speed v_g = v ≈ 6 × 10⁶ m/s",
                      font=DISPLAY, color=TEAL, font_size=22)
        vg_lbl.move_to(UP * -0.4)
        self.play(Create(vg_box), FadeIn(vg_lbl), run_time=0.5)

        # State 5: Detector note
        det_line = Line(LEFT * 5.5 + UP * -1.6, RIGHT * 5.5 + UP * -1.6,
                        color=SLATE, stroke_width=0.8)
        det_note = Text("Detector clicks at group-velocity arrival time",
                        font=DISPLAY, color=INK, font_size=19)
        det_note.move_to(UP * -2.3)
        ratio_note = Text("Quadratic dispersion (ω ∝ k²) locks this 2:1 ratio",
                          font=DISPLAY, color=SLATE, font_size=18)
        ratio_note.move_to(UP * -3.0)
        self.play(Create(det_line), FadeIn(det_note), FadeIn(ratio_note), run_time=0.5)

        self.wait(_dur("B09") - 3.1)


# ── B10 CARD ──────────────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Phase: ω/k = v/2.\nGroup: dω/dk = v.\nParticle rides the envelope.",
                        font=SERIF, color=INK, font_size=34, line_spacing=1.25)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B10") - 1.3)
