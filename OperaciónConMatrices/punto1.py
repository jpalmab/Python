import numpy as np

a = np.matrix([-1, 1, 2]) 
b = np.matrix([-4, 2, 1,-1])
m = np.matrix([[3,-9,0,5], [2,-5,-3,1],[-1,5,8,4]])

print("--------------------");
print(" Multiplicaciones");
print("");
print(" ---------------- ");
print("      A x M       ");
print(" ---------------- ");
print(" " + str(a*m)); 
print("");  
print(" ---------------- ");
print("  A.transpose x b ");
print(" ---------------- ");
at = np.transpose(a); 
print(" " + str(at * b));
print(""); 
print(" ---------------- ");
print("  M * B.transpose ");
print(" ---------------- ");
bt = np.transpose(b);
print(" " + str(m * bt));
print(""); 
print(" ---------------- ");
print("  A * A.transpose ");
print(" ---------------- ");
print(" " + str(a*at));





 