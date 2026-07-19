#!/usr/bin/env python3
"""why_hot_ones_are_jerks.py — Bear's Doodles: Why the Hot Ones Are Jerks.

Berkson's paradox. Scenes 1–3 (INTRO..A17) render here in Manim; scene 4
(A18–A22) is the doodle kicker — those beats are SKIPPED in this scene and
their Wan clips are concatenated by assemble.py in beat order.

THE ONE TRICK: the dot cloud is drawn from a seeded RNG (SEED=42), so scene 1,
scene 2, and scene 3 show literally the same 120 people. The selection score
is s = u + v; the two red cuts are the lines s=0.55 and s=1.45; the surviving
band is 0.55 <= s <= 1.45.

Render:
    ai
    manim -pqh why_hot_ones_are_jerks.py BearsDoodlesVideo
"""
import json
from pathlib import Path

import numpy as np
from manim import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent
SHEET = json.loads((HERE / "beat_sheet.json").read_text())
TIMINGS_PATH = HERE / "mp3" / "timings.json"
TIMINGS = json.loads(TIMINGS_PATH.read_text()) if TIMINGS_PATH.exists() else {}

META = SHEET["metadata"]
INK = "#1a1a1a"
ACCENT = META.get("accent_color", "#5A5653")
FORBIDDEN = META.get("forbidden_color", "#C0392B")
FONT = META.get("text_font", "Shadows Into Light")
TITLE = META.get("title", "")

# ── the shared population (seeded — scenes 1/2/3 show the same people) ──────
SEED = 42
_rng = np.random.default_rng(SEED)
N_DOTS = 120
UV = _rng.uniform(0.04, 0.96, size=(N_DOTS, 2))   # (attractive, nice) in unit box
LOW_CUT, HIGH_CUT = 0.55, 1.45                     # s = u + v thresholds

# axes rectangle in frame coords (16:9 frame is 14.22 x 8; stay in the middle)
X0, Y0, W, H = -4.6, -2.45, 9.2, 5.0


def px(u): return X0 + u * W
def py(v): return Y0 + v * H
def score(i): return UV[i, 0] + UV[i, 1]


def dur(beat_id: str, fallback: float = 4.0) -> float:
    return float(TIMINGS.get(beat_id, fallback))


def label(text: str, size: int = 36, color: str = INK):
    return Text(text, font=FONT, font_size=size, color=color)


