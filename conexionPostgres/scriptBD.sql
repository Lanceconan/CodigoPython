-- Database: "crudPython"

-- DROP DATABASE "crudPython";

CREATE DATABASE "crudPython"
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'Spanish_Chile.1252'
       LC_CTYPE = 'Spanish_Chile.1252'
       CONNECTION LIMIT = -1;

-- Table: public.persona

-- DROP TABLE public.persona;

CREATE TABLE public.persona
(
  per_id bigint NOT NULL,
  per_nombre character varying(100),
  per_apellidomaterno character varying(100),
  per_apellidopaterno character varying(100),
  per_rut character varying(20),
  per_observacion character varying(1000),
  CONSTRAINT persona_pkey PRIMARY KEY (per_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.persona
  OWNER TO postgres;

INSERT INTO public.persona(
per_id, 
per_nombre, 
per_apellidomaterno, 
per_apellidopaterno,
per_rut, 
per_observacion
)
VALUES
(1, 'DANIEL', 'PUELLES', 'TOLOZA', '17339126-9', 'MUY INGENUO'),
(2, 'TOMAS', 'TOLOZA', 'GUTIERREZ', '18864782-9', 'MUY SEGURO'),
(3, 'NICOLAS', 'GUTIERREZ', 'MIRANDA', '17951115-0', 'MUY MAMA');