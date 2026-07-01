USE AstraNova_OLTP;

DROP TABLE IF EXISTS ProductCategory;

CREATE TABLE ProductCategory
(
    CategoryID CHAR(6) PRIMARY KEY,

    CategoryName VARCHAR(100) NOT NULL UNIQUE,

    CategoryDescription VARCHAR(255),

    Status ENUM
    (
        'Active',
        'Inactive'
    ) NOT NULL DEFAULT 'Active',

    CreatedDate DATE NOT NULL DEFAULT (CURRENT_DATE)
);

DESCRIBE ProductCategory;

INSERT INTO ProductCategory
(
    CategoryID,
    CategoryName,
    CategoryDescription,
    Status
)
VALUES
('CAT001','Electronics','Electronic devices and accessories','Active'),
('CAT002','Furniture','Home and office furniture','Active'),
('CAT003','Grocery','Food and grocery products','Active'),
('CAT004','Fashion','Clothing and fashion accessories','Active'),
('CAT005','Sports','Sports and fitness equipment','Active'),
('CAT006','Books','Books and educational materials','Active'),
('CAT007','Beauty','Beauty and personal care products','Active'),
('CAT008','Home','Home improvement and kitchen products','Active'),
('CAT009','Toys','Toys and games','Active'),
('CAT010','Automotive','Vehicle accessories and tools','Active');

SELECT *
FROM ProductCategory;