# 72 dpi, 4" x 3"
size(288, 216)

# gird variables
origin = (16, 16)
height = 184
width = 256
center = width/2
num_x_units = 24
num_y_units = 16
gut = 8 
col = 25
col_num = 8

def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(0.5)
    stroke(0.9, 0.1, 0.1, 0.7)  
    fill(None)

    step_y = 0 
    unit_y = height / num_y_units
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
        
    step_col = 0 
    stroke(0.1, 0.1, 0.9, 0.7)
    for column in range(8): 
        rect(step_col, 0, col, height)
        step_col += (col + gut)


#fill(0.8, 0.8, 0.8)
#stroke(None)
#rect(0, 0, 288, 216)

translate(*origin) # grid off
#grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

# Debug 
x, y, w, h = 0, 0, ((col * 8)+(gut *7)), 173

font("fonts/Wilmette-Italic.otf")
#font("fonts/Spectral-RegularItalic.otf")
fill(0, 0, 0)
stroke(None)

# Line 1
tracking(0)
fontSize(40)
textBox("Save the Date",
    (x, y+7, w, h), align="center")

# Line 2
tracking(0)
fontSize(24)
textBox("Sarah Jones",
    (x, y-46, w, h), align="center")

# Line 3
fontSize(31)
textBox("&",
    (x, y-66, w, h), align="center")

# Line 4
fontSize(24)
textBox("Eli  Heuer",
    (x, y-92, w, h), align="center")

tracking(1)
# Line 5
fontSize(13)
textBox("Are Getting Married",
    (x, y-117, w, h), align="center")

tracking(0)
# Line 6
fontSize(13)
#❤
#textBox("❦",
#    (x, y-137, w, h), align="center")

#openTypeFeatures(onum=True, smcp=True)
# Line 7
fontSize(13)
textBox("8-18-18 • NYC • https://sarah-eli.com",
    (x, y-153, w, h), align="center")

#saveImage("save-the-date.pdf")
#saveImage("save-the-date.png")