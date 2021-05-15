const express = require("express");
// const fetch = require("node-fetch");
const app = express();
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

app.listen(3000);
app.set("view engine", "ejs");
var data,
  i = 0;
// app.use(bodyParser.json()); // for parsing application/json
// app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.json());

// function abcd(districtID, date) {
//   url =
//     "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" +
//     districtID +
//     "&date=" +
//     date;
//   console.log(url);
//   var request = new XMLHttpRequest();
//   request.open("GET", url, true);
//   var centres;
//   request.onload = function () {
//     if (request.status >= 200 && request.status < 400) {
//       // Success!
//       data[0] = JSON.parse(request.responseText); //bug over here
//       // centres = data[i]["sessions"];
//       i++;
//       // console.log(centres);
//     } else {
//       // We reached our target server, but it returned an error
//     }
//   };
//   request.onerror = function () {
//     // There was a connection error of some sort
//   };
//   request.send();
//   return data;
// }

function abcd(districtID, date) {
  //aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  return new Promise((resolve, reject) => {
    url =
      "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" +
      districtID +
      "&date=" +
      date;
    console.log(url);
    const request = new XMLHttpRequest();
    request.open("GET", url, true);
    var centres;
    request.onload = function () {
      if (request.status >= 200 && request.status < 400) {
        // Success!
        data = JSON.parse(request.responseText); //bug over here
        resolve(data);
        // centres = data[i]["sessions"];
        i++;
        // console.log(centres);
      } else {
        // We reached our target server, but it returned an error
      }
    };
    request.onerror = function () {
      // There was a connection error of some sort
    };
    request.send();
    // return data;
  });
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
// centres = abcd("149", "24-05-2021"); //works with this
// centres = abcd(districtID, "24-05-2021");    ///doesn't work with it

// console.log(centres);
app.get("/show/:id", (req, res) => {
  const id = req.params.id;
  districtID = String(id);
  // console.log(id);
  // centres = abcd("149", "24-05-2021");
  // centres = abcd(districtID, "24-05-2021");//works
  abcd(districtID, "24-05-2021")
    .then((data) => {
      // console.log("aaa");
      res.render("index", { centres: data["centers"] });
    })
    .catch((err) => console.log(err));
  // console.log(centres[0]["centers"]);
  // res.render("index", { centres: centres[0]["centers"] });
});

app.get("/form", (req, res) => res.render("getDistrict"));

app.post("/form", (req, res) => {
  // const { districtID, districtName, date } = req.body;
  const { districtID, date } = req.body;
  console.log(districtID, date);
  res.json({ redirect: "/show/" + districtID });
  // res.redirect("/");
});
