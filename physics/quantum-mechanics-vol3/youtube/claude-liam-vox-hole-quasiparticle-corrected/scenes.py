import sys,json,pathlib,math,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t,size=29): return Text(t,font=DISPLAY,font_size=size,color=INK).to_edge(UP)

class B02_TwoPuzzles(Scene):
 def construct(self):
  left=VGroup(Text("ELECTRON NEAR TOP",font=DISPLAY,font_size=30,color=TEAL),Text("q = -e",font=MONO,font_size=42,color=INK),Text("accelerates along E",font=SERIF,font_size=30,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("MISSING ELECTRON",font=DISPLAY,font_size=30,color=CRIMSON),Text("hole q = +e",font=MONO,font_size=42,color=INK),Text("carries positive current",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3)
  self.play(FadeIn(heading("CURVATURE AND MISSING-STATE BOOKKEEPING ARE LINKED")),FadeIn(left),FadeIn(right),run_time=1); hold(self,"B02")

class B03_Dispersion(Scene):
 def construct(self):
  ax=Axes(x_range=[-3.2,3.2,1.6],y_range=[-2.3,2.3,1],x_length=9,y_length=5,axis_config={"color":INK},tips=False).shift(DOWN*.3); curve=ax.plot(lambda x:-2*math.cos(x),x_range=[-math.pi,math.pi],color=TEAL); labs=VGroup(Text("E(k) = E0 - 2t cos(ka)",font=MONO,font_size=35,color=INK).shift(UP*2.6),Text("upward curvature",font=SERIF,font_size=26,color=TEAL).shift(DOWN*2.5),Text("downward curvature",font=SERIF,font_size=26,color=CRIMSON).shift(LEFT*3+UP*1.4)); tops=VGroup(Dot(ax.c2p(-math.pi,2),color=CRIMSON),Dot(ax.c2p(math.pi,2),color=CRIMSON))
  self.play(FadeIn(heading("A TIGHT-BINDING BAND IS A COSINE ARCH")),FadeIn(ax),Create(curve),FadeIn(tops),FadeIn(labs),run_time=1.1); hold(self,"B03",1.1)

class B04_GroupVelocity(Scene):
 def construct(self):
  ax=Axes(x_range=[-1.5,1.5,.5],y_range=[-1.2,.2,.25],x_length=8,y_length=4.5,axis_config={"color":INK},tips=False).shift(DOWN*.5); curve=ax.plot(lambda x:-.55*x*x,x_range=[-1.4,1.4],color=TEAL); tangent=Line(ax.c2p(-.8,-.352)+LEFT*1.2,ax.c2p(-.8,-.352)+RIGHT*1.2+UP*1.05,color=CRIMSON); top=Dot(ax.c2p(0,0),color=INK); labs=VGroup(Text("v_g = (1/hbar) dE/dk",font=MONO,font_size=37,color=INK).shift(UP*2.2),Text("slope = 0 at exact maximum",font=SERIF,font_size=29,color=TEAL).shift(DOWN*2.5))
  self.play(FadeIn(heading("THE SLOPE, NOT THE HEIGHT, GIVES VELOCITY")),FadeIn(ax),Create(curve),Create(tangent),FadeIn(top),FadeIn(labs),run_time=1); hold(self,"B04")

class B05_KForce(Scene):
 def construct(self):
  axis=NumberLine(x_range=[-3,3,1],length=10,include_numbers=False,color=INK); dot=Dot(axis.n2p(1),color=CRIMSON); arrow=Arrow(axis.n2p(1),axis.n2p(-1),color=TEAL,buff=.1); labs=VGroup(Text("electric field E ->",font=MONO,font_size=34,color=CRIMSON).shift(UP*1.5),Text("hbar k_dot = qE",font=MONO,font_size=42,color=INK).shift(DOWN*1.5),Text("electron q=-e: k moves left",font=SERIF,font_size=30,color=TEAL).shift(DOWN*2.4))
  self.play(FadeIn(heading("THE FIELD MOVES CRYSTAL MOMENTUM")),Create(axis),FadeIn(dot),GrowArrow(arrow),FadeIn(labs),run_time=1); hold(self,"B05")

class B06_EffectiveMass(Scene):
 def construct(self):
  eq=VGroup(Text("a = (qE / hbar^2) d^2E/dk^2",font=MONO,font_size=38,color=INK),Text("define",font=SERIF,font_size=27,color=INK),Text("1/m* = (1/hbar^2) d^2E/dk^2",font=MONO,font_size=38,color=TEAL),Text("so  a = qE/m*",font=MONO,font_size=46,color=CRIMSON)).arrange(DOWN,buff=.45)
  self.play(FadeIn(heading("BAND CURVATURE BECOMES AN EFFECTIVE MASS")),FadeIn(eq),run_time=1); hold(self,"B06")

class B07_SignCancel(Scene):
 def construct(self):
  row=VGroup(Text("q = -e",font=MONO,font_size=44,color=CRIMSON),Text("/",font=MONO,font_size=38,color=INK),Text("m* < 0",font=MONO,font_size=44,color=TEAL),Text("=",font=MONO,font_size=38,color=INK),Text("a along E",font=MONO,font_size=46,color=INK)).arrange(RIGHT,buff=.5); note=Text("the electron's fundamental charge did not change",font=SERIF,font_size=31,color=INK).shift(DOWN*1.8)
  self.play(FadeIn(heading("TWO MINUS SIGNS REVERSE THE ACCELERATION")),FadeIn(row),FadeIn(note),run_time=1); hold(self,"B07")

class B08_FilledBand(Scene):
 def construct(self):
  axis=NumberLine(x_range=[-4,4,1],length=10,include_numbers=False,color=INK); xs=[.7,1.5,2.3,3.1]; pairs=VGroup(*[VGroup(Dot(axis.n2p(x),color=TEAL),Dot(axis.n2p(-x),color=TEAL)) for x in xs]); arrows=VGroup(*[Arrow(axis.n2p(x),axis.n2p(x)+RIGHT*.55,color=CRIMSON,buff=.08) for x in xs],*[Arrow(axis.n2p(-x),axis.n2p(-x)+LEFT*.55,color=CRIMSON,buff=.08) for x in xs]); total=Text("SUM current = 0",font=MONO,font_size=44,color=INK).shift(DOWN*1.8)
  self.play(FadeIn(heading("A COMPLETELY FILLED BAND HAS VELOCITY PARTNERS")),Create(axis),LaggedStart(*[FadeIn(p) for p in pairs],lag_ratio=.1),FadeIn(arrows),FadeIn(total),run_time=1.1); hold(self,"B08",1.1)

class B09_SubtractState(Scene):
 def construct(self):
  full=Text("J_full = 0",font=MONO,font_size=44,color=INK).shift(UP*1.7); miss=Text("remove electron:  j_e = (-e) v_e",font=MONO,font_size=36,color=CRIMSON); remain=Text("J_remaining = -j_e = (+e) v_e",font=MONO,font_size=40,color=TEAL).shift(DOWN*1.7); arr=Arrow(full.get_bottom(),remain.get_top(),color=INK,buff=.2)
  self.play(FadeIn(heading("ONE MISSING STATE REVERSES THAT STATE'S CURRENT")),FadeIn(full),FadeIn(miss),GrowArrow(arr),FadeIn(remain),run_time=1); hold(self,"B09")

class B10_HoleBowl(Scene):
 def construct(self):
  ax1=Axes(x_range=[-1.5,1.5,.5],y_range=[-1,.2,.25],x_length=4,y_length=4,axis_config={"color":INK},tips=False).shift(LEFT*3+DOWN*.5); electron=ax1.plot(lambda x:-.5*x*x,x_range=[-1.4,1.4],color=CRIMSON); ax2=Axes(x_range=[-1.5,1.5,.5],y_range=[0,1.2,.25],x_length=4,y_length=4,axis_config={"color":INK},tips=False).shift(RIGHT*3+DOWN*.5); hole=ax2.plot(lambda x:.5*x*x,x_range=[-1.4,1.4],color=TEAL); arr=Arrow(LEFT*.7,RIGHT*.7,color=INK); labs=VGroup(Text("electron near maximum",font=SERIF,font_size=27,color=CRIMSON).shift(LEFT*3+UP*2),Text("hole energy bowl",font=SERIF,font_size=27,color=TEAL).shift(RIGHT*3+UP*2),Text("m_h = |m_e*| > 0",font=MONO,font_size=35,color=INK).shift(DOWN*2.8))
  self.play(FadeIn(heading("REDEFINE MOMENTUM RELATIVE TO THE BAND MAXIMUM")),FadeIn(ax1),Create(electron),GrowArrow(arr),FadeIn(ax2),Create(hole),FadeIn(labs),run_time=1.1); hold(self,"B10",1.1)

class B11_HoleEquation(Scene):
 def construct(self):
  eq=VGroup(Text("HOLE",font=DISPLAY,font_size=38,color=INK),Text("q_h = +e",font=MONO,font_size=45,color=CRIMSON),Text("m_h > 0",font=MONO,font_size=45,color=TEAL),Text("a_h = (+e)E / m_h",font=MONO,font_size=42,color=INK),Text("same collective valence-band current",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.42)
  self.play(FadeIn(heading("THE QUASIPARTICLE HAS ORDINARY-LOOKING DYNAMICS")),FadeIn(eq),run_time=1); hold(self,"B11")

class B12_Boundaries(Scene):
 def construct(self):
  items=VGroup(*[Text("• "+x,font=SERIF,font_size=28,color=TEAL if i==0 else INK) for i,x in enumerate(["effective mass is generally a tensor","heavy and light hole branches can mix","scattering changes transport","Berry curvature can add transverse motion","a hole is a quasiparticle, not an empty marble"])]).arrange(DOWN,aligned_edge=LEFT,buff=.42)
  self.play(FadeIn(heading("REAL VALENCE BANDS ADD STRUCTURE")),LaggedStart(*[FadeIn(x,shift=RIGHT*.2) for x in items],lag_ratio=.12),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
 def construct(self):
  q=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=38,color=INK),Text("q = -e",font=MONO,font_size=43,color=CRIMSON),Text("m* = -0.4 m_e",font=MONO,font_size=43,color=TEAL),Text("E points right",font=SERIF,font_size=31,color=INK),Text("which way does a = qE/m* point?",font=MONO,font_size=33,color=INK)).arrange(DOWN,buff=.4)
  self.play(FadeIn(q),run_time=.8); hold(self,"B13",.8)

class B14_Answer(Scene):
 def construct(self):
  a=VGroup(Text("ANSWER",font=DISPLAY,font_size=38,color=INK),Text("negative / negative = positive",font=MONO,font_size=37,color=INK),Text("acceleration points RIGHT",font=MONO,font_size=45,color=CRIMSON),Text("equivalent hole:  +e,  +0.4 m_e",font=MONO,font_size=34,color=TEAL)).arrange(DOWN,buff=.55)
  self.play(FadeIn(a),run_time=.8); hold(self,"B14",.8)

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  bg=FullScreenRectangle(fill_color="#1f1d1b",fill_opacity=1,stroke_width=0); title=Text("How a Missing Valence Electron\nBecomes a Positive Hole",font=DISPLAY,font_size=38,color="#f4efe8",line_spacing=.8); sig=Text("Liam, in for Bear",font=SERIF,font_size=22,color="#c46b4f").shift(DOWN*1.2)
  self.add(bg); self.play(FadeIn(title),FadeIn(sig),run_time=.8); hold(self,"B15",.8)
