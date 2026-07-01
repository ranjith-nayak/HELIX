USE AstraNova_OLTP;

DROP TABLE IF EXISTS Orders;

CREATE TABLE Orders
(
    OrderID CHAR(9) PRIMARY KEY,

    CustomerID CHAR(9) NOT NULL,

    ProductID CHAR(9) NOT NULL,

    Quantity INT NOT NULL,

    UnitPrice DECIMAL(10,2) NOT NULL,

    DiscountPercent DECIMAL(5,2) DEFAULT 0,

    OrderDate DATE NOT NULL,

    DeliveryDate DATE,

    OrderStatus ENUM
    (
        'Pending',
        'Processing',
        'Shipped',
        'Delivered',
        'Cancelled'
    ) NOT NULL,

    FOREIGN KEY (CustomerID)
        REFERENCES Customer(CustomerID),

    FOREIGN KEY (ProductID)
        REFERENCES Product(ProductID)
);


DESCRIBE Orders;