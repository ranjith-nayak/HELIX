USE AstraNova_OLTP;

INSERT INTO CustomerSegment
(
    SegmentID,
    SegmentName,
    Description,
    MinLifetimeValue,
    MaxLifetimeValue,
    IsActive
)

VALUES

(
'SEG001',
'Prospect',
'Registered customer with no completed purchases.',
0,
0,
TRUE
),

(
'SEG002',
'Standard',
'Regular customer with normal purchasing behaviour.',
0.01,
49999.99,
TRUE
),

(
'SEG003',
'Premium',
'High-value customer with significant lifetime spending.',
50000,
199999.99,
TRUE
),

(
'SEG004',
'Enterprise',
'Corporate or business customer.',
200000,
NULL,
TRUE
),

(
'SEG005',
'Partner',
'Strategic partner organization.',
NULL,
NULL,
TRUE
);