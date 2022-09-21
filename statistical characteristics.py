#!/usr/bin/env python
# coding: utf-8

import sqlite3
from math import sqrt
from tabulate import tabulate
import matplotlib.pyplot as plt

conn = sqlite3.connect('frequency_dict.db')
cursor = conn.cursor()

def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS noun_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS noun_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS verb_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS verb_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adjective_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adjective_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS conjunction_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS conjunction_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pronoun_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pronoun_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS preposition_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS preposition_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS particle_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS particle_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adverb_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adverb_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS exclemation_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS exclemation_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS comparative_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS comparative_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adverbial_participle_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adverbial_participle_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS predicative_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS predicative_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS numeral_aver_freq
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS numeral_statistics
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
      cursor.execute('''CREATE TABLE IF NOT EXISTS noun_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS noun_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS verb_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS verb_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adjective_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adjective_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS conjunction_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS conjunction_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pronoun_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pronoun_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS preposition_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS preposition_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS particle_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS particle_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adverb_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adverb_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS exclemation_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS exclemation_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS comparative_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS comparative_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adverbial_participle_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS adverbial_participle_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS predicative_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS predicative_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS numeral_aver_freq_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    xi INTEGER,
                    ni INTEGER,
                    xini INTEGER,
                    x_aver INTEGER,
                    xi_minus_x_aver INTEGER,
                    xi_minus_x_aver_squared INTEGER,
                    xi_minus_x_aver_mult_ni_squared INTEGER)
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS numeral_statistics_2
                    (id INTEGER PRIMARY KEY NOT NULL,
                    mean_square_deviation REAL,
                    aver_freq_fluctuation REAL,
                    x_aver_plus_minus_sigma TEXT,
                    x_aver_plus_minus_2_sigma TEXT,
                    x_aver_plus_minus_3_sigma TEXT,
                    sigma_fluctuation_interval TEXT,
                    2sigma_fluctuation_interval TEXT,
                    3sigma_fluctuation_interval TEXT,
                    V REAL,
                    Vmax REAL,
                    D REAL,
                    error REAL)
    ''')
conn.commit()

def count_aver_freq():
        global aver_freq_x
        global aver_freq_x_ordered
        global freq
        global part_of_sp
        aver_freq_x = {}
        rows = cursor.fetchall()
        for row in rows:
             freq = row[4:24]
             part_of_sp = row[0]
             for i in freq:
                if i in aver_freq_x:
                    aver_freq_x[i][1] += 1
                    xini0 = aver_freq_x[i][0]*aver_freq_x[i][1]
                    aver_freq_x[i][2] = xini0
                else:
                    aver_freq_x[i] = [i]
                    aver_freq_x[i].append(1)
                    xini0 = aver_freq_x[i][0]*aver_freq_x[i][1]
                    aver_freq_x[i].append(xini0)
        aver_freq_x = list(aver_freq_x.values())

        aver_freq_x_ordered = sorted(aver_freq_x, key=lambda x:x[0])

        count=0
        while count in range (0, len(aver_freq_x_ordered)):
            xini0= []
            ni0 = []
            for i in aver_freq_x_ordered:
                xini0.append(i[2])
                ni0.append(i[1])
            x_aver0 = sum(xini0)/sum(ni0)
            aver_freq_x_ordered[count].append(x_aver0)
            aver_freq_x_ordered[count].append((aver_freq_x_ordered[count][0]-x_aver0))
            aver_freq_x_ordered[count].append(((aver_freq_x_ordered[count][0]-x_aver0)**2))
            aver_freq_x_ordered[count].append(((aver_freq_x_ordered[count][0]-x_aver0)**2*aver_freq_x_ordered[count][1]))
            count += 1

