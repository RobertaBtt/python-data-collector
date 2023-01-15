CREATE TABLE IF NOT EXISTS  "transactions" (
	"id"	INTEGER NOT NULL UNIQUE,
	"job_id"	INTEGER NOT NULL,
	"uuid"	TEXT NOT NULL,
	"timestamp"	TEXT NOT NULL,
	"driver_id"	INTEGER NOT NULL,
	"driver_name"	TEXT,
	"amount_total"	REAL NOT NULL,
	"amount_driver"	REAL NOT NULL,
	"distance"	REAL NOT NULL,
	"time_spent"	REAL NOT NULL,
	"amount_currency"	TEXT NOT NULL,
	"distance_unit"	TEXT NOT NULL,
	"time_spent_unit"	TEXT NOT NULL,
	"original_json"	BLOB NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
