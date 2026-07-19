import sys,json,pathlib,math,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t,size=29): return Text(t,font=DISPLAY,font_size=size,color=INK).to_edge(UP)

class B02_ErrorMeasure(Scene):
 def construct(self):
  bad=VGroup(Text("POINTWISE %",font=DISPLAY,font_size=31,color=CRIMSON),Text("nodes can divide by zero",font=SERIF,font_size=28,color=INK),Text("normalization changes scale",font=SERIF,font_size=28,color=INK)).arrange(DOWN,buff=.45).move_to(LEFT*3); good=VGroup(Text("NORMALIZED STATE DISTANCE",font=DISPLAY,font_size=28,color=TEAL),Text("choose global phase",font=SERIF,font_size=29,color=INK),Text("compare directions in state space",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.45).move_to(RIGHT*3)
  self.play(FadeIn(heading("FIRST DEFINE WHAT 'WRONG WAVEFUNCTION' MEANS")),FadeIn(bad),FadeIn(good),run_time=1); hold(self,"B02")

class B03_Landscape(Scene):
 def construct(self):
  ax=Axes(x_range=[-2,2,1],y_range=[0,4,1],x_length=8,y_length=4.8,axis_config={"color":INK},tips=False).shift(DOWN*.5); bowl=ax.plot(lambda x:x*x,x_range=[-2,2],color=TEAL); dot=Dot(ax.c2p(0,0),color=CRIMSON); tangent=Line(ax.c2p(-1,0),ax.c2p(1,0),color=CRIMSON); labs=VGroup(Text("exact ground state",font=SERIF,font_size=28,color=CRIMSON).next_to(dot,DOWN),Text("first derivative = 0",font=MONO,font_size=35,color=INK).shift(UP*2.2))
  self.play(FadeIn(heading("THE RAYLEIGH QUOTIENT IS STATIONARY AT ITS MINIMUM")),FadeIn(ax),Create(bowl),FadeIn(dot),Create(tangent),FadeIn(labs),run_time=1); hold(self,"B03")

class B04_ToyState(Scene):
 def construct(self):
  eq=VGroup(Text("|psi_eps> =",font=MONO,font_size=41,color=INK),Text("sqrt(1-eps^2) |0>",font=MONO,font_size=39,color=TEAL),Text("+ eps |1>",font=MONO,font_size=43,color=CRIMSON)).arrange(RIGHT,buff=.4); norm=Text("<psi_eps|psi_eps> = 1",font=MONO,font_size=42,color=INK).shift(DOWN*1.8); basis=VGroup(Text("ground direction",font=SERIF,font_size=28,color=TEAL).shift(LEFT*2.5+UP*1.5),Text("orthogonal excited direction",font=SERIF,font_size=28,color=CRIMSON).shift(RIGHT*2.5+UP*1.5))
  self.play(FadeIn(heading("USE AN EXACTLY NORMALIZED TWO-STATE DEFORMATION")),FadeIn(eq),FadeIn(norm),FadeIn(basis),run_time=1); hold(self,"B04")

class B05_EnergyExpectation(Scene):
 def construct(self):
  eq=VGroup(Text("E[psi_eps] =",font=MONO,font_size=42,color=INK),Text("(1-eps^2) E0",font=MONO,font_size=42,color=TEAL),Text("+ eps^2 E1",font=MONO,font_size=42,color=CRIMSON)).arrange(RIGHT,buff=.45).shift(UP*.5); cross=Text("cross terms = 0",font=MONO,font_size=39,color=INK).shift(DOWN*1.3); why=Text("orthogonal energy eigenstates",font=SERIF,font_size=29,color=INK).shift(DOWN*2.2)
  self.play(FadeIn(heading("THE EXPECTATION IS A PROBABILITY-WEIGHTED AVERAGE")),FadeIn(eq),FadeIn(cross),FadeIn(why),run_time=1); hold(self,"B05")

class B06_QuadraticError(Scene):
 def construct(self):
  eq=VGroup(Text("E[psi_eps] - E0",font=MONO,font_size=46,color=INK),Text("= eps^2 (E1-E0)",font=MONO,font_size=52,color=CRIMSON),Text("NO linear eps term",font=DISPLAY,font_size=31,color=TEAL),Text("10% amplitude -> 1% excited weight",font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.55)
  self.play(FadeIn(heading("NORMALIZATION REMOVES THE FIRST-ORDER ENERGY ERROR")),FadeIn(eq),run_time=1); hold(self,"B06")

class B07_BowlGeometry(Scene):
 def construct(self):
  ax=Axes(x_range=[-.5,.5,.25],y_range=[0,.3,.1],x_length=8,y_length=4.5,axis_config={"color":INK},tips=False).shift(DOWN*.5); curve=ax.plot(lambda x:x*x,x_range=[-.5,.5],color=TEAL); p=Dot(ax.c2p(.3,.09),color=CRIMSON); run=Line(ax.c2p(0,0),ax.c2p(.3,0),color=INK); rise=Line(ax.c2p(.3,0),ax.c2p(.3,.09),color=CRIMSON); labs=VGroup(Text("sideways ~ eps",font=SERIF,font_size=28,color=INK).next_to(run,DOWN),Text("height ~ eps^2",font=SERIF,font_size=28,color=CRIMSON).next_to(rise,RIGHT),Text("flat tangent at the bottom",font=MONO,font_size=34,color=TEAL).shift(UP*2.2))
  self.play(FadeIn(heading("THE LOCAL ENERGY LANDSCAPE IS A BOWL")),FadeIn(ax),Create(curve),FadeIn(p),Create(run),Create(rise),FadeIn(labs),run_time=1); hold(self,"B07")

class B08_Numbers(Scene):
 def construct(self):
  g=VGroup(Text("eps = 0.1",font=MONO,font_size=46,color=TEAL),Text("gap = E1-E0 = 10 eV",font=MONO,font_size=39,color=INK),Text("Delta E = (0.1)^2 x 10 eV",font=MONO,font_size=40,color=CRIMSON),Text("= 0.1 eV",font=MONO,font_size=54,color=CRIMSON)).arrange(DOWN,buff=.55)
  self.play(FadeIn(heading("LINEAR AMPLITUDE, QUADRATIC ENERGY WEIGHT")),FadeIn(g),run_time=1); hold(self,"B08")

class B09_Normalization(Scene):
 def construct(self):
  before=Text("|phi> -> c |phi>",font=MONO,font_size=47,color=CRIMSON).shift(UP*1.6); quotient=VGroup(Text("<c phi|H|c phi>",font=MONO,font_size=35,color=TEAL),Line(LEFT*2.4,RIGHT*2.4,color=INK),Text("<c phi|c phi>",font=MONO,font_size=35,color=TEAL)).arrange(DOWN,buff=.2); result=Text("c cancels",font=DISPLAY,font_size=35,color=INK).shift(DOWN*2.1)
  self.play(FadeIn(heading("AN OVERALL COEFFICIENT IS NOT A SHAPE ERROR")),FadeIn(before),FadeIn(quotient),FadeIn(result),run_time=1); hold(self,"B09")

class B10_HighEnergySpike(Scene):
 def construct(self):
  axis=NumberLine(x_range=[0,100,20],length=10,include_numbers=False,color=INK); low=Dot(axis.n2p(0),color=TEAL); high=Dot(axis.n2p(95),color=CRIMSON); tiny=Text("tiny amplitude eps",font=SERIF,font_size=29,color=CRIMSON).next_to(high,UP); gap=Arrow(axis.n2p(2),axis.n2p(93),color=INK,buff=.1); eq=Text("Delta E = eps^2 x HUGE GAP",font=MONO,font_size=40,color=CRIMSON).shift(DOWN*1.8)
  self.play(FadeIn(heading("SMALL NORM ERROR CAN HIDE HIGH ENERGY")),Create(axis),FadeIn(low),FadeIn(high),FadeIn(tiny),GrowArrow(gap),FadeIn(eq),run_time=1); hold(self,"B10")

class B11_GapBound(Scene):
 def construct(self):
  eq=VGroup(Text("excited weight",font=SERIF,font_size=31,color=INK),Text("1 - |c0|^2",font=MONO,font_size=46,color=TEAL),Text("<=",font=MONO,font_size=40,color=INK),Text("(E-E0)/(E1-E0)",font=MONO,font_size=43,color=CRIMSON)).arrange(DOWN,buff=.45); note=Text("requires an isolated ground-state gap",font=SERIF,font_size=30,color=INK).shift(DOWN*2.6)
  self.play(FadeIn(heading("CLOSE ENERGY IMPLIES OVERLAP ONLY WITH A GAP")),FadeIn(eq),FadeIn(note),run_time=1); hold(self,"B11")

class B12_Scope(Scene):
 def construct(self):
  items=VGroup(*[Text("• "+x,font=SERIF,font_size=28,color=TEAL if i==0 else INK) for i,x in enumerate(["normalized state in the form domain","degeneracy changes which state is selected","energy may be unbounded above","other observables can have first-order error","cusps and pointwise features may converge slowly"])]).arrange(DOWN,aligned_edge=LEFT,buff=.42)
  self.play(FadeIn(heading("STATIONARITY IS POWERFUL, NOT MAGICAL")),LaggedStart(*[FadeIn(x,shift=RIGHT*.2) for x in items],lag_ratio=.12),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
 def construct(self):
  q=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=38,color=INK),Text("eps = 0.2",font=MONO,font_size=45,color=TEAL),Text("gap = 5 eV",font=MONO,font_size=41,color=CRIMSON),Text("Delta E = eps^2 x gap = ?",font=MONO,font_size=40,color=INK)).arrange(DOWN,buff=.6)
  self.play(FadeIn(q),run_time=.8); hold(self,"B13",.8)

class B14_Answer(Scene):
 def construct(self):
  a=VGroup(Text("ANSWER",font=DISPLAY,font_size=38,color=INK),Text("(0.2)^2 x 5 eV",font=MONO,font_size=43,color=TEAL),Text("= 0.2 eV",font=MONO,font_size=55,color=CRIMSON),Text("20% amplitude; 4% excited weight",font=SERIF,font_size=30,color=INK)).arrange(DOWN,buff=.55)
  self.play(FadeIn(a),run_time=.8); hold(self,"B14",.8)

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  bg=FullScreenRectangle(fill_color="#1f1d1b",fill_opacity=1,stroke_width=0); title=Text("Why Variational Energy Errors Are Often\nQuadratic in State Error",font=DISPLAY,font_size=36,color="#f4efe8",line_spacing=.8); sig=Text("Liam, in for Bear",font=SERIF,font_size=22,color="#c46b4f").shift(DOWN*1.2)
  self.add(bg); self.play(FadeIn(title),FadeIn(sig),run_time=.8); hold(self,"B15",.8)
