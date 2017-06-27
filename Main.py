var1="background1.jpg"
var2="background2.jpg"
var3="background3.jpg"
var4="andgate.jpg"
var5="orgate.jpg"
var6="notgate.jpg"
var7="nandgate.jpg"
var8="norgate.jpg"
var9="exorgate.jpg"
var10="xnorgate.jpg"
var11="adder4.jpg"

import pygame,sys
import time
import random
from locals import *
pygame.init()

screen_width=1366
screen_height=768
screen=pygame.display.set_mode((screen_width,screen_height),0,32)

backg=pygame.image.load(var1).convert()
startscr=pygame.image.load(var2).convert()
menuscr=pygame.image.load(var3).convert()
andscr=pygame.image.load(var4).convert()
orgscr=pygame.image.load(var5).convert()
notscr=pygame.image.load(var6).convert()
nandscr=pygame.image.load(var7).convert()
norscr=pygame.image.load(var8).convert()
xorscr=pygame.image.load(var9).convert()
xnorscr=pygame.image.load(var10).convert()
addbg=pygame.image.load(var11).convert()
subbg=pygame.image.load(var11).convert()

white=[255,255,255]
black=[0,0,0]
red=[150,0,0]
light_red=[255,0,0]
green=[34,177,76]
light_green=[0,255,0]
snake_green=[0,155,0]
blue=[0,0,255]
yellow=[220,220,0]
light_yellow=[255,255,0]

string1=[]
string2=[]
num1=0
num2=0
sum=0

clock=pygame.time.Clock()
flag=0

smallfont=pygame.font.SysFont("comicsnasms",32)
medfont=pygame.font.SysFont("comicsnasms",50)
largefont=pygame.font.SysFont("comicsnasms",80)

def text_objects(text,color,size):
	if size == "small":	
		screen_surf = smallfont.render(text,True,color)
	if size == "medium":	
		screen_surf = medfont.render(text,True,color)
	if size == "large":	
		screen_surf = largefont.render(text,True,color)
	return screen_surf,screen_surf.get_rect()

def message(msg,color,y_disp=0,size="small"):
	screen_surface,text_rect = text_objects(msg,color,size)
	#screen_text=font.render(msg,True,color)
	#screen.blit(screen_text,(screen_width/3,screen_height/3))
	text_rect.center=(screen_width/2),(screen_height/2)+y_disp
	screen.blit(screen_surface,text_rect)

def button_text(msg,button_x,button_y,button_width,button_height,size="small"):	
	screen_surface,text_rect = text_objects(msg,black,size)
	text_rect.center = (button_x + button_width/2),(button_y + button_height/2) 
	screen.blit(screen_surface,text_rect)
		
