USE AstraNova_OLTP;

DROP TABLE IF EXISTS Supplier;

CREATE TABLE Supplier
(
    SupplierID CHAR(9) PRIMARY KEY,

    SupplierName VARCHAR(150) NOT NULL,

    ContactPerson VARCHAR(100) NOT NULL,

    Email VARCHAR(150) UNIQUE NOT NULL,

    Phone VARCHAR(20) UNIQUE,

    City VARCHAR(100) NOT NULL,

    State VARCHAR(100) NOT NULL,

    Country VARCHAR(100) NOT NULL,

    SupplierRating DECIMAL(2,1) NOT NULL,

    LeadTimeDays INT NOT NULL,

    Status ENUM
    (
        'Active',
        'Inactive'
    ) DEFAULT 'Active',

    CreatedDate DATE NOT NULL
);


DESCRIBE Supplier;