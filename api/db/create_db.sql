BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Roads" (
	"id"	INTEGER NOT NULL UNIQUE,
	"road_name"	        TEXT NOT NULL,
	"last_updated"	    DATETIME NOT NULL,
	"event_count"       INTEGER NOT NULL,
	FOREIGN KEY("road_name") REFERENCES "Roads"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);


CREATE TABLE IF NOT EXISTS "LaneLocations" (
	"id"	            INTEGER NOT NULL UNIQUE,
	"road_name"	        TEXT NOT NULL,
	"km"                INTEGER NOT NULL,
	"lane"              INTEGER NOT NULL,
	"carriage_way"      TEXT NOT NULL,
	"uuid"              TEXT NOT NULL,
	FOREIGN KEY("road_name") REFERENCES "Roads"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Events" (
    "id"	            INTEGER NOT NULL UNIQUE,
    "road_name"	        TEXT NOT NULL,
    "avg_speed"         TEXT NOT NULL,
    "flow_count"        TEXT NOT NULL,
    "ts_event"          DATETIME NOT NULL,
    "uuid"              TEXT NOT NULL,
    FOREIGN KEY ("uuid") REFERENCES "LaneLocations"("uuid"),
    FOREIGN KEY("road_name") REFERENCES "Roads"("id"),
    PRIMARY KEY("id" AUTOINCREMENT)
);