def statistics():
        global xi, ni, xini, ni_sum, x_aver, xi_minus_x_aver, xi_minus_x_aver_squared, xi_minus_x_aver_squared_ni, sigma, \
            sigma_x_aver, interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver, \
            interval_sigma_3_x_aver, coef_of_variation, coef_of_variation_max, D, error
        global my_list
        rows = cursor.fetchall()
        xi = []
        for row in rows:
            xi.append(row[1])

        ni = []
        for row in rows:
            ni.append(row[2])
        ni_sum = sum(ni)

        xini = []
        for row in rows:
            xini.append(row[3])
        xini_sum = sum(xini)

        x_aver = rows[0][4]

        xi_minus_x_aver = []
        for row in rows:
            xi_minus_x_aver.append(row[5])

        xi_minus_x_aver_squared = []
        for row in rows:
            xi_minus_x_aver_squared.append(row[6])

        xi_minus_x_aver_squared_ni = []
        for row in rows:
            xi_minus_x_aver_squared_ni.append(row[7])

        sigma = sqrt(sum(xi_minus_x_aver_squared_ni)/ni_sum)

        sigma_x_aver = sigma/sqrt(ni_sum)

        interval_sigma = [round(x_aver-sigma), round(x_aver+sigma)]
        interval_2_sigma = [round(x_aver-2*sigma), round(x_aver+2*sigma)]
        interval_3_sigma = [round(x_aver-3*sigma), round(x_aver+3*sigma)]

        interval_sigma_x_aver = [round(x_aver-sigma_x_aver), round(x_aver+sigma_x_aver)]
        interval_sigma_2_x_aver = [round(x_aver-2*sigma_x_aver), round(x_aver+2*sigma_x_aver)]
        interval_sigma_3_x_aver = [round(x_aver-3*sigma_x_aver), round(x_aver+3*sigma_x_aver)]

        coef_of_variation = round(sigma/x_aver, 2)
        coef_of_variation_max = sqrt(ni_sum-1)
        D = 1-coef_of_variation/coef_of_variation_max
        error = round((1.96*coef_of_variation)/sqrt(sum(ni)), 2)

        my_list = []
        my_list.append(sigma)
        my_list.append(sigma_x_aver)
        my_list.append(str(interval_sigma))
        my_list.append(str(interval_2_sigma))
        my_list.append(str(interval_3_sigma))
        my_list.append(str(interval_sigma_x_aver))
        my_list.append(str(interval_sigma_2_x_aver))
        my_list.append(str(interval_sigma_3_x_aver))
        my_list.append(coef_of_variation)
        my_list.append(coef_of_variation_max)
        my_list.append(D)
        my_list.append(error)

