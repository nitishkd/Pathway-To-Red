import QueryCF as QCF

class Ladder:
    def __init__(self):
        self.A = [489,266,401,479,455,478,268,431,441,486]
        self.B = ["C","C","C","C","A","C","C","C","C","C"]
        self.N = len(self.A)
        self.problemNames = ["Given Length and Sum of Digits ...", "Number of Ways",
        "Team","Exam","Boredom","Table Decoration","Beautiful Set of Points","k-tree",
        "Valera and Tubes","Palindrome Transformation"]
        print ("Ladder Initiated!")

    def showAllProblems(self,handle):
        fp = open('pylogic/regUsers.txt')
        userList = fp.read().split("\n")
        fp.close()
        solvedCount = 0
        if(handle not in userList):
            print("User doesnt exists")
        else:
            fp = open("pylogic/static/Ladder/users/"+handle+".txt")    
            solvedCount = int(fp.read())
            fp.close()
        Visible = []
        for i in range(self.N):
            if(i < solvedCount):
                Visible.append("1")
            else:
                Visible.append("0")
        return Visible
        

    def signupUserForLadder(self, handle):
        
        fp = open('pylogic/regUsers.txt','r')
        userList = fp.read().split("\n")
        fp.close()
        if(handle in userList):
            print ("UserName already exist!")
            return 0
        else:
            fp = open("pylogic/static/Ladder/users/"+handle+".txt",'w+')
            fp.write(str(1))
            fp.close()
            fp = open('pylogic/regUsers.txt','a')
            fp.write(str(handle)+"\n")
            fp.close()
            print("User Registered!") 
            return 1           

    def updateProblemCount(self,handle):
        fp = open("pylogic/static/Ladder/users/"+handle+".txt")    
        solvedCount = int(fp.read())
        fp.close()
        lastProblemSolved = False
        print("Querying On Codeforces")
        obj = QCF.QueryCodeForces()
        obj.userStat(handle)
        print("Querying On Codeforces Successful") 
        PC = str(self.A[solvedCount-1]) + self.B[solvedCount-1]
        print('PC : ' + PC)

        if(obj.solvedProblemsByUser.has_key(PC)):
            print("Problem Found")
            lastProblemSolved = True
                
        if(lastProblemSolved):
            solvedCount = solvedCount + 1
            fp = open("pylogic/static/Ladder/users/"+handle+".txt",'w')
            fp.write(str(solvedCount))
            fp.close()
