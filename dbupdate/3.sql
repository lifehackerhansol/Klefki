-- V3: add invite filter table

create table invitefilter
(
	id BIGINT PRIMARY KEY,
	guild_id BIGINT NOT NULL REFERENCES guilds(id),
    invite TEXT,
    alias TEXT
);
