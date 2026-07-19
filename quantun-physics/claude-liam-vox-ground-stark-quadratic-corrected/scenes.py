import sys,json,pathlib,math,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t,size=29): return Text(t,font=DISPLAY,font_size=size,color=INK).to_edge(UP)

class B02_CompareScaling(Scene):
 def construct(self):
  left=VGroup(Text("GROUND 1s",font=DISPLAY,font_size=32,color=TEAL),Text("Delta E ~ -E^2",font=MONO,font_size=40,color=INK),Text("induced dipole",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("IDEAL n=2 PAIR",font=DISPLAY,font_size=31,color=CRIMSON),Text("Delta E ~ +/-E",font=MONO,font_size=40,color=INK),Text("degenerate mixing",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3)
  self.play(FadeIn(heading("THE SAME FIELD PROBES TWO DIFFERENT STRUCTURES")),FadeIn(left),FadeIn(right),run_time=1); hold(self,"B02")

class B03_FirstOrder(Scene):
 def construct(self):
  eq=VGroup(Text("H' = e E z",font=MONO,font_size=47,color=INK),Text("Delta E^(1) = <n|H'|n>",font=MONO,font_size=43,color=TEAL),Text("= e E <z>",font=MONO,font_size=49,color=CRIMSON),Text("linear shift tests the permanent dipole",font=SERIF,font_size=30,color=INK)).arrange(DOWN,buff=.45)
  self.play(FadeIn(heading("FIRST ORDER ASKS FOR A DIAGONAL DIPOLE")),FadeIn(eq),run_time=1); hold(self,"B03")

class B04_Parity(Scene):
 def construct(self):
  cloud=Circle(radius=1.6,color=TEAL,fill_color=TEAL,fill_opacity=.08); axis=Line(LEFT*3,RIGHT*3,color=INK); left=Text("z < 0",font=MONO,font_size=30,color=CRIMSON).shift(LEFT*2); right=Text("z > 0",font=MONO,font_size=30,color=CRIMSON).shift(RIGHT*2); arrows=VGroup(Arrow(ORIGIN,LEFT*1.5,color=CRIMSON,buff=.1),Arrow(ORIGIN,RIGHT*1.5,color=CRIMSON,buff=.1)); eq=Text("<1s|z|1s> = 0",font=MONO,font_size=45,color=TEAL).shift(DOWN*2.4)
  self.play(FadeIn(heading("EVEN PROBABILITY TIMES ODD z CANCELS")),Create(cloud),Create(axis),FadeIn(left),FadeIn(right),FadeIn(arrows),FadeIn(eq),run_time=1); hold(self,"B04")

class B05_InducedDipole(Scene):
 def construct(self):
  neutral=Circle(radius=1.3,color=INK,fill_color=TEAL,fill_opacity=.08).shift(LEFT*3); distorted=Ellipse(width=3.5,height=2.2,color=TEAL,fill_color=TEAL,fill_opacity=.09).shift(RIGHT*3); nucleus=VGroup(Dot(LEFT*3,color=CRIMSON),Dot(RIGHT*3,color=CRIMSON)); arrow=Arrow(LEFT*1.2,RIGHT*1.2,color=INK); field=Text("E ->",font=MONO,font_size=35,color=CRIMSON).shift(UP*2); eq=Text("Delta E = -1/2 alpha E^2",font=MONO,font_size=43,color=TEAL).shift(DOWN*2.2)
  self.play(FadeIn(heading("THE FIELD INDUCES A DIPOLE AT SECOND ORDER")),FadeIn(neutral),FadeIn(nucleus[0]),GrowArrow(arrow),FadeIn(distorted),FadeIn(nucleus[1]),FadeIn(field),FadeIn(eq),run_time=1); hold(self,"B05")

class B06_Polarizability(Scene):
 def construct(self):
  g=VGroup(Text("HYDROGEN 1s",font=DISPLAY,font_size=35,color=INK),Text("alpha = 4 pi eps0 (9/2) a0^3",font=MONO,font_size=40,color=TEAL),Text("Delta E = -alpha E^2 / 2",font=MONO,font_size=43,color=CRIMSON),Text("negative curvature: the field lowers the energy",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.55)
  self.play(FadeIn(heading("POLARIZABILITY MEASURES HOW EASILY THE CLOUD DISTORTS")),FadeIn(g),run_time=1); hold(self,"B06")

class B07_N2Pair(Scene):
 def construct(self):
  pair=VGroup(Line(LEFT*3,RIGHT*3,color=TEAL),Line(LEFT*3,RIGHT*3,color=CRIMSON)).shift(UP*.2); pair[0].shift(UP*.04); pair[1].shift(DOWN*.04); labs=VGroup(Text("2s",font=MONO,font_size=34,color=TEAL).next_to(pair,LEFT),Text("2p, m=0",font=MONO,font_size=34,color=CRIMSON).next_to(pair,RIGHT),Text("opposite parity, same ideal Coulomb energy",font=SERIF,font_size=30,color=INK).shift(DOWN*1.5),Text("<2s|eEz|2p0> != 0",font=MONO,font_size=39,color=INK).shift(DOWN*2.5)); arc=CurvedArrow(LEFT*1+UP*.3,RIGHT*1+UP*.3,color=INK)
  self.play(FadeIn(heading("THE IDEAL n=2 MANIFOLD HAS A DEGENERATE PARTNER")),Create(pair),FadeIn(labs),FadeIn(arc),run_time=1); hold(self,"B07")

class B08_DegenerateSplit(Scene):
 def construct(self):
  center=Line(LEFT*2,RIGHT*2,color=INK); upper=Line(LEFT*2,RIGHT*2,color=CRIMSON).shift(UP*1.3); lower=Line(LEFT*2,RIGHT*2,color=TEAL).shift(DOWN*1.3); arrows=VGroup(Arrow(center.get_center(),upper.get_center(),color=CRIMSON,buff=.1),Arrow(center.get_center(),lower.get_center(),color=TEAL,buff=.1)); labs=VGroup(Text("|2s> + |2p0>",font=MONO,font_size=31,color=CRIMSON).next_to(upper,RIGHT),Text("|2s> - |2p0>",font=MONO,font_size=31,color=TEAL).next_to(lower,RIGHT),Text("Delta E = +/- 3 e a0 E",font=MONO,font_size=43,color=INK).shift(DOWN*2.7))
  self.play(FadeIn(heading("DIAGONALIZING THE PAIR CREATES LINEAR BRANCHES")),Create(center),GrowArrow(arrows[0]),GrowArrow(arrows[1]),Create(upper),Create(lower),FadeIn(labs),run_time=1.1); hold(self,"B08",1.1)

class B09_Curves(Scene):
 def construct(self):
  ax=Axes(x_range=[-1,1,.5],y_range=[-1,1,.5],x_length=8,y_length=5,axis_config={"color":INK},tips=False).shift(DOWN*.3); quad=ax.plot(lambda x:-.7*x*x,x_range=[-1,1],color=TEAL); up=ax.plot(lambda x:.75*x,x_range=[-1,1],color=CRIMSON); down=ax.plot(lambda x:-.75*x,x_range=[-1,1],color=CRIMSON); qlab=Text("1s: induced dipole",font=SERIF,font_size=27,color=TEAL).shift(RIGHT*3+DOWN*1.8); qchip=VGroup(BackgroundRectangle(qlab,fill_color="#f7f4ef",fill_opacity=1,stroke_width=0,buff=.1),qlab); labs=VGroup(qchip,Text("ideal n=2: degenerate split",font=SERIF,font_size=27,color=CRIMSON).shift(RIGHT*2.6+UP*1.8))
  self.play(FadeIn(heading("QUADRATIC BEND VERSUS LINEAR OPENING")),FadeIn(ax),Create(quad),Create(up),Create(down),FadeIn(labs),run_time=1); hold(self,"B09")

class B10_Numbers(Scene):
 def construct(self):
  g=VGroup(Text("E = 10^5 V/m",font=MONO,font_size=42,color=INK),Text("ideal n=2:  |Delta E| ~ 1.6 x 10^-5 eV",font=MONO,font_size=35,color=CRIMSON),Text("ground 1s: |Delta E| ~ 5.1 x 10^-13 eV",font=MONO,font_size=35,color=TEAL),Text("ratio ~ 3 x 10^7",font=MONO,font_size=47,color=INK),Text("not sixty",font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN,buff=.45)
  self.play(FadeIn(heading("THE CORRECTED SCALE DIFFERENCE IS ENORMOUS")),FadeIn(g),run_time=1); hold(self,"B10")

class B11_Crossover(Scene):
 def construct(self):
  ax=Axes(x_range=[0,2,.5],y_range=[0,2,.5],x_length=8,y_length=4.8,axis_config={"color":INK},tips=False).shift(DOWN*.4); weak=ax.plot(lambda x:.45*x*x,x_range=[0,.85],color=TEAL); strong=ax.plot(lambda x:.72*x-.18,x_range=[.6,2],color=CRIMSON); dash=DashedLine(ax.c2p(.7,0),ax.c2p(.7,1.7),color=INK); labs=VGroup(Text("very weak: quadratic",font=SERIF,font_size=27,color=TEAL).shift(LEFT*2.5+DOWN*1.8),Text("mixing dominates: linear-like",font=SERIF,font_size=27,color=CRIMSON).shift(RIGHT*2.5+UP*1.5),Text("fine structure + Lamb splitting",font=MONO,font_size=29,color=INK).shift(UP*2.7))
  self.play(FadeIn(heading("REAL HYDROGEN HAS A WEAK-FIELD CROSSOVER")),FadeIn(ax),Create(weak),Create(strong),Create(dash),FadeIn(labs),run_time=1); hold(self,"B11")

class B12_Scope(Scene):
 def construct(self):
  items=VGroup(*[Text("• "+x,font=SERIF,font_size=28,color=TEAL if i==0 else INK) for i,x in enumerate(["static, approximately uniform field","isolated hydrogen parity eigenstates","molecules may have permanent dipoles","near-degeneracy changes field scaling","strong fields eventually ionize the atom"])]).arrange(DOWN,aligned_edge=LEFT,buff=.43)
  self.play(FadeIn(heading("THE POWER LAW HAS A DOMAIN")),LaggedStart(*[FadeIn(x,shift=RIGHT*.2) for x in items],lag_ratio=.12),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
 def construct(self):
  q=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=38,color=INK),Text("state parity: EVEN",font=MONO,font_size=39,color=TEAL),Text("perturbing operator: ODD x E",font=MONO,font_size=37,color=CRIMSON),Text("Delta E^(1) = ?",font=MONO,font_size=44,color=INK),Text("first allowed field power?",font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.42)
  self.play(FadeIn(q),run_time=.8); hold(self,"B13",.8)

class B14_Answer(Scene):
 def construct(self):
  a=VGroup(Text("ANSWER",font=DISPLAY,font_size=38,color=INK),Text("<even|odd|even> = 0",font=MONO,font_size=43,color=TEAL),Text("first order vanishes",font=SERIF,font_size=31,color=INK),Text("leading shift ~ E^2",font=MONO,font_size=50,color=CRIMSON)).arrange(DOWN,buff=.55)
  self.play(FadeIn(a),run_time=.8); hold(self,"B14",.8)

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  bg=FullScreenRectangle(fill_color="#1f1d1b",fill_opacity=1,stroke_width=0); title=Text("Why Hydrogen's Ground-State\nStark Shift Starts Quadratic",font=DISPLAY,font_size=38,color="#f4efe8",line_spacing=.8); sig=Text("Liam, in for Bear",font=SERIF,font_size=22,color="#c46b4f").shift(DOWN*1.2)
  self.add(bg); self.play(FadeIn(title),FadeIn(sig),run_time=.8); hold(self,"B15",.8)
