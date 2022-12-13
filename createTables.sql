USE Library;

CREATE TABLE Member(  
     memberID  VARCHAR(10)   NOT NULL UNIQUE,
     name      VARCHAR(30)   NOT NULL,
     faculty   VARCHAR(30)   NOT NULL,
     phone     INT        	 NOT NULL,
     email     VARCHAR(50)   NOT NULL,     
	 PRIMARY KEY (memberID)); 
CREATE TABLE Book(
     accessionNo VARCHAR(10)  NOT NULL UNIQUE,
     title       VARCHAR(100) NOT NULL,
     isbn        BIGINT     	  NOT NULL,
     publisher   VARCHAR(100) NOT NULL,
	 pubYear     INT 	  	  NOT NULL,
	 PRIMARY KEY (accessionNo));      
CREATE TABLE Author(
	 accessionNo VARCHAR(10)  NOT NULL,
     author      VARCHAR(100) NOT NULL,
     PRIMARY KEY (accessionNo, author),
     CONSTRAINT authorAN FOREIGN KEY (accessionNo) 
		REFERENCES Book (accessionNo)
		ON DELETE CASCADE); 
CREATE TABLE Borrows( 
     accessionNo VARCHAR(10) NOT NULL UNIQUE,
     memberID    VARCHAR(10) NOT NULL,
     borrowDate  DATE 		 NOT NULL,
     returnDate  DATE DEFAULT NULL,
	PRIMARY KEY (accessionNo),
    CONSTRAINT borrowsAN FOREIGN KEY (accessionNo) 
		REFERENCES Book (accessionNo)
		ON DELETE CASCADE,
    CONSTRAINT borrowsID FOREIGN KEY (memberID) 
		REFERENCES Member (memberID)
		ON DELETE CASCADE      
    );
CREATE TABLE Reserves (
    accessionNo VARCHAR(10) NOT NULL UNIQUE,
    memberID    VARCHAR(10) NOT NULL,
    reserveDate  DATE 		NOT NULL,
    PRIMARY KEY (accessionNo),
    CONSTRAINT reservesAN FOREIGN KEY (accessionNo) 
		REFERENCES Book (accessionNo)
		ON DELETE CASCADE,
    CONSTRAINT reservesID FOREIGN KEY (memberID) 
		REFERENCES Member (memberID)
		ON DELETE CASCADE
);	     
CREATE TABLE Fine (
	memberID    VARCHAR(10) NOT NULL,
	fineAmt int,
	paymentDate DATE,
	PRIMARY KEY (memberID),
    CONSTRAINT fineID FOREIGN KEY (memberID) 
		REFERENCES Member (memberID)
		ON DELETE CASCADE
);	 
     
