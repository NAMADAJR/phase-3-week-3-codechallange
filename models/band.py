from db.connections import get_connection, get_cursor

class Band:
    
    @staticmethod
    def play_in_venue(band_id, venue_id, date):
        connection = get_connection()
        cursor = get_cursor(connection)
        
        try:
            # Check if the concert already exists
            cursor.execute("SELECT * FROM concerts WHERE band_id = ? AND venue_id = ? AND date = ?", (band_id, venue_id, date))
            if cursor.fetchone() is None:  # If no record is found
                cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (band_id, venue_id, date))
                connection.commit()
                print("Concert added.")
            else:
                print("Concert already exists.")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def concerts(band_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT concerts.* FROM concerts
        WHERE concerts.band_id = ?
        """
        cursor.execute(sql, (band_id,))
        return cursor.fetchall()

    @staticmethod
    def venues(band_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT DISTINCT venues.* FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?
        """
        cursor.execute(sql, (band_id,))
        return cursor.fetchall()

    @staticmethod
    def play_in_venue(band_id, venue_id, date):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (band_id, venue_id, date))
        connection.commit()

    @staticmethod
    def all_introductions(band_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT venues.city, bands.name, bands.hometown FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE bands.id = ?
        """
        cursor.execute(sql, (band_id,))
        concerts = cursor.fetchall()
        return [f"Hello {concert['city']}!!!!! We are {concert['name']} and we're from {concert['hometown']}" for concert in concerts]

    @staticmethod
    def most_performances():
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT bands.*, COUNT(concerts.id) as performance_count FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        GROUP BY bands.id
        ORDER BY performance_count DESC
        LIMIT 1
        """
        cursor.execute(sql)
        return cursor.fetchone()
