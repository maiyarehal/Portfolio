DROP TABLE IF EXISTS `contact`;
CREATE TABLE `contact` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `cellPhone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `contact` WRITE;
INSERT INTO `contact` VALUES (5,'Leigh','Wake Tech','098-765-4321','leigh@midmich.edu'),(6,'Todd','Wake Tech','123-456-7890','todd@anywhere.com'),(7,'Joe','Wake Tech','555-555-5555','joe@home.com');
UNLOCK TABLES;
