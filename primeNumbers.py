__author__ = 'Asim Poptani'
__version__ = 1
import multiprocessing
import sys
#set number of skips to 0
skipNumbers=0
def skip():
    #return true if we need to skip
    global skipNumbers
    if (skipNumbers==0):
        return False
    else:
        skipNumbers-=1
        return True

def isPrimeCheckAndWrite(number):
    #enable to change numberOfSkips
    global skipNumbers
    # isPrime is to check if a int is Prime
    if not isinstance(number,int):

        #check if number is a int
        raise Exception("Please enter a int. Function: isPrime.")

    #create array of numbers to check
    rangeOfNumbers=range(1,number+1,1)

    #count of how many multiplacations if it is a prime number it would be 2
    multiplicationCount=0
    #loop through all possibilities
    for n1 in rangeOfNumbers:
        for n2 in rangeOfNumbers:
            if skip():
                continue
            total=n1*n2
            if (total==number):
                #if there is a match count it
                multiplicationCount +=1
            if (total>number or multiplicationCount>2):
                skipNumbers=number-n2


    #if multiplication =2 this means it is a prime number
    if (multiplicationCount==2):
        #open to file and write it down
        f=open("prime.log","a")
        f.write(''.join([str(number),",\n"]))
        #return true for if checking
        return True
    else:
        #return false for if checking
        return False



#how i always start my python scripts
if __name__ == "__main__":
    #check if python version is 3 if not shout about it!
    if not sys.version_info[0] == 3:
        raise Exception("Please Upgrade or Downgrade your python to python 3.")
    #number we start with to check +1
    numberToCheck=int(input("What number would you like to Start with? \n"))-1
    #asks how many procces you would like
    amountProcess=int(input("How many Process would you like to give? \n"))
    #my main loop
    while True:
        #a proccess list to kill them off !
        processList=[]
        for i in range(amountProcess):
            numberToCheck+=1
            process=multiprocessing.Process(target=isPrimeCheckAndWrite,args=[numberToCheck])
            process.start()
            processList.append(process)
        for process in processList:
            process.join()
