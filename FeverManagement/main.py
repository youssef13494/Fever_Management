#Run this cell
import sys
import driver_simple

sys.path.append("E:\\Python\\pythonProject1")

#driver_simple.bc_test()

print("1 : Do you have respiratory symptoms?")
print()
print("2 : Do you suffer from abdominal pain ?")
print()
print("3 : Do you suffer from urine pain?")
print()
print("4 : other?")
Input = int(input("Choose what you are experiencing : "))
if(Input==1):
    driver_simple.bc_test_questions1()

elif(Input==2):
    driver_simple.bc_test_questions2()

elif(Input==3):
    driver_simple.bc_test_questions3()

elif(Input==4):
    driver_simple.bc_test_questions4()


