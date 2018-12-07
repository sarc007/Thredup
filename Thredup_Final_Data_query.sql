select * from scrapped_diff_thredup_tbl
INTO OUTFILE 'G:/pycharmprojects/thredup/data/final/thredup_data.csv'
FIELDS TERMINATED BY '|'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';