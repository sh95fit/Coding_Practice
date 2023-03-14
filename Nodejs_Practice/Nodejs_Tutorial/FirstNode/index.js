const express = require('express'),
      app = express();

const Pool = require("./pool"),
      Testdb = require("./db_conn");

const testJson = require(__dirname + '/../test/test.json');

const pool = new Pool();

app.use(express.static('public'));
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


app.get('/dbtest/:user', (req, res) => {
  let user = req.params.user;
  let dbconn = new Testdb(pool);
  dbconn.execute( conn => {
    conn.query("select * from User where uid=?", [user], (err, ret) => {
      res.json(ret);
    });
  });
});

// app.get('/', (req, res) => {
//   // res.send("Nodejs TEST!");
//   res.send(testJson);
// });

const server = app.listen(7000, function(){
  console.log("Express's started on port 7000")
});