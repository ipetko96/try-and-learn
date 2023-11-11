import re
import turtle

t = turtle.Turtle()

logo = "pu fd 50 pd lt 30 fd 70 rt 60 fd 100"
pattern = r"([a-z]+ \d*)"
commands = re.findall(pattern, logo)

for i in commands:
    i = i.strip().split()
    if len(i) < 2:
        i.append("")
    eval(f"t.{i[0]}({i[1]})")

turtle.mainloop()
