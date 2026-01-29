###########################################
## EXAMPLE: simple Coordinate class
## Taken from MIT Courseware: MIT6_0001F16
###########################################

class Coordinate:
    """ A coordinate made up of an x and y value """
    def __init__(self, x , y ): #how can I build an instance of the coordinate system (x,y)
        """ Sets the x and y values """
        self._x = x
        self._y = y   
    def get_x(self):    #getters/accessors : access private data attributes
        return self._x
    
    def get_y(self):    #getter/accessor: accesses the y paramater
        return self._y
    
    def set_x(self,new_x = 0 ):  #setters/mutators : the function sets the private data member to a certain value
        self._x = new_x
        
    def set_y(self,new_y ):  #setter/mutator function
        self._y = new_y
        
    def __str__(self):  #Would allow you to print the instance/object of your class
        """ Returns a string representation of self """
        return "(" + str(self._x) + "," + str(self._y) + ")"  #design this based on your taste
    
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self._x + other._x)**2
        y_diff_sq = (self._y + other._y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
    def add_coordinates(self,other):
        new_x = self._x + other._x
        new_y = self._y + other._y
        return (new_x, new_y)      #(1,2) +(3,4) = (4, 6)


if __name__ == '__main__':   #you create a test function that only works within this script

    c = Coordinate(3,4)   #this is how you create an instance, using the class name with some parameters
    origin = Coordinate(0,0)
    d = Coordinate (-3,-4)

    print(c)
    print(origin)
    print(d)
   
    distance= c.distance(origin)
    print(distance)

    #should be the same
    addition = d.add_coordinates(c)
    addition2 = c.add_coordinates(d)
    print(addition, addition2, addition == addition2)

    # NEVER USE THE DOT OPERATOR WITH THE PRIVATE DATA MEMBERS
    #c._x or c._y
    #Use Getter functions instead
    print(c.get_x())
    print(c.get_y())

    #Change the values using Setter function
    c.set_x(300)
   
   
  
