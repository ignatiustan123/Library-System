LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/LibBooks.txt'
INTO TABLE Book
FIELDS TERMINATED BY ','     
ENCLOSED BY '"'             
LINES TERMINATED BY '\n'    
IGNORE 1 ROWS
(accessionNo, title, @dummy, @dummy2, @dummy3, isbn, publisher, pubYear);     