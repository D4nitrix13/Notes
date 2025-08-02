-- Author: Daniel Benjamin Perez Morales
-- GitHub: https://github.com/D4nitrix13
-- Email: danielperezdev@proton.me

DROP DATABASE IF EXISTS ContactsApp;

CREATE DATABASE IF NOT EXISTS ContactsApp;

USE ContactsApp;

-- El Motor De Almacenamiento Innodb Es Necesario Para Que Las Claves Foráneas Funcionen.

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
    name VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL UNIQUE, 
    password VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS contacts (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
    user_id INT NOT NULL, 
    name VARCHAR(255) NOT NULL, 
    phone_number VARCHAR(255) NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- El ON DELETE CASCADE Es Opcional, Pero Es Una Buena Práctica, Ya Que Asegura Que Cuando Se Elimine Un Usuario De La Tabla Users, Los Registros Correspondientes En La Tabla Contacts También Se Eliminarán Automáticamente.

-- INSERT INTO contacts (name, phone_number) VALUES ("Daniel Perez", "123456789"), ("Danna Morales", "876543210"), ("Benjamin Perez", "122443377");