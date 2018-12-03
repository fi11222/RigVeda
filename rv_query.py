#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys

__author__ = 'Nicolas Reimen'

g_dbServer = 'localhost'
g_dbDatabase = 'Rig Veda'
g_dbUser = 'postgres'
g_dbPassword = '15Eyyaka'

# ---------------------------------------------------- Main section ----------------------------------------------------
if __name__ == "__main__":
    print('+------------------------------------------------------------+', file=sys.stderr)
    print('| Output of Rig Veda queries                                 |', file=sys.stderr)
    print('|                                                            |', file=sys.stderr)
    print('| rv_query.py                                                |', file=sys.stderr)
    print('|                                                            |', file=sys.stderr)
    print('| v. 1.0 - 19/10/2018                                        |', file=sys.stderr)
    print('+------------------------------------------------------------+', file=sys.stderr)

    l_db_connection = psycopg2.connect(
        host=g_dbServer,
        database=g_dbDatabase,
        user=g_dbUser,
        password=g_dbPassword
    )

    l_cursor_read = l_db_connection.cursor()

    try:
        l_cursor_read.execute("""
            select * from "TB_RV" where "TX_VERSE" like '%धर्मा%'
        """)

        print("""
            <html>
            <head></head>
            <body>
            <table>
            <tr>
                <td>Ref</td>
                <td>Sloka</td>
            </tr>
        """)

        for l_mandala, l_sootka, l_sloka, l_text in l_cursor_read:
            print('<tr><td>{0}:{1}:{2}</td><td>{3}</td></tr>'.format(
                l_mandala, l_sootka, l_sloka, l_text))

        print("""
            </table>
            </body>
            </html>
        """)

    except Exception as e:
        print('DB ERROR:', repr(e))
        print(l_cursor_read.query)
        sys.exit(0)
    finally:
        # release DB objects once finished
        l_cursor_read.close()

    l_db_connection.close()
