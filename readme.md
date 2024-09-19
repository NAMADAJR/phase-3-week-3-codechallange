# Concert Management System

This project is a simple concert management system that tracks bands, venues, and concerts using an SQLite database. It allows users to manage concert data, including band performances, venue details, and concert scheduling.

## Features

- List all concerts for a band.
- Record a band's performance at a venue.
- Retrieve introductions for a band at a concert.
- Find the most frequent band at a venue.
- Check if a concert is in the band's hometown.

## Requirements

- Python 3.x
- SQLite (included with Python standard library)


# Usage
To run the application, execute the main.py script:
```
python main.py
```

### Example Usage
List all concerts for a band:
```
band_concerts = Band.concerts(band_id=1)
```

Play in a venue:
```
Band.play_in_venue(band_id=1, venue_id=2, date='2024-09-10')
```

Get all introductions for a band:
```
introductions = Band.all_introductions(band_id=1)
```

Find the most frequent band at a venue:
```
frequent_band = Venue.most_frequent_band(venue_id=1)
```

## Contributing
Contributions are welcome!

 Please fork the repository and create a pull request for any improvements or bug fixes.

## Acknowledgments
- SQLite for the lightweight database.
- Python for its simplicity and versatility.

## License

MIT License

Copyright (c) [2024] [Namada Junior]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.