def print_results():
        table = {'xi': xi,'ni': ni, 'xi*ni': xini, 'х̅': [x_aver], 'xi - х̅': xi_minus_x_aver,
                 '(xi - х̅)^2': xi_minus_x_aver_squared, '(xi - х̅)^2*ni': xi_minus_x_aver_squared_ni}
        print(tabulate(table, headers='keys'))

        table = [['σ', 'σх̅', 'інт. із σ', 'інт. із 2σ',
                  'інт. із 3σ', 'інт. σх̅', 'інт. 2σх̅',
                  'інт. 3σх̅', 'V', 'Vmax', 'D', 'похибка'], [round(sigma), round(sigma_x_aver),
                  interval_sigma, interval_2_sigma, interval_3_sigma, interval_sigma_x_aver, interval_sigma_2_x_aver,
                  interval_sigma_3_x_aver, coef_of_variation, coef_of_variation_max, D, error]]
        print('\n')
        print(tabulate(table, headers='firstrow'))


        x_aver_minus_sigma = round(interval_sigma[0])
        x_aver_plus_sigma = round(interval_sigma[1])
        global ni_in_interval_sigma_sum
        ni_in_interval_sigma = []
        for i in aver_freq_x_ordered:
            if i[0] in range(x_aver_minus_sigma, x_aver_plus_sigma+1):
                ni_in_interval_sigma.append(i[1])
                ni_in_interval_sigma_sum = sum(ni_in_interval_sigma)
        percentage = round(ni_in_interval_sigma_sum*100/ni_sum, 1)

        print('\n' + 'There are ' "(" + str(sum(ni_in_interval_sigma)) + ') -  ' + str(percentage) + '% of absolute frequecies in the interval x_aver ± sigma')

        if round((68.3 - percentage)*100/68.3, 1) < 5:
            print('This indicates a good agreement between the theoretically calculated and empirical results')
        else:
            print('This indicates a bad agreement between the theoretically calculated and empirical results')

        x_aver_minus_2_sigma = round(interval_2_sigma[0])
        x_aver_plus_2_sigma = round(interval_2_sigma[1])
        global ni_in_interval_2_sigma_sum
        ni_in_interval_2_sigma = []
        for i in aver_freq_x_ordered:
            if i[0] in range(x_aver_minus_2_sigma, x_aver_plus_2_sigma+1):
                ni_in_interval_2_sigma.append(i[1])
                ni_in_interval_2_sigma_sum = sum(ni_in_interval_2_sigma)
        percentage = round(ni_in_interval_2_sigma_sum*100/ni_sum, 1)
        print('\n' + 'There are ' + "(" + str(sum(ni_in_interval_2_sigma)) + ') -  ' + str(percentage) + '% of absolute frequecies in the interval x_aver ± 2*sigma')

        if round((95.5 - percentage)*100/95.5, 1) < 5:
            print('This indicates a good agreement between the theoretically calculated and empirical results')
        else:
            print('This indicates a bad agreement between the theoretically calculated and empirical results')

        x_aver_minus_3_sigma = round(interval_3_sigma[0])
        x_aver_plus_3_sigma = round(interval_3_sigma[1])
        global ni_in_interval_3_sigma_sum
        ni_in_interval_3_sigma = []
        for i in aver_freq_x_ordered:
            if i[0] in range(x_aver_minus_3_sigma, x_aver_plus_3_sigma+1):
                ni_in_interval_3_sigma.append(i[1])
                ni_in_interval_3_sigma_sum = sum(ni_in_interval_3_sigma)
        percentage = round(ni_in_interval_3_sigma_sum*100/ni_sum, 1)
        print('\n' + 'There are ' + str(percentage) + '% of absolute frequecies in the interval x_aver ± 3*sigma')

        if round((99.7 - percentage)*100/99.7, 1) < 5:
            print('This indicates a good agreement between the theoretically calculated and empirical results')
        else:
            print('This indicates a bad agreement between the theoretically calculated and empirical results')

        x_aver_minus_sigma_x_aver = round(interval_sigma_x_aver[0])
        x_aver_plus_sigma_x_aver = round(interval_sigma_x_aver[1])
        print('\n' + '''With a probability of 68.3%, we can state that in this general population, the average frequency of this part of speech will vary within '''
              + str(x_aver_minus_sigma_x_aver) + ' and ' + str(x_aver_plus_sigma_x_aver))

        x_aver_minus_2_sigma_x_aver = round(interval_sigma_2_x_aver[0])
        x_aver_plus_2_sigma_x_aver = round(interval_sigma_2_x_aver[1])
        print('\n' + '''With a probability of 95.5%, we can state that in this general population, the average frequency of this part of speech will vary within '''
              + str(x_aver_minus_2_sigma_x_aver) + ' and ' + str(x_aver_plus_2_sigma_x_aver))

        x_aver_minus_3_sigma_x_aver = round(interval_sigma_3_x_aver[0])
        x_aver_plus_3_sigma_x_aver = round(interval_sigma_3_x_aver[1])
        print('\n' + '''With a probability of 99.7%, we can state that in this general population, the average frequency of this part of speech will vary within '''
              + str(x_aver_minus_3_sigma_x_aver) + ' and ' + str(x_aver_plus_3_sigma_x_aver))

def interval_row(K):
    global interval_row_list # a list with interval limits and midpoints
    global ni_in_intervals   # a list of amount of xi values in each interval

    R = max(xi) - min(xi)
    h = R/K
    interval_row_list = []
    ni_in_intervals = []
    xini_intervals = []
    for i in range(0, K):
        interval_row_list.append([min(xi)+i*h, round((min(xi)+i*h)+h, 1), round((min(xi)+i*h)+h/2, 1)])
        ni_for_one_interval = []
        for o in aver_freq_x_ordered:
            if min(xi)+i*h <= o[0] <= (min(xi)+i*h)+h:
                ni_for_one_interval.append(o[1])
            else:
                continue
        ni_in_intervals.append(ni_for_one_interval)
        xini_intervals.append([round((min(xi)+i*h)+h/2, 1), sum(ni_for_one_interval)])
    ni_interval_sum = []
    xini_intervals_sum = []
    for i in xini_intervals:
        ni_interval_sum.append(i[1])
        xini_intervals_sum.append(i[0]*i[1])
    ni_interval_sum = sum(ni_interval_sum)
    xini_intervals_sum = sum(xini_intervals_sum)
    x_aver_interval = xini_intervals_sum/ni_interval_sum

