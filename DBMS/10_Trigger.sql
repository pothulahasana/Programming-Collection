-- Trigger Example
CREATE TRIGGER update_timestamp BEFORE UPDATE ON Students FOR EACH ROW SET NEW.updated_at = NOW();
