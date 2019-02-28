import random
import numpy as np



class DecisionFactory:
	
	def __init__ (self, name='Davros'):
		self.name = name
		self.directions = [ 'wait','up' , 'down', 'right', 'left' ]
		self.last_result = 'success'
		self.last_direction = 'wait'
		self.result=3
		self.a=1
		self.b=1
		self.x=0
		self.y=0
		self.pos = [self.x,self.y]
		self.start=self.start=np.zeros((1,1),dtype=int)
		self.start[self.a-1,self.b-1] = 5
		self.upcounter=1
		self.downcounter=1
		self.leftcounter=1
		self.rightcounter=1
	def get_decision(self, verbose = True):
		
		return self.random_direction()
	
	def random_direction(self):
		x=self.x
		y=self.y
		while (self.last_direction!='success'):
			self.start[self.x-1,self.y-1] = 5
			
		  # Includes wait state
			
			if(self.last_result=='wall'):
					self.start[self.a-1,self.b-1]=1
					
					if(self.result==2):
						if(self.downcounter==0):
							self.result=random.randint(3,4)
						while(self.upcounter>0):
							self.result=1
							self.upcounter-=1
						self.result=random.randint(3,4)
					elif(self.result==1):
						if(self.upcounter==0):
							self.result=random.randint(3,4)
						while(self.downcounter>0):
							self.result=2
							self.downcounter-=1
						self.downcounter=1
						self.result=random.randint(3,4)
					elif(self.result==3):
						if(self.rightcounter==0):
							self.result=random.randint(1,2)
						while(self.leftcounter>0):
							self.result=4
							self.leftcounter-=1
						self.leftcounter=1
						self.result=random.randint(1,2)
					elif(self.result==4):
						if(self.leftcounter==0):
							self.result=random.randint(1,2)
						while(self.rightcounter>0):
							self.result=3
							self.rightcounter-=1
						self.rightcounter=1
						self.result=random.randint(1,2)
						
					
					#add=np.zeros((self.a,self.start[self.a-1,self.b-1]=11))
			if(self.directions[self.result] =='down'):
					
				if(self.last_result=='wall'):
					
					if(self.last_direction!='down'):
						if(self.last_direction=='left'):
							self.start[self.a-1,self.b-1]=1
						self.a+=1
						if(x<0):
							self.x=0
						self.x+=1													
						add=np.zeros((1,self.b),dtype=int)
						self.start=np.append(self.start,add,axis=0)
						
						
				elif(self.last_result!='wall' or self.start[self.a-1,self.b-1]!=5):
					self.a+=1
					if(x<0):
						self.x=0
					self.x+=1
					add=np.zeros((1,self.b),dtype=int)
					self.start=np.append(self.start,add,axis=0)
					
				
				

			if(self.directions[self.result] =='up'):
				
				if(self.last_result=='wall'):
					self.start[self.a-1,self.b-1]=1
					
					if(self.last_direction!='up'and self.start[self.a-1,self.b-1]!=5):
						self.a+=1
						if(x<0):
							self.x=0
						self.x-=1
						add=np.zeros((1,self.b),dtype=int)
						self.start=np.append(add,self.start,axis=0)
						
				elif(self.last_result!='wall' or self.start[self.a-1,self.b-1]!=5):
					self.a+=1
					if(x<0):
						self.x=0
					self.x-=1
					add=np.zeros((1,self.b),dtype=int)
					self.start=np.append(add,self.start,axis=0)
				
				
					
					



					
			if(self.directions[self.result] =='right' ):
				
				if(self.last_result=='wall'):
					self.start[self.a-1,self.b-1]=1
					
					if(self.last_direction!='right' and self.start[self.a-1,self.b-1]!=5):
						self.b+=1
						if(y<0):
							self.y=0
						self.y+=1
						add=np.zeros((self.a,1),dtype=int)
						self.start=np.append(self.start,add,axis=1)
						

				elif(self.last_result!='wall' or self.start[self.a-1,self.b-1]!=5):
					self.b+=1
					if(y<0):
						self.y=0
					self.y+=1
					add=np.zeros((self.a,1),dtype=int)
					self.start=np.append(self.start,add,axis=1)	
				
				
					
					

			if(self.directions[self.result] =='left' ):
				
				if(self.last_result=='wall'):
					self.start[self.a-1,self.b-1]=1
					
					if(self.last_direction!='left' and self.start[self.a-1,self.b-1]!=5):
						self.b+=1
						if(y<0):
							self.y=0
						self.y-=1
						add=np.zeros((self.a,1),dtype=int)
						self.start=np.append(add,self.start,axis=1)	
						
				elif(self.last_result!='wall' or self.start[self.a-1,self.b-1]!=5):
					self.b+=1
					if(y<0):
						self.y=0
					self.y-=1
					add=np.zeros((self.a,1),dtype=int)	
					self.start=np.append(add,self.start,axis=1)	
				
				
						
			
				#r = random.randint(0,4)
					
				# print(self.a)
				# print(self.b)
				
			return self.directions[self.result]
			
		# if(self.directions[r] =='left'):
		#     if(self.last_result=='wall'):
		#         self.b+=1
		#         new=np.zeros((self.a,self.b),dtype=int)
		#         self.start=np.hstack((new,self.start))
		#         add=np.adds((self.a,1))
		#         self.start=np.hstack((add,new))
		#         print(self.start)
		
		
		# if(self.directions[r] =='right'):
		#     if(self.last_result=='wall'):
		#         self.b+=1
		#         new=np.zeros((self.a,self.b),dtype=int)
		#         self.start=np.hstack((new,self.start))
		#         add=np.adds((self.a,1))
		#         self.start=np.hstack((self.start,add))
		#         print(self.start)
		
			 #print(start)
		#if(self.last_result == 'wall'):
			#if(self.directions[r] == self.last_direction):
				#self.random_direction()    
			
		
		# Update last direction to be the add just

	  
		
	
	def put_result(self, result):
		self.last_result = result