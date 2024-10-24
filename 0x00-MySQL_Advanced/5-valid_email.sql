-- SQL script that creates a trigger that resets
DELIMITER $$
CREATE TRIGGER email_track
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END $$
DELIMITER;
