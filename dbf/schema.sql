CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

CREATE TABLE libros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  autor VARCHAR(255),
  anio SMALLINT,
  ol_key VARCHAR(32) UNIQUE,
  estado ENUM('por_leer','leyendo','leido') NOT NULL DEFAULT 'por_leer',
  puntaje TINYINT CHECK (puntaje BETWEEN 1 AND 5),
  notas TEXT
);

CREATE TABLE listas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL UNIQUE,
  descripcion VARCHAR(255)
);

CREATE TABLE lista_libros (
  lista_id INT NOT NULL,
  libro_id INT NOT NULL,
  PRIMARY KEY (lista_id, libro_id),
  FOREIGN KEY (lista_id) REFERENCES listas(id) ON DELETE CASCADE,
  FOREIGN KEY (libro_id) REFERENCES libros(id) ON DELETE CASCADE
);
