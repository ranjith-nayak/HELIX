# Customer Entity Specification

**Document Version:** 0.1  
**Status:** Draft  
**Project:** HELIX - Enterprise Data Intelligence Platform  
**Module:** Customer Domain  
**Entity Type:** Master Data  
**Author:** Ranjith A R  
**Last Updated:** 26 June 2026

---

# 1. Overview

The Customer entity stores the master information of every individual or organization registered with AstraNova Global.

A customer can:

- Purchase products
- Receive shipments
- Submit product reviews
- Raise support tickets
- Earn loyalty rewards
- Participate in marketing campaigns

The Customer entity serves as the foundation for multiple business processes across the organization.

---

# 2. Business Purpose

The Customer entity enables AstraNova Global to:

- Maintain customer profiles
- Track customer lifecycle
- Support order management
- Personalize customer experiences
- Analyze purchasing behavior
- Manage loyalty programs
- Generate business intelligence

---

# 3. Business Identifier

| Field | Value |
|--------|-------|
| Business Key | CustomerID |
| Format | CUS000001 |
| Example | CUS000001 |

---

# 4. Relationships

The Customer entity has relationships with the following entities:

| Entity | Relationship |
|---------|--------------|
| CustomerSegment | Many Customers belong to One Segment |
| CustomerAddress | One Customer can have Multiple Addresses |
| Orders | One Customer can place Multiple Orders |
| Reviews | One Customer can submit Multiple Reviews |
| SupportTickets | One Customer can create Multiple Support Tickets |
| LoyaltyAccount | One Customer has One Loyalty Account |
| MarketingPreferences | One Customer has One Marketing Preference |

---

# 5. Entity Attributes

## Identity Information

| Column | Data Type | Required | Description |
|---------|-----------|----------|-------------|
| CustomerID | VARCHAR(10) | Yes | Business Identifier |
| FirstName | VARCHAR(50) | Yes | Customer First Name |
| LastName | VARCHAR(50) | Yes | Customer Last Name |

---

## Contact Information

| Column | Data Type | Required | Description |
|---------|-----------|----------|-------------|
| Email | VARCHAR(255) | Yes | Email Address |
| Phone | VARCHAR(20) | Yes | Contact Number |

---

## Personal Information

| Column | Data Type | Required | Description |
|---------|-----------|----------|-------------|
| DateOfBirth | DATE | No | Customer Birth Date |
| Gender | VARCHAR(20) | No | Gender |

---

## Business Information

| Column | Data Type | Required | Description |
|---------|-----------|----------|-------------|
| SegmentID | VARCHAR(10) | Yes | Customer Segment |
| Status | VARCHAR(20) | Yes | Customer Status |
| RegistrationDate | DATE | Yes | Registration Date |

---

## Preferences

| Column | Data Type | Required | Description |
|---------|-----------|----------|-------------|
| PreferredLanguage | VARCHAR(20) | No | Preferred Language |
| PreferredCurrency | VARCHAR(10) | No | Preferred Currency |
| MarketingOptIn | BOOLEAN | Yes | Marketing Consent |

---

## Loyalty

| Column | Data Type | Required | Description |
|---------|-----------|----------|-------------|
| LoyaltyPoints | INT | Yes | Reward Points |

---

## Audit Information

| Column | Data Type | Required | Description |
|---------|-----------|----------|-------------|
| CreatedDate | DATETIME | Yes | Record Creation Timestamp |
| UpdatedDate | DATETIME | Yes | Last Modification Timestamp |

---

# 6. Business Rules

| Rule ID | Rule |
|----------|------|
| BR-001 | CustomerID must be unique. |
| BR-002 | Email address must be unique. |
| BR-003 | Phone number must be unique. |
| BR-004 | RegistrationDate cannot be greater than the current date. |
| BR-005 | LoyaltyPoints cannot be negative. |
| BR-006 | SegmentID must exist in the CustomerSegment table. |
| BR-007 | MarketingOptIn must contain either TRUE or FALSE. |
| BR-008 | Customer Status must be one of: Prospect, Active, Loyal, Dormant, Inactive, Blocked. |

---

# 7. Data Quality Rules

HELIX validates the following:

- Missing Customer ID
- Duplicate Customer ID
- Duplicate Email
- Duplicate Phone Number
- Invalid Email Format
- Invalid Phone Number
- Future Registration Date
- Missing Required Fields
- Invalid Segment ID
- Invalid Customer Status

---

# 8. Dirty Data Simulation

The HELIX Data Generator intentionally creates realistic data quality issues for testing purposes.

Examples include:

- Duplicate email addresses
- Duplicate phone numbers
- Missing first names
- Missing last names
- NULL gender values
- Invalid currency codes
- Future registration dates
- Incorrect customer segments
- Leading and trailing spaces
- Mixed-case email addresses

---

# 9. Downstream Dependencies

This entity is used by:

- Orders
- Payments
- Shipments
- Customer Reviews
- Support Tickets
- Loyalty Program
- Marketing Campaigns
- Enterprise Data Warehouse
- Power BI Dashboards
- AI Intelligence Engine

---

# 10. Future Enhancements

Future versions may include:

- Customer Risk Score
- Customer Lifetime Value
- Preferred Store
- Device Information
- Customer Time Zone
- Communication History
- Customer Referral Program
- AI Customer Profile

---

**End of Document**