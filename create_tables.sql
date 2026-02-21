CREATE DATABASE youtube_project;

USE youtube_project;

CREATE TABLE channel_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    channel_name VARCHAR(255),
    subscribers BIGINT,
    total_views BIGINT,
    total_videos INT,
    collected_at DATETIME
);

SELECT * FROM channel_stats;
