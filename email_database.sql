DROP TABLE IF EXISTS users;

-- users table
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    mail_address VARCHAR(100) UNIQUE
);



-- mail_info table
CREATE TABLE IF NOT EXISTS mail_info (
    sender VARCHAR(50),
    receiver VARCHAR(50),
    title VARCHAR(100),
    subject VARCHAR(100),
	message_data VARCHAR(500),
    send_date DATE
);



-- valid_mails tablosunu mail kolonunu email olarak değiştirdik
CREATE TABLE IF NOT EXISTS valid_mails (
    email VARCHAR(250) UNIQUE
);

-- valid_mails tablosuna veri ekleme
INSERT INTO valid_mails (email) VALUES
    ('metehan@mail.com'),
    ('irem@mail.com'),
    ('kaan@mail.com'),
    ('duru@mail.com'),
    ('ahsen@mail.com');

INSERT INTO users (username, password) VALUES
    ('MetehanK', 'Metehan.1602'),
    ('Irem', 'Irem1'),
    ('Kaan', 'Kaan'),
    ('Duru', 'Duru'),
    ('Ahsen', 'Ahsen');

SELECT * FROM mail_info;

