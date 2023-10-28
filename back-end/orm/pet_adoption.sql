CREATE TABLE "animals" (
  "id" char(64) PRIMARY KEY NOT NULL,
  "name" varchar(100) NOT NULL,
  "species" varchar(100) NOT NULL,
  "brithdate" timestamp NOT NULL,
  "location" varchar(300) NOT NULL,
  "gender" char(1) NOT NULL,
  "breed" varchar(50),
  "color" varchar(50),
  "sterilization" bool NOT NULL,
  "vaccination" bool NOT NULL,
  "story" varchar(3000),
  "character" varchar(500),
  "wishes" varchar(500),
  "salt" char(32) NOT NULL,
  "status" varchar(5) NOT NULL DEFAULT 'In',
  "shelter_name" varchar(100) NOT NULL
);

CREATE TABLE "users" (
  "hashed_email" char(64) PRIMARY KEY NOT NULL,
  "hashed_password" char(64) NOT NULL,
  "salt" char(32) NOT NULL,
  "encrypted_first_name" varchar(300) NOT NULL,
  "encrypted_last_name" varchar(300) NOT NULL,
  "encrypted_private_key" varchar(300),
  "encrypted_phone" varchar(50) NOT NULL,
  "encrypted_location" varchar(300),
  "verified_email" bool NOT NULL,
  "verified_phone_number" bool NOT NULL,
  "two_factor_authentication" bool NOT NULL,
  "registration" timestamp NOT NULL
);

CREATE TABLE "shelters" (
  "name" varchar(100) PRIMARY KEY NOT NULL,
  "email" varchar(100) NOT NULL,
  "hashed_password" char(64) NOT NULL,
  "salt" char(32) NOT NULL,
  "encrypted_private_key" varchar(300) NOT NULL,
  "phone" varchar(9) NOT NULL,
  "location" varchar(300) NOT NULL,
  "head_first_name" varchar(300) NOT NULL,
  "head_last_name" varchar(300) NOT NULL,
  "verified_email" bool NOT NULL,
  "verified_phone_number" bool NOT NULL,
  "registration" timestamp NOT NULL
);

CREATE TABLE "email_verification" (
  "proof_of_authority" varchar(100) PRIMARY KEY NOT NULL,
  "email_proof" char(64) NOT NULL,
  "expiration_at" timestamp NOT NULL,
  "used" bool NOT NULL DEFAULT false
);

CREATE TABLE "phone_verification" (
  "proof_of_authority" varchar(100) PRIMARY KEY NOT NULL,
  "phone_proof" char(64) NOT NULL,
  "expiration_at" timestamp NOT NULL,
  "used" bool NOT NULL DEFAULT false
);

ALTER TABLE "animals" ADD FOREIGN KEY ("shelter_name") REFERENCES "shelters" ("name");