class BearsDoodlesVideo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        for beat in SHEET["beats"]:
            bid = beat["beat_id"]
            btype = beat["beat_type"]
            audio = beat.get("audio_file") or f"mp3/beat-{bid}.mp3"
            if (HERE / audio).exists():
                self.add_sound(str(HERE / audio))

            if btype == "INTRO":
                self._intro(dur(bid, 3.0))
                continue
            if btype == "CUT":
                if self.mobjects:
                    self.play(FadeOut(*self.mobjects), run_time=0.4)
                    self.wait(0.1)

            if beat.get("render") == "doodle":
                # SLATE (borrowed from the vox slate law): the pass-1 cut is
                # always watchable; this slot's Wan clip replaces the slate at
                # final assembly (trim at A17 boundary + concat clips).
                self._slate(bid, beat.get("new_visual_element", ""), dur(bid))
                continue

            method = getattr(self, f"draw_{bid}", None)
            if method is not None:
                method(dur(bid))
            elif btype == "HOLD":
                self.wait(dur(bid, 2.0))
            else:
                ph = label(f"[{bid}]", size=28, color="#999999")
                self.play(Write(ph), run_time=min(1.5, dur(bid)))
                self.wait(max(0.1, dur(bid) - 1.5))
                self.play(FadeOut(ph), run_time=0.3)

    # ── slate for unfilled doodle slots (pass-1 watchability) ────────────────
    def _slate(self, bid: str, desc: str, t: float):
        prev = getattr(self, "_slate_grp", None)
        if prev is not None and prev in self.mobjects:
            self.play(FadeOut(prev), run_time=0.25)
        card = RoundedRectangle(width=9.5, height=3.4, corner_radius=0.25,
                                color="#999999", stroke_width=3)
        tid = label(bid, size=46, color="#999999").move_to(card.get_center() + UP * 0.6)
        de = label((desc or "doodle slot")[:52], size=26, color="#bbbbbb")
        de.next_to(tid, DOWN, buff=0.35)
        note = label("DOODLE SLOT — clip pending", size=20, color="#bbbbbb")
        note.next_to(card.get_bottom(), UP, buff=0.25)
        self._slate_grp = VGroup(card, tid, de, note)
        self.play(FadeIn(self._slate_grp), run_time=min(0.5, t * 0.25))
        self.wait(max(0.1, t - min(0.5, t * 0.25) - (0.25 if prev is not None else 0)))

    # ── INTRO ────────────────────────────────────────────────────────────────
    def _intro(self, t: float):
        brand = label("Bear's Doodles", size=54)
        title = label(TITLE, size=38, color=ACCENT).next_to(brand, DOWN, buff=0.5)
        self.play(Write(brand), run_time=min(1.2, t * 0.4))
        self.play(Write(title), run_time=min(1.0, t * 0.4))
        self.wait(max(0.2, t - 2.2))
        self.play(FadeOut(brand, title), run_time=0.4)

    # ── shared builders ─────────────────────────────────────────────────────
    def _axes(self):
        x_ax = Line([X0 - 0.2, Y0, 0], [X0 + W + 0.3, Y0, 0], color=INK, stroke_width=5)
        y_ax = Line([X0, Y0 - 0.2, 0], [X0, Y0 + H + 0.3, 0], color=INK, stroke_width=5)
        return VGroup(x_ax, y_ax)

    def _dots(self, keep=None):
        g = VGroup()
        for i in range(N_DOTS):
            if keep is not None and not keep(i):
                continue
            d = Dot([px(UV[i, 0]), py(UV[i, 1]), 0], radius=0.05, color=INK)
            d.set_opacity(0.9)
            g.add(d)
        return g

    def _cut_line(self, s):
        """The line u+v = s clipped to the unit box, in frame coords."""
        u1, v1 = (max(0.0, s - 1.0), min(1.0, s))
        u2, v2 = (min(1.0, s), max(0.0, s - 1.0))
        return Line([px(u1), py(v1), 0], [px(u2), py(v2), 0],
                    color=FORBIDDEN, stroke_width=6)

    def _hatch(self, corner):
        """A few light red hatch strokes in the excluded corner."""
        g = VGroup()
        if corner == "low":
            anchors = [(0.06, 0.06), (0.22, 0.06), (0.06, 0.22), (0.20, 0.20)]
        else:
            anchors = [(0.94, 0.94), (0.78, 0.94), (0.94, 0.78), (0.80, 0.80)]
        for (u, v) in anchors:
            g.add(Line([px(u) - 0.25, py(v) - 0.25, 0], [px(u) + 0.25, py(v) + 0.25, 0],
                       color=FORBIDDEN, stroke_width=3).set_opacity(0.3))
        return g

    # ── Scene 1 — the world as it is ────────────────────────────────────────
    def draw_A02(self, t):
        self.axes = self._axes()
        self.play(Create(self.axes), run_time=t * 0.7, rate_func=linear)
        self.wait(max(0.1, t * 0.3))

    def draw_A03(self, t):
        xl = label("attractive", size=30).move_to([px(0.85), Y0 - 0.55, 0])
        self.play(Write(xl), run_time=t * 0.7)
        self.wait(max(0.1, t * 0.3))

    def draw_A04(self, t):
        yl = label("nice", size=30).move_to([X0 + 0.9, py(0.97), 0])
        self.ylab = VGroup(yl)
        self.play(Write(yl), run_time=t * 0.7)
        self.wait(max(0.1, t * 0.3))

    def draw_A05(self, t):
        self.cloud = self._dots()
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in self.cloud],
                              lag_ratio=0.01), run_time=t * 0.85)
        self.wait(max(0.1, t * 0.15))

    def draw_A06(self, t):
        flat = Line([px(0.04), py(0.5), 0], [px(0.96), py(0.5), 0],
                    color=ACCENT, stroke_width=5)
        self.play(Create(flat), run_time=t * 0.7, rate_func=linear)
        self.wait(max(0.1, t * 0.3))

    # ── Scene 2 — your filters ──────────────────────────────────────────────
    def draw_A07(self, t):
        self.axes = self._axes()
        self.cloud = self._dots()
        self.play(Create(self.axes), run_time=t * 0.3)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in self.cloud],
                              lag_ratio=0.005), run_time=t * 0.5)
        self.wait(max(0.1, t * 0.2))

    def draw_A08(self, t):
        self.low_line = self._cut_line(LOW_CUT)
        self.play(Create(self.low_line), run_time=t * 0.7, rate_func=linear)
        self.wait(max(0.1, t * 0.3))

    def draw_A09(self, t):
        gone = VGroup(*[d for i, d in enumerate(self.cloud) if score(i) < LOW_CUT])
        hatch = self._hatch("low")
        self.play(gone.animate.set_opacity(0.12), FadeIn(hatch), run_time=t * 0.7)
        self.wait(max(0.1, t * 0.3))

    def draw_A10(self, t):
        self.high_line = self._cut_line(HIGH_CUT)
        self.play(Create(self.high_line), run_time=t * 0.7, rate_func=linear)
        self.wait(max(0.1, t * 0.3))

    def draw_A11(self, t):
        gone = VGroup(*[d for i, d in enumerate(self.cloud) if score(i) > HIGH_CUT])
        hatch = self._hatch("high")
        self.play(gone.animate.set_opacity(0.12), FadeIn(hatch), run_time=t * 0.7)
        self.wait(max(0.1, t * 0.3))

    def draw_A12(self, t):
        band = Polygon(
            [px(0.0), py(LOW_CUT), 0], [px(LOW_CUT), py(0.0), 0],
            [px(1.0), py(HIGH_CUT - 1.0), 0], [px(HIGH_CUT - 1.0), py(1.0), 0],
            color=ACCENT, stroke_width=4)
        band.set_fill(ACCENT, 0.06)
        self.play(Create(band), run_time=t * 0.6, rate_func=linear)
        self.wait(max(0.1, t * 0.4))

    # ── Scene 3 — the reveal ────────────────────────────────────────────────
    def draw_A13(self, t):
        self.axes = self._axes()
        self.band_dots = self._dots(keep=lambda i: LOW_CUT <= score(i) <= HIGH_CUT)
        self.play(Create(self.axes), run_time=min(0.5, t * 0.3))
        self.play(FadeIn(self.band_dots), run_time=min(0.7, t * 0.45))
        self.wait(max(0.1, t - min(0.5, t * 0.3) - min(0.7, t * 0.45)))

    def draw_A14(self, t):
        self.trend = Line([px(0.08), py(0.92), 0], [px(0.92), py(0.13), 0],
                          color=ACCENT, stroke_width=5)
        self.play(Create(self.trend), run_time=t * 0.7, rate_func=linear)
        self.wait(max(0.1, t * 0.3))

    def draw_A15(self, t):
        note = label("in YOUR pool", size=30, color=ACCENT).move_to([2.9, 1.9, 0])
        arr = Arrow(note.get_bottom() + DOWN * 0.05, [px(0.72), py(0.32), 0],
                    color=ACCENT, stroke_width=3, max_tip_length_to_length_ratio=0.12)
        self.play(Write(note), run_time=t * 0.5)
        self.play(Create(arr), run_time=t * 0.25)
        self.wait(max(0.1, t * 0.25))

    def draw_A16(self, t):
        ghosts = VGroup(self._cut_line(LOW_CUT), self._cut_line(HIGH_CUT))
        ghosts.set_stroke(opacity=0.4)
        self.play(FadeIn(ghosts), run_time=t * 0.6)
        self.wait(max(0.1, t * 0.4))

    def draw_A17(self, t):
        name = label("Berkson's paradox", size=42).move_to([0, 3.3, 0])
        under = Line(name.get_corner(DL) + DOWN * 0.12, name.get_corner(DR) + DOWN * 0.12,
                     color=ACCENT, stroke_width=3)
        self.play(Write(name), run_time=t * 0.6)
        self.play(Create(under), run_time=t * 0.2, rate_func=linear)
        self.wait(max(0.1, t * 0.2))
