SELECT * FROM Member;
SELECT * FROM Book;
SELECT * FROM Author;
SELECT * FROM Reserves;
SELECT * FROM Fine;
SELECT * FROM Borrows;

SELECT b.*,
	GROUP_CONCAT(Author SEPARATOR ', ') AS 'author(s)'
FROM Author a, Book b
WHERE b.accessionNo = a.accessionNo AND author != ''
GROUP BY b.accessionNo;

SELECT
	accessionNo,
    memberID,
    borrowDate,
    returnDate,
    DATE_ADD(borrowDate, INTERVAL +14 DAY) as dueDate
    FROM Borrows;    
    
/*
GROUP BY accessionNo;
/*
accessionNo, title, isbn, publisher, pubYear
FROM Book
JOIN Author
SELECT accessionNo, author
FROM Author
ORDER BY accessionNo ASC;

/*
SELECT COUNT(DISTINCT propertyNo) AS myCount
FROM Viewing
WHERE dateView BETWEEN DATE("2013-05-01") And DATE("2013-05-31");
SELECT MIN(salary) AS myMin, MAX(salary) AS myMax, AVG(salary) AS myAvg
FROM Staff;
SELECT branchNo, COUNT(staffNo) AS myCount, SUM(salary) AS mySum
FROM Staff
GROUP BY branchNo
ORDER BY branchNo;
SELECT branchNo, COUNT(staffNo) AS myCount, SUM(salary) AS mySum
FROM Staff
GROUP BY branchNo
HAVING COUNT(staffNo) > 1
ORDER BY branchNo;
SELECT staffNo, fName, lName, position
FROM Staff
WHERE branchNo = (SELECT branchNo
				  FROM Branch
                  WHERE street = "163 Main St");
SELECT staffNo, fName, lName, position, salary - (SELECT AVG(salary) FROM Staff) AS salDiff
FROM Staff
WHERE salary > (SELECT AVG(salary) FROM Staff);
SELECT propertyNo, street, city, postcode, propertyType, rooms, rent
FROM PropertyForRent
WHERE staffNo IN (SELECT staffNo
                  FROM Staff
                  WHERE branchNo = (SELECT branchNo
						            FROM Branch
                                    WHERE street = "163 Main St"));

SELECT c.clientNo, fName, lName, propertyNo, comment
FROM Client c, Viewing v
WHERE c.clientNo = v.clientNo;
SELECT s.branchNo, s.staffNo, fName, lName, propertyNo
FROM Staff s, PropertyForRent p
WHERE s.staffNo = p.staffNo
ORDER BY s.branchNo, s.staffNo, propertyNo;
SELECT b.branchNo, b.city, s.staffNo, fName, lName, propertyNo
FROM Branch b, Staff s, PropertyForRent p
WHERE b.branchNo = s.branchNo AND s.staffNo = p.staffNo
ORDER BY b.branchNo, s.staffNo, propertyNo;
SELECT s.branchNo, s.staffNo, COUNT(*) AS myCount 
FROM Staff s, PropertyForRent p
WHERE s.staffNo = p.staffNo
GROUP BY s.branchNo, s.staffNo
ORDER BY s.branchNo, s.staffNo;
SELECT staffNo, fName, lName, position
FROM Staff s
WHERE EXISTS (SELECT *
              FROM Branch b
              WHERE s.branchNo = b.branchNo AND city = "London");

                                    



