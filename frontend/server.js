const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get("/add", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "add_employee.html"));
});

app.get("/view", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "view_employee.html"));
});

app.get("/calculate", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "calculate_salary.html"));
});

app.get("/signup", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "signup.html"));
});

app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "login.html"));
});

app.listen(PORT, () => {
  console.log(`Frontend running at http://localhost:${PORT}`);
});
