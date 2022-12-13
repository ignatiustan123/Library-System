1. Membership Creation
INSERT INTO Member VALUES ("A101A","Hermione Granger","Science",33336663,"flying@als.edu");


2. Membership Deletion
DELETE FROM Member
WHERE memberID = "A101A"


3. Membership Update
UPDATE Member
SET name = "newName" /* name can be any column */
WHERE memberID = "A101A"


4. Book Acquisition
INSERT INTO Book VALUES ("A01","A 1984 Story",9790000000001,"Intra S.r.l.s.",2021);
INSERT INTO Author VALUES ("A01", "George Orwell");


5. Book Withdrawal
DELETE FROM Book
WHERE accessionNo = "A01" 
/* Cascade will delete from author table also */


6. Book Borrowing
INSERT INTO Borrows VALUES ("A01", "A101A", '2022-02-20', NULL); 
/* Date must be in single quotes in this format */


7. Book Returning
UPDATE Borrows
SET returnDate = '2022-02-21' 
WHERE accessionNo = "A01"

/* If you want to remove the record */
DELETE FROM Borrows
WHERE accessionNo = "A01" 


8. Book Reservation
INSERT INTO Reserves VALUES ("A01", "A101A", '2022-02-20'); 


9. Reservation Cancellation
DELETE FROM Reserves
WHERE accessionNo = "A01" 


10. Book Search
SELECT * FROM Book
WHERE title LIKE "%1984%"
/* title can be any column, " or ' is ok. Must surround search term with % */

/* If searching for author */
SELECT * FROM Book
WHERE accessionNo IN (SELECT accessionNo
					  FROM author
                      WHERE author LIKE "%George%")


11. Fine Payment                
/* If creating new fine */
INSERT INTO Fine VALUES ("A101A", 10, NULL); 

/* If creating new paid fine */
INSERT INTO Fine VALUES ("A101A", 0, '2022-02-20'); 

/* If paying existing fine */
UPDATE Fine
SET fineAmt = 0, paymentDate = '2022-02-20'
WHERE memberID = "A101A"

/* If deleting fine record */
DELETE FROM Fine
WHERE memberID = "A101A"


12. Display books on loan
/* Create TempTable holding books currently on loan */
DROP TABLE IF EXISTS TempTable;
    CREATE TEMPORARY TABLE TempTable AS (
    SELECT * 
    FROM Book
    WHERE accessionNo IN (SELECT accessionNo
					  FROM Borrows));

/* Concat TempTable with author */
SELECT t.*,
	GROUP_CONCAT(Author SEPARATOR ', ') AS 'author(s)'
FROM Author a, TempTable t
WHERE t.accessionNo = a.accessionNo AND author != ''
GROUP BY t.accessionNo;


13. Display books on reservation
SELECT r.accessionNo, b.title, r.memberID, m.name
FROM Reserves r
LEFT JOIN Book b
ON r.accessionNo = b.accessionNo
LEFT JOIN Member m
ON r.memberID = m.memberID


14. Display members who have outstanding fines
SELECT * FROM Member 
WHERE memberID IN (SELECT memberID
				   FROM Fine)
                   
                   
15. Display the books on loan to a member given the membership id
DROP TABLE IF EXISTS TempTable;
    CREATE TEMPORARY TABLE TempTable AS (
    SELECT * 
    FROM Book
    WHERE accessionNo IN (SELECT accessionNo
					  FROM Borrows WHERE memberID = "A101A"));

/* Concat TempTable with author */
SELECT t.*,
	GROUP_CONCAT(Author SEPARATOR ', ') AS 'author(s)'
FROM Author a, TempTable t
WHERE t.accessionNo = a.accessionNo AND author != ''
GROUP BY t.accessionNo;