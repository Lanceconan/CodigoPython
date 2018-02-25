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