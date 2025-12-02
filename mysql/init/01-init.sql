-- Super Club 数据库初始化脚本
-- 此脚本在 MySQL 容器首次启动时自动执行

-- 设置字符集
SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

-- 确保数据库使用正确的字符集
ALTER DATABASE super_club CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- 注意：表结构由 SQLAlchemy 自动创建，这里只做一些初始化配置
-- 如果需要预置数据，可以在这里添加 INSERT 语句

