COPY "TB_RV"("ID_SLOKA","N_MANDALA","N_SOOTKA","N_SLOKA","TX_SLOKA")
FROM '/home/fi11222/disk-partage/Dev/Rig_Veda2/RV.csv' DELIMITER ';' CSV HEADER;

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

select "W"."S_WORD", "P".*
from "TB_WORDS" "W" join "TB_PADAPATHA" "P" on "P"."ID_SLOKA" = "W"."ID_SLOKA"
where "W"."S_WORD" like 'brahm%'
order by "W"."S_WORD", "P"."N_MANDALA", "P"."N_SOOTKA", "P"."N_SLOKA"

select *
from "TB_PADAPATHA"
-- where "N_MANDALA"=1 and "N_SOOTKA"=63 and "N_SLOKA"=3
where "TX_PADAPATHA" like '% indra%' --and "TX_PADAPATHA" like '% satya%'
order by "N_MANDALA", "N_SOOTKA", "N_SLOKA"

select "W"."S_WORD", "P".*
from "TB_WORDS" "W" join "TB_PADAPATHA" "P" on "P"."ID_SLOKA" = "W"."ID_SLOKA"
where "W"."S_WORD" like 'saty%' or "W"."S_WORD" like '%-saty%'
order by "P"."N_MANDALA", "P"."N_SOOTKA", "P"."N_SLOKA"

select "A".*, "B".*
from "TB_PADAPATHA" "A" join "TB_PADAPATHA" "B" on "A"."TX_PADAPATHA" = "B"."TX_PADAPATHA"
where not "A"."ID_SLOKA" = "B"."ID_SLOKA"
order by "A"."N_MANDALA", "A"."ID_SLOKA"

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









