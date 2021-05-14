const express = require("express");
// const fetch = require("node-fetch");
const app = express();
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

app.listen(3000);
app.set("view engine", "ejs");
var data = [],
  i = 0;
// app.use(bodyParser.json()); // for parsing application/json
// app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.json());

function abcd(districtID, date) {
  url =
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" +
    districtID +
    "&date=" +
    date;
  console.log(url);
  var request = new XMLHttpRequest();
  request.open("GET", url, true);
  request.onload = function () {
    if (request.status >= 200 && request.status < 400) {
      // Success!
      data[i] = JSON.parse(request.responseText);
      // centres = data[i]["sessions"];
      i++;
      // console.log(centres);
    } else {
      // We reached our target server, but it returned an error
    }
  };

  request.onerror = function () {
    // There was a connection error of some sort
    console.log("Connection Error...");
  };
  request.send();
  return data;
}

var districtID;

today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1; //As January is 0.
var yyyy = today.getFullYear();
if (dd < 10) dd = "0" + dd;
if (mm < 10) mm = "0" + mm;
date = dd + "-" + mm + "-" + yyyy;
// centres = abcd("149", date);
centres = abcd(districtID, date);
console.log(centres);

app.get("/:id", (req, res) => {
  // console.log(date);
  const id = req.params.id;
  districtID = id;
  res.render("index", { centres: centres[0]["centers"] });
});

app.get("/form", (req, res) => res.render("getDistrict"));

app.post("/form", (req, res) => {
  // const { districtID, districtName, date } = req.body;
  const { districtID, date } = req.body;
  console.log(districtID, date);
  res.json({ redirect: "/" + districtID });
  // res.redirect("/");
});
