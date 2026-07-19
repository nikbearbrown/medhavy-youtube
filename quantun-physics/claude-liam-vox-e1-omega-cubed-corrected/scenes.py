import sys,json,pathlib,math,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t,size=29): return Text(t,font=DISPLAY,font_size=size,color=INK).to_edge(UP)

class B02_TwoFactors(Scene):
 def construct(self):
  a=VGroup(Text("AVAILABLE MODES",font=DISPLAY,font_size=31,color=TEAL),Text("rho(omega)",font=MONO,font_size=42,color=INK),Text("how many places to emit",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); b=VGroup(Text("ONE-PHOTON COUPLING",font=DISPLAY,font_size=30,color=CRIMSON),Text("|matrix element|^2",font=MONO,font_size=34,color=INK),Text("how strongly each mode couples",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3)
  self.play(FadeIn(heading("THE VACUUM CONTRIBUTES TWO DISTINCT FACTORS")),FadeIn(a),FadeIn(b),run_time=1); hold(self,"B02")

class B03_GoldenRule(Scene):
 def construct(self):
  parts=VGroup(Text("RATE",font=MONO,font_size=48,color=INK),Text("proportional to",font=SERIF,font_size=29,color=INK),Text("|M|^2",font=MONO,font_size=50,color=CRIMSON),Text("x",font=MONO,font_size=40,color=INK),Text("rho(omega)",font=MONO,font_size=46,color=TEAL)).arrange(RIGHT,buff=.45); labs=VGroup(Text("coupling",font=SERIF,font_size=27,color=CRIMSON).shift(LEFT*1.2+DOWN*1.5),Text("final photon states",font=SERIF,font_size=27,color=TEAL).shift(RIGHT*3+DOWN*1.5))
  self.play(FadeIn(heading("FERMI'S GOLDEN RULE IS A PRODUCT")),FadeIn(parts),FadeIn(labs),run_time=1); hold(self,"B03")

class B04_ModeShells(Scene):
 def construct(self):
  rings=VGroup(*[Circle(radius=r,color=TEAL,stroke_opacity=.35+.12*i) for i,r in enumerate([.8,1.5,2.2])]); dots=VGroup(*[Dot(rings[2].point_at_angle(a),radius=.06,color=CRIMSON) for a in np.linspace(0,2*PI,20,endpoint=False)]); eq=VGroup(Text("shell area ~ k^2",font=MONO,font_size=36,color=INK),Text("k = omega / c",font=MONO,font_size=34,color=INK),Text("rho(omega) ~ omega^2",font=MONO,font_size=42,color=TEAL)).arrange(DOWN,buff=.4).move_to(RIGHT*3)
  rings.shift(LEFT*3); dots.shift(LEFT*3); self.play(FadeIn(heading("PHOTON MODES FILL SPHERICAL SHELLS IN K-SPACE")),LaggedStart(*[Create(x) for x in rings],lag_ratio=.2),FadeIn(dots),FadeIn(eq),run_time=1.2); hold(self,"B04",1.2)

class B05_FieldAmplitude(Scene):
 def construct(self):
  one=Text("ONE PHOTON",font=DISPLAY,font_size=31,color=INK).shift(UP*2); amp=Text("E_1ph ~ sqrt(omega)",font=MONO,font_size=48,color=TEAL); sq=Text("|d E_1ph|^2 ~ omega |d|^2",font=MONO,font_size=39,color=CRIMSON).shift(DOWN*1.6); arr=Arrow(amp.get_bottom(),sq.get_top(),color=INK)
  self.play(FadeIn(heading("FIELD NORMALIZATION SUPPLIES ONE MORE POWER")),FadeIn(one),FadeIn(amp),GrowArrow(arr),FadeIn(sq),run_time=1); hold(self,"B05")

class B06_Combine(Scene):
 def construct(self):
  row=VGroup(Text("omega^2",font=MONO,font_size=48,color=TEAL),Text("x",font=MONO,font_size=38,color=INK),Text("omega",font=MONO,font_size=48,color=CRIMSON),Text("=",font=MONO,font_size=38,color=INK),Text("omega^3",font=MONO,font_size=55,color=INK)).arrange(RIGHT,buff=.55).shift(UP*1); eq=Text("A_E1 = omega^3 |d|^2 / (3 pi eps0 hbar c^3)",font=MONO,font_size=31,color=INK).shift(DOWN*1.2); cap=Text("allowed E1 transition in homogeneous free space",font=SERIF,font_size=28,color=TEAL).shift(DOWN*2.2)
  self.play(FadeIn(heading("PHASE SPACE TIMES COUPLING GIVES THE CUBE")),FadeIn(row),FadeIn(eq),FadeIn(cap),run_time=1); hold(self,"B06")

class B07_Scaling(Scene):
 def construct(self):
  cards=VGroup(VGroup(Text("2x frequency",font=SERIF,font_size=29,color=INK),Text("8x rate",font=MONO,font_size=44,color=TEAL)).arrange(DOWN,buff=.5),VGroup(Text("10x frequency",font=SERIF,font_size=29,color=INK),Text("1000x rate",font=MONO,font_size=44,color=CRIMSON)).arrange(DOWN,buff=.5)).arrange(RIGHT,buff=2); tau=Text("lifetime tau = 1/A",font=MONO,font_size=35,color=INK).shift(DOWN*2)
  self.play(FadeIn(heading("HOLD THE DIPOLE STRENGTH FIXED")),FadeIn(cards),FadeIn(tau),run_time=1); hold(self,"B07")

class B08_ControlledComparison(Scene):
 def construct(self):
  axis=NumberLine(x_range=[8,15,1],length=10,include_numbers=False,color=INK); radio=Dot(axis.n2p(math.log10(3e8)),color=TEAL); optical=Dot(axis.n2p(math.log10(6e14)),color=CRIMSON); labs=VGroup(Text("300 MHz",font=MONO,font_size=29,color=TEAL).next_to(radio,DOWN),Text("600 THz",font=MONO,font_size=29,color=CRIMSON).next_to(optical,DOWN),Text("frequency ratio = 2,000,000",font=MONO,font_size=34,color=INK).shift(UP*1.5),Text("rate ratio = 8 x 10^18",font=MONO,font_size=40,color=CRIMSON).shift(DOWN*1.8))
  self.play(FadeIn(heading("A FAIR TEST KEEPS THE E1 DIPOLE MOMENT THE SAME")),Create(axis),FadeIn(radio),FadeIn(optical),FadeIn(labs),run_time=1); hold(self,"B08")

class B09_MatrixAudit(Scene):
 def construct(self):
  eq=Text("A ~ omega^3 |d|^2",font=MONO,font_size=49,color=INK).shift(UP*1.7); items=VGroup(*[Text("• "+x,font=SERIF,font_size=30,color=TEAL if i==0 else INK) for i,x in enumerate(["wave-function overlap","selection rules","multipole channel","electromagnetic environment"])]).arrange(DOWN,aligned_edge=LEFT,buff=.45).shift(DOWN*.7)
  self.play(FadeIn(heading("REAL TRANSITIONS CHANGE MORE THAN FREQUENCY")),FadeIn(eq),LaggedStart(*[FadeIn(x,shift=RIGHT*.2) for x in items],lag_ratio=.13),run_time=1); hold(self,"B09")

class B10_E1M1(Scene):
 def construct(self):
  left=VGroup(Text("ATOMIC OPTICAL LINE",font=DISPLAY,font_size=28,color=TEAL),Text("electric dipole E1",font=MONO,font_size=34,color=INK),Text("operator: e r",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("PROTON SPIN FLIP",font=DISPLAY,font_size=28,color=CRIMSON),Text("magnetic dipole M1",font=MONO,font_size=34,color=INK),Text("operator: magnetic moment",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3); no=Text("NOT THE SAME MATRIX ELEMENT",font=DISPLAY,font_size=30,color=CRIMSON).shift(DOWN*2.3)
  self.play(FadeIn(heading("THE PROTON COMPARISON CHANGES THE CHANNEL")),FadeIn(left),FadeIn(right),FadeIn(no),run_time=1); hold(self,"B10")

class B11_Environment(Scene):
 def construct(self):
  emitter=Dot(color=CRIMSON,radius=.16); free=VGroup(*[Arrow(emitter.get_center(),2.3*np.array([math.cos(a),math.sin(a),0]),color=TEAL,buff=.2) for a in np.linspace(0,2*PI,8,endpoint=False)]); walls=VGroup(Line(LEFT*4+UP*2.4,RIGHT*4+UP*2.4,color=INK),Line(LEFT*4+DOWN*2.4,RIGHT*4+DOWN*2.4,color=INK)); labs=VGroup(Text("cavity / surface / band gap",font=SERIF,font_size=30,color=INK).shift(DOWN*3),Text("local photon density changes",font=MONO,font_size=35,color=CRIMSON).shift(UP*2.8))
  self.play(FadeIn(heading("THE ENVIRONMENT CAN RESHAPE THE VACUUM MODES")),FadeIn(emitter),LaggedStart(*[GrowArrow(a) for a in free],lag_ratio=.08),Create(walls),FadeIn(labs),run_time=1.2); hold(self,"B11",1.2)

class B12_Channels(Scene):
 def construct(self):
  root=Text("E1 FORBIDDEN",font=DISPLAY,font_size=35,color=CRIMSON).shift(UP*2); kids=VGroup(*[Text(x,font=MONO,font_size=31,color=TEAL) for x in ["M1","E2","two-photon"]]).arrange(RIGHT,buff=1.4).shift(DOWN*.5); arrows=VGroup(*[Arrow(root.get_bottom(),k.get_top(),color=INK,buff=.15) for k in kids]); cap=Text("different operators, scalings, and lifetimes",font=SERIF,font_size=30,color=INK).shift(DOWN*2.2)
  self.play(FadeIn(heading("FORBIDDEN DOES NOT MEAN IMPOSSIBLE")),FadeIn(root),LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.15),FadeIn(kids),FadeIn(cap),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
 def construct(self):
  q=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=38,color=INK),Text("omega_2 = 3 omega_1",font=MONO,font_size=48,color=TEAL),Text("same |d| and same free space",font=SERIF,font_size=31,color=INK),Text("A_2 / A_1 = ?",font=MONO,font_size=45,color=CRIMSON)).arrange(DOWN,buff=.55)
  self.play(FadeIn(q),run_time=.8); hold(self,"B13",.8)

class B14_Answer(Scene):
 def construct(self):
  a=VGroup(Text("ANSWER",font=DISPLAY,font_size=38,color=INK),Text("A_2 / A_1 = 3^3",font=MONO,font_size=46,color=TEAL),Text("= 27",font=MONO,font_size=58,color=CRIMSON),Text("only when dipole strength and environment match",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.55)
  self.play(FadeIn(a),run_time=.8); hold(self,"B14",.8)

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  bg=FullScreenRectangle(fill_color="#1f1d1b",fill_opacity=1,stroke_width=0); title=Text("Why Electric-Dipole Spontaneous Emission\nSpeeds Up as Frequency Cubed",font=DISPLAY,font_size=35,color="#f4efe8",line_spacing=.8); sig=Text("Liam, in for Bear",font=SERIF,font_size=22,color="#c46b4f").shift(DOWN*1.2)
  self.add(bg); self.play(FadeIn(title),FadeIn(sig),run_time=.8); hold(self,"B15",.8)
