from math import *
from random import randint,choice
import pygame
pygame.init()
win=pygame.display.set_mode((1200,600))
run=True
clock=pygame.time.Clock()
from World_Placement import world,m_world_x,m_world_y
world_x=0
world_y=0
player_pic=[pygame.image.load("Textures\PPrototype.png"),pygame.image.load("Textures\PPrototype2.png")]
def generate_map(level):
    global squar
    squar=[]
    map_=open("Maps\Map"+level+".txt","r")
    for i in map_:
        world1=[]
        for i1 in i:
            if i1!="\n":
                world1.append(i1)
        squar.append(world1)
players=0
Players=[]
generate_map(world[world_y][world_x])
class Player:
    def __init__(self,team,gun=randint(0,2)):
        global players
        players+=1
        self.a_frame=0
        self.bx=59
        self.by=29
        self.j_cooldown=0
        self.sx=0
        self.sy=0
        self.team=team
        self.x=29.5
        self.y=28
        self.xspeed=0
        self.yspeed=0
        self.alive=True
        self.gun=gun
        self.angle=pi*3/2
        self.jumping=False
        self.player=players
        self.burst1=0
        self.btimer=0
        self.charge=0
        self.s_frame=0
        if self.team==1:
            self.pcolor=(255,0,0)
        elif self.team==2:
            self.pcolor=(255,255,0)
        elif self.team==3:
            self.pcolor=(0,255,0)
        elif self.team==4:
            self.pcolor=(0,255,255)
        else:
            self.pcolor=(255,255,255)
    def move(self):
        if self.alive:
            global world_y,Transition_frame
            if self.player==1:
                self.up_k=keys[pygame.K_UP]
                self.down_k=keys[pygame.K_DOWN]
                self.left_k=keys[pygame.K_LEFT]
                self.right_k=keys[pygame.K_RIGHT]
            elif self.player==2:
                self.up_k=keys[pygame.K_w]
                self.down_k=keys[pygame.K_s]
                self.left_k=keys[pygame.K_a]
                self.right_k=keys[pygame.K_d]
            elif self.player==3:
                self.up_k=keys[pygame.K_t]
                self.down_k=keys[pygame.K_g]
                self.left_k=keys[pygame.K_f]
                self.right_k=keys[pygame.K_h]
            elif self.player==4:
                self.up_k=keys[pygame.K_i]
                self.down_k=keys[pygame.K_k]
                self.left_k=keys[pygame.K_j]
                self.right_k=keys[pygame.K_l]
            amx=round(self.x)
            amy=round(self.y)
            
            if self.right_k:
                if self.xspeed<0.11:
                    self.xspeed+=0.01
                elif self.x!=self.bx:
                    self.xspeed=0.11
                else:
                    self.xspeed=0.05
            elif self.left_k:
                if self.xspeed>-0.11:
                    self.xspeed-=0.01
                elif self.x!=self.sx:
                    self.xspeed=-0.11
                else:
                    self.xspeed=-0.05
            else:
                self.xspeed=self.xspeed*0.9
                if round(self.xspeed*100)==0:
                    self.xspeed=0
            if self.xspeed>0 and self.x<self.bx:
                self.x+=self.xspeed
                
            elif self.xspeed<0 and self.x>self.sx:
                self.x+=self.xspeed
            if squar[amy][amx]=="2" and self.up_k:
                self.y-=0.1
                self.yspeed=0
            elif squar[amy][amx]=="2" and not self.up_k:
                self.y+=0.1
                self.yspeed=0
            elif self.up_k and not self.jumping and self.j_cooldown==0 and self.y>self.sy:
                self.jumping=True
                self.j_cooldown=4
                self.yspeed=-0.2
            else:
                if self.yspeed<0.5:
                    self.yspeed+=0.01
                else:
                    self.yspeed=0.5
            if self.yspeed<0 and self.y<=self.by:
                self.y+=self.yspeed
                self.jumping=True
            
            if self.yspeed>0 and self.y>=self.sy:
                self.y+=self.yspeed
                self.jumping=True
            if self.j_cooldown>0:
                self.j_cooldown-=1
            if self.x<self.sx:
                self.x=self.sx
            elif self.x>self.bx:
                self.x=self.bx
            if self.y<self.sy:
                self.y=self.sy
                self.jumping=False
                self.yspeed=0
            elif self.y>self.by:
                self.y=self.by
                self.jumping=False
                self.yspeed=0
            self.angle+=self.xspeed
            self.pic=player_pic[round(self.a_frame)]
            if abs(self.xspeed)>0.1:
                self.a_frame+=0.04
                if round(self.a_frame)>=len(player_pic):
                    self.a_frame=0
            self.pic=player_pic[round(self.a_frame)]
            if self.xspeed<0:
                self.pic=pygame.transform.flip(self.pic,True,False)
            self.pic.set_colorkey((200,191,231))
            win.blit(self.pic,(self.x*20,self.y*20-60))
            #pygame.draw.rect(win,(self.pcolor),(self.x*20,self.y*20-20,20,40))
            if self.y==29:
                self.y=0.01
                world_y+=1
                Transition_frame=100
            elif self.y==0:
                self.y=28.99
                world_y-=1
                Transition_frame=100
