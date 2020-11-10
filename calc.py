from wx import *

a = App()
f = Frame(None, title="Faizan's Calculator", size=(400,550))
p = Panel(f)
p.SetBackgroundColour("#DCEDC8")
main = BoxSizer(orient=VERTICAL)

t = TextCtrl(p, style=TE_READONLY)
t.SetBackgroundColour("#f8f8ff")
t.SetFont(Font(40,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))

text = "0"
t.SetValue(text)
back_text = "0"

def one_fun(e):
    global text
    global back_text
    if(text=="0"):
        text = "1"
    else:
        text += "1"
    if(back_text=="0"):
        back_text = "1"
    else:
        back_text += "1"
    t.SetValue(text)

def two_fun(e):
    global text 
    global back_text 
    if(text=="0"):
        text = "2"
    else:
        text += "2"
    if(back_text=="0"):
        back_text = "2"
    else:
        back_text += "2"

    t.SetValue(text)

def three_fun(e):
    global text 
    global back_text 
    if(text=="0"):
        text = "3"
    else:
        text += "3"
    if(back_text=="0"):
        back_text = "3"
    else:
        back_text += "3"
    t.SetValue(text)

def four_fun(e):
    global text 
    global back_text 
    if(text=="0"):
        text = "4"
    else:
        text += "4"
    if(back_text=="0"):
        back_text = "4"
    else:
        back_text += "4"
    t.SetValue(text)

def five_fun(e):
    global text
    global back_text
    if(text=="0"):
        text = "5"
    else:
        text += "5"
    if(back_text=="0"):
        back_text = "5"
    else:
        back_text += "5"
    t.SetValue(text)

def six_fun(e):
    global text
    global back_text
    if(text=="0"):
        text = "6"
    else:
        text += "6"
    if(back_text=="0"):
        back_text = "6"
    else:
        back_text += "6"
    t.SetValue(text)

def seven_fun(e):
    global text
    global back_text
    if(text=="0"):
        text = "7"
    else:
        text += "7"
    if(back_text=="0"):
        back_text = "7"
    else:
        back_text += "7"
    t.SetValue(text)

def eight_fun(e):
    global text
    global back_text
    if(text=="0"):
        text = "8"
    else:
        text += "8"
    if(back_text=="0"):
        back_text = "8"
    else:
        back_text += "8"
    t.SetValue(text)

def nine_fun(e):
    global text
    global back_text
    if(text=="0"):
        text = "9"
    else:
        text += "9"
    if(back_text=="0"):
        back_text = "9"
    else:
        back_text += "9"
    t.SetValue(text)

def zero_fun(e):
    global text 
    global back_text 
    if(text=="0"):
        text = "0"
    else:
        text += "0"
    if(back_text=="0"):
        back_text = "0"
    else:
        back_text += "0"
    t.SetValue(text)

def ce_fun(e):
    global text
    global back_text
    text = "0"
    back_text = "0"
    t.SetValue(text)

def c_fun(e):
    global text 
    global back_text 
    text = text[:-1]
    back_text = back_text[:-1]
    t.SetValue(text)

def add_fun(e):
    global text
    global back_text
    if back_text[-1] != "+":
        text = "0"
        back_text += "+"
        t.SetValue(text)

def sub_fun(e):
    global text
    global back_text
    if back_text[-1] != "-":
        text = "0"
        back_text += "-"
        t.SetValue(text)
    
    
def mul_fun(e):
    global text
    global back_text
    if back_text[-1] != "*":
        text = "0"
        back_text += "*"
        t.SetValue(text)

def div_fun(e):
    global text
    global back_text
    if back_text[-1] != "/":
        text = "0"
        back_text += "/"
        t.SetValue(text)

def equal_fun(e):
    global text
    global back_text
    text = str(eval(back_text))
    t.SetValue(text)

def dot_fun(e):
    global text
    global back_text
    if back_text[-1] != "." and '.' not in text:
        if(text=="0"):
            text = "0"
        else:
            text += "."
        if(back_text=="0"):
            back_text = "0."
        else:
            back_text += "."
        t.SetValue(text)

def per_fun(e):
    global text
    global back_text
    text = "0"
    back_text += "/100*"
    t.SetValue(text)

def pm_fun(e):
    global text
    global back_text
    ln = len(text)
    if text[:1] == "-":
        text = text[1:]
    else:
        text = "-"+text
    back_text = back_text[:-ln]
    back_text += text
    t.SetValue(text)

main.Add(t,1,EXPAND|ALL, border=15)

g = GridSizer(5,4,5,5)

