-- Create keyspace
CREATE KEYSPACE auth
WITH replication = {'class': 'NetworkTopologyStrategy', 'datacenter1': 3};

-- Use keyspace
USE auth;

-- Create user table
CREATE TABLE user (
user_id text,
username text,
email text,
password_hash text,
created_at timestamp,
updated_at timestamp,
enabled boolean,
verified boolean,
PRIMARY KEY (user_id)
);

-- Create user_by_username table
CREATE TABLE user_by_username (
username text,
user_id text,
email text,
created_at timestamp,
PRIMARY KEY (username)
);

-- Create user_by_email table
CREATE TABLE user_by_email (
email text,
user_id text,
username text,
created_at timestamp,
PRIMARY KEY (email)
);

-- Create user_role table
CREATE TABLE user_role (
user_id text,
role_id text,
granted_at timestamp,
PRIMARY KEY (user_id, role_id)
);

-- Create role table
CREATE TABLE role (
role_id text,
name text,
description text,
created_at timestamp,
updated_at timestamp,
PRIMARY KEY (role_id)
);

-- Create permission table
CREATE TABLE permission (
permission_id text,
name text,
description text,
created_at timestamp,
updated_at timestamp,
PRIMARY KEY (permission_id)
);

-- Create role_permission table
CREATE TABLE role_permission (
role_id text,
permission_id text,
granted_at timestamp,
PRIMARY KEY (role_id, permission_id)
);

-- Create user_session table
CREATE TABLE user_session (
session_id text,
user_id text,
created_at timestamp,
expires_at timestamp,
last_accessed_at timestamp,
user_agent text,
ip_address text,
PRIMARY KEY (session_id)
);

-- Create user_session_by_user table
CREATE TABLE user_session_by_user (
user_id text,
session_id text,
created_at timestamp,
expires_at timestamp,
PRIMARY KEY (user_id, created_at)
) WITH CLUSTERING ORDER BY (created_at DESC);

-- Create user_login_history table
CREATE TABLE user_login_history (
user_id text,
login_timestamp timestamp,
ip_address text,
user_agent text,
status text,
PRIMARY KEY (user_id, login_timestamp)
) WITH CLUSTERING ORDER BY (login_timestamp DESC);

-- Create user_failed_login_attempts table
CREATE TABLE user_failed_login_attempts (
user_id text,
attempt_timestamp timestamp,
ip_address text,
user_agent text,
reason text,
PRIMARY KEY (user_id, attempt_timestamp)
) WITH CLUSTERING ORDER BY (attempt_timestamp DESC);

-- Create password_reset_token table
CREATE TABLE password_reset_token (
token text,
user_id text,
created_at timestamp,
expires_at timestamp,
used boolean,
PRIMARY KEY (token)
);