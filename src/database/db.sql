CREATE SCHEMA IF NOT EXISTS `academia_jam2023`;
use `academia_jam2023`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone` varchar(14) DEFAULT NULL,
  `dni` varchar(9) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(150) NOT NULL,
  `role` varchar(7) NOT NULL,
  `gender` varchar(50),
  `block` TINYINT(1) DEFAULT 0 ,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `dni_UNIQUE` (`dni`),
  UNIQUE KEY `email_UNIQUE` (`email`)
);

CREATE TABLE IF NOT EXISTS `course` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `id_teacher` INT NOT NULL, 
  `name` VARCHAR(45) NOT NULL,
  `duration` VARCHAR(45) NOT NULL,
  `description` MEDIUMTEXT NOT NULL,
  FOREIGN KEY (`id_teacher`) REFERENCES user(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `inscription` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_user INT NOT NULL,
  id_course INT NOT NULL,
  role VARCHAR(7),
  FOREIGN KEY (`id_user`) REFERENCES user(id) ON DELETE CASCADE,
  FOREIGN KEY (`id_course`) REFERENCES course(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `attendance` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_inscription INT NOT NULL,
  `date` DATE NOT NULL,
  present TINYINT(1) DEFAULT 0 ,
  FOREIGN KEY (id) REFERENCES inscription(id)
);