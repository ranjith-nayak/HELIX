USE AstraNova_OLTP;

DROP TABLE IF EXISTS Product;

CREATE TABLE Product
(
    ProductID CHAR(9) PRIMARY KEY,

    CategoryID CHAR(6) NOT NULL,

    ProductName VARCHAR(150) NOT NULL,

    Brand VARCHAR(100) NOT NULL,

    SKU VARCHAR(30) NOT NULL UNIQUE,

    CostPrice DECIMAL(10,2) NOT NULL,

    SellingPrice DECIMAL(10,2) NOT NULL,

    ReorderLevel INT NOT NULL,

    ProductStatus ENUM
    (
        'Active',
        'Inactive',
        'Discontinued'
    ) DEFAULT 'Active',

    CreatedDate DATE DEFAULT (CURRENT_DATE),

    CONSTRAINT FK_Product_Category
        FOREIGN KEY(CategoryID)
        REFERENCES ProductCategory(CategoryID)
);

DESCRIBE Product;