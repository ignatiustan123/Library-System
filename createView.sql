INSERT INTO Borrows VALUES ("A01", "A101A", "2022-02-16");
CREATE VIEW Borrow As
SELECT
	accessionNo,
    memberID,
    borrowDate, 
    DATE_ADD(borrowDate, INTERVAL +14 DAY) as dueDate
    FROM Borrows;    