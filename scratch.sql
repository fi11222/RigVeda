COPY "TB_RV"("N_MANDALA","N_SOOTKA","N_VERSE","TX_VERSE") 
FROM '/home/fi11222/disk-partage/Dev/Rig_Veda/RV.csv' DELIMITER ';' CSV HEADER;

ALTER TABLE "TB_RV" ADD PRIMARY KEY ("ID_SLOKA");

select * from "TB_RV" where "TX_VERSE" like '%सत्यसत्वन्%'

select "W"."S_WORD", "P".*
from "TB_WORDS" "W" join "TB_PADAPATHA" "P" on "P"."ID_SLOKA" = "W"."ID_SLOKA"
where "W"."S_WORD" like 'sat%' and not "W"."S_WORD" like '%satya%'
order by "P"."N_MANDALA", "P"."N_SOOTKA", "P"."N_SLOKA"

select "W"."S_WORD", "P".*
from "TB_WORDS" "W" join "TB_PADAPATHA" "P" on "P"."ID_SLOKA" = "W"."ID_SLOKA"
where "W"."S_WORD" like 'ṛt%' or "W"."S_WORD" like 'anṛt%'
order by "P"."N_MANDALA", "P"."N_SOOTKA", "P"."N_SLOKA"

select *
from "TB_PADAPATHA"
-- where "N_MANDALA"=1 and "N_SOOTKA"=63 and "N_SLOKA"=3
where "TX_PADAPATHA" like '% indra%' --and "TX_PADAPATHA" like '% satya%'
order by "N_MANDALA", "N_SOOTKA", "N_SLOKA"

select "W"."S_WORD", "P".*
from "TB_WORDS" "W" join "TB_PADAPATHA" "P" on "P"."ID_SLOKA" = "W"."ID_SLOKA"
where "W"."S_WORD" like 'saty%' or "W"."S_WORD" like '%-saty%'
order by "P"."N_MANDALA", "P"."N_SOOTKA", "P"."N_SLOKA"

-- Index: public."index_ID_SLOKA"

-- DROP INDEX public."index_ID_SLOKA";

CREATE INDEX "index_ID_SLOKA"
  ON public."TB_WORDS"
  USING btree
  ("ID_SLOKA");

select "N_MANDALA", count(1) from "TB_PADAPATHA" group by "N_MANDALA" order by "N_MANDALA"

select "W"."S_WORD", "P".*
from "TB_WORDS" "W" join "TB_PADAPATHA" "P" on "W"."ID_SLOKA" = "P"."ID_SLOKA"
where "W"."S_WORD" like 'saty%'
order by "P"."N_MANDALA", "P"."N_SOOTKA", "P"."N_SLOKA"

select "W"."S_WORD", "P".*
from "TB_WORDS" "W" join "TB_PADAPATHA" "P" on "W"."ID_SLOKA" = "P"."ID_SLOKA"
where "W"."S_WORD" = 'sat' or "W"."S_WORD" like 'sat-%' or "W"."S_WORD" like 'satv%'
order by "P"."N_MANDALA", "P"."N_SOOTKA", "P"."N_SLOKA"

select * from "TB_PADAPATHA" where "N_MANDALA" = 8 and "N_SOOTKA" = 100

DROP TABLE if exists public."TB_PADAPATHA";

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

CREATE UNIQUE INDEX "Numbers_Idx" ON "TB_PADAPATHA"("N_MANDALA", "N_SOOTKA", "N_SLOKA");

DROP TABLE if exists public."TB_WORDS";

CREATE TABLE public."TB_WORDS"
(
  "ID_WORD" integer NOT NULL,
  "ID_SLOKA" integer  NOT NULL,
  "S_WORD" character varying(30),
  "S_WORD_DEVA" character varying(30),
  CONSTRAINT "TB_WORDS_pkey" PRIMARY KEY ("ID_WORD")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."TB_WORDS"
  OWNER TO postgres;
