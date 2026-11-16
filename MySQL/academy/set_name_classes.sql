USE academy;

CREATE TRIGGER set_name_classes
BEFORE INSERT ON classes
FOR EACH ROW
SET NEW.class_name = Concat(NEW.class_name, 'class');