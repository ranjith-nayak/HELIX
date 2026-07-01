# Customer Table Design

## Table Name

Customer

---

## Purpose

Stores the identity of every registered customer within AstraNova Global.

The Customer table represents the master record for each customer and serves as the parent entity for customer-related operations such as addresses, loyalty, orders, reviews, support tickets, and marketing preferences.

---

## Primary Key

CustomerID

Format:

CUS000001

Example:

CUS000001

---

## Parent Tables

CustomerSegment

---

## Child Tables

CustomerAddress

CustomerLoyalty

Orders

CustomerPreference

CustomerReview

SupportTicket

---

## Business Rules

- Every customer belongs to exactly one customer segment.
- Every customer must have a unique email address.
- Every customer must have a unique phone number.
- Customer registration date cannot be in the future.
- Customer status must come from predefined values.
- Customer cannot exist without a valid customer segment.

---