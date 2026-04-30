#!/usr/bin/env python3

import pymysql
from pymysql.cursors import DictCursor

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="",
    autocommit=True,
    cursorclass=DictCursor,
)

## second edited (woosj)
