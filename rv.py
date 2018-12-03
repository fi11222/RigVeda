#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import sys

__author__ = 'Nicolas Reimen'

# ---------------------------------------------------- Main section ----------------------------------------------------
if __name__ == "__main__":
    print('+------------------------------------------------------------+')
    print('| Rig Veda database loading                                  |')
    print('|                                                            |')
    print('| rv.py                                                      |')
    print('|                                                            |')
    print('| v. 1.0 - 19/03/2018                                        |')
    print('+------------------------------------------------------------+')

    with open('./RV.txt', 'r') as l_file:
        l_content = l_file.read()

    print('size : {0}'.format(len(l_content)))

    with open('./RV.csv', 'w', encoding='utf-8') as l_csv:
        l_csv.write('N_MANDALA;N_SOOTKA;N_VERSE;TX_VERSE\n')

        l_mandala = 0
        l_mandala_prev = 0
        l_sootka = 0
        l_sootka_calc = 0
        l_verse_calc = 0
        for l_line in l_content.split('\n'):
            l_found_verse = re.search('([^॥]+)॥(\d+)', l_line)
            if l_found_verse:
                l_verse_calc += 1
                l_verse = l_found_verse.group(1) + '॥'
                try:
                    l_number = int(l_found_verse.group(2))
                except Exception as e:
                    print('Incorrect verse number in [{0}]'.format(l_line))
                    sys.exit(0)

                if l_verse_calc != l_number:
                    print('verse number mismatch: [{0}] calc: {1} verse: {2}'.format(l_line, l_verse_calc, l_number))
                    sys.exit(0)

                print('{0} : {1}'.format(l_number, l_verse))
                l_csv.write('{0};{1};{2};"{3}"\n'.format(l_mandala, l_sootka, l_number, l_verse))
            else:
                l_found_sootka = re.search('\((\d+).(\d+)\)', l_line)
                if l_found_sootka:
                    try:
                        l_mandala = int(l_found_sootka.group(1))
                        l_sootka = int(l_found_sootka.group(2))
                    except Exception as e:
                        print('Incorrect sootka number in [{0}]'.format(l_line))
                        sys.exit(0)

                    if l_mandala == l_mandala_prev:
                        l_sootka_calc += 1
                    else:
                        l_sootka_calc = 1
                        l_mandala_prev = l_mandala

                    if l_sootka_calc != l_sootka:
                        print('Sootka number mismatch: [{0}] calc: {1} verse: {2}'.format(
                            l_line, l_sootka_calc, l_sootka))
                        sys.exit(0)

                    l_verse_calc = 0
                    print('Mandala {0} Sootka {1}'.format(l_mandala, l_sootka))

