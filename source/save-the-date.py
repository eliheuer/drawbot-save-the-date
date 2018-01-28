# 72 dpi, 4" x 3"
size(288, 216)

# Debug tools
# print installedFonts()

# gird variables
origin = (16, 16)
height = 184
width = 256
center = width/2
num_x_units = 24
num_y_units = 4
gut = 8 
col = 25
col_num = 8

def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(0.5)
    stroke(0.9, 0.1, 0.1, 0.1)  
    fill(None)

    step_y = 0 
    unit_y = height / num_y_units
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
        
    step_col = 0 
    stroke(0.1, 0.1, 0.9, 0.2)
    for column in range(8): 
        rect(step_col, 0, col, height)
        step_col += (col + gut)


fill(0.9, 0.9, 0.9)
stroke(None)
rect(0, 0, 288, 216)
#translate(*origin) # grid off
grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# Debug 
x, y, w, h = 0, 0, ((col * 8)+(gut *7)), 173
#fill(1, 0, 0, .1)
#rect(x, y, w, h)

font("fonts/Wilmette-Italic.otf")
fill(0, 0, 0)
stroke(None)

# Line 1
fontSize(38)
textBox("Save the Date",
    (x, y+19, w, h), align="center")

# Line 2
#fontSize(32)
#textBox("0-00-0",
#    (x, y-38, w, h), align="center")

# Line 2
fontSize(24)
textBox("Person One",
    (x, y-35, w, h), align="center")

# Line 2
fontSize(24)
textBox("&",
    (x, y-65, w, h), align="center")

# Line 3
fontSize(24)
textBox("Person Two",
    (x, y-81, w, h), align="center")

# Line disc
fontSize(13)
textBox("Are Getting Married",
    (x, y-114, w, h), align="center")
    
# Line location
fontSize(13)
textBox("8-18-18 | NYC | https://one-two.wedding",
    (x, y-160, w, h), align="center")
       
# Line end
#fontSize(12)
#textBox("https://sarah-eli.wedding",
#    (x, y-161, w, h), align="center")

#saveImage("save-the-date.pdf")