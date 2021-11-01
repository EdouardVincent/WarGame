#WarGame

import pygame, sys, time, random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

nb_joysticks = pygame.joystick.get_count()
 
#Et on en crée un s'il y a en au moins un
if nb_joysticks > 0:
    joystick = pygame.joystick.Joystick(0)
 
    joystick.init() #Initialisation
    
fenetre= pygame.display.set_mode ((1000,400))
fond = pygame.font.Font('freesansbold.ttf', 18)
fond2 = pygame.font.Font('freesansbold.ttf', 50)
fond3 = pygame.font.Font('freesansbold.ttf', 30)
image_droite_rambo = pygame.image.load('C:\Jeu personnages\chasseur.png')
bullet = pygame.image.load('C:\Jeu personnages\Z.gif')
bg=pygame.image.load('C:\Jeu personnages\OIP.png')
cs = pygame.image.load('C:\Jeu personnages\OIP (2).png')
papi = pygame.image.load('C:\Jeu personnages\OIP (1).png')
sanglier_image = pygame.image.load('C:\Jeu personnages\OIP (3).png')
Icone = pygame.image.load('C:\Jeu personnages\OIP.ico')
coeur1 = pygame.image.load('C:\Jeu personnages\OIP (6).png')
coeur2 = pygame.image.load('C:\Jeu personnages\OIP (6).png')
soldier_image = pygame.image.load('C:\Jeu personnages\OIP (4).png')
space_soldier_image = pygame.image.load('C:\Jeu personnages\OIP (5).png')
james_image = pygame.image.load('C:\Jeu personnages\OIP (7).png')
icone_balle = pygame.image.load('C:\Jeu personnages\OIP (8).png')
menu_img = pygame.image.load('C:\Jeu personnages\OIP (13).png')
bouton_jouer = pygame.image.load('C:\Jeu personnages\OIP (12).png')
bouton_quitter = pygame.image.load('C:\Jeu personnages\OIP (14).png')
play = pygame.image.load('C:\Jeu personnages\OIP (15).png')
terroriste_image = pygame.image.load('C:\Jeu personnages\OIP (17).png')
kamikaze = pygame.image.load('C:\Jeu personnages\OIP (18).png')
colonel = pygame.image.load('C:\Jeu personnages\OIP (19).png')
dialogue_colonel_1 = pygame.image.load('C:\Jeu personnages\OIP (20).png')
dialogue_colonel_2 = pygame.image.load('C:\Jeu personnages\OIP (21).png')
bouton_commencer = pygame.image.load('C:\Jeu personnages\OIP (22).png')
stop = pygame.image.load('C:\Jeu personnages\OIP (16).png')
Kaboul = pygame.image.load('C:\Jeu personnages\OIP (23).png')
nouvelle_partie = pygame.image.load('C:\Jeu personnages\OIP (24).png')
continuer_partie = pygame.image.load('C:\Jeu personnages\OIP (25).png')
capitaine_Mitchell_image = pygame.image.load('C:\Jeu personnages\OIP (26).png')
foret = pygame.image.load('C:\Jeu personnages\OIP (27).png')
balle_gauche_image = pygame.image.load('C:\Jeu personnages\OIP (28).png')
ground = pygame.image.load('C:\Jeu personnages\OIP (29).png')
échelle_image = pygame.image.load('C:\Jeu personnages\OIP (31).png')
passerelle = pygame.image.load('C:\Jeu personnages\OIP (32).png')
passerelle_spéciale = pygame.image.load('C:\Jeu personnages\OIP (33).png')
zone_vide = pygame.image.load('C:\Jeu personnages\OIP (34).png')
detection_ennemi = pygame.image.load('C:\Jeu personnages\OIP (35).png')
dialogue_colonel_3 = pygame.image.load('C:\Jeu personnages\OIP (36).png')
arrow_image = pygame.image.load('C:\Jeu personnages\OIP (37).png')
black_animation = pygame.image.load('C:\Jeu personnages\OIP (38).png')
bouton_oui = pygame.image.load('C:\Jeu personnages\OIP (39).png')
bouton_non = pygame.image.load('C:\Jeu personnages\OIP (40).png')
Kaboul_level = pygame.image.load('C:\Jeu personnages\OIP (41).png')
terroriste_parachute = pygame.image.load('C:\Jeu personnages\OIP (56).png') 
menu_musique = pygame.mixer.Sound('C:\Jeu personnages\OIP (4).mp3')
Kaboul_musique = pygame.mixer.Sound ('C:\Jeu personnages\oip (5).mp3')
singe = pygame.mixer.Sound('C:\Jeu personnages\OIP (7).mp3')
pygame.mixer.music.load('C:\Jeu personnages\OIP (6).mp3')
pygame.display.set_icon(Icone)

