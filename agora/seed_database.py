import MySQLdb
from agora import settings
import sys
import os

dir = os.path.dirname(os.path.realpath(__file__))

def import_csv(table, csv):

    db = get_database()
    cursor = db.cursor()

    csv = dir + "/" + csv

    for line in open(csv):
        fields = [field[1:-1] if field[0] == '"' and field[-1] == '"' else field for field in line.strip().split(',')]
        break

    # fields = get_table_columns(table)
    sql = "LOAD DATA INFILE '{0}' INTO TABLE {1} FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES  ({2})  ;".format(csv, table, ','.join(fields))


    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print e
        db.rollback()
        db.close()
        return

    db.close()
    print "Successfully inserted"


def get_database():
    database = settings.DATABASES["default"]
    return MySQLdb.connect(host=database["HOST"], user=database["USER"], passwd=database["PASSWORD"], db=database["NAME"])


def get_table_columns(table):
    db = get_database()
    cursor = db.cursor()

    sql = "DESCRIBE " + table
    columns = []
    cursor.execute(sql)

    for (field, type, null, key, default, extra) in cursor:
        columns.append(field)

    return columns



table = sys.argv[1]
csv_or_columns = sys.argv[2]

if csv_or_columns == "-columns":
    columns = get_table_columns(table)
    for c in columns:
        print c
else:
    import_csv(table, csv_or_columns)