DROP TABLE IF EXISTS public."TB_PADAPATHA";

CREATE TABLE public."TB_PADAPATHA"
(
  "ID_SLOKA" integer NOT NULL,
  "N_MANDALA" integer,
  "N_SOOTKA" integer,
  "N_SLOKA" integer,
  "TX_PADAPATHA" text,
  "TX_PADAPATHA_DEVA" text,
  CONSTRAINT "TB_PADAPATHA_pkey" PRIMARY KEY ("ID_SLOKA")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."TB_PADAPATHA"
  OWNER TO postgres;

-- Index: public."index_ID"

-- DROP INDEX public."index_ID";

CREATE UNIQUE INDEX "index_ID"
  ON public."TB_PADAPATHA"
  USING btree
  ("N_MANDALA", "N_SOOTKA", "N_SLOKA");

DROP TABLE IF EXISTS public."TB_RV";

CREATE TABLE public."TB_RV"
(
  "N_MANDALA" integer,
  "N_SOOTKA" integer,
  "N_SLOKA" integer,
  "TX_SLOKA" text,
  "ID_SLOKA" integer NOT NULL,
  CONSTRAINT "TB_RV_pkey" PRIMARY KEY ("ID_SLOKA")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."TB_RV"
  OWNER TO postgres;

DROP TABLE IF EXISTS public."TB_WORDS";

CREATE TABLE public."TB_WORDS"
(
  "ID_WORD" integer NOT NULL,
  "ID_SLOKA" integer NOT NULL,
  "S_WORD" character varying(30),
  "S_WORD_DEVA" character varying(30),
  CONSTRAINT "TB_WORDS_pkey" PRIMARY KEY ("ID_WORD")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."TB_WORDS"
  OWNER TO postgres;
