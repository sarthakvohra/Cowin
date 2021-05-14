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
  var centres;
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
centres = abcd("149", "16-05-2021");
console.log(centres);
app.get("/", (req, res) =>
  res.render("index", { centres: centres[0]["centers"] })
);

app.get("/form", (req, res) => res.render("getDistrict"));

app.post("/form", (req, res) => {
  // const { districtID, districtName, date } = req.body;
  const { districtID, date } = req.body;
  console.log(districtID, date);
});
