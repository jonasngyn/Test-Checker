import os
import shutil 
import filecmp
from config import *

print("ANH NGUYEN TEST CHECKER\n")

os.system("c++ "+FILE_NAME+" -o test.out")

#Copy test to input.txt 
def cmp_lines(path_1, path_2):
    l1 = l2 = True
    with open(path_1, 'r') as f1, open(path_2, 'r') as f2:
        while (l1 and l2):
            l1 = f1.readline()
            l2 = f2.readline()
            if l1==(l2+'\n') or l2==l1+'\n':
                return True
            elif l1 != l2:
                return False
    return True

cnt=0.0;

if MODE==0:
    for i in range(FIRST,LAST+1):
        shutil.copyfile("./test/"+TEST_INPUT_TYPE+str(i).zfill(SUFFIX_SIZE), INPUT_SOURCE)
        os.system("./test.out")
        shutil.copyfile("./test/"+TEST_OUTPUT_TYPE+str(i).zfill(SUFFIX_SIZE), "answer.txt")
        print("Test "+str(i)+": ",end='')
        
        res=cmp_lines(OUTPUT_SOURCE, 'answer.txt')
        if (res==True):
            cnt=cnt+1.0;
        
        print(str(res))
        print("Done")
        print()
    print("DONE!!")
    print("Correct: " + str(round(cnt/(LAST+1.0-FIRST)*100 , 2))+"%" )
        
else:
    for i in range(FIRST,LAST+1):
        shutil.copyfile("./test/"+TEST_INPUT_TYPE+str(i).zfill(SUFFIX_SIZE), INPUT_SOURCE)
        os.system("./test.out")
        shutil.copyfile("./test/"+TEST_OUTPUT_TYPE+str(i).zfill(SUFFIX_SIZE), "answer.txt")
        #print("Test "+str(i)+": ",end='')
        
        res=cmp_lines(OUTPUT_SOURCE, 'answer.txt')
        
        if(res==False):
            print("Wrong Answer as test: "+str(i))
            print("Exited")
            exit()
            
    print("Done, all anwsers are correct :)")



