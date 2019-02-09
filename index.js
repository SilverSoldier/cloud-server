const express = require('express')
const app = express()
const port = 3000

app.get("*", (req, res) => {
  res.send(req.url.slice(1).split("").reverse().join(""))
});

app.listen(port, function(){
  console.log("Started")
})

