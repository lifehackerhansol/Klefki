-- upgrade --
ALTER TABLE "guild" ADD "autorole" INT NOT NULL  DEFAULT 0;
-- downgrade --
ALTER TABLE "guild" DROP COLUMN "autorole";
