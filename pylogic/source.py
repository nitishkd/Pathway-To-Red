#!/usr/bin/env python
import time 
from flask import Flask, render_template, jsonify
from flask import request
import QueryCF as CF
import saveProblemsOffline as SPO
import ladder

app = Flask(__name__)
tt = 1
@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route('/users')
def analyze():
    handle = request.args.get('handle', '')
    print("Testing") 
    query = CF.QueryCodeForces()
    query.allProblemStat()
    query.prepareProblemQueue()
    query.userStat(handle)
    result = query.problemRecommender()
    print("Testing")
    return render_template('analysis.html', handle=handle, result=result)

@app.route('/editorcpp')
def textEditorCpp():
    return app.send_static_file('editor_cpp.html')

@app.route('/editorjava')
def textEditorJava():
    return app.send_static_file('editor_java.html')

@app.route('/editorpython')
def textEditorPython():
    return app.send_static_file('editor_python.html')

@app.route('/ladder')
def openLadder():
    handle = request.args.get('handle', '')
    obj = ladder.Ladder()
    vis = obj.showAllProblems(handle)
    return render_template('listLadderProblems.html', handle=handle, vis=vis,A=obj.A, B=obj.B,N=obj.N,probName=obj.problemNames)    

@app.route('/ladderReg')
def registerUserForLadder():
    handle = request.args.get('handleLadder', '')
    obj = ladder.Ladder()
    vis = obj.signupUserForLadder(handle)
    print vis
    if(vis == 1):
        return jsonify(success='True', msg='User Registered')
    else:
        return jsonify(success='False', msg='User already Registered!')

@app.route('/updateLadder/<handle>')
def updateUserLadder(handle):
    obj = ladder.Ladder()
    obj.updateProblemCount(handle)
    vis = obj.showAllProblems(handle)
    return render_template('listLadderProblems.html', handle=handle, vis=vis,A=obj.A, B=obj.B,N=obj.N,probName=obj.problemNames)    

@app.route('/offline/<contestId>/<index>')
def SaveProblemOff(contestId, index):
    obj = SPO.SaveProblemOffline()
    obj.SaveProblem(contestId, index)
    return jsonify(success='True', msg='Page Saved')

@app.route('/problems/offline/<contestId>/<index>')
def offlineProblem(contestId, index):
    problemCode = str(contestId) + str(index) + '.html'
    print problemCode
    return app.send_static_file('problems/' + problemCode)

@app.route('/listSavedProblem')
def listOfflineProblems():
    obj = SPO.SaveProblemOffline()
    obj.listSavedProblem()
    return render_template('listOfflineProblems.html', problems=obj.offlineProblems)

@app.route('/updateProblemSet')
def problemSetUpdater():
    obj = CF.QueryCodeForces()
    obj.problemsetUpdater()
    return jsonify(success='True', msg='Problem Set Updated!')
    
if __name__ == '__main__':
    print("oh Hello")
    app.run(host = '127.0.0.1', port=1234)

