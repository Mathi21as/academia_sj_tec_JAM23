CREATE SCHEMA IF NOT EXISTS `academia_jam2023`;

CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone` varchar(14) DEFAULT NULL,
  `dni` varchar(9) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(150) NOT NULL,
  `role` varchar(7) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `dni_UNIQUE` (`dni`),
  UNIQUE KEY `email_UNIQUE` (`email`)
);

CREATE TABLE IF NOT EXISTS `course` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_teacher` INT NULL DEFAULT, -- profesor que da la materia
  `name` VARCHAR(45) NOT NULL,
  `duration` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `inscription` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_user INT NOT NULL,
  id_course INT NOT NULL,
  role VARCHAR(7)
);

CREATE TABLE IF NOT EXISTS `attendance` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_inscription INT NOT NULL,
  `date` DATE NOT NULL,
  present BOOLEAN NOT NULL,
  FOREIGN KEY (id) REFERENCES inscription(id) ON DELETE CASCADE
);