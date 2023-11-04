CREATE SCHEMA `academia_jam2023`;
--normalizo en español
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `usuario_name` varchar(50) NOT NULL,
  `usuario_apellido` varchar(50) NOT NULL,
  `usuario_telefono` varchar(14) DEFAULT NULL,
  `usuario_dni` varchar(9) NOT NULL,
  `usuario_email` varchar(100) NOT NULL,
  `usuario_password` varchar(150) NOT NULL,
  -- lo manejamos como string o con integer (0 admin 1 profe 2 alumno?)
  `usuario_rol` varchar(7) NOT NULL, 
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `id_UNIQUE` (`id_usuario`),
  UNIQUE KEY `dni_UNIQUE` (`usuario_dni`),
  UNIQUE KEY `email_UNIQUE` (`usuario_email`)
);


/*
    Referencia para colegas:
        nombretabla (en plural)
        id_tabla (en singular)
        rela_tabla (en singular - relación a la tabla foranea)
        tabla_campo (para que sea mas facil ubicar a que tabla hace referencia el campo,
        ej: nombre de las tablas usuarios y cursos es el mismo nombre de campo)
*/

-- creo tabla cursos
CREATE TABLE IF NOT EXISTS `academia_jam2023`.`Cursos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rela_user` INT NULL DEFAULT profe que dá la materia,
  `name` VARCHAR(45) NOT NULL,
  `duration` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_curso`)
  ) ;

-- creo tabla asistencias
CREATE TABLE IF NOT EXISTS `academia_jam2023`.`Asistencias` (
  `id_asistencia` INT NOT NULL AUTO_INCREMENT,
  `rela_cursante` INT NOT NULL,
  `asistencia_fecha` DATE NOT NULL,
  `asistencia_presente` INT NULL DEFAULT 0 ausente / 1 presente,
  PRIMARY KEY (`id_asistencia`)
  ) ;


-- creo tabla cursantes
CREATE TABLE IF NOT EXISTS `academia_jam2023`.`Cursantes` (
  `id_cursante` INT NOT NULL AUTO_INCREMENT,
  `rela_usuario` INT NOT NULL,
  `rela_curso` INT NOT NULL,
  `cursante_rol` INT NOT NULL DEFAULT 0 admin / 1 profe / 2 alumno,
  PRIMARY KEY (`id_cursante`)
  ) ;