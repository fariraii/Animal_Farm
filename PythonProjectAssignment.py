import random
from uuid import uuid4
#OS used when deliting a file 
import os
import schedule
import time


class Location():
    def __init__ (self) :
        x = random.randint(0,5)
        y = random.randint(0,5)
        self.Across = x
        self.Down = y
        self.locationArray = [[0 for i in range(2) ]for j in range(2)]
        
    def generateMoveX(self):
        self.minMove=-1
        self.maxMove=1
        self.movX=random.randint(self.minMove,self.maxMove)
        return self.movX
    
    def generateMoveY(self):
        self.minMove=-1
        self.maxMove=1
        self.movY=random.randint(self.minMove,self.maxMove)
        return self.movY 
    
    def LocationFile(self):
        prevLoc=open('Locations.txt','a')
        loc=Location()
        loc.locationArray[0][0]=loc.Across
        loc.locationArray[0][1]=loc.Down        
        prevLoc.write(str(loc.locationArray[0]))
        
        prevLoc.close()
        print("Location written to a file")
        
class AnimalInfo:
    def __init__(self):
        self.location=Location().locationArray[0]
        self.ID=""
        self.name=""
        self.newAnimal=""
        self.randomAnimal=""
        
    def getID(self):
        return self.ID
    def GetLocation(self):
        return self.location
    def SetID(self,name):
        self.name=name
        id_num=str(uuid4())
        self.ID=id_num
        self.newAnimal= self.ID +","+self.name+","
       # print(self.newAnimal)
        return self.newAnimal
          
    
    def checkLocation(self):
        try:
            self.locations=open('Locations.txt','r')
            line= self.locations.read()
            if line[0:6]==line[6:12] and line[0:6]==line[12:18]:
                print("Warning! Check on animal: "+ self.name)
            print(line[6:12])
            self.locations.close()
        except:
            print("Location File does not exist")


    
    def animalFile(self,name):
        self.animalFile= open("AnimalsOnFarm.txt","a")
        self.animalFile.write(str(AnimalInfo().SetID(name))+"\n")
        self.animalFile.close()
        print("An Animal "+name+"has been added to a file with coodinates"+ str(Location().locationArray[0]))
        
    def NumAnimals(self):
        try:
            self.fileName="AnimalsOnFarm.txt"
            count=0
            with open(self.fileName,"r") as files:
                for i in files:
                    count=count+1
            if count>0:
                print('There are  '+ str(count)+" animal(s) in the file.")
            files.close()
        except:
            print('There are no animals yet')
    
    def DeleteA(self,delete):
        try:
            self.fh_read=open("AnimalsOnFarm.txt","r")
            self.fh_write=open("temp.txt","w")
            s= " "
            while (s):
                s=self.fh_read.readline()
                line=s.split(",")
                #print(line[1])
                if len(s)>0:
                    if line[1]!=delete:
                        print(line[1])
                        self.fh_write.write(s)
            self.fh_read.close()
            self.fh_write.close()
            os.remove("AnimalsOnFarm.txt")
            os.rename("temp.txt","AnimalsOnFarm.txt")
            print("animal deleted")
        except:
            print('There are no animals yet.')
            
        #select a random Animal from the animal text file
    def SelectRandomAnimal(self):
        try:
            print("***********************************************************************")
            print("all animals in the file are")
            AnimalArray=[]
            self.fh_read=open("AnimalsOnFarm.txt","r")
            s= " "
            while (s):
                s=self.fh_read.readline()
                line=s.split(",")
                if len(s)>0:
                    AnimalArray.append(line[1])
            
            self.fh_read.close()
            print(AnimalArray)
            self.randomAnimal=random.choice(AnimalArray)
            print("One Animal chosen at Random is    :"+self.randomAnimal)
            return self.randomAnimal
        except:
            print('There are no animals yet.')
    def GetRandomAnimal(self):
        return self.randomAnimal
            
    def GiveRandomAnimalRandomMove(self):
        Ro=AnimalInfo()
               
        GRAR=Ro.SelectRandomAnimal()
        print("intial location for  "+str(GRAR)+"  was  :"+str(Location().locationArray[0]))
        
        across=Location.generateMoveX(self)
        down=Location.generateMoveY(self)
        p=  int(across+ Location().locationArray[0][0])
      
        q=  down + Location().locationArray[0][1]
        
        print("Current location for  "+str(GRAR)+" is  :"+str([p,q]))
    def DisplayAnimalWithIDs(self):
        try:
            print("****************************************************************")
            print("        ANIMAL UNIQUE IDs           ,Animal Human Name,")
            self.fh_read=open("AnimalsOnFarm.txt","r")
            s= " "
            while (s):
                s=self.fh_read.readline()
                print(s)
            self.fh_read.close()
        except:
            print('There are no animals yet.')   

def createPword():
    password=input("Enter new password: ")
    
    FileHandle = open("Password.txt", "w")
    FileHandle.write(password)
    FileHandle.close()
    print('Password changed successfuly')


def Main():
    print(
        """
        Hello! Welcome to the farm control room. Select an option from the menu below. 

        0-Exit
        1-Change password
        2-Add an animal to the record
        3-Remove an animal from the record
        4-Display the total number of animals 
        5-Display animal locations
        6-Select Random Animal
        
        """)
    choice=" "

    while choice!="0":
        choice=input("Enter choice: ")

        if choice=="0":
            print("Goodbye")
    
        elif choice=="1":
            createPword()
            
   
        elif choice=="2":
            name=input("Enter human name for animal: ")
            y=AnimalInfo()
            y.animalFile(name)

        elif choice=="3":
            y=AnimalInfo()
            delete=input("Enter animal to be removed: ")
            y.DeleteA(delete)

        elif choice=="4":
            y=AnimalInfo()
            y.NumAnimals()

        elif choice=="5":
            y=AnimalInfo()
            print("Displaying animal locations.")
            schedule.every(4).seconds.do(y.GiveRandomAnimalRandomMove)
            while 1:
                schedule.run_pending()
                time.sleep(1) 
        elif choice=="6":
            y=AnimalInfo()
            y.SelectRandomAnimal()        
                
        else:
            choice=input('Invalid choice. Try again: ')


password1="FaRm"
attempt=input('Enter password to start: ')
if  attempt!="FaRm":
    try:
        FileHandle = open("Password.txt", "r")
        password1 = FileHandle.read()
        FileHandle.close()
    except:
        wrong=True
        print("Please try again ,use the Default password")
else:
    p1=""


while attempt!=password1 :
    attempt=input('Incorrect password ,try again  ')
        #if wrong==True:
            #attempt=input("Please try again ,use the Default password")
        #else:
    

Main()

input("\nPress the enter key to exit")
