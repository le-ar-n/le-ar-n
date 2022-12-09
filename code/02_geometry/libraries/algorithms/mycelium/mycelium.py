'''
. . . . . . . . . . . . . . . . . . . . . 
.                                       .
.    <<      ><      ><       >< <<     .
.    < ><   ><<     ><<<    ><    ><<   .
.    << >< > ><    ><  ><     ><        .  
.    <<  ><  ><   ><<<<<><      ><      .
.    <<      >< ><<     ><< ><    ><<   .
.    <<      ><><<       ><<  >< <<     .
.                                       .
.             DFAB 2016/17              .
. . . . . . . . . . . . . . . . . . . . . 

Created on 27.09.2016

@author: rustr

http://www.creativeapplications.net/processing/mycelium-processing/

'''

import math
import random as rnd
import json


#===============================================================================
class Mycelium:
    
    def __init__(self, image_file, number_of_worms, speed = 10, branch_thresh = 1000, max_worms = 100, tresh_worm = 30, favour="light"):
        
        self.load_image(image_file)
        
        self.max_worms = max_worms # maximum number of worms
     
        # controls when a worm will branch
        self.branch_thresh = branch_thresh
        self.tresh_worm = tresh_worm
        self.speed = speed
        
        self.init_worms(number_of_worms)
        
        self.dead_worms = []
        self.just_branched = 0
        self.favour = favour
        
        self.looking_angle = math.pi/12
        
    def load_image(self, image_file):
        from PIL import Image
        image = Image.open(image_file).convert("L")
        width, height = image.size
        self.width = width
        self.height = height
        self.image = image
    
    def get_color(self, x, y):
        tx = int(math.floor(x))
        ty = int(math.floor(y))
        pix = self.image.load()
        grey = pix[tx % self.width, ty % self.height]
        ts = 4 * grey
        return {'grey': grey, 'score': ts}
     
    def init_worms(self, number_of_worms):
        
        self.worms = []
        
        """
        for i in range(number_of_worms):
            tx = math.floor(rnd.random() * self.width)
            ty = math.floor(rnd.random() * self.height)
            angle = rnd.random() * 2 * math.pi
            worm = Worm(tx, ty, angle, self)
            worms.append(worm)
        """
        
        for i in range(number_of_worms * 10):
            
            tx = math.floor(rnd.random() * self.width)
            ty = math.floor(rnd.random() * self.height)
            angle = rnd.random() * 2 * math.pi
            
            grey = self.get_color(tx, ty)['grey']
            if grey < self.tresh_worm:
                self.add_worm(tx, ty, angle)
            if len(self.worms) == number_of_worms:
                break
    
    def add_worm(self, tx, ty, angle, index=None):
        if index:
            self.worms[index] = Worm(tx, ty, angle, self)
        else:
            self.worms.append(Worm(tx, ty, angle, self))
    
    def step(self):
        for i, w in enumerate(self.worms):
            if not w.dead:

                # save the worms points       
                w.points.append((w.x,w.y))
                 
                # move all the worms
                w.x += (math.cos(w.angle) * self.speed)
                w.y += (math.sin(w.angle) * self.speed)
     
                w.update_direction()
     
                
                if (w.x > self.width) or (w.x < 0) or (w.y > self.height) or (w.y < 0):
                    w.points.append(())
                
                # Wrap the worms around the canvas 
                if w.x > self.width: w.x = 0
                if w.x < 0: w.x = self.width
                if w.y > self.height: w.y = 0
                if w.y < 0: w.y = self.height
                
            else:
                # regenerate an available worm at a random slot
                grey = 255
                while grey > self.tresh_worm:            
                    tx = math.floor(rnd.random() * self.width)
                    ty = math.floor(rnd.random() * self.height)
         
                    # assign a random vector to begin with
                    angle = rnd.random() * 2 * math.pi
                     
                    grey = self.get_color(tx, ty)['grey']
                    
                    self.dead_worms.append(self.worms[i])
                    
                    self.add_worm(tx, ty, angle, i)

    @property    
    def data(self):
        paths = []
        for worm in self.worms:
            paths += worm.data
        return paths


    def to_json(self, filepath):
        """
        """
        with open(filepath, 'w') as f:
            json.dump(self.data, f, indent=4, sort_keys=True)
                    
         
     
         
