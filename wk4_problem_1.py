#The code below has 2 bugs. Please tell me what they are. Try and do this without running the code.
class Pet:
    def init(self, name): #the "init" needs two underscores
        self.name = name 
    def introduce(): #the parentheses are missing the "self" keyword thing
        #you need to say self so that you can access it
        print ("hello, I am ", self.name)   
