import sys,json,pathlib,math,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t,size=29): return Text(t,font=DISPLAY,font_size=size,color=INK).to_edge(UP)

class B02_TwoLimits(Scene):
 def construct(self):
  left=VGroup(Text("ZERO ENERGY",font=DISPLAY,font_size=31,color=TEAL),Text("a_s -> infinity",font=MONO,font_size=42,color=INK),Text("a length diverges",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("FIXED k > 0",font=DISPLAY,font_size=31,color=CRIMSON),Text("sigma stays finite",font=MONO,font_size=38,color=INK),Text("unitarity caps area",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3)
  self.play(FadeIn(heading("DO NOT MIX THE TWO LIMITS")),FadeIn(left),FadeIn(right),run_time=1); hold(self,"B02")

class B03_Intercept(Scene):
 def construct(self):
  ax=Axes(x_range=[0,7,1],y_range=[-2,4,1],x_length=9,y_length=5,axis_config={"color":INK},tips=False).shift(DOWN*.4); line=ax.plot(lambda r:r-4,x_range=[1.8,7],color=TEAL); ext=ax.plot(lambda r:r-4,x_range=[0,1.8],color=TEAL,stroke_opacity=.4); dot=Dot(ax.c2p(4,0),color=CRIMSON); labs=VGroup(Text("u_0(r) ~ r - a_s",font=MONO,font_size=36,color=TEAL).shift(UP*2.3),Text("intercept = a_s",font=SERIF,font_size=30,color=CRIMSON).next_to(dot,DOWN))
  self.play(FadeIn(heading("THE SCATTERING LENGTH IS A ZERO-ENERGY INTERCEPT")),FadeIn(ax),Create(line),Create(ext),FadeIn(dot),FadeIn(labs),run_time=1.1); hold(self,"B03",1.1)

class B04_ShallowState(Scene):
 def construct(self):
  ax=Axes(x_range=[0,8,1],y_range=[0,1.2,.2],x_length=9,y_length=4.5,axis_config={"color":INK},tips=False).shift(DOWN*.5); fast=ax.plot(lambda x:math.exp(-x),x_range=[0,7],color=INK); slow=ax.plot(lambda x:math.exp(-.2*x),x_range=[0,7],color=TEAL); size=Text("size ~ 1/kappa",font=MONO,font_size=39,color=CRIMSON).shift(RIGHT*2+DOWN*1.65); size_chip=VGroup(BackgroundRectangle(size,fill_color="#f7f4ef",fill_opacity=1,stroke_width=0,buff=.12),size); labs=VGroup(Text("deep: large kappa",font=SERIF,font_size=27,color=INK).shift(RIGHT*2+UP*.8),Text("shallow: kappa -> 0",font=SERIF,font_size=29,color=TEAL).shift(RIGHT*2+UP*1.8),size_chip)
  self.play(FadeIn(heading("A SHALLOW BOUND STATE SPREADS FAR OUTSIDE THE WELL")),FadeIn(ax),Create(fast),TransformFromCopy(fast,slow),FadeIn(labs),run_time=1.2); hold(self,"B04",1.2)

class B05_Pole(Scene):
 def construct(self):
  ax=Axes(x_range=[-2,2,1],y_range=[-4,4,2],x_length=8,y_length=5,axis_config={"color":INK},tips=False).shift(DOWN*.3); left=ax.plot(lambda x:-1/x,x_range=[-2,-.15],color=TEAL); right=ax.plot(lambda x:-1/x,x_range=[.15,2],color=CRIMSON); dash=DashedLine(ax.c2p(0,-4),ax.c2p(0,4),color=INK); labs=VGroup(Text("virtual-state side",font=SERIF,font_size=26,color=TEAL).shift(LEFT*3+DOWN*2.2),Text("shallow bound state",font=SERIF,font_size=26,color=CRIMSON).shift(RIGHT*3+UP*2),Text("threshold",font=MONO,font_size=29,color=INK).shift(UP*2.8))
  self.play(FadeIn(heading("THE THRESHOLD CREATES A POLE AND A SIGN FLIP")),FadeIn(ax),Create(left),Create(right),Create(dash),FadeIn(labs),run_time=1.1); hold(self,"B05",1.1)

class B06_LowK(Scene):
 def construct(self):
  eq=VGroup(Text("sigma -> 4 pi a_s^2",font=MONO,font_size=49,color=TEAL),Text("ONLY WHEN",font=DISPLAY,font_size=28,color=CRIMSON),Text("k |a_s| << 1",font=MONO,font_size=48,color=CRIMSON),Text("elastic, distinguishable-particle s wave",font=SERIF,font_size=28,color=INK)).arrange(DOWN,buff=.5)
  self.play(FadeIn(heading("THE FAMILIAR AREA FORMULA IS AN APPROXIMATION")),FadeIn(eq),run_time=1); hold(self,"B06")

class B07_BreakCondition(Scene):
 def construct(self):
  start=Text("k |a_s| << 1",font=MONO,font_size=51,color=TEAL).shift(UP*1.4); arr=Arrow(UP*.7,DOWN*.7,color=INK); end=Text("a_s -> infinity at fixed k",font=MONO,font_size=44,color=CRIMSON).shift(DOWN*1.3); no=Cross(start,stroke_color=CRIMSON,stroke_width=7)
  self.play(FadeIn(heading("THE POLE BREAKS THE ASSUMPTION USED TO GET 4 pi a^2")),FadeIn(start),GrowArrow(arr),FadeIn(end),Create(no),run_time=1); hold(self,"B07")

class B08_Unitarity(Scene):
 def construct(self):
  eq=VGroup(Text("sigma(k) =",font=MONO,font_size=42,color=INK),Text("4 pi a_s^2",font=MONO,font_size=41,color=TEAL),Line(LEFT*2.2,RIGHT*2.2,color=INK),Text("1 + k^2 a_s^2",font=MONO,font_size=37,color=INK)).arrange(DOWN,buff=.2).shift(LEFT*2); arrow=Arrow(RIGHT*.3,RIGHT*2,color=INK); lim=VGroup(Text("|a_s| -> infinity",font=MONO,font_size=31,color=CRIMSON),Text("sigma -> 4 pi / k^2",font=MONO,font_size=42,color=CRIMSON)).arrange(DOWN,buff=.5).shift(RIGHT*3.2)
  self.play(FadeIn(heading("KEEP k AND UNITARITY SUPPLIES THE CEILING")),FadeIn(eq),GrowArrow(arrow),FadeIn(lim),run_time=1); hold(self,"B08")

class B09_OrderLimits(Scene):
 def construct(self):
  left=VGroup(Text("FIX k",font=DISPLAY,font_size=30,color=TEAL),Text("a_s -> infinity",font=MONO,font_size=33,color=INK),Text("sigma = 4 pi/k^2",font=MONO,font_size=34,color=TEAL)).arrange(DOWN,buff=.45).move_to(LEFT*3); right=VGroup(Text("THEN k -> 0",font=DISPLAY,font_size=30,color=CRIMSON),Text("ceiling rises",font=MONO,font_size=34,color=INK),Text("4 pi/k^2 -> infinity",font=MONO,font_size=34,color=CRIMSON)).arrange(DOWN,buff=.45).move_to(RIGHT*3)
  self.play(FadeIn(heading("ORDER OF LIMITS RESOLVES THE INFINITY PARADOX")),FadeIn(left),FadeIn(right),run_time=1); hold(self,"B09")

class B10_Feshbach(Scene):
 def construct(self):
  ax=Axes(x_range=[-2,2,1],y_range=[-2,2,1],x_length=8,y_length=4.8,axis_config={"color":INK},tips=False).shift(DOWN*.4); threshold=ax.plot(lambda x:0,x_range=[-2,2],color=TEAL); molecule=ax.plot(lambda x:-x,x_range=[-2,2],color=CRIMSON); dot=Dot(ax.c2p(0,0),color=INK); labs=VGroup(Text("open-channel threshold",font=SERIF,font_size=26,color=TEAL).shift(RIGHT*3+UP*.4),Text("closed-channel molecule",font=SERIF,font_size=26,color=CRIMSON).shift(LEFT*2.5+UP*1.6),Text("a(B) = a_bg [1 - Delta/(B-B0)]",font=MONO,font_size=30,color=INK).shift(DOWN*2.25))
  self.play(FadeIn(heading("A FESHBACH RESONANCE TUNES A CHANNEL CROSSING")),FadeIn(ax),Create(threshold),Create(molecule),FadeIn(dot),FadeIn(labs),run_time=1.1); hold(self,"B10",1.1)

class B11_ManyBody(Scene):
 def construct(self):
  items=VGroup(*[Text("• "+x,font=SERIF,font_size=29,color=TEAL if i==0 else INK) for i,x in enumerate(["unitarity makes scattering momentum-limited","inelastic losses may grow","statistics and density matter","temperature and range set extra scales"])]).arrange(DOWN,aligned_edge=LEFT,buff=.55)
  self.play(FadeIn(heading("INFINITE a_s IS NOT A BLANKET 'STRONGEST' LABEL")),LaggedStart(*[FadeIn(x,shift=RIGHT*.2) for x in items],lag_ratio=.14),run_time=1); hold(self,"B11")

class B12_Scope(Scene):
 def construct(self):
  core=Text("LOW-ENERGY ELASTIC S WAVE",font=DISPLAY,font_size=34,color=TEAL).shift(UP*2); branches=VGroup(*[Text(x,font=MONO,font_size=28,color=INK) for x in ["identical-particle factors","complex a_s with loss","effective range","higher partial waves"]]).arrange(DOWN,buff=.42).shift(DOWN*.5)
  self.play(FadeIn(heading("THE UNIVERSAL FORMULA HAS A DOMAIN")),FadeIn(core),LaggedStart(*[FadeIn(x) for x in branches],lag_ratio=.15),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
 def construct(self):
  q=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=38,color=INK),Text("sigma = 4 pi a_s^2 / (1 + k^2 a_s^2)",font=MONO,font_size=34,color=TEAL),Text("fixed k,  |a_s| -> infinity",font=MONO,font_size=37,color=CRIMSON),Text("sigma -> ?",font=MONO,font_size=46,color=INK)).arrange(DOWN,buff=.55)
  self.play(FadeIn(q),run_time=.8); hold(self,"B13",.8)

class B14_Answer(Scene):
 def construct(self):
  a=VGroup(Text("ANSWER",font=DISPLAY,font_size=38,color=INK),Text("divide by a_s^2",font=SERIF,font_size=31,color=INK),Text("sigma -> 4 pi / k^2",font=MONO,font_size=52,color=CRIMSON),Text("the s-wave unitarity limit",font=SERIF,font_size=30,color=TEAL)).arrange(DOWN,buff=.55)
  self.play(FadeIn(a),run_time=.8); hold(self,"B14",.8)

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  bg=FullScreenRectangle(fill_color="#1f1d1b",fill_opacity=1,stroke_width=0); title=Text("Why a Threshold Bound State Makes\nthe Scattering Length Diverge",font=DISPLAY,font_size=36,color="#f4efe8",line_spacing=.8); sig=Text("Liam, in for Bear",font=SERIF,font_size=22,color="#c46b4f").shift(DOWN*1.2)
  self.add(bg); self.play(FadeIn(title),FadeIn(sig),run_time=.8); hold(self,"B15",.8)
