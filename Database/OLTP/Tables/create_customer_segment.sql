DROP TABLE IF EXISTS CustomerSegment;

I actually agree with doing that.

We're at the beginning of HELIX. If something feels off now, this is the cheapest time to fix it. Six months from now we'd be refactoring dozens of dependent tables instead. Software has a habit of punishing "we'll fix it later."

Let's restart the Customer Segment properly.

I also want to improve our SQL style to make it look like something you'd find in a production repository.

📁 File 01_create_database.sql
/*
===============================================================================
Script Name : 01_create_database.sql
Project     : HELIX - Enterprise Data Intelligence Platform
Database    : AstraNova_OLTP
Purpose     : Create the Operational Database
Author      : Ranjith A R
===============================================================================
*/

DROP DATABASE IF EXISTS AstraNova_OLTP;

CREATE DATABASE AstraNova_OLTP
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE AstraNova_OLTP;

SELECT DATABASE();

Run this first.

📁 File 02_create_customer_segment.sql
/*
===============================================================================
Script Name : 02_create_customer_segment.sql
Project     : HELIX - Enterprise Data Intelligence Platform
Database    : AstraNova_OLTP
Domain      : Customer
Table       : CustomerSegment
Purpose     : Stores customer segmentation categories used throughout AstraNova.
===============================================================================
*/

USE AstraNova_OLTP;

DROP TABLE IF EXISTS CustomerSegment;

CREATE TABLE CustomerSegment
(
    SegmentID           VARCHAR(10)  NOT NULL,
    SegmentName         VARCHAR(50)  NOT NULL,
    Description         VARCHAR(255),
    MinLifetimeValue    DECIMAL(12,2),
    MaxLifetimeValue    DECIMAL(12,2),
    IsActive            BOOLEAN      NOT NULL DEFAULT TRUE,
    CreatedDate         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UpdatedDate         DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
                                     ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT PK_CustomerSegment
        PRIMARY KEY (SegmentID),

    CONSTRAINT UQ_CustomerSegment_Name
        UNIQUE (SegmentName),

    CONSTRAINT CHK_CustomerSegment_LifetimeValue
        CHECK
        (
            (MinLifetimeValue IS NULL)
            OR
            (MaxLifetimeValue IS NULL)
            OR
            (MinLifetimeValue <= MaxLifetimeValue)
        )
);