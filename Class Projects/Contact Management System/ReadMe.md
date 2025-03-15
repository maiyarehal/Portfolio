# Contact Management System

This JavaFX application allows users to perform CRUD (Create, Read, Update, Delete) operations on a list of contacts. The contacts are stored in a MySQL database.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Classes and Packages](#classes-and-packages)
- [Database Schema](#database-schema)
- [Styling](#styling)

## Features
- Add new contacts with name, phone number, email, and address.
- Update existing contacts.
- Delete contacts.
- View all contacts in a table format.

## Prerequisites
- Java Development Kit (JDK) 8 or later.
- MySQL database.
- JavaFX library.
- IDE (Eclipse used).

## Setup
1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    ```
2. **Open the project in your IDE**.

3. **Set up the MySQL database**:
    - Import the `contact.sql` file to create the `contact` table and insert sample data.

4. **Configure the database connection**:
    - Update the `DbConnection.java` file with your MySQL database URL, username, and password:
      ```java
      DriverManager.getConnection("jdbc:mysql://<your-database-url>", "<username>", "<password>");
      ```

5. **Run the application**:
    - Execute the `MainApp.java` file.

## Usage
- The main window displays a table with all contacts.
- Use the text fields to enter contact details.
- Click "Add New" to add a new contact.
- Select a contact from the table and update its details using the text fields, then click "Update".
- Select a contact from the table and click "Delete" to remove it.

## Classes and Packages
### contactCRUD
- **Contact.java**: Represents a contact entity with properties for ID, name, phone number, email, and address.
- **ContactDAO.java**: Data Access Object (DAO) class for interacting with the database to perform CRUD operations.
- **ContactView.java**: JavaFX UI class for displaying and interacting with the contact table and input fields.
- **DbConnection.java**: Manages the database connection.
- **Main.java**: Main application class that initializes the UI and sets up event handlers.

## Database Schema
The database schema for the `contact` table:
```sql
DROP TABLE IF EXISTS `contact`;
CREATE TABLE `contact` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `cellPhone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `contact` WRITE;
INSERT INTO `contact` VALUES 
(5,'Leigh','Wake Tech','098-765-4321','leigh@midmich.edu'),
(6,'Todd','Wake Tech','123-456-7890','todd@anywhere.com'),
(7,'Joe','Wake Tech','555-555-5555','joe@home.com');
UNLOCK TABLES;
````

## Styling
- The application is styled using CSS defined in the application.css file.
