# HELIX Engineering Standards

**Version:** 1.0  
**Status:** Approved  
**Project:** HELIX - Enterprise Data Intelligence Platform  
**Author:** Ranjith A R  
**Last Updated:** 26 June 2026

---

# 1. Purpose

This document defines the engineering standards used throughout HELIX.

Every engineering artifact must follow these standards to ensure consistency, scalability, readability, and maintainability.

---

# 2. Naming Conventions

## Tables

Use PascalCase.

Examples:

- Customer
- CustomerAddress
- CustomerSegment
- Product
- Order
- OrderItem

Warehouse tables use prefixes.

Examples:

- DimCustomer
- DimProduct
- FactSales
- FactInventory

---

## Columns

Use PascalCase.

Examples:

- CustomerID
- FirstName
- LastName
- RegistrationDate

---

## Primary Keys

Always use:

<EntityName>ID

Examples:

- CustomerID
- ProductID
- OrderID

Warehouse surrogate keys:

<EntityName>Key

Examples:

- CustomerKey
- ProductKey

---

## Foreign Keys

Always reference the parent entity.

Examples:

- CustomerID
- ProductID
- SupplierID

---

# 3. Audit Columns

Every master and transaction table must include:

- CreatedDate
- UpdatedDate

Future versions may include:

- CreatedBy
- UpdatedBy

---

# 4. Boolean Fields

Always begin with:

- Is
- Has
- Can

Examples:

- IsActive
- IsDefault
- HasConsent
- CanReturn

---

# 5. Date Standards

Use UTC wherever possible.

Examples:

- CreatedDate
- RegistrationDate
- OrderDate

---

# 6. Status Fields

Avoid free-text values.

Status values must be predefined.

Example:

Customer Status

- Prospect
- Active
- Loyal
- Dormant
- Inactive
- Blocked

---

# 7. File Naming

Markdown

PascalCase.md

Examples:

Customer.spec.md

Product.spec.md

Python

snake_case.py

Examples:

generate_customers.py

customer_etl.py

SQL

snake_case.sql

Examples:

create_customer.sql

insert_customer.sql

Power BI

Module_Name.pbix

Example:

Customer_Analytics.pbix

---

# 8. Folder Structure

database/

python/

datasets/

design/

powerbi/

tests/

docs/

standards/

---

# 9. Documentation Rules

Every specification must include:

- Overview
- Business Purpose
- Relationships
- Attributes
- Business Rules
- Data Quality Rules
- Dependencies
- Future Enhancements

---

# 10. Engineering Principles

- Business First
- Normalize Before Optimizing
- Reuse Before Rebuilding
- Validate Before Loading
- Document Important Decisions
- Test Every Component
- Keep Designs Simple
- Build for Scalability

---

**End of Document**