#===============================================================================

class Worm:
     
    def __init__(self, x, y, angle, parent):
        self.x = x
        self.y = y
        self.angle = angle
        self.food = 100
        self.dead = False
        self.grey = 0
        self.points = []
        self.parent = parent

    @property
    def data(self):
        worm_paths = [[]]
        idx = 0
        for p in self.points:
            if len(p):
                worm_paths[idx].append({'x': p[0], 'y': p[1], 'z': 0})
            else:
                worm_paths.append([])
                idx +=1
        return worm_paths
        
    def update_direction(self):
                
        # we know the current location, we know the vector
        # calculate a few variations between -30 degrees and +30 degree and get their colors
        # whichever is brightest, that's where we go to. 
         
        angle = 0
        best_angle = 0
        best_score_so_far = {'grey': 0, 'angle': 0, 'score': 99999999 }
     
        # look for the best place to go
        for i in range(12):
     
            angle = self.angle - ((rnd.random() * self.parent.looking_angle)) + ((rnd.random() * self.parent.looking_angle))
            # calculate a new direction                
            tx = self.x + (math.cos(angle) * self.parent.speed)
            ty = self.y + (math.sin(angle) * self.parent.speed) # 5 makes it look further out
     
            # test the source image
            score = self.parent.get_color(tx, ty)
     
            # swap > for < 
            if (score['score'] < best_score_so_far['score']):
                best_angle = angle
                score['angle'] = angle
                best_score_so_far = score        
     
        self.parent.just_branched -= 1
     
        # If the score is SOO good, we should branch (unless maximum worms have been reached
        if (best_score_so_far['score'] > self.parent.branch_thresh):
     
            if (self.parent.just_branched <= 0):
                # assign a new vector, close to the original
                start_angle = self.angle + ((rnd.random() * self.parent.looking_angle))
                self.angle -= 0.37
     
                if (len(self.parent.worms) < self.parent.max_worms):
                    # new worm

                    self.parent.add_worm(self.x, self.y, start_angle)
                    # we don't want everything branching at once
                    self.parent.just_branched = 500
                else:
                    # maybe we can find a dead-worm and re-use him
                    for i, w in enumerate(self.parent.worms):
                        if w.dead == True:
                            self.parent.add_worm(self.x, self.y, start_angle, i)
                            break
     
        self.angle = best_angle
        self.food -= 1
     
        if self.parent.favour == "light": # favor the light
            if best_score_so_far['score'] > 755:
                self.food = 200
        else: # favor the dark
            if best_score_so_far['score'] < 355:
                self.food = 200
     
        if self.food == 0:
            self.dead = True
 

#===============================================================================


if __name__ == "__main__": 
    
    #image_file = "food/queen.jpg"
    image_file = "food/clint.jpg"
    
    number_of_worms = 10 # how many worms to start with
    num_steps = 500
    #"""
    MAX_WORMS = 100 # Maximum worms
     
    # controls when a worm will branch
    BRANCH_THRESH = 230 * 4
    TRESH_WORM = 30
    SPEED = 2
    #"""

    
    my = Mycelium(image_file, number_of_worms, speed=SPEED, branch_thresh=BRANCH_THRESH, max_worms=MAX_WORMS, tresh_worm=TRESH_WORM, favour="light")
         
    for i in range(num_steps):
        my.step()
    filepath = r"C:\Users\rustr\Desktop\_postdoc\Nationaler Zukunftstag\mycelium.json"
    my.to_json(filepath)