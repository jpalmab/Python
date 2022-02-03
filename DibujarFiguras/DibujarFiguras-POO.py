class Shape():
    def __init__(self, color):
        self.color = color;
    
    def area(self):
        pass;
    
    def perimeter(self):
        pass;
    
    def draw(self):
        pass;   
        
class Line(Shape):
    
    def __init__(self,color,length):
        super().__init__(color);
        self.length = length;
        
    def area(self):
        print("   LENGTH: ", self.length);
        print("   AREA: ", 0);
        
    def perimeter(self):   
        print("   PERIMETER: ",self.length);
        
    def draw(self):
        temp = "   ";
        for i in range(self.length):
            temp = temp + self.color + " ";
        print(temp);  

class Square(Shape):
    
    def __init__(self,color,w,h):
        super().__init__(color);
        self.weight = w;
        self.height = h;
      
    def area(self): 
        if self.weight == self.height:      
            print("   WEIGHT: ", self.weight, "  ", "HEIGHT: ",self.height);   
            print("   AREA: ",self.weight * self.height);
        else:
            print("   WEIGHT: ", self.weight, "  ", "HEIGHT: ",self.height);    
            
    def perimeter(self):
        if self.weight == self.height:
            print("   PERIMETER: ",(self.weight * 2 + self.height * 2));                 
      
    def draw(self):
        if self.weight == self.height:
            print("   DRAW:  ");
            temp = "   ";
            for i in range(self.weight):
                temp = temp + self.color + " ";
            for i in range(self.height):
                print(temp);
        else:
            print("   THE SIDES OF THE SQUARE ARE NOT THE SAME ");        
            
class Triangle(Shape):
    
    def __init__(self, color, h):
        super().__init__(color);
        self.height = h;
        
    def area(self):
        print("   HEIGHT: ", self.height);
        print("   AREA: ", ((self.height * self.height) / 2));    
    
    def perimeter(self):
        print("   PERIMETER: ", (self.height * 3));
        
    def draw(self):
        temp = "   ";  
        for i in range(self.height):
                temp = temp + self.color + " ";
                print(temp);

print("------------------");          
print(" - HOMEWORK POO - ");

print("---------------");        
print(" - LINE - ");
print("---------------");

line1 = Line("*", 5);
line1.area();
line1.perimeter();
print("   DRAW:   ");
line1.draw();
print();

print("---------------");
print(" - SQUARE - ");
print("---------------");

square1 = Square("*", 6, 6);
square1.area();
square1.perimeter();
square1.draw();
print();

print("---------------");
print(" - TRIANGLE - ");
print("---------------");

triangle1 = Triangle("*", 10);
triangle1.area();
triangle1.perimeter();
print("   DRAW:  ");
triangle1.draw();




    
    
        
              