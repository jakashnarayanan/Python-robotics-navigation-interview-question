import math
import numpy as np

class poker:
    goal_coordinates = [(0,0), (0,100), (100,0), (100,100), (200,0), (200,100)]
    balls = []
    def get_input(self): # returns the x,y coordinates of striker and red balls , where white ball position is [0]
        # Let user enter the striker x,y coordinates
        striker_x , striker_y =  map(int, input("enter the striker position in following type x y").split())
        self.striker = (striker_x,striker_y)
        self.balls.append(self.striker)
        # let user enter number of inputs
        while input("do you want add red ball position  y/n") == "y":
            val1 , val2 = map(int,input("enter the rd ball orgin in following type x y").split())
            red_balls = (val1,val2)
            self.balls.append(red_balls)
        return self.balls
            
    def distance_from(self,striker,red_balls): # Gives two nearest balls from the white ball
        dist=[]
        for x in red_balls:
            distance = p.distance(striker,x)    
            dist.append(distance)           
        return dist            
    
    def two_nearest_ball(self,d): # returns two nearest ball from the orgin of striker
        sd = float('inf')
        ssd = float('inf')
        for num in d:
            if num <= sd:
                sd,ssd = num,sd
            elif num <= ssd:
                ssd = num
        return sd,ssd,inputs[1+d.index(sd)],inputs[1+d.index(ssd)]

    def nearest(self,s):
        near = float('inf')
        for num in s:
            if num < near:
                near = num
        num = p.goal_coordinates[s.index(near)]
        # print("the nearest goal pose is",p.goal_coordinates[s.index(near)])
        return num

    def distance(self,b1,b2): # returns the distance between two balls using pythogras theorem.
        distance = math.sqrt( ((int(b1[0])-int(b2[0]))**2)+((int(b1[1])-int(b2[1]))**2) )
        return distance

    def probability1(self,d1,d2,d3,d4):
        pr1 = d2+d1
        pr2 = d3+d4
        # print(pr1,pr2)
        if pr1 < pr2:
            prob1 = pr1
            return prob1,d1
        else:
            prob1 = pr2
            return prob1 , d3 
    
    def find_angle(self,striker,red_balls): # returns the angle of all possible red balls with goal but with negataive and postive
        degree_math = []
        p2 = striker
        for p1 in red_balls:
            goal_distances = p.distance_from(p1,p.goal_coordinates)
            p3 = p.nearest(goal_distances)
            a = (p1[0] - p2[0], p1[1] - p2[1])
            b = (p1[0] - p3[0], p1[1] - p3[1])
            degree = math.degrees(math.atan2(p3[1]-p2[1], p3[0]-p2[0]) - math.atan2(p1[1]-p2[1], p1[0]-p2[0]))
            # a = math.atan2(x1*y2-y1*x2,x1*x2+y1*y2)
            # degree = math.degrees(a)
            degree_math.append(degree)
        return degree_math

    def angle_np(self,striker,red_balls):#retruns the angle of red balls with nearest goal coordinates with postive values.
        degree_np = []
        degree_sorted =[]
        b = np.array([striker[0],striker[1]])
        for p1 in red_balls:
            a = np.array([p1[0],p1[1]])
            goal_distances = p.distance_from(p1,p.goal_coordinates)
            p3 = p.nearest(goal_distances) 
            c = np.array([p3[0],p3[1]])
            ba = a - b
            bc = c - b
            cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
            angle = np.arccos(cosine_angle)
            degree_np.append(np.degrees(angle))
            degree_sorted.append(np.degrees(angle))
        degree_sorted.sort()
        return degree_np.index(degree_sorted[0])

    
    def run_prob1(self,inputs): # Return the probobility 1 of sucessfully placing a ball
        striker = inputs[0]
        red_balls = inputs[1:]
        distances = p.distance_from(striker,red_balls)
        
        d1,d3,p1,p2 = p.two_nearest_ball(distances)
        b1 = p.distance_from(p1,p.goal_coordinates)
        b1n = p.nearest(b1)
        b2 = p.distance_from(p2,p.goal_coordinates)
        b2n = p.nearest(b2)
        d2 = p.distance(b1n,p1)
        d4 = p.distance(b2n,p2)
        prd, pr1 = p.probability1(d1,d2,d3,d4)
        return inputs[1+distances.index(pr1)]
        
p = poker()
inputs = [(40,50),(70,50),(60,80),(70,20),(160,20),(180,35),(120,70),(190,80),(40,80),(100,60)]
# inputs = p.get_input()
striker = inputs[0]
red_balls = inputs[1:]
print("The best shot by probability 1 is ", p.run_prob1(inputs)) 
print("The best match for probability 2 is ",red_balls[p.angle_np(striker,red_balls)])





