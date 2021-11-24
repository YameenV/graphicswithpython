try:
	from os import environ
	environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
except ImportError:
	print("Ignore this",ImportError)

from typing import Optional
import pygame
from pygame import gfxdraw

win = None

def window(width:int, height:int):
	pygame.init()
	SCREEN_WIDTH = width 
	SCREEN_HEIGHT = height

	global win
	win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('GraphicswithPython')

def putpixel(xcordinates:int, ycordinates:int, color:str, intensity:Optional[int] = None):
	if intensity != None:
		pygame.draw.line(win, color, (xcordinates,ycordinates),(xcordinates,ycordinates), intensity)
	else:
		gfxdraw.pixel(win, xcordinates, ycordinates,color)
	pygame.display.update()

def getpixel(xcordinates:int, ycordinates:int) -> tuple:
	color = win.get_at((xcordinates, ycordinates))[:3]
	pygame.display.update()
	return color

def pointInCircle(centerx:int, centery:int, radius:int, x:int, y:int) -> bool:
    square_dist = (centerx - x) ** 2 + (centery - y) ** 2
    return square_dist <= radius ** 2

def line(x1:int ,y1:int,x2:int,y2:int, color:tuple):
	pygame.draw.line(win, color, (x1,y1),(x2,y2))
	pygame.display.update()

def circle(xcordinates:int, ycordinates:int, radius:int, color:tuple):
	pygame.draw.circle(win, color, center=(xcordinates, ycordinates), radius=radius, width=1)
	pygame.display.update()

def rectangle(left:int, top:int, width:int, height:int, color:tuple):
	pygame.draw.rect(win,color, pygame.Rect(left, top, width, height), width=2)
	pygame.display.update()

def ellipse(left:int, top:int, width:int, height:int, color:tuple):
	pygame.draw.ellipse(win, color, (left, top, width, height), width=2)
	pygame.display.update()

def polygon(points:tuple, color: tuple):
	pygame.draw.polygon(win, color, points, width=2)
	pygame.display.update()

def triangle(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int, color:tuple):
	pygame.draw.polygon(win, color, ((x1,y1),(x2,y2),(x3,y3)), width=2)
	pygame.display.update()

def delay(millisecond:int):
	pygame.time.delay(millisecond)

def color(color:str) -> tuple:
	colors = {"black":(0, 0, 0), 
			 "gray":(127, 127, 127),
			 "white":(255, 255, 255),
			 "red":(238, 75, 43),
			 "green":(0, 255, 0),
			 "blue":((135, 206, 235)),
			 "yellow":(255, 255, 0),
			 "orange":(255, 165, 0),
			 "purple":(191, 64, 191)
			 }
	for colorkey, rgbcolor in colors.items():
		if color.lower() == colorkey:
			return rgbcolor

def dda(x1:int, y1:int, x2:int, y2:int, DDatype:str, color:tuple):
	selectedType = None

	types={
		"line":1,
		"solid":2,
		"dotted":3,
		"dash":4
	}
	for type ,value in types.items():
		if DDatype.lower() == type:
			selectedType = value

	dx = abs(x2 - x1)
	dy = abs(y2 - y1)


	if (x1 > x2):
		x, y = x2, y2
	else:
		x, y = x1, y1

	steps = dx if (dx > dy) else dy

	x_inc = dx / steps
	y_inc = dy / steps

	putpixel(round(x), round(y), color)

	for i in range(steps):
		x = x + x_inc
		y = y + y_inc

		if selectedType == 1:
			putpixel(round(x), round(y), color)
			print(f"Xinc == {x}    Yinc == {y}")

		if selectedType == 2:
			putpixel(round(x), round(y), color, 2)
			print(f"Xinc == {x}    Yinc == {y}")

		if selectedType == 3:
			if (i % 4 == 0):
				putpixel(round(x), round(y), color)
				print(f"Xinc == {x}    Yinc == {y}")

		if selectedType == 4:
			if ((i%9>4)==0):
				putpixel(round(x), round(y), color)
				print(f"Xinc == {x}    Yinc == {y}")
		
		delay(10)
		
