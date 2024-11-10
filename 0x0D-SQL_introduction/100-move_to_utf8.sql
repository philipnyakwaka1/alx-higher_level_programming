-- convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- SHOW VARIABLES LIKE 'character_set%';
-- SHOW VARIABLES LIKE 'collation%';
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;