zero = Button(p, label="0")
one = Button(p, label="1")
two = Button(p, label="2")
three = Button(p, label="3")
four = Button(p, label="4")
five = Button(p, label="5")
six = Button(p, label="6")
seven = Button(p, label="7")
eight = Button(p, label="8")
nine = Button(p, label="9")
equal = Button(p, label="=")
add = Button(p, label="+")
sub = Button(p, label="-")
mul = Button(p, label="*")
div = Button(p, label="÷")
per = Button(p, label="%")
c = Button(p, label="⌫")
ce = Button(p, label="CE")
dot =Button(p, label=".")
plus_minus = Button(p, label="+/-")

g.AddMany([
    (per, 1, EXPAND|ALL),
    (c, 1, EXPAND|ALL),
    (ce, 1, EXPAND|ALL),
    (div, 1, EXPAND|ALL),
    (seven, 1, EXPAND|ALL),
    (eight, 1, EXPAND|ALL),
    (nine, 1, EXPAND|ALL),
    (mul, 1, EXPAND|ALL),
    (four, 1, EXPAND|ALL),
    (five, 1, EXPAND|ALL),
    (six, 1, EXPAND|ALL),
    (sub, 1, EXPAND|ALL),
    (one, 1, EXPAND|ALL),
    (two, 1, EXPAND|ALL),
    (three, 1, EXPAND|ALL),
    (add, 1, EXPAND|ALL),
    (plus_minus, 1, EXPAND|ALL),
    (zero, 1, EXPAND|ALL),
    (dot, 1, EXPAND|ALL),
    (equal, 1, EXPAND|ALL),

])

one.Bind(EVT_BUTTON, one_fun, one)
two.Bind(EVT_BUTTON, two_fun, two)
three.Bind(EVT_BUTTON, three_fun, three)
four.Bind(EVT_BUTTON, four_fun, four)
five.Bind(EVT_BUTTON, five_fun, five)
six.Bind(EVT_BUTTON, six_fun, six)
seven.Bind(EVT_BUTTON, seven_fun, seven)
eight.Bind(EVT_BUTTON, eight_fun, eight)
nine.Bind(EVT_BUTTON, nine_fun, nine)
zero.Bind(EVT_BUTTON, zero_fun, zero)
ce.Bind(EVT_BUTTON, ce_fun, ce)
c.Bind(EVT_BUTTON, c_fun, c)
add.Bind(EVT_BUTTON, add_fun, add)
sub.Bind(EVT_BUTTON, sub_fun, sub)
mul.Bind(EVT_BUTTON, mul_fun, mul)
div.Bind(EVT_BUTTON, div_fun, div)
equal.Bind(EVT_BUTTON, equal_fun, equal)
dot.Bind(EVT_BUTTON, dot_fun, dot)
per.Bind(EVT_BUTTON, per_fun, per)
plus_minus.Bind(EVT_BUTTON, pm_fun, plus_minus)

zero.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
one.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
two.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
three.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
four.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
five.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
six.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
seven.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
eight.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
nine.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
sub.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
mul.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
add.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
plus_minus.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
div.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
per.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
dot.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
c.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_NORMAL, FONTWEIGHT_BOLD))
ce.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))
equal.SetFont(Font(18,FONTFAMILY_DECORATIVE, FONTSTYLE_SLANT, FONTWEIGHT_BOLD))

zero.SetBackgroundColour("#1e272e")
one.SetBackgroundColour("#1e272e")
two.SetBackgroundColour("#1e272e")
three.SetBackgroundColour("#1e272e")
four.SetBackgroundColour("#1e272e")
five.SetBackgroundColour("#1e272e")
six.SetBackgroundColour("#1e272e")
seven.SetBackgroundColour("#1e272e")
eight.SetBackgroundColour("#1e272e")
nine.SetBackgroundColour("#1e272e")

mul.SetBackgroundColour("#485460")
div.SetBackgroundColour("#485460")
sub.SetBackgroundColour("#485460")
dot.SetBackgroundColour("#485460")
add.SetBackgroundColour("#485460")
equal.SetBackgroundColour("#485460")
c.SetBackgroundColour("#485460")
ce.SetBackgroundColour("#485460")
plus_minus.SetBackgroundColour("#485460")
per.SetBackgroundColour("#485460")

c.SetForegroundColour("white")
ce.SetForegroundColour("white")
per.SetForegroundColour("white")
div.SetForegroundColour("white")
sub.SetForegroundColour("white")
mul.SetForegroundColour("white")
add.SetForegroundColour("white")
equal.SetForegroundColour("white")
dot.SetForegroundColour("white")
plus_minus.SetForegroundColour("white")
zero.SetForegroundColour("white")
one.SetForegroundColour("white")
two.SetForegroundColour("white")
three.SetForegroundColour("white")
four.SetForegroundColour("white")
five.SetForegroundColour("white")
six.SetForegroundColour("white")
seven.SetForegroundColour("white")
eight.SetForegroundColour("white")
nine.SetForegroundColour("white")

main.Add(g,4,EXPAND|ALL,border=15)
p.SetSizer(main)
f.Show()
a.MainLoop()