RED = 255, 0, 0 #création de couleurs
YELLOW = 220, 220, 0
BLACK = 0, 0, 0

#Créations de variables qui cont etre utile tout au long du programme :

menu = 1
son_joué = 1
choose_soldier = 0
image_son = play
menu_Kaboul=0

tir = 0
close = 0
Won = 0
training = 0
lvl1 = 0
lvl2 = 0
die_terrorist = 0
loop = 0
tombee = 0
joueur_echelle = 0
detection_soldat = 0
tir_tero = 0
congratulations = 0
grade = ''
animation_victoire = 0
nouvelle_fenetre = 0
son_joué = 1

bouton_continuer = continuer_partie.get_rect(topleft = (300, 240))
quitter = bouton_quitter.get_rect(topleft = (362, 300))
bouton_son_play = play.get_rect(topleft = (0, 0))
bouton_son_quitter = stop.get_rect(topleft = (0,0))
bouton_commencer_rect = bouton_jouer.get_rect(topleft = (370, 200))
bouton_nouvelle_partie = nouvelle_partie.get_rect(topleft = (310, 182))

class Soldat () :
    def __init__ (self) :
        self.x = 0
        self.y = 0
        self.image = image_droite_rambo
        self.increment = 15

    def affichage (self) :
        fenetre.blit(self.image,(self.x, self.y))
      
    def deplacement_haut (self) :
        self.y -= self.increment
      
    def deplacement_bas (self) :
        self.y += self.increment

    def deplacement_droite (self) :
        self.x += self.increment

    def deplacement_gauche (self) :
        self.x -= self.increment
      
class Balle () :
    def __init__(self) :
        self.x = 0
        self.y = 0
        self.image = bullet
        self.increment = 2
      
    def affichage (self) :
        fenetre.blit(self.image,(self.x, self.y))
      
    def deplacement (self) :
        self.x += self.increment

class animal () :
    def __init__(self) :
        self.x = 1000
        self.y = 0
        self.image = sanglier_image
        self.increment = 1.25

    def affichage(self) :
        fenetre.blit(self.image,(self.x, self.y))

    def deplacement_gauche (self) :
        self.x -= self.increment

class Terroriste () :
    def __init__(self) :
        self.x = 1500
        self.y = 105
        self.image = terroriste_image
        self.increment = 5

    def affichage (self) :
        fenetre.blit(self.image,(self.x, self.y))

    def deplacement_gauche(self) :
        self.x -= self.increment

    def deplacement_droite(self) :
        self.x += self.increment

    def deplacement_bas(self) :
        self.y += self.increment

class Sol () :
    def __init__(self) :
        self.x = 0
        self.y = 360
        self.image = ground

    def affichage(self) :
        fenetre.blit(self.image,(self.x, self.y))

class Echelle () :
    def __init__(self) :
        self.x = 100
        self.y = 300
        self.image = échelle_image

    def affichage (self) :
        fenetre.blit(self.image,(self.x, self.y))

class Plateforme () :
    def __init__ (self) :
        self.x = 0
        self.y = 200
        self.image = passerelle

    def affichage(self) :
        fenetre.blit(self.image,(self.x, self.y))

def draw (texte, x, y) :
    fenetre.blit(texte,(x, y))

barbu_rect = papi.get_rect(topleft = (0,0))
chasseur_rect = image_droite_rambo.get_rect(topleft = (200,0))
cs_rect = cs.get_rect(topleft = (400,0))
soldier_rect = soldier_image.get_rect(topleft = (600,0))
space_soldier_rect = space_soldier_image.get_rect(topleft = (800,0))
james_rect = james_image.get_rect(topleft = (0, 200))

pygame.key.set_repeat(1,20)

