USE AstraNova_OLTP;

DROP TABLE IF EXISTS Inventory;

CREATE TABLE Inventory
(
    InventoryID CHAR(9) PRIMARY KEY,

    ProductID CHAR(9) NOT NULL,

    SupplierID CHAR(9) NOT NULL,

    QuantityInStock INT NOT NULL,

    ReorderPoint INT NOT NULL,

    MaximumStockLevel INT NOT NULL,

    UnitCost DECIMAL(10,2) NOT NULL,

    LastRestockDate DATE NOT NULL,


    Status ENUM
    (
        'In Stock',
        'Low Stock',
        'Out of Stock'
    ) NOT NULL,

    FOREIGN KEY (ProductID)
        REFERENCES Product(ProductID),

    FOREIGN KEY (SupplierID)
        REFERENCES Supplier(SupplierID)
);