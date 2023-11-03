-- Change the default character set and collation of the database
ALTER DATABASE hbtn_0c_0
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Change the table's character set and collation
ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change the character set and collation of the name field
ALTER TABLE first_table
  MODIFY name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
