const express = require("express");
const app = express();
const mysql = require("mysql");
const bodyParser = require("body-parser");
const cors = require("cors");

var db = mysql.createConnection({
    host: '35.224.26.16',
    user: 'root',
    password: '16JOkJm5xjsp304L',
    database:'PeopleEatSmart',
})

// app.post("/api/insert", (require, response) => {
// //     const ID = require.body.ID;
// //     const RatingValue = require.body.RatingValue;
// //     const COMMENT = require.body.Comments;
// //     const UserName = require.body.UserName;
// //     const RecipeID = require.body.RecipeID;

// //     const sqlInsert = "Insert Into 'RatingComment' ('ID', 'RatingValue', 'COMMENT', 'UserName', 'RecipeID') VALUES (?,?,?,?,?)";
// //     db.query(sqlInsert, [ID, RatingValue, COMMENT, UserName, RecipeID], (err, result) => {
// //         console.log(error);
// //     })
// // });

app.use(cors());
app.use(bodyParser.urlencoded({extended: true }));
app.use(express.json());

// app.get('/', (require, response) => {
    
// })

app.listen(3002, () => {
    console.log("running on port 3002");
})