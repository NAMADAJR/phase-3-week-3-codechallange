from models.band import Band
from models.venue import Venue
from models.concert import Concert

# Example: List all concerts for a band
band_concerts = Band.concerts(band_id=1)
print(band_concerts)

# Example: Play in a venue
Band.play_in_venue(band_id=1, venue_id=2, date='2024-09-10')

# Example: Get all introductions for a band
introductions = Band.all_introductions(band_id=1)
print(introductions)

# Example: Find the most frequent band at a venue
frequent_band = Venue.most_frequent_band(venue_id=1)
print(frequent_band)