hitboxes="1"
Players.append(Player(1))
Players.append(Player(1))
Players.append(Player(1))
Players.append(Player(1))

Transition_frame=0
while run:
    while run and Transition_frame==0:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        keys=pygame.key.get_pressed()
        win.fill((225,225,225))
        for i in Players:
            i.bx=59
            i.by=29
            i.sx=0
            i.sy=0
        for i in range(len(squar)):
            for i1 in range(len(squar[i])):
                if squar[i][i1] in hitboxes: 
                    #pygame.draw.rect(win,(155,155,155),(i1*20,i*20,20,20))
                    for i3 in Players:
                        if i3.y<=i+0.9 and i3.y>=i-0.9:
                            if i3.sx<=i1 and i1<=i3.x:
                                i3.sx=i1+1
                            if i3.bx>=i1 and i1>=i3.x:
                                i3.bx=i1-1
                        if i3.x<=i1+0.9 and i3.x>=i1-0.9:
                            if i3.sy<=i and i<=i3.y:
                                i3.sy=i+1
                            if i3.by>=i and i>=i3.y:
                                i3.by=i-1
                if squar[i][i1]=="1":
                    pygame.draw.rect(win,(55,55,255),(i1*20,i*20,20,20))
                elif squar[i][i1]=="2":
                    pygame.draw.rect(win,(128,61,0),(i1*20,i*20,20,20))
        clock.tick(100)
        for i in Players:
            i.move()
            #pygame.draw.rect(win,(255,0,0),(i.sx*20,i.y*20+10,20*(i.bx-i.sx+1),1))
            #pygame.draw.rect(win,(255,0,0),(i.x*20+10,i.sy*20,1,20*(i.by-i.sy+1)))    
        pygame.display.update()
    else:
        if Transition_frame>0:
            Transition_frame-=1
            if Transition_frame>50:
                pygame.draw.rect(win,(0,0,0),(0,0,1200,12*(100-Transition_frame)))
                clock.tick(100)
                pygame.display.update()
            else:
                if Transition_frame==50:
                    generate_map(world[world_y][world_x])
                win.fill((225,225,225))
                for i in range(len(squar)):
                    for i1 in range(len(squar[i])):
                        if squar[i][i1]=="1":
                            pygame.draw.rect(win,(55,55,55),(i1*20,i*20,20,20))
                        elif squar[i][i1]=="2":
                            pygame.draw.rect(win,(128,61,0),(i1*20,i*20,20,20))
                for i in Players:
                    pygame.draw.rect(win,i.pcolor,(i.x*20,i.y*20,20,20))
                clock.tick(100)
                pygame.draw.rect(win,(0,0,0),(0,0,1200,12*Transition_frame))
                
                pygame.display.update()
pygame.quit()