def button(text,x,y,width,height,inactive_color,active_color,action = None):
	cursor = pygame.mouse.get_pos()
	if x+width > cursor[0] >x and y +height> cursor[1] > y:
		pygame.draw.rect(screen,active_color,(x,y,width,height))
		click = pygame.mouse.get_pressed()
		if click[0] == 1 and action != None:
			if action == "start":
				menuScreen()
			elif action == "quit":
				pygame.quit()
				quit()
			elif action == "menu":
				s1=0
				s2=0
				string1=[]
				string2=[]
				menuScreen()
			if action == "and":
				andLoop()
			if action == "or":
				orLoop()
			if action == "not":
				notLoop()
			if action == "nand":
				nandLoop()
			if action == "nor":
				norLoop()
			if action == "exor":
				exorLoop()
			if action == "exnor":
				exnorLoop()
			if action == "adder":
				addLoop()
			if action == "subtr":
				subLoop()
			if action == "comp":
				compLoop()
			elif action == "0not" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "1not" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")		
			elif action == "00and" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "01and" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "10and" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "11and" :
				button("1",1100,150,50,50,light_red,light_red,"Output 1")
			elif action == "00or" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "01or" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "10or" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "11or" :
				button("1",1100,150,50,50,light_red,light_red,"Output 1")
			elif action == "00nand" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "01nand" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "10nand" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "11nand" :
				button("0",1100,150,80,80,light_red,light_red,"Output 1")
			elif action == "00nor" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "01nor" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "10nor" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "11nor" :
				button("0",1100,150,80,80,light_red,light_red,"Output 1")
			elif action == "00xor" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "01xor" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "10xor" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "11xor" :
				button("0",1100,150,80,80,light_red,light_red,"Output 1")
			elif action == "00xnor" :
				button("1",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "01xnor" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "10xnor" :
				button("0",1100,150,80,80,light_red,light_red,"Output 0")
			elif action == "11xnor" :
				button("1",1100,150,80,80,light_red,light_red,"Output 1")	
			if action == "findsum":
				button(sum,1000,600,80,80,light_green,light_green,"answer")
				
				
			elif action == "Output 0" or action == "Output 1" :	
				pygame.display.update()
				clock.tick(20)	
	else:
		pygame.draw.rect(screen,inactive_color,(x,y,width,height))

	button_text(text,x,y,width,height,"small")
	
def startScreen():
	intro = True
	while intro:
		screen.blit(startscr,(0,0))		
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
		
		button("Start",600,400,175,80,green,light_green,"start")
		button("Quit",600,500,175,80,red,light_red,"quit")
		
		pygame.display.update()
		clock.tick(10)

def menuScreen():
	menu = True
	while menu:
		screen.blit(menuscr,(0,0))		
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
		
		button("AND",600,50,200,75,yellow,light_green,"and")
		button("OR",600,150,200,75,yellow,light_green,"or")
		button("NOT",600,250,200,75,yellow,light_green,"not")
		button("NAND",600,350,200,75,yellow,light_green,"nand")
		button("NOR",600,450,200,75,yellow,light_green,"nor")
		button("EX-OR",600,550,200,75,yellow,light_green,"exor")
		button("EX-NOR",600,650,200,50,yellow,light_green,"exnor")
		button("ADDER",900,50,100,75,green,light_green,"adder")
		button("SUBTRACTOR",900,150,160,75,green,light_green,"subtr")
		button("COMPARATOR",900,250,160,75,green,light_green,"comp")
		button("Quit",100,600,200,80,red,light_red,"quit")
		
		pygame.display.update()
		clock.tick(10)		
		
def andLoop():
	gameExit=False
	screen.blit(andscr,(0,0))
	pygame.draw.rect(screen,red,(1100,150,80,80))
	while not gameExit:
		#pygame.draw.rect(screen,red,(1000,100,50,50))
		button("0 0",174,170,90,75,red,light_red,"00and")
		button("0 1",174,270,90,75,red,light_red,"01and")
		button("1 0",174,370,90,75,red,light_red,"10and")
		button("1 1",174,470,90,75,red,light_red,"11and")
		button("Quit",100,650,150,50,green,light_green,"quit")
		button("Menu",1180,650,150,80,light_green,light_yellow,"menu")
			
		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit=True
						
		pygame.display.update()
		clock.tick(20)
	
	pygame.quit()
	quit()

def orLoop():
	gameExit=False
	pygame.draw.rect(screen,red,(1000,100,50,50))
	screen.blit(orgscr,(0,0))
	while not gameExit:
		#pygame.draw.rect(screen,red,(1000,100,50,50))
		button("0 0",174,170,90,75,red,light_red,"00or")
		button("0 1",174,270,90,75,red,light_red,"01or")
		button("1 0",174,370,90,75,red,light_red,"10or")
		button("1 1",174,470,90,75,red,light_red,"11or")
		button("Quit",100,650,150,50,green,light_green,"quit")
		button("Menu",1180,650,150,50,green,light_green,"menu")
			
				
		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit=True
						
		pygame.display.update()
		clock.tick(20)
	
	pygame.quit()
	quit()
	
def notLoop():
	gameExit=False
	pygame.draw.rect(screen,red,(1000,100,50,50))
	screen.blit(notscr,(0,0))
	while not gameExit:
		#pygame.draw.rect(screen,red,(1000,100,50,50))
		button("0",174,170,90,75,red,light_red,"0not")
		button("1",174,270,90,75,red,light_red,"1not")
		
		button("Quit",100,650,150,50,green,light_green,"quit")
		button("Menu",1180,650,150,50,green,light_green,"menu")	
				
		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit=True
						
		pygame.display.update()
		clock.tick(20)
	
	pygame.quit()
	quit()

def nandLoop():
	gameExit=False
	pygame.draw.rect(screen,red,(1000,100,50,50))
	screen.blit(nandscr,(0,0))
	while not gameExit:
		#pygame.draw.rect(screen,red,(1000,100,50,50))
		button("0 0",174,170,90,75,red,light_red,"00nand")
		button("0 1",174,270,90,75,red,light_red,"01nand")
		button("1 0",174,370,90,75,red,light_red,"10nand")
		button("1 1",174,470,90,75,red,light_red,"11nand")
		button("Quit",100,650,150,50,green,light_green,"quit")
		button("Menu",1180,650,150,50,green,light_green,"menu")
			
				
		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit=True
						
		pygame.display.update()
		clock.tick(20)
	
	pygame.quit()
	quit()	

def norLoop():
	gameExit=False
	pygame.draw.rect(screen,red,(1000,100,50,50))
	screen.blit(norscr,(0,0))
	while not gameExit:
		#pygame.draw.rect(screen,red,(1000,100,50,50))
		button("0 0",174,170,90,75,red,light_red,"00nor")
		button("0 1",174,270,90,75,red,light_red,"01nor")
		button("1 0",174,370,90,75,red,light_red,"10nor")
		button("1 1",174,470,90,75,red,light_red,"11nor")
		button("Quit",100,650,150,50,green,light_green,"quit")
		button("Menu",1180,650,150,50,green,light_green,"menu")	
				
		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit=True
						
		pygame.display.update()
		clock.tick(20)
	
	pygame.quit()
	quit()
	
def exorLoop():
	gameExit=False
	pygame.draw.rect(screen,red,(1000,100,50,50))
	screen.blit(xorscr,(0,0))
	while not gameExit:
		#pygame.draw.rect(screen,red,(1000,100,50,50))
		button("0 0",174,170,90,75,red,light_red,"00xor")
		button("0 1",174,270,90,75,red,light_red,"01xor")
		button("1 0",174,370,90,75,red,light_red,"10xor")
		button("1 1",174,470,90,75,red,light_red,"11xor")
		button("Quit",100,650,150,50,green,light_green,"quit")
		button("Menu",1180,650,150,50,green,light_green,"menu")	
				
		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit=True
						
		pygame.display.update()
		clock.tick(20)
	
	pygame.quit()
	quit()

def exnorLoop():
	gameExit=False
	pygame.draw.rect(screen,red,(1000,100,50,50))
	screen.blit(xnorscr,(0,0))
	while not gameExit:
		#pygame.draw.rect(screen,red,(1000,100,50,50))
		button("0 0",174,170,90,75,red,light_red,"00xnor")
		button("0 1",174,270,90,75,red,light_red,"01xnor")
		button("1 0",174,370,90,75,red,light_red,"10xnor")
		button("1 1",174,470,90,75,red,light_red,"11xnor")
		button("Quit",100,650,150,50,green,light_green,"quit")
		button("Menu",1180,650,150,50,green,light_green,"menu")	
				
		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit=True
						
		pygame.display.update()
		clock.tick(20)
	
	pygame.quit()
	quit()	
	
def addLoop():
	gameExit = False
	global string1
	global str1
	global str2
	global s1
	global s2
	global num1
	global num2
	global sum1
	global sum2
	global sum
	
	sum=0
	
	string1=[]
	string2=[]
	button("",1000,600,80,80,light_green,light_green,"answer")
	screen.blit(addbg,(0,0))
	while not gameExit:
		button("Quit",100,700,80,50,green,light_green,"quit")
		button("Menu",1180,700,80,50,green,light_green,"menu")

		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit == True
			
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					string1.append('0')
					s1=''.join(string1)
					button(s1,750,220,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_w:
					string1.append('1')
					s1=''.join(string1)
					button(s1,750,220,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_a:
					string2.append('0')
					s2=''.join(string2)
					button(s2,750,380,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_s:
					string2.append('1')	
					s2=''.join(string2)
					button(s2,750,380,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_RETURN:
					str1=''.join(string1)
					str2=''.join(string2)
					#print str1,str2
					num1=int(str1,2)
					num2=int(str2,2)
					sum1=num1+num2
					sum2=int(bin(sum1)[2:])
					sum=str(sum2)
					print sum
					button(sum,580,610,140,70,green,green,"akshay")
					
		
		pygame.display.update()
		clock.tick(20)
	pyagme.quit()
	quit()	
	
def subLoop():
	gameExit = False
	global string1
	global str1
	global str2
	global s1
	global s2
	global num1
	global num2
	global sum1
	global sum2
	global sum
	
	sum=0
	
	string1=[]
	string2=[]
	button("",1000,600,80,80,light_green,light_green,"answer")
	screen.blit(addbg,(0,0))
	while not gameExit:
		button("Quit",100,700,80,50,green,light_green,"quit")
		button("Menu",1180,700,80,50,green,light_green,"menu")

		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit == True
			
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					string1.append('0')
					s1=''.join(string1)
					button(s1,750,220,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_w:
					string1.append('1')
					s1=''.join(string1)
					button(s1,750,220,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_a:
					string2.append('0')
					s2=''.join(string2)
					button(s2,750,370,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_s:
					string2.append('1')	
					s2=''.join(string2)
					button(s2,750,370,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_RETURN:
					str1=''.join(string1)
					str2=''.join(string2)
					#print str1,str2
					num1=int(str1,2)
					num2=int(str2,2)
					sum1=num1-num2
					sum2=int(bin(sum1)[2:])
					sum=str(sum2)
					print sum
					button(sum,580,610,140,70,light_green,light_green,"akshay")
				
		
		pygame.display.update()
		clock.tick(20)
	pygame.quit()
	quit()		

def compLoop():
	gameExit = False
	global string1
	global str1
	global str2
	global s1
	global s2
	global num1
	global num2
	global sum1
	global sum2
	global sum
	
	sum=0
	
	string1=[]
	string2=[]
	button("",1000,600,80,80,light_green,light_green,"answer")
	screen.blit(addbg,(0,0))
	while not gameExit:
		button("Quit",100,700,80,50,green,light_green,"quit")
		button("Menu",1180,700,80,50,green,light_green,"menu")

		for event in pygame.event.get():
			if event.type == QUIT:
				gameExit == True
			
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					string1.append('0')
					s1=''.join(string1)
					button(s1,750,220,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_w:
					string1.append('1')
					s1=''.join(string1)
					button(s1,750,220,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_a:
					string2.append('0')
					s2=''.join(string2)
					button(s2,750,370,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_s:
					string2.append('1')	
					s2=''.join(string2)
					button(s2,750,370,140,70,light_green,light_green,"akshay")
				elif event.key==pygame.K_RETURN:
					str1=''.join(string1)
					str2=''.join(string2)
					#print str1,str2
					num1=int(str1,2)
					num2=int(str2,2)
					if num1 > num2:
						sum1=num1
					else:
						sum1=num2
					sum2=int(bin(sum1)[2:])
					sum=str(sum2)
					print sum
					button(sum,580,610,140,70,light_green,light_green,"akshay")
				
		
		pygame.display.update()
		clock.tick(20)
	pygame.quit()
	quit()		
	
startScreen()	