#!/usr/bin/env node
var fs = require('fs');
var uglify = require('uglifyjs');
var catw = require('catw');

var cmd = process.argv[2];
if (cmd === 'build') build({ watch: false })
else if (cmd === 'watch') build({ watch: true })
else usage(1)

function build (opts) {
  var jsfiles = ['js/underscore-min.js', 'js/jquery-2.1.0.min.js', 'js/backbone-min.js', 'js/main.js'];
  
  // var min = uglify.minify(jsfiles);
  // console.log(min.code);
  var js = catw(jsfiles, { watch: opts.watch });
  
  
  js.on('stream', function (stream) {
    stream.pipe(fs.createWriteStream('../static/main.js'));
    console.log('ccc');
  });  
  

  var css = catw('style/*.css', { watch: opts.watch });
  css.on('stream', function (stream) {
    stream.pipe(fs.createWriteStream('../static/bundle.css'));
  });
}

function usage (code) {
  console.error('usage: ./task.js { build | watch }');
  if (code) process.exit(code);
}
