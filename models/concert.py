from db.connections import get_connection, get_cursor

class Concert:
    @staticmethod
    def band(concert_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT bands.* FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.id = ?
        """
        cursor.execute(sql, (concert_id,))
        return cursor.fetchone()

    @staticmethod
    def venue(concert_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT venues.* FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        cursor.execute(sql, (concert_id,))
        return cursor.fetchone()

    @staticmethod
    def hometown_show(concert_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT bands.hometown, venues.city FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        cursor.execute(sql, (concert_id,))
        result = cursor.fetchone()
        return result['hometown'] == result['city']

    @staticmethod
    def introduction(concert_id):
        connection = get_connection()
        cursor = get_cursor(connection)
        sql = """
        SELECT bands.name, bands.hometown, venues.city FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        cursor.execute(sql, (concert_id,))
        result = cursor.fetchone()
        return f"Hello {result['city']}!!!!! We are {result['name']} and we're from {result['hometown']}"
