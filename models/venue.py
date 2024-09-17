from db.connection import get_connection, get_cursor

class Venue:
    @staticmethod
    def concerts(venue_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT concerts.* FROM concerts
        WHERE concerts.venue_id = ?
        """
        cursor.execute(sql, (venue_id,))
        return cursor.fetchall()

    @staticmethod
    def bands(venue_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT DISTINCT bands.* FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        """
        cursor.execute(sql, (venue_id,))
        return cursor.fetchall()

    @staticmethod
    def concert_on(venue_id, date):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT * FROM concerts
        WHERE venue_id = ? AND date = ?
        LIMIT 1
        """
        cursor.execute(sql, (venue_id, date))
        return cursor.fetchone()

    @staticmethod
    def most_frequent_band(venue_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT bands.*, COUNT(concerts.id) as performance_count FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY performance_count DESC
        LIMIT 1
        """
        cursor.execute(sql, (venue_id,))
        return cursor.fetchone()
