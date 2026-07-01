USE AstraNova_OLTP;

DROP TABLE IF EXISTS Customer;

CREATE TABLE Customer
(
    CustomerID        VARCHAR(10)  NOT NULL,
    SegmentID         VARCHAR(10)  NOT NULL,

    FirstName         VARCHAR(50)  NOT NULL,
    LastName          VARCHAR(50)  NOT NULL,

    Email             VARCHAR(255) NOT NULL,
    Phone             VARCHAR(20)  NOT NULL,

    DateOfBirth       DATE,

    Gender ENUM
    (
        'Male',
        'Female',
        'Non-Binary',
        'Prefer Not To Say'
    ),

    RegistrationDate  DATE NOT NULL,

    Status ENUM
    (
        'Prospect',
        'Active',
        'Loyal',
        'Dormant',
        'Inactive',
        'Blocked'
    ) NOT NULL DEFAULT 'Prospect',

    CreatedDate DATETIME
        NOT NULL DEFAULT CURRENT_TIMESTAMP,

    UpdatedDate DATETIME
        NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT PK_Customer
        PRIMARY KEY (CustomerID),

    CONSTRAINT FK_Customer_CustomerSegment
        FOREIGN KEY (SegmentID)
        REFERENCES CustomerSegment(SegmentID),

    CONSTRAINT UQ_Customer_Email
        UNIQUE (Email),

    CONSTRAINT UQ_Customer_Phone
        UNIQUE (Phone)

);

SHOW CREATE TABLE Customer;

DESCRIBE Customer;