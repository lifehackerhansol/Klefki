-- upgrade --
ALTER TABLE "guild" ADD "mb2" INT NOT NULL  DEFAULT 0;
ALTER TABLE "guild" ADD "xyd" INT NOT NULL  DEFAULT 0;
-- downgrade --
ALTER TABLE "guild" DROP COLUMN "mb2";
ALTER TABLE "guild" DROP COLUMN "xyd";
