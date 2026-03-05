CREATE DATABASE estoque;


USE estoque;

CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    provider VARCHAR(100)
);


SELECT * FROM products;



