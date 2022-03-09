-- upgrade --
CREATE TABLE IF NOT EXISTS "muterole" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "guild_id" BIGINT NOT NULL REFERENCES "guild" ("id") ON DELETE CASCADE
);
-- downgrade --
DROP TABLE IF EXISTS "muterole";
