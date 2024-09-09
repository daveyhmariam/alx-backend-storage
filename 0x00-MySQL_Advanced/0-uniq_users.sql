--- create table

CREATE TABLE IF NOT EXISTS users(
                                id INT PRIMARY_KEY NOT NULL AUTO_INCREMENT,
                                email NOT NULL UNIQUE VARCHAR(255),
                                name VARCHAR(225)
                                );
