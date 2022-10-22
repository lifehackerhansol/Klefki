drop table if exists guilds;
drop table if exists modroles;
drop table if exists warns;


create table guilds
(
	id BIGINT PRIMARY KEY,
	mute_id BIGINT
);


create table modroles
(
	id BIGINT PRIMARY KEY,
	guild_id BIGINT NOT NULL REFERENCES guilds(id)
);


create table warns
(
	id BIGINT PRIMARY KEY,
	user_id BIGINT NOT NULL,
	issuer_id BIGINT NOT NULL,
    guild_id BIGINT NOT NULL REFERENCES guilds(id),
	reason TEXT
);

