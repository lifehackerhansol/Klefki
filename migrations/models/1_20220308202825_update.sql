-- upgrade --
CREATE TABLE IF NOT EXISTS "modrole" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "guild_id" BIGINT NOT NULL REFERENCES "guild" ("id") ON DELETE CASCADE
);
-- downgrade --
DROP TABLE IF EXISTS "modrole";
