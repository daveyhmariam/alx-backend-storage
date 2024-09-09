## 0x00. MySQL Advanced
### Back-end
- SQL
- MySQL

### MySQL Cheatsheet
- MySQL Performance: How To Leverage MySQL Database Indexing
- Stored Procedure
- Triggers
- Views
- Functions and Operators
- Trigger Syntax and Examples
- CREATE TABLE Statement
- CREATE PROCEDURE and CREATE FUNCTION Statements
- CREATE INDEX Statement
- CREATE VIEW Statement

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### Tasks

1. **We are all unique!**

    **Requirements:**
    - Attributes:
        - `id`, integer, never null, auto increment and primary key
        - `email`, string (255 characters), never null and unique
        - `name`, string (255 characters)
    - If the table already exists, your script should not fail.
    - Your script can be executed on any database.
    
    **Context:** Make an attribute unique directly in the table schema to enforce your business rules and avoid bugs in your application.

2. **In and not out**

    **Requirements:**
    - Attributes:
        - `id`, integer, never null, auto increment and primary key
        - `email`, string (255 characters), never null and unique
        - `name`, string (255 characters)
        - `country`, enumeration of countries: US, CO and TN, never null (default will be US)
    - If the table already exists, your script should not fail.
    - Your script can be executed on any database.

3. **Best band ever!**

    **Requirements:**
    - Import this table dump: `metal_bands.sql.zip`
    - Column names must be: `origin` and `nb_fans`
    - Your script can be executed on any database.
    
    **Context:** Calculating or computing something is always power-intensive; it's better to distribute the load!

4. **Old school band**

    **Requirements:**
    - Import this table dump: `metal_bands.sql.zip`
    - Column names must be: `band_name` and `lifespan` (in years until 2022 - use 2022 instead of `YEAR(CURDATE())`)
    - You should use attributes `formed` and `split` for computing the lifespan.
    - Your script can be executed on any database.

5. **Buy buy buy**

    **Context:** Quantity in the table items can be negative. Updating multiple tables for one action from your application can generate issues (network disconnection, crash, etc.). Let MySQL handle it for you!

6. **Email validation to send**

    **Initial SQL:**
    ```sql
    DROP TABLE IF EXISTS users;

    CREATE TABLE IF NOT EXISTS users (
        id int not null AUTO_INCREMENT,
        email varchar(255) not null,
        name varchar(255),
        valid_email boolean not null default 0,
        PRIMARY KEY (id)
    );

    INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
    INSERT INTO users (email, name, valid_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
    INSERT INTO users (email, name, valid_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);
    ```

7. **Add bonus**

    **Requirements:**
    - Procedure `AddBonus` takes 3 inputs (in this order):
        - `user_id`, a `users.id` value (linked to an existing user)
        - `project_name`, a new or already existing project (create if not found)
        - `score`, the score value for the correction

    **Context:** Writing code in SQL is a nice level up!

8. **Average score**

    **Requirements:**
    - Procedure `ComputeAverageScoreForUser` takes 1 input:
        - `user_id`, a `users.id` value (linked to an existing user)

9. **Optimize simple search**

    **Requirements:**
    - Import this table dump: `names.sql.zip`
    - Only the first letter of `name` must be indexed.

    **Context:** Indexes are powerful when used correctly!

10. **Optimize search and score**

    **Requirements:**
    - Import this table dump: `names.sql.zip`
    - Only the first letter of `name` AND `score` must be indexed.

11. **Safe divide**

    **Requirements:**
    - Create a function `SafeDiv` with 2 arguments:
        - `a`, INT
        - `b`, INT
    - Returns `a / b` or 0 if `b == 0`.

    **Initial SQL:**
    ```sql
    DROP TABLE IF EXISTS numbers;

    CREATE TABLE IF NOT EXISTS numbers (
        a int default 0,
        b int default 0
    );

    INSERT INTO numbers (a, b) VALUES (10, 2);
    INSERT INTO numbers (a, b) VALUES (4, 5);
    INSERT INTO numbers (a, b) VALUES (2, 3);
    INSERT INTO numbers (a, b) VALUES (6, 3);
    INSERT INTO numbers (a, b) VALUES (7, 0);
    INSERT INTO numbers (a, b) VALUES (6, 8);
    ```

12. **No table for a meeting**

    **Requirements:**
    - The view `need_meeting` should return all student names when:
        - Their scores are under 80
        - No `last_meeting` date or more than a month ago.

    **Initial SQL:**
    ```sql
    DROP TABLE IF EXISTS students;

    CREATE TABLE IF NOT EXISTS students (
        name VARCHAR(255) NOT NULL,
        score INT default 0,
        last_meeting DATE NULL 
    );

    INSERT INTO students (name, score) VALUES ("Bob", 80);
    INSERT INTO students (name, score) VALUES ("Sylvia", 120);
    INSERT INTO students (name, score) VALUES ("Jean", 60);
    INSERT INTO students (name, score) VALUES ("Steeve", 50);
    INSERT INTO students (name, score) VALUES ("Camilia", 80);
    INSERT INTO students (name, score) VALUES ("Alexa", 130);
    ```

13. **Average weighted score**

    **Requirements:**
    - Procedure `ComputeAverageScoreForUser` takes 1 input:
        - `user_id`, a `users.id` value (linked to an existing user)

    **Tips:** Calculate Weighted Average.

14. **Average weighted score for all!**

    **Requirements:**
    - Procedure `ComputeAverageWeightedScoreForUsers` does not take any input.

    **Tips:** Calculate Weighted Average.