while menu: # boucle principale
    
    if son_joué == 1 :
        menu_musique.play(999,0,0)
    
    pygame.display.set_caption('WAR GAME')

    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
              
        if event.type == KEYDOWN :            
            if event.key == K_ESCAPE :
                pygame.quit()
                sys.exit()
          
        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
            
            if bouton_continuer.collidepoint(event.pos) :
                with open("Niveau.txt","r") as level :
                    texte = level.readlines()

                menu = 0
                if texte == ['niveau 0'] :
                    training = 1
                    Won = 0
                    lvl1 = 0

                elif texte == ['congratulations'] :
                    congratulations = 1
                    Won = 0
                    lvl1 = 0
                    training = 0

                elif texte == ['level 1']  :
                    choose_soldier = 1
                    Won = 1
                    training = 0
                    lvl1 = 1

                elif texte == ['level 2'] :
                    choose_soldier = 1
                    Won = 0
                    training = 0
                    menu_Kaboul = 0
                    lvl1 = 0
                    lvl2 = 1

            if quitter.collidepoint(event.pos) :
                pygame.quit()
                sys.exit()
                          
            if bouton_son_play.collidepoint(event.pos):
                image_son = stop
                son_joué = 0

            if bouton_nouvelle_partie.collidepoint(event.pos) :
                menu = 0
                choose_soldier = 1

                training = 1
                Won = 0
                with open("Niveau.txt","w") as level :
                    level.write("niveau 0")
                    
    draw(bg,0,0)
    draw(menu_img,0,0)
    draw(image_son,0,0)
    draw(continuer_partie,300,240)
    draw(bouton_quitter,362, 300)
    draw(nouvelle_partie,310, 182)
    
    
    with open("Niveau.txt","r") as RankTexte :
        rank = RankTexte.read()

    if rank == 'niveau 0' :
        grade = 'soldat 2nde classe'

    if rank == 'level 1' :
        grade = 'soldat 2nde classe'

    if rank == 'level 2' :
        grade = 'soldat 2nde classe'

    if rank == 'congratulations' :
        grade = 'soldat 1ère classe'
        
    RankSurf = fond3.render('Grade : %s' % (grade), True, RED)
    draw(RankSurf, 260,0)
    pygame.display.flip()

    if choose_soldier == 1:
        menu_musique.stop()
        joueur = Soldat()
        balle = Balle()
        sanglier = animal()

        vie_sanglier = [1, 1, 1, 1, 1]
        vie_chasseur = [1]

        nb_balles = 10

    while choose_soldier :
                            
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
       
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if barbu_rect.collidepoint(event.pos) :
                    joueur.image = papi
                    choose_soldier = 0
                    training = 1

                if chasseur_rect.collidepoint(event.pos) :
                    joueur.image = image_droite_rambo
                    choose_soldier = 0
                    training = 1
               
                if cs_rect.collidepoint(event.pos) :              
                    joueur.image = cs
                    choose_soldier = 0
                    training = 1

                if soldier_rect.collidepoint(event.pos) :
                    joueur.image = soldier_image
                    choose_soldier = 0
                    training = 1

                if space_soldier_rect.collidepoint(event.pos) :
                    joueur.image = space_soldier_image
                    choose_soldier = 0
                    training = 1
       
                if james_rect.collidepoint(event.pos) :
                    joueur.image = james_image
                    choose_soldier = 0
                    training = 1
                                              
        draw(bg,0,0)
        draw(papi,0,0)
        draw(image_droite_rambo,200,0)
        draw(cs,400,0)
        draw(soldier_image,600,0)
        draw(space_soldier_image,800,0)
        draw(james_image,0,200)
        pygame.display.flip()

    if choose_soldier == 0 :
        
        with open("Niveau.txt","r") as level :
            texte = level.readlines()

        if texte == ['niveau 0'] :
            training = 1
            Won = 0
       
        if training == 1 :
            if texte != ['niveau 0'] :
                training = 0
                Won = 1
                menu_Kaboul = 1

        if training == 1 :
            with open("Niveau.txt","w") as level :
                level.write("niveau 0")
                    
            menu_musique.stop()
            pygame.display.set_caption('training')
           
            vie_chasseur =[1]
            vie_sanglier = [1, 1, 1, 1, 1]

            sanglier.x = 1000
            sanglier.y = random.randint(0,300)
           
            fenetre.blit(bg, (0,0))
            Level1Surf = fond2.render('ENTRAINEMENT', True, RED)
            draw(Level1Surf, 280, 100)
            pygame.display.flip()
            time.sleep(2)
            KillSurf = fond2.render('TUEZ LE SANGLIER !', True, RED)
            draw(KillSurf, 220, 200)
            pygame.display.flip()
            time.sleep(3)

    while training :
        if Won == 1 :
            training = 0
            menu = 1
   
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
          
            if event.type == KEYDOWN :

                if event.key == K_RETURN and tir == 0 and nb_balles > 0:
                    if son_joué == 1 :
                        pygame.mixer.music.play(1, 0.9, 0)
                    nb_balles-=1
                    tir=1
              
                if event.key == K_UP :
                    joueur.deplacement_haut()
          
                if event.key == K_DOWN :
                    joueur.deplacement_bas()

            elif event.type == JOYAXISMOTION:
                if event.axis == 1 and event.value < -0.5:
                    joueur.deplacement_haut()
 
                elif event.axis == 1 and event.value > 0.5:
                    joueur.deplacement_bas()

            elif event.type == JOYBUTTONDOWN :
                if event.button == 2 and tir == 0 and nb_balles > 0:
                    if son_joué == 1 :
                        pygame.mixer.music.play(1, 0.9, 0)
                nb_balles-=1
                tir=1

        sanglier.deplacement_gauche()
        sanglier_rect = sanglier_image.get_rect(topleft = (sanglier.x, sanglier.y))
   
        if balle.x > 1000 :
            balle.x = joueur.x
            balle.y = joueur.y
            tir = 0

        if tir == 1 :
            balle.deplacement()
              
        if tir == 0 :
            balle.x = joueur.x +50
            balle.y = joueur.y +50

        if joueur.y <= -10:
            joueur.deplacement_bas()

        if joueur.y >= 315:
            joueur.deplacement_haut()

        if sanglier.x <= -50 :
            sanglier.x = 1000
            sanglier.y = random.randint(0,300)

        if sanglier_rect.collidepoint(balle.x, balle.y) and tir == 1 :
            vie_sanglier.pop()  
            tir = 0
       
        if sanglier_rect.collidepoint(joueur.x, joueur.y) :
            vie_chasseur.pop()

        if len(vie_chasseur) == 0 :
            YouLose = fond2.render('YOU LOSE !', True, RED)
            draw(YouLose, 350, 100)
            pygame.display.flip()
            time.sleep(2)
            training = 0
            menu = 1

       
        if len(vie_sanglier) == 0 :
            YouWon = fond2.render('YOU WON !', True, RED)
            draw(YouWon, 350, 100)
            pygame.display.flip()
            time.sleep(2)
            Won = 1
            training =0
            with open("Niveau.txt","w") as level :
                level.write("level 1")
                
            ColonelSurf = fond.render('COLONEL GEORGES', True, BLACK) #discours du colonel
            draw(bg,0,0)
            draw(colonel,0,100)
            draw(dialogue_colonel_1,80,10)
            draw(ColonelSurf,0,220)
            pygame.display.flip()
            time.sleep(10)
            draw(bg,0,0)
            draw(colonel,0,100)
            draw(dialogue_colonel_2,80,10)
            draw(ColonelSurf,0,220)
            pygame.display.flip()
            time.sleep(10)
       
        draw(bg, 0,0)
        scoreSurfChasseur = fond.render('Vie : %s' % (len(vie_chasseur)), True, RED)
        scoreSurfSanglier = fond.render('Vies : %s' % (len(vie_sanglier)), True, RED)
        nb_balles_surf = fond.render('balles : %s' % nb_balles,True,YELLOW)
        draw(scoreSurfChasseur ,0 ,3)
        draw(scoreSurfSanglier ,895 ,3)
        draw(coeur1 ,60 ,0)
        draw(coeur2 ,965 ,0)
        draw(icone_balle ,100 ,25)
        draw(nb_balles_surf,0 ,30)
   
        if tir == 1 :
            balle.affichage()
       
        joueur.affichage()
        sanglier.affichage()
        pygame.display.flip()
   
    if Won == 1 :
        menu_musique.stop()
        if son_joué == 1 :
            Kaboul_musique.play(999,0,0)
        
        Level1Surf = fond3.render('LEVEL 1 : Position : Kaboul, Local hour : 7:00 AM', True, YELLOW)
        draw(Kaboul,0,0)
        draw(Level1Surf, 120, 100)
        pygame.display.flip()
        time.sleep(5)
        menu_Kaboul = 1

    while menu_Kaboul  :
               
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                
                if bouton_commencer_rect.collidepoint(event.pos) :
                    Kaboul_musique.stop()
                    
                    with open("Niveau.txt","r") as RankTexte :
                        rank = RankTexte.read()

                    if rank == 'congratulations' :
                        lvl1 = 0
                        lvl2 = 0
                        congratulations = 1

                    if rank == 'level 2' :
                        lvl1 = 0
                        lvl2 = 1
                     
                    if rank == 'level 1' :
                        lvl1 = 1
                        lvl2 = 0

                    if rank == 'niveau 0' :
                        lvl1 = 1
                        lvl2 = 0
                      
                    menu_Kaboul=0
                       
                if quitter.collidepoint(event.pos) :
                    Kaboul_musique.stop()
                    menu_Kaboul = 0
                    menu = 1
                    son_joué = 1
                    choose_soldier = 0
                    Won = 0
               
        draw(Kaboul,0,0)
        draw(Level1Surf, 120, 100)
        draw(bouton_commencer, 370,200)
        draw(bouton_quitter, 362, 300)
        pygame.display.flip()
       

    if lvl1 == 1 :

        terroriste = Terroriste()
        sol1 = Sol()
        sol2 = Sol()
        echelle1 = Echelle()
        echelle2 = Echelle()
        echelle3 = Echelle()
        echelle4 = Echelle()
        balle_tero = Balle()
        Mitchell = Soldat()
        passerelle1 = Plateforme()
        passerelle2 = Plateforme()
        passerelle3 = Plateforme()
        passerelle4 = Plateforme()
        passerelle5 = Plateforme()
        passerelle6 = Plateforme()
        passerelle7 = Plateforme()
        passerelle8 = Plateforme()
        passerelle9 = Plateforme()
        passerelle10 = Plateforme()
        passerelle11 = Plateforme()
        passerelle12 = Plateforme()
        passerelle13 = Plateforme()
        passerelle14 = Plateforme()
        passerelle15 = Plateforme()
       
        terroristes_restants = 15
        tir = 0
        nb_balles = 30
        balle_tero.image = balle_gauche_image
        balle_tero.increment = -15
        Mitchell.image = capitaine_Mitchell_image
        Mitchell.x = 80
        Mitchell.y = 300
        sol2.x = 716
        sol2.y = 360
        joueur.x = 0
        joueur.y = 300
        echelle2.x = 100
        echelle2.y = 195
        echelle3.x = 143
        echelle3.y = 300
        echelle4.x = 143
        echelle4.y = 195
        balle_tero.x = terroriste.x + 50
        balle_tero.y = terroriste.y + 50 
        terroriste.y = 105
        passerelle2.x = 71
        passerelle3.x = 142
        passerelle4.x = 213
        passerelle5.x = 284
        passerelle6.x = 355
        passerelle7.x = 426
        passerelle8.x = 497
        passerelle9.x = 568
        passerelle10.x = 639
        passerelle11.x = 710
        passerelle12.x = 781
        passerelle13.x = 852
        passerelle14.x = 923
        passerelle14.image = passerelle_spéciale
        black_x = -1000
        black_y = 0
       
        obj1 = fond3.render('TUEZ TOUS LES TERRORISTES !', True, RED)
        draw(obj1,300,0)
        pygame.display.flip()
        balle.increment = 15

        if son_joué == 1 :
            singe.play(999,0,0)
            Kaboul_musique.stop()
       
    while lvl1:
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN :
                if event.key == K_RIGHT and joueur.x < 915 and not joueur_echelle == 1:
                    joueur.deplacement_droite()
                           
                if event.key == K_LEFT and joueur.x > 0 and not joueur_echelle == 1:
                    joueur.deplacement_gauche()

                if event.key == K_UP :
                    if (echelle1_rect.collidepoint(joueur.x, joueur.y) or echelle2_rect.collidepoint(joueur.x, joueur.y))or (echelle3_rect.collidepoint(joueur.x, joueur.y) or echelle4_rect.collidepoint(joueur.x, joueur.y)):
                        joueur.deplacement_haut()
                        joueur_echelle = 1

                    elif joueur.y <= 180 and joueur.y > 117:
                        joueur.deplacement_haut()
                        joueur_echelle = 0

                if event.key == K_DOWN and joueur.y < 300 :
                    if zone_vide_rect.collidepoint(joueur.x, joueur.y) :
                        joueur.deplacement_bas()
                        joueur_echelle = 1
                   
                    elif (echelle1_rect.collidepoint(joueur.x, joueur.y) or echelle2_rect.collidepoint(joueur.x, joueur.y)) :
                        joueur.deplacement_bas()
                        joueur_echelle = 1
                   
                if event.key == K_RETURN and tir == 0 and nb_balles > 0 :
                    if son_joué == 1 :
                        pygame.mixer.music.play(1, 0.9, 0)
                        
                    nb_balles-=1
                    tir=1

            elif event.type == JOYAXISMOTION:
                if event.axis == 0 and event.value > 0.5 and joueur.x < 915 and not joueur_echelle == 1:
                    joueur.deplacement_droite()
 
                elif event.axis == 0 and event.value < -0.5 and joueur.x > 0 and not joueur_echelle == 1:
                    joueur.deplacement_gauche()
 
                elif event.axis == 1 and event.value > 0.5 and joueur.y < 300 :
                    if zone_vide_rect.collidepoint(joueur.x, joueur.y) :
                        joueur.deplacement_bas()
                        joueur_echelle = 1
                   
                    elif (echelle1_rect.collidepoint(joueur.x, joueur.y) or echelle2_rect.collidepoint(joueur.x, joueur.y)) :
                        joueur.deplacement_bas()
                        joueur_echelle = 1

                elif event.axis == 1 and event.value < -0.5:
                    if (echelle1_rect.collidepoint(joueur.x, joueur.y) or echelle2_rect.collidepoint(joueur.x, joueur.y))or (echelle3_rect.collidepoint(joueur.x, joueur.y) or echelle4_rect.collidepoint(joueur.x, joueur.y)):
                        joueur.deplacement_haut()
                        joueur_echelle = 1

                    elif joueur.y <= 180 and joueur.y > 117:
                        joueur.deplacement_haut()
                        joueur_echelle = 0
                        
            elif event.type == JOYBUTTONDOWN :
                if event.button == 2 and tir == 0 and nb_balles > 0:
                    if son_joué == 1 :
                        pygame.mixer.music.play(1, 0.9, 0)
                nb_balles-=1
                tir=1
               
        tero_rect = terroriste_image.get_rect(topleft = (terroriste.x, terroriste.y))
        echelle1_rect = échelle_image.get_rect(topleft = (echelle1.x, echelle1.y))
        echelle2_rect = échelle_image.get_rect(topleft = (echelle2.x, echelle2.y))
        echelle3_rect = échelle_image.get_rect(topleft = (echelle3.x, echelle3.y))
        echelle4_rect = échelle_image.get_rect(topleft = (echelle4.x, echelle4.y))
        zone_vide_rect = zone_vide.get_rect(topleft = (100,90))
        joueur_rect = joueur.image.get_rect(topleft = (joueur.x, joueur.y))

        if detection_soldat == 1 and die_terrorist == 0:
            tir_tero = 1
            detection_soldat = 0

        if terroriste.y == joueur.y and terroristes_restants > 0 :
            detection_soldat = 1

        if joueur.y == 300 :
            joueur_echelle = 0

        if terroriste.x > 915 :
            terroriste.deplacement_gauche()
       
        if tir == 1 :
            balle.deplacement()

        if tir_tero == 1 :
            balle_tero.deplacement()

        if balle.x > 1000 :
            balle.x = joueur.x
            balle.y = joueur.y
            tir = 0

        if balle_tero.x < 0 :
            balle_tero.x = terroriste.x
            balle_tero.y = terroriste.y
            tir_tero = 0

        if tir == 0 :
            balle.x = joueur.x +50
            balle.y = joueur.y +50

        if tir_tero == 0 :
            balle_tero.x = terroriste.x + 50
            balle_tero.y = terroriste.y + 50

        if tero_rect.collidepoint(balle.x, balle.y) and tir == 1 :
            die_terrorist = 1
           
            if terroristes_restants > 0 :
                terroristes_restants -= 1
            tir = 0

        if joueur_rect.collidepoint(balle_tero.x, balle_tero.y) and tir_tero == 1 and len(vie_chasseur) > -1  :
            vie_chasseur = []
            tir_tero = 0
           
        if die_terrorist == 1 :
            if random.randint(0,1) :
                loop += 1
           
                if loop == 20 :
                    terroriste.x = 1500
                    terroriste.y = 105
                    die_terrorist= 0
                    loop = 0

            if random.randint(0,1) :
                loop += 1
           
                if loop == 20 :
                    terroriste.x = 1500
                    terroriste.y = 300
                    die_terrorist= 0
                    loop = 0

        scoreSurfChasseur = fond.render('Vie : %s' % (len(vie_chasseur)), True, RED)
        terroristes_restantsSurf = fond.render('Terroristes restants: %s' % terroristes_restants, True, RED)
        nb_balles_surf = fond.render('balles : %s' % nb_balles,True,YELLOW)
        draw(foret,0,0)
        draw(obj1,300,0)
        draw(scoreSurfChasseur ,0 ,3)
        draw(coeur1 ,60 ,0)
        draw(icone_balle ,100 ,25)
        draw(nb_balles_surf,0 ,30)
        draw(terroristes_restantsSurf,790,0)

        if detection_soldat == 1 :
            draw(detection_ennemi, terroriste.x-30, terroriste.y)
               
        if tir == 1 :
            balle.affichage()

        if tir_tero == 1 :
            balle_tero.affichage()

        if vie_chasseur == [] :
            singe.stop()
            YouLose = fond2.render('YOU LOSE !', True, RED)
            draw(YouLose, 350, 100)
            pygame.display.flip()
            time.sleep(2)
            lvl1 = 0
            menu = 1
            Won = 0
            
        if terroristes_restants > 0 :
            terroriste.affichage()

        elif terroristes_restants == 0 :
            draw(arrow_image, 835,40)
            
            if joueur.y == 105 and joueur.x == 915 :
                animation_victoire = 1
                 
        joueur.affichage()
        echelle1.affichage()
        echelle2.affichage()
        echelle3.affichage()
        echelle4.affichage()
        sol1.affichage()
        sol2.affichage()
        passerelle1.affichage()
        passerelle2.affichage()
        passerelle3.affichage()
        passerelle4.affichage()
        passerelle5.affichage()
        passerelle6.affichage()
        passerelle7.affichage()
        passerelle8.affichage()
        passerelle9.affichage()
        passerelle10.affichage()
        passerelle11.affichage()
        passerelle12.affichage()
        passerelle13.affichage()
        passerelle14.affichage()
        
        if animation_victoire == 1 :
            draw(black_animation,black_x,black_y)
            black_x += 10

            if black_x > -50 :
                black_x = -1000
                black_y = 0
                time.sleep(1.5)
                animation_victoire = 0
                lvl1 = 0
                lvl2 = 1
                Won = 0
            
        pygame.display.flip()

    if lvl2 == 1 :

        singe.stop()
        Kaboul_musique.stop()
        
        with open("Niveau.txt","w") as level :
            level.write("level 2")
            
        terroriste = Terroriste()
        balle.increment = 15
        balle.x = joueur.x+350
        balle.y = joueur.y+350
        balle_tero = Balle()
        balle_tero.x = terroriste.x + 350
        balle_tero.y = terroriste.y + 350
        balle_tero.image = balle_gauche_image
        balle_tero.increment = -15
        joueur.x = 0
        joueur.y = 300
        nb_balles = 20
        tir = 0
        terroristes_restants = 10
        black_x = -1000
        black_y = 0
        vie_chasseur = [1]
        die_terrorist = 1
        animation_victoire = 1 

    while lvl2 :
        for event in pygame.event.get() :
             
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    pygame.quit()
                    sys.exit()

                if event.key == K_RIGHT and joueur.x < 915 :
                    joueur.deplacement_droite()
                           
                if event.key == K_LEFT and joueur.x > 0 :
                    joueur.deplacement_gauche()

                if event.key == K_RETURN and tir == 0 and nb_balles > 0 :
                    if son_joué == 1 :
                        pygame.mixer.music.play(1, 0.9, 0)
                        
                    nb_balles-=1
                    tir=1

            if event.type == JOYAXISMOTION :

                if event.axis == 0 and event.value > 0.5 and joueur.x < 915 and not joueur_echelle == 1:
                    joueur.deplacement_droite()
 
                elif event.axis == 0 and event.value < -0.5 and joueur.x > 0 and not joueur_echelle == 1:
                    joueur.deplacement_gauche()

            elif event.type == JOYBUTTONDOWN :
                if event.button == 2 and tir == 0 and nb_balles > 0:
                    if son_joué == 1 :
                        pygame.mixer.music.play(1, 0.9, 0)
                nb_balles-=1
                tir=1

        tero_rect = terroriste_image.get_rect(topleft = (terroriste.x, terroriste.y))
        joueur_rect = joueur.image.get_rect(topleft = (joueur.x, joueur.y))

        if detection_soldat == 1 and die_terrorist == 0:
            tir_tero = 1
            detection_soldat = 0

        if terroriste.y == joueur.y and terroristes_restants > 0 :
            detection_soldat = 1
            
        if terroriste.x > 915 :
            terroriste.deplacement_gauche()
       
        if tir == 1 :
            balle.deplacement()

        if tir_tero == 1 :
            balle_tero.deplacement()

        if balle.x > 1000 :
            balle.x = joueur.x
            balle.y = joueur.y
            tir = 0

        if balle_tero.x < 0 :
            balle_tero.x = terroriste.x
            balle_tero.y = terroriste.y
            tir_tero = 0

        if tir == 0 :
            balle.x = joueur.x +50
            balle.y = joueur.y +50

        if tir_tero == 0 :
            balle_tero.x = terroriste.x + 50
            balle_tero.y = terroriste.y + 50

        if tero_rect.collidepoint(balle.x, balle.y) and tir == 1 :
            die_terrorist = 1
           
            if terroristes_restants > 0 :
                terroristes_restants -= 1
            tir = 0

        if joueur_rect.collidepoint(balle_tero.x, balle_tero.y) and tir_tero == 1 and len(vie_chasseur) > -1  :
            vie_chasseur = []
            tir_tero = 0

        if die_terrorist == 1 :
            
            terroriste.x = random.randint(100, 800)
            terroriste.y = -105
            die_terrorist = 0

        if terroriste.y >= -105 and terroriste.y != 300 :
            terroriste.deplacement_bas()
            terroriste.image = terroriste_parachute
            
            if terroriste.y >= 280 :
                terroriste.image = terroriste_image
                
        if vie_chasseur == [] :
            YouLose = fond2.render('YOU LOSE !', True, RED)
            draw(YouLose, 350, 100)
            pygame.display.flip()
            time.sleep(2)
            lvl2 = 0
            menu = 1
            Won = 0

        #affichage :

        draw(Kaboul_level,0,0)
        joueur.affichage()
        
        if terroristes_restants > 0 :
            terroriste.affichage()

        if tir == 1 :
            balle.affichage()

        if tir_tero == 1 :
            balle_tero.affichage()

        if terroristes_restants > 0 :
            terroriste.affichage()
            
        scoreSurfChasseur = fond.render('Vie : %s' % (len(vie_chasseur)), True, RED)
        terroristes_restantsSurf = fond.render('Terroristes restants: %s' % terroristes_restants, True, RED)
        nb_balles_surf = fond.render('balles : %s' % nb_balles,True,YELLOW)
        draw(scoreSurfChasseur ,0 ,3)
        draw(coeur1 ,60 ,0)
        draw(icone_balle ,100 ,25)
        draw(nb_balles_surf,0 ,30)
        draw(terroristes_restantsSurf,790,0)
        obj1 = fond3.render('ATTENTION AUX PARACHUTISTES !', True, RED)
        draw(obj1,300,0)

        if terroristes_restants == 0 and animation_victoire == 1 :
            draw(black_animation,black_x,black_y)
            black_x += 10

            if black_x > -50 :
                animation_victoire = 0
                time.sleep(1.5)
                lvl1 = 0
                lvl2 = 1
                congratulations = 1
                Won = 0
        
        pygame.display.flip()

    if congratulations == 1 :
        with open("Niveau.txt","w") as level :
            level.write("congratulations")
           
        ColonelSurf = fond.render('COLONEL GEORGES', True, BLACK)
        draw(bg,0,0)
        draw(colonel,0,100)
        draw(dialogue_colonel_3,80,10)
        draw(ColonelSurf,0,220)
        pygame.display.flip()
        time.sleep(10)
        congratulations = 0
        lvl2 = 0
        menu = 1
        rank = 'soldat 1ère classe'     