def student(x, y, s_1_x, s_2_x):
    global t
    t = abs(x-y)/sqrt(s_1_x+s_2_x)
    print('Student criteria: ' + str(t))

def X_squared_count(M1, M2, K):
    global X_squared
    X_squared = []
    for i in range(0, ni_sum):
        X_squared.append(M1[i]**2/(sum(M1)*sum(K[i])))
        X_squared.append(M2[i]**2/(sum(M2)*sum(K[i])))
    N = sum(M1)+sum(M2)
    X_squared = N*((sum(X_squared))-1)
    print('xi squared ' + str(X_squared))



#CREATE A VARIATION SERIES FOR THE NOUN
cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'NOUN'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO noun_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()
M1 = freq

# WE ADD THE VALUE X_AVERAGE TO THE TABLE, AND THE VALUES NEEDED FOR FURTHER CALCULATIONS
cursor.execute("select * from noun_aver_freq")
statistics()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute(""" INSERT INTO noun_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()



print('STATISTICAL DATA FOR THE NOUN, TEXT 1' + '\n')
print_results()

# CREATE A NOUN FREQUENCY POLYGON
interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))
print(xi_interval)
plt.plot(xi_interval, ni_interval, label = '1 text, by interval series', marker = 'o', markersize = 4)




cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'NOUN'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO noun_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

# WE ADD THE VALUE X_AVERAGE TO THE TABLE, AND THE VALUES NEEDED FOR FURTHER CALCULATIONS
cursor.execute("select * from noun_aver_freq_2")
statistics()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute(""" INSERT INTO noun_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()



print('STATISTICAL DATA FOR THE NOUN, TEXT 2' + '\n')
print_results()

interval_row(11)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 text, by interval series', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('polygon of noun frequencies')
plt.legend()
plt.show()


student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp

cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()



cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'VERB'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO verb_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from дієслово_середня_частота")
statistics()
cursor.execute(""" INSERT INTO verb_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq
print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄСЛОВА, ВИБІРКА 1' + '\n')
print_results()
#СТВОРЮЄМО ПОЛІГОН ЧАСТОТ ДІЄСЛОВА
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(9)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)




cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'VERB'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO verb_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from дієслово_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO verb_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄСЛОВА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот дієслова')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()





cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'ADJF'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO adjective_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from прикметник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO adjective_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИКМЕТНИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)
print(xi_interval)




cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'ADJF'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO adjective_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from прикметник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO adjective_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))
print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИКМЕТНИКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прикметника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()







cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'CONJ'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO conjunction_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()
#print(aver_freq_conj_ordered)

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from сполучник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO conjunction_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ СПОЛУЧНИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)
#plt.legend()
#plt.show()




cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'CONJ'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO conjunction_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from сполучник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO conjunction_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))
print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ СПОЛУЧНИКА, ВИБІРКА 2' + '\n')
print_results()

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот сполучника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()






cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'NPRO'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO pronoun_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()
#print(aver_freq_npro_ordered)

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from займенниковий_іменник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO pronoun_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()
M1 = freq

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЗАЙМЕННИКОВОГО ІМЕННИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(9)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)





cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'NPRO'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO pronoun_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from займенниковий_іменник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO pronoun_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЗАЙМЕННИКОВОГО ІМЕННИКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот займенникового іменника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()








cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'PREP'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO preposition_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from прийменник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO preposition_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИЙМЕННИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)








cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'PREP'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO preposition_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from прийменник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO preposition_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИЙМЕННИКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2  вибірка', marker = 'o', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)


plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прийменника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()





cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'PRCL'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO particle_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from частка_середня_частота")
statistics()
cursor.execute(""" INSERT INTO particle_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧАСТКИ, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)






cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'PRCL'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO particle_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from частка_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO particle_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧАСТКИ, ВИБІРКА 2' + '\n')
print_results()

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)

#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот частки')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()







cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'ADVB'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO adverb_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from прислівник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO adverb_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИСЛІВНИКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)




cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'ADVB'""")
count_aver_freq()
#print(aver_freq_x_ordered)
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO adverb_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from прислівник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO adverb_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРИСЛІВНИКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(7)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)


plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот прислівника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()






cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'INTJ'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO exclemation_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from вигук_середня_частота")
statistics()
cursor.execute(""" INSERT INTO exclemation_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ВИГУКА, ВИБІРКА 1' + '\n')
print_results()
#plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '1 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)




cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'INTJ'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO exclemation_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from вигук_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO exclemation_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ВИГУКА, ВИБІРКА 2' + '\n')
print_results()
#plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)

interval_row(5)
xi_interval = []
ni_interval = []
for i in interval_row_list:
    xi_interval.append(i[2])

for i in ni_in_intervals:
    ni_interval.append(sum(i))

plt.plot(xi_interval, ni_interval, label = '2 вибірка, за інтервальним рядом', marker = 'o', markersize = 4)


plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот вигука')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()








cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'COMP'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO comparative_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from компаратив_середня_частота")
statistics()
cursor.execute(""" INSERT INTO comparative_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ КОМПАРАТИВУ, ВИБІРКА 1' + '\n')
print_results()
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)















cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'GRND'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO adverbial_participle_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from дієприслівник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO adverbial_participle_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄПРИСЛІВНИКА, ВИБІРКА 1' + '\n')
print_results()
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)






cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'GRND'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO adverbial_participle_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                       VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from дієприслівник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO adverbial_participle_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ДІЄПРИСЛІВНИКА, ВИБІРКА 2' + '\n')
print_results()
plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот дієприслівника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()







cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'PRED'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO predicative_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from предикатив_середня_частота")
statistics()
cursor.execute(""" INSERT INTO predicative_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРЕДИКАТИВА, ВИБІРКА 1' + '\n')
print_results()
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)






cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'PRED'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO predicative_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from предикатив_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO predicative_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ПРЕДИКАТИВА, ВИБІРКА 2' + '\n')
print_results()
plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот предикативу')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()






cursor.execute("""select * from part_of_speech_freq
                   where part_of_speech = 'NUMR'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO numeral_aver_freq (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_1_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
x = x_aver
cursor.execute("select * from числівник_середня_частота")
statistics()
cursor.execute(""" INSERT INTO numeral_statistics (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M1 = freq


print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧИСЛІВНИКА, ВИБІРКА 1' + '\n')
print_results()
plt.plot(xi, ni, label = '1 вибірка', marker = 'o', markerfacecolor = 'blue', markersize = 4)





cursor.execute("""select * from part_of_speech_freq_2
                   where part_of_speech = 'NUMR'""")
count_aver_freq()
for i in aver_freq_x_ordered:
    cursor.execute("""INSERT INTO numeral_aver_freq_2 (xi, ni, xini, x_aver, xi_minus_x_aver,
                       xi_minus_x_aver_squared, xi_minus_x_aver_mult_ni_squared)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", i)
conn.commit()

s_2_x = sum(xi_minus_x_aver_squared_ni)/(ni_sum*(ni_sum-1))
y = x_aver
cursor.execute("select * from числівник_середня_частота_2")
statistics()
cursor.execute(""" INSERT INTO numeral_statistics_2 (mean_square_deviation, aver_freq_fluctuation,
               x_aver_plus_minus_sigma, x_aver_plus_minus_2_sigma, x_aver_plus_minus_3_sigma, sigma_fluctuation_interval,
               2sigma_fluctuation_interval, 3sigma_fluctuation_interval, V, Vmax, D, error)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", my_list)
conn.commit()

M2 = freq
K = list(zip(M1, M2))

print('\n' + 'СТАТИСТИЧНІ ДАНІ ДЛЯ ЧИСЛІВНИКА, ВИБІРКА 2' + '\n')
print_results()
plt.plot(xi, ni, label = '2 вибірка', marker = 'o', markersize = 4)
plt.xlabel('xi')
plt.ylabel('ni')
plt.title('полігон частот числівника')
plt.legend()
plt.show()

student(x, y, s_1_x, s_2_x)
X_squared_count(M1, M2, K)
part_of_sp = part_of_sp
cursor.execute("""INSERT INTO Student_criteria_xi_squared (part_of_sp, student, xi_squared)
                  VALUES (?, ?, ?)""", (str(part_of_sp), t, X_squared))
conn.commit()

conn.close()
