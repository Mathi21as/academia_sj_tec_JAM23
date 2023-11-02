CREATE SCHEMA `academia_jam2023`;

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone` varchar(14) DEFAULT NULL,
  `dni` varchar(9) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(150) NOT NULL,
  `role` varchar(7) NOT NULL,
  `gender` varchar(50),
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `dni_UNIQUE` (`dni`),
  UNIQUE KEY `email_UNIQUE` (`email`)
);