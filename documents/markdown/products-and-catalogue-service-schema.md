-- Create keyspace
CREATE KEYSPACE product_catalogue
WITH replication = {'class': 'NetworkTopologyStrategy', 'datacenter1': 3};

-- Use keyspace
USE product_catalogue;

-- Create product table
CREATE TABLE product (
product_id text,
name text,
description text,
price decimal,
category text,
brand text,
created_at timestamp,
updated_at timestamp,
available boolean,
quantity int,
tags set<text>,
attributes map<text, text>,
PRIMARY KEY (product_id)
);

-- Create product_by_category table
CREATE TABLE product_by_category (
category text,
product_id text,
name text,
price decimal,
created_at timestamp,
PRIMARY KEY ((category), created_at, product_id)
) WITH CLUSTERING ORDER BY (created_at DESC);

-- Create product_by_brand table
CREATE TABLE product_by_brand (
brand text,
product_id text,
name text,
price decimal,
created_at timestamp,
PRIMARY KEY ((brand), created_at, product_id)
) WITH CLUSTERING ORDER BY (created_at DESC);

-- Create product_by_name table
CREATE TABLE product_by_name (
name text,
product_id text,
category text,
price decimal,
created_at timestamp,
PRIMARY KEY ((name), created_at, product_id)
) WITH CLUSTERING ORDER BY (created_at DESC);

-- Create product_by_tag table
CREATE TABLE product_by_tag (
tag text,
product_id text,
name text,
category text,
price decimal,
created_at timestamp,
PRIMARY KEY ((tag), created_at, product_id)
) WITH CLUSTERING ORDER BY (created_at DESC);

-- Create product_price_range table
CREATE TABLE product_price_range (
price_range text,
product_id text,
name text,
category text,
price decimal,
created_at timestamp,
PRIMARY KEY ((price_range), price, created_at, product_id)
) WITH CLUSTERING ORDER BY (price ASC, created_at DESC);

-- Create product_attribute table
CREATE TABLE product_attribute (
attribute_key text,
attribute_value text,
product_id text,
name text,
category text,
price decimal,
created_at timestamp,
PRIMARY KEY ((attribute_key, attribute_value), created_at, product_id)
) WITH CLUSTERING ORDER BY (created_at DESC);

-- Create category table
CREATE TABLE category (
category_id text,
name text,
description text,
parent_category_id text,
created_at timestamp,
updated_at timestamp,
PRIMARY KEY (category_id)
);

-- Create brand table
CREATE TABLE brand (
brand_id text,
name text,
description text,
created_at timestamp,
updated_at timestamp,
PRIMARY KEY (brand_id)
);