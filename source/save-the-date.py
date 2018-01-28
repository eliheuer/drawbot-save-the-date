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
num_y_units = 15
gut = 8 
col = 25
col_num = 8

def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(0.5)
    stroke(0.9, 0.1, 0.1, 0.5)  
    fill(None)

    step_y = 0 
    unit_y = height / num_y_units
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
        
    step_col = 0 
    stroke(0.1, 0.1, 0.9, 0.8)
    for column in range(8): 
        rect(step_col, 0, col, height)
        step_col += (col + gut)

#translate(*origin) # grid off
grid(origin, width, height, num_x_units*2, num_y_units*2) # grid on

x, y, w, h = 0, 32, ((col * 8) + (gut *7)), 104
font("LibrePlantin-Regular")
# fill(1, 0, 0)
# rect(x, y, w, h)
# fill(0)
fontSize(32)
lineHeight(32)
textBox("Save the Date",(x, y, w, h))
textBox("Name One & Name Two",(x, y-32, w, h))

saveImage("LibrePlantin-Regular-Proof.pdf")