import urllib2
class SaveProblemOffline:
    
    def __init__(self):
        self.offlineProblems = []
        print 'Save to Problem Module'

    def SaveProblem(self, contestId, index):
        url = 'http://codeforces.com/problemset/problem/'+ str(contestId) + '/' + str(index)
        response = urllib2.urlopen(url)
        webContent = response.read()
        fname = str(contestId) + str(index) + '.html'
        path = 'pylogic/static/problems/'
        f = open(path + fname, 'w')
        f.write(webContent)
        f.close()
        fp = open(path+'problemList.txt', 'a+')
        fp.write(str(contestId)+" "+str(index)+'\n')
        fp.close()

    def listSavedProblem(self):
        fp = open("pylogic/static/problems/problemList.txt",'r')
        data = fp.read().split('\n')
        fp.close()
        for d in data:
            if(d != ''):
                u = d.split(' ')
                self.offlineProblems.append((u[0], u[1]))


