const express = require('express')
const app = express()
const port = 3000

app.get("*", (req, res) => {
  ans = 1;
  n = parseInt(req.url.slice(1))
  for (var i = 2; i <= n; i++) {
	ans = ans * i;
  }
  res.send("Done")
});

app.listen(port, function(){
  console.log("Started")
})

