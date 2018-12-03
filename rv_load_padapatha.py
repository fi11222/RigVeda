#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys
import os
import re

__author__ = 'Nicolas Reimen'

g_dbServer = 'localhost'
g_dbDatabase = 'RigVeda'
g_dbUser = 'postgres'
g_dbPassword = 'murugan!'

g_root = '/home/fi11222/disk-partage/Dev/Rig_Veda/GRETIL/'

g_consonants = [
    ('क', 'k'),
    ('ख', 'kh'),
    ('ग', 'g'),
    ('घ', 'gh'),
    ('ङ', 'ṅ'),
    ('च', 'c'),
    ('छ', 'ch'),
    ('ज', 'j'),
    ('झ', 'jh'),
    ('ञ', 'ñ'),
    ('ट', 'ṭ'),
    ('ठ', 'ṭh'),
    ('ड', 'ḍ'),
    ('ढ', 'ḍh'),
    ('ण', 'ṇ'),
    ('त', 't'),
    ('थ', 'th'),
    ('द', 'd'),
    ('ध', 'dh'),
    ('न', 'n'),
    ('प', 'p'),
    ('फ', 'ph'),
    ('ब', 'b'),
    ('भ', 'bh'),
    ('म', 'm'),
    ('य', 'y'),
    ('र', 'r'),
    ('ल', 'l'),
    ('व', 'v'),
    ('ह', 'h'),
    ('श', 'ś'),
    ('ष', 'ṣ'),
    ('स', 's'),
    ('ळ', 'ḷ')
]

g_vowels = [
    ('ऐ', 'ै', 'ai'),
    ('औ', 'ौ', 'au'),
    ('अ', '', 'a'),
    ('आ', 'ा', 'ā'),
    ('इ', 'ि', 'i'),
    ('ई', 'ी', 'ī'),
    ('उ', 'ु', 'u'),
    ('ऊ', 'ू', 'ū'),
    ('ऋ', 'ृ', 'ṛ'),
    ('ॠ', 'ॄ', 'ṝ'),
    ('ऌ', 'ॢ', 'ḷ'),
    ('ॡ', 'ॣ', 'ḹ'),
    ('ए', 'े', 'e'),
    ('ओ', 'ो', 'o')
]

g_visarga_d = 'ः'
g_visarga_l = 'ḥ'

g_anusvara_l = 'ṃ'
g_anusvara_d = 'ं'

g_virama = '्'


# ---------------------------------------------------- Functions -------------------------------------------------------
def iast_to_deva(p_string):
    """
    Transforms a string in IAST Sanskrit script into its Devanagari equivalent

    :param p_string: string in IAST alphabet
    :return: Devanagari equivalent
    """
    l_result = p_string
    for l_kd, l_kl in g_consonants:
        for _, l_vd, l_vl in g_vowels:
            l_from = l_kl + l_vl
            l_to = l_kd + l_vd
            l_result = re.sub(l_from, l_to, l_result)

    for l_kd, l_kl in g_consonants:
        l_result = re.sub(l_kl, l_kd + g_virama, l_result)

    for l_vd, _, l_vl in g_vowels:
        l_result = re.sub(l_vl, l_vd, l_result)

    l_result = re.sub(g_visarga_l, g_visarga_d, l_result)

    l_result = re.sub(g_anusvara_l, g_anusvara_d, l_result)

    return l_result


# ---------------------------------------------------- Main section ----------------------------------------------------
if __name__ == "__main__":
    print('+------------------------------------------------------------+', file=sys.stderr)
    print('| Load Rig Veda Padapatha into DB                            |', file=sys.stderr)
    print('|                                                            |', file=sys.stderr)
    print('| rv_load_padapatha.py                                       |', file=sys.stderr)
    print('|                                                            |', file=sys.stderr)
    print('| v. 1.0 - 19/10/2018                                        |', file=sys.stderr)
    print('| v. 1.1 - 03/12/2018 Correction for ळ / ḷ and ai/au         |', file=sys.stderr)
    print('+------------------------------------------------------------+', file=sys.stderr)

    l_db_connection = psycopg2.connect(
        host=g_dbServer,
        database=g_dbDatabase,
        user=g_dbUser,
        password=g_dbPassword
    )

    # empty tables TB_PADAPATHA and TB_WORDS
    l_cursor_write = l_db_connection.cursor()

    try:
        l_cursor_write.execute("""
                delete from "TB_PADAPATHA"
            """)

        l_cursor_write.execute("""
                delete from "TB_WORDS"
            """)

    except Exception as e:
        print('DB ERROR:', repr(e))
        print(l_cursor_write.query)
        sys.exit(0)
    finally:
        # release DB objects once finished
        l_cursor_write.close()

    l_count_sloka = 0
    l_count_word = 0
    for l_file in os.listdir(g_root):
        l_path = os.path.join(g_root, l_file)

        if os.path.isfile(l_path) and re.match('rvpp_\d\du', os.path.basename(l_path)):
            print(l_path)
            with open(l_path, "r") as l_content:
                for l_line in l_content.readlines():
                    l_match = re.match('(.*)\s*//\s*RV_(\d+),(\d+).(\d+)\s*//<BR>\n', l_line)
                    if l_match:
                        l_text = l_match.group(1)
                        l_mandala = int(l_match.group(2))
                        l_sootka = int(l_match.group(3))
                        l_sloka = int(l_match.group(4))

                        l_text_deva = iast_to_deva(l_text)
                        print('[{0}] {1}:{2}:{3} {4} / {5}'.format(
                            l_count_sloka, l_mandala, l_sootka, l_sloka, l_text, l_text_deva))

                        l_cursor_write = l_db_connection.cursor()

                        try:
                            l_cursor_write.execute("""
                                    insert into 
                                        "TB_PADAPATHA"(
                                            "ID_SLOKA"
                                            , "N_MANDALA"
                                            , "N_SOOTKA"
                                            , "N_SLOKA"
                                            , "TX_PADAPATHA"
                                            , "TX_PADAPATHA_DEVA"
                                        )
                                        values( %s, %s, %s, %s, %s, %s );
                                """, (l_count_sloka, l_mandala, l_sootka, l_sloka, l_text, l_text_deva))

                            l_db_connection.commit()
                        except Exception as e:
                            l_db_connection.rollback()

                            print('DB ERROR:', repr(e))
                            print(l_cursor_write.query)
                            sys.exit(0)
                        finally:
                            # release DB objects once finished
                            l_cursor_write.close()

                        l_words = list(zip(
                            [w.strip() for w in l_text.split('|')],
                            [w.strip() for w in l_text_deva.split('|')]
                        ))
                        print('   -->', l_words)

                        for l_word_l, l_word_d in l_words:
                            l_cursor_write = l_db_connection.cursor()

                            try:
                                l_cursor_write.execute("""
                                    insert into 
                                        "TB_WORDS"(
                                            "ID_WORD"
                                            , "ID_SLOKA"
                                            , "S_WORD"
                                            , "S_WORD_DEVA"
                                        )
                                        values( %s, %s, %s, %s );
                                """, (l_count_word, l_count_sloka, l_word_l, l_word_d))

                                l_db_connection.commit()
                            except Exception as e:
                                l_db_connection.rollback()
                                print('DB ERROR:', repr(e))
                                print(l_cursor_write.query)
                                sys.exit(0)
                            finally:
                                # release DB objects once finished
                                l_cursor_write.close()

                            l_count_word += 1

                        l_count_sloka += 1

    l_db_connection.close()
