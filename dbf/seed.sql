-- Datos de ejemplo (opcional). Cargar después de schema.sql:
--   mysql -uroot -p biblioteca < dbf/seed.sql
-- Con docker compose se carga solo la primera vez que se crea la base.
USE biblioteca;

INSERT INTO libros (id, titulo, autor, anio, ol_key, estado, puntaje, notas) VALUES
  (1, 'Ladrilleros', 'Selva Almada', 2013, '/works/OL23133858W', 'leido', 5, NULL),
  (4, 'The Caves of Steel', 'Isaac Asimov', 1953, '/works/OL46401W', 'leido', 5, NULL);

INSERT INTO listas (id, nombre, descripcion) VALUES
  (3, 'Ciencia Ficción', NULL),
  (4, 'Literaltura argentina', NULL);

INSERT INTO lista_libros (lista_id, libro_id) VALUES
  (4, 1),
  (3, 4);
