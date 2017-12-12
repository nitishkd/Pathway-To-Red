const electron = require('electron');
const app = electron.app;
const path = require('path');
const url = require('url');
var BrowserWindow = electron.BrowserWindow;
var mainWindow = null;

app.on('ready', function() {
  var subpy = require('child_process').spawn('python', ['pylogic/source.py']);
  //var subpy = require('child_process').spawn('./dist/hello.exe');
  var rq = require('request-promise');
  var mainAddr = 'http://127.0.0.1:1234';

  var openWindow = function(){
    mainWindow = new BrowserWindow({width: 800, height: 600});
    //mainWindow.loadURL('file://' + __dirname + '/index.html');
    mainWindow.loadURL('http://127.0.0.1:1234');
    //mainWindow.webContents.openDevTools();
    mainWindow.on('closed', function() {
      mainWindow = null;
      subpy.kill('SIGINT');
    });
  };
  var startUp = function(){
    rq(mainAddr)
      .then(function(htmlString){
        openWindow();
        console.log('server started!');
        
      })
      .catch(function(err){
        //console.log('waiting for the server start...');
        startUp();
      });
  };

  // fire!
  startUp();
});