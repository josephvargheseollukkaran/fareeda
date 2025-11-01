// server.js
import express from "express";
const app = express();
app.use(express.json());

let latestData = {};

app.post("/api/update", (req, res) => {
  latestData = req.body;
  res.send("✅ Data received");
});

app.get("/api/content", (req, res) => {
  res.json(latestData);
});

app.listen(3000);
