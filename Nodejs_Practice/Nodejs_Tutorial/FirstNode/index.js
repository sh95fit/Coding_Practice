const express = require('express');
const app = express(),
      testJson = require(__dirname + '/../test/test.json');

app.set('views', __dirname + "/./views");
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

app.get('/', (req, res) => {
  res.render('index', {name: 'KIM'});
});

app.get('/test/:email', (req, res) => {
  testJson.email = req.params.email;
  testJson.test_num = req.query.test_num;
  res.json(testJson);
})

app.use(express.static('public'));

// app.get('/', (req, res) => {
//   // res.send("Nodejs TEST!");
//   res.send(testJson);
// });

const server = app.listen(7000, function(){
  console.log("Express's started on port 7000")
});