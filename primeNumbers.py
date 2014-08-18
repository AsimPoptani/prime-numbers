__author__ = 'Asim Poptani'
__version__ = 1
import multiprocessing
import sys

def isPrime(number):
    # isPrime is to check if a int is Prime
    if not isinstance(number,int):
        #check if number is a int
        raise Exception("Please enter a int. Function: isPrime.")
    #create array of numbers to check
    rangeOfNumbers=range(1,number+1,1)
    #count of how many multiplacations if it is a prime number it would be 2
    multiplicationCount=0
    #tow for loops to loop through all possibilities
    for n1 in rangeOfNumbers:
        for n2 in rangeOfNumbers:
            if (n1*n2==number):
                multiplicationCount +=1
    if (multiplicationCount==2):
        f=open("prime.txt","a")
        f.write(str(number)+",\n")
        return True
    else:
        return False




if __name__ == "__main__":
    if not sys.version_info[0] == 3:
        raise Exception("Please Upgrade or Downgrade your python to python 3.")
    number=0
    while True:
        processList=[]
        for i in range(4):
            number+=1
            process=multiprocessing.Process(target=isPrime,args=[number])
            process.start()
            processList.append(process)
        for process in processList:
            process.join()
