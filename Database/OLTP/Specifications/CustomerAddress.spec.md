# Customer Address Entity Specification

**Document Version:** 0.1  
**Status:** Draft  
**Project:** HELIX - Enterprise Data Intelligence Platform  
**Module:** Customer Domain  
**Entity Type:** Master Data  
**Author:** Ranjith A R  
**Last Updated:** 26 June 2026

---

# 1. Overview

The Customer Address entity stores one or more addresses associated with a customer.

A customer may maintain multiple addresses for shipping, billing, home, office, or other business purposes.

Separating addresses from the Customer entity ensures normalization and provides flexibility for future expansion.

---

# 2. Business Purpose

Customer Addresses enable AstraNova Global to:

- Deliver customer orders
- Generate invoices
- Calculate shipping charges
- Support multiple delivery locations
- Analyze regional customer distribution

---

# 3. Business Identifier

| Field | Value |
|--------|-------|
| Business Key | AddressID |
| Format | ADD000001 |
| Example | ADD000001 |

---

# 4. Relationships

| Entity | Relationship |
|---------|--------------|
| Customer | One Customer can have Many Addresses |
| Country | One Country can have Many Addresses |
| Region | One Region can have Many Addresses |

---

# 5. Entity Attributes

| Column | Data Type | Required | Description |
|---------|-----------|----------|-------------|
| AddressID | VARCHAR(10) | Yes | Business Identifier |
| CustomerID | VARCHAR(10) | Yes | Customer Reference |
| AddressType | VARCHAR(20) | Yes | Home, Billing, Shipping, Office |
| AddressLine1 | VARCHAR(255) | Yes | Primary Address |
| AddressLine2 | VARCHAR(255) | No | Secondary Address |
| City | VARCHAR(100) | Yes | City |
| State | VARCHAR(100) | Yes | State |
| PostalCode | VARCHAR(20) | Yes | ZIP / PIN Code |
| CountryCode | VARCHAR(5) | Yes | Country Reference |
| IsDefault | BOOLEAN | Yes | Default Address |
| CreatedDate | DATETIME | Yes | Record Creation |
| UpdatedDate | DATETIME | Yes | Last Modification |

---

# 6. Supported Address Types

- Home
- Shipping
- Billing
- Office

---

# 7. Business Rules

| Rule ID | Rule |
|----------|------|
| BR-001 | Every Address must belong to one Customer. |
| BR-002 | A Customer can have multiple Addresses. |
| BR-003 | Only one Address of each type can be marked as Default. |
| BR-004 | PostalCode cannot be empty. |
| BR-005 | CountryCode must exist in Country Master. |

---

# 8. Data Quality Rules

HELIX validates:

- Missing Customer IDs
- Invalid Postal Codes
- Missing Cities
- Missing Countries
- Duplicate Default Addresses
- Invalid Address Types

---

# 9. Downstream Dependencies

This entity is used by:

- Orders
- Shipments
- Returns
- Customer Analytics
- Regional Dashboards

---

# 10. Future Enhancements

Future versions may include:

- GPS Coordinates
- Address Verification
- Delivery Zones
- Geospatial Analytics

---

**End of Document**