def bresenhams(x1:int, y1:int, x2:int, y2:int, bresenhamstype:str, color:tuple):
	selectedType = None

	types={
		"line":1,
		"solid":2,
		"dotted":3,
		"dash":4
	}
	for type ,value in types.items():
		if bresenhamstype.lower() == type:
			selectedType = value
	
		
	dx = abs(x2 - x1)
	dy = abs(y2 - y1)

	steps = dx if (dx > dy) else dy

	x, y = x1, y1

	p = 2*dy-dx

	for i in range(steps):
		
		if p > 0:
			p = p+2*dy-2*dx
			y = y+1
			x = x+1
			
		else:
			p = p+2*dy
			x = x+1
			y = y

		if selectedType == 1:
			putpixel(round(x), round(y), color)
			print(f"Xinc == {x}    Yinc == {y}")

		if selectedType == 2:
			putpixel(round(x), round(y), color, 2)
			print(f"Xinc == {x}    Yinc == {y}")

		if selectedType == 3:
			if (i % 4 == 0):
				putpixel(x, y, color)
				print(f"Xinc == {x}    Yinc == {y}")

		if selectedType == 4: 
			if ((i%9>4)==0):
				putpixel(x, y, color)
				print(f"Xinc == {x}   Yinc == {y}")
		
		delay(10)

def midpointcircle(radius:int, xcenter:int, ycenter:int, midpointtype:str, color:tuple):
	selectedType = None

	types={
		"line":1,
		"solid":2,
		"dotted":3,
		"dash":4,
		"dottedandline":5
	}
	for type ,value in types.items():
		if midpointtype.lower() == type:
			selectedType = value
	
	x = 0
	y = radius

	# Decision Parameter
	p = 1-radius

	i = 0

	while (x < y):

		if selectedType == 1:
			putpixel( xcenter+x, ycenter+y, color)
			putpixel( xcenter+x, ycenter-y, color)
			putpixel( xcenter-x, ycenter+y, color)
			putpixel( xcenter-x, ycenter-y, color)
			putpixel( xcenter+y, ycenter+x, color)
			putpixel( xcenter+y, ycenter-x, color)
			putpixel( xcenter-y, ycenter+x, color)
			putpixel( xcenter-y, ycenter-x, color)

		if selectedType == 2:
			putpixel( xcenter+x, ycenter+y, color,2)
			putpixel( xcenter+x, ycenter-y, color,2)
			putpixel( xcenter-x, ycenter+y, color,2)
			putpixel( xcenter-x, ycenter-y, color,2)
			putpixel( xcenter+y, ycenter+x, color,2)
			putpixel( xcenter+y, ycenter-x, color,2)
			putpixel( xcenter-y, ycenter+x, color,2)
			putpixel( xcenter-y, ycenter-x, color,2)

		if selectedType == 3: 
			if (i % 4 == 0):
				putpixel( xcenter+x, ycenter+y, color)
				putpixel( xcenter+x, ycenter-y, color)
				putpixel( xcenter-x, ycenter+y, color)
				putpixel( xcenter-x, ycenter-y, color)
				putpixel( xcenter+y, ycenter+x, color)
				putpixel( xcenter+y, ycenter-x, color)
				putpixel( xcenter-y, ycenter+x, color)
				putpixel( xcenter-y, ycenter-x, color)
		
		if selectedType == 4: 
			if ((i%9>4)==0):
				putpixel( xcenter+x, ycenter+y, color)
				putpixel( xcenter+x, ycenter-y, color)
				putpixel( xcenter-x, ycenter+y, color)
				putpixel( xcenter-x, ycenter-y, color)
				putpixel( xcenter+y, ycenter+x, color)
				putpixel( xcenter+y, ycenter-x, color)
				putpixel( xcenter-y, ycenter+x, color)
				putpixel( xcenter-y, ycenter-x, color)

		if selectedType == 5:
			dottedandline(xcenter, ycenter,x,y, color)

		
		if(p < 0):
			x = x+1
			y = y
			p = p + 2 * x + 1
		else :
			x = x + 1
			y = y - 1
			p = p + 2 *(x - y) + 1
		
		print(f"P=={p}  Xinc=={x}  Yinc=={y}")

		i += 1

		delay(10)

def floodfill(xcenter:int, ycenter:int, backgroundcolor:tuple, newcolor:tuple, seeds:int, radius:Optional[int] = None):
		if seeds in [4,8]:
			tofill = set()
			tofill.add((xcenter,ycenter))
			while len(tofill) > 0:
				(x,y) = tofill.pop()
				a =  getpixel(x,y)
				if a == backgroundcolor :
					if radius != None:
						if pointInCircle(xcenter,ycenter,radius, x,y) == True:
							if seeds == 4:
								putpixel(x,y,newcolor)
								tofill.add((x-1,y))
								tofill.add((x+1,y))
								tofill.add((x,y-1))
								tofill.add((x,y+1))
							else:
								putpixel(x,y,newcolor)
								tofill.add((x-1,y))
								tofill.add((x+1,y))
								tofill.add((x,y-1))
								tofill.add((x,y+1))
								tofill.add((x-1,y-1))
								tofill.add((x-1,y+1))
								tofill.add((x+1,y-1))
								tofill.add((x+1,y+1))
					else:
						if seeds == 4:
							putpixel(x,y,newcolor)
							tofill.add((x-1,y))
							tofill.add((x+1,y))
							tofill.add((x,y-1))
							tofill.add((x,y+1))
						else:
							putpixel(x,y,newcolor)
							tofill.add((x-1,y))
							tofill.add((x+1,y))
							tofill.add((x,y-1))
							tofill.add((x,y+1))
							tofill.add((x-1,y-1))
							tofill.add((x-1,y+1))
							tofill.add((x+1,y-1))
							tofill.add((x+1,y+1))

		else: 
			return "plz enter seed as 4 or 8"

def boundaryfill(xcenter:int, ycenter:int, bordercolor:tuple, newcolor:tuple, seeds:int, radius:Optional[int] = None):
		if seeds in [4,8]:
			tofill = set()
			tofill.add((xcenter,ycenter))
			while len(tofill) > 0:
				(x,y) = tofill.pop()
				a =  getpixel(x,y)
				if a != bordercolor and a != newcolor:
					if radius != None:
						if pointInCircle(xcenter,ycenter,radius, x,y) == True:
							if seeds == 4:
								putpixel(x,y,newcolor)
								tofill.add((x-1,y))
								tofill.add((x+1,y))
								tofill.add((x,y-1))
								tofill.add((x,y+1))
							else:
								putpixel(x,y,newcolor)
								tofill.add((x-1,y))
								tofill.add((x+1,y))
								tofill.add((x,y-1))
								tofill.add((x,y+1))
								tofill.add((x-1,y-1))
								tofill.add((x-1,y+1))
								tofill.add((x+1,y-1))
								tofill.add((x+1,y+1))
					else:
						if seeds == 4:
							putpixel(x,y,newcolor)
							tofill.add((x-1,y))
							tofill.add((x+1,y))
							tofill.add((x,y-1))
							tofill.add((x,y+1))
						else:
							putpixel(x,y,newcolor)
							tofill.add((x-1,y))
							tofill.add((x+1,y))
							tofill.add((x,y-1))
							tofill.add((x,y+1))
							tofill.add((x-1,y-1))
							tofill.add((x-1,y+1))
							tofill.add((x+1,y-1))
							tofill.add((x+1,y+1))

		else: 
			return "plz enter seed as 4 or 8"

def dottedandline(xcenter:int, ycenter:int, x:int, y:int, colors:str):
	for i in range(0, x):
		if i%2 == 1:
			putpixel( xcenter+x, ycenter+y, color("black"))
			putpixel( xcenter+y, ycenter+x, color("black"))
			putpixel( xcenter-y, ycenter-x, color("black"))
			putpixel( xcenter-x, ycenter-y, color("black"))

		else:
			putpixel( xcenter+x, ycenter+y, colors)
			putpixel( xcenter+y, ycenter+x, colors)
			putpixel( xcenter-y, ycenter-x, colors)
			putpixel( xcenter-x, ycenter-y, colors)

		putpixel( xcenter+x, ycenter-y, colors)
		putpixel( xcenter-x, ycenter+y, colors)
		putpixel( xcenter+y, ycenter-x, colors)
		putpixel( xcenter-y, ycenter+x, colors)

