LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/LibBooks.txt'
REPLACE INTO TABLE Author
FIELDS TERMINATED BY ','     
ENCLOSED BY '"'             
LINES TERMINATED BY '\n'    
IGNORE 1 ROWS
(accessionNo, @dummy, author, @dummya2, @dummya3, @dummy2, @dummy3, @dummy4);    
 
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/LibBooks.txt'
REPLACE INTO TABLE Author
FIELDS TERMINATED BY ','     
ENCLOSED BY '"'             
LINES TERMINATED BY '\n'    
IGNORE 1 ROWS
(accessionNo, @dummy, @dummya1, author, @dummya3, @dummy2, @dummy3, @dummy4);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/LibBooks.txt'
REPLACE INTO TABLE Author
FIELDS TERMINATED BY ','     
ENCLOSED BY '"'             
LINES TERMINATED BY '\n'    
IGNORE 1 ROWS
(accessionNo, @dummy, @dummya1, @dummya2, author, @dummy2, @dummy3, @dummy4);