--- create table

CREATE TABLE IF NOT EXISTS users(
                                id INT  NOT NULL PRIMARY_KEY AUTO_INCREMENT,
                                email NOT NULL UNIQUE VARCHAR(255),
                                name VARCHAR(225),
                                country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US');
