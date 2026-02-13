// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

const express = require("express");
const app = express();

/**
 * Get all users
 * @name List Users
 * @path {GET} /api/users
 * @returns {object} A list of users
 */
app.get("/api/users", (req, res) => {
  res.json({ users: [] });
});

/**
 * Get all products
 * @name List Products
 * @path {GET} /api/products
 * @returns {object} A list of products
 */
app.get("/api/products", (req, res) => {
  res.json({ products: [] });
});

/**
 * Get authentication token
 * @name Get Auth Token
 * @path {GET} /api/auth
 * @returns {object} An authentication token
 */
app.get("/api/auth", (req, res) => {
  res.json({ token: "xyz123" });
});

app.listen(3000);
console.log("Server on port", 3000);
