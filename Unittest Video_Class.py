import unittest
from Video_Class import Video

class TestVideo(unittest.TestCase):

    def test_constructor(self):
        video = Video("Kill Bill: Volume 1", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        result = video.name
        self.assertEqual(result, 'Kill Bill: Volume 1')

        result = video.year
        self.assertEqual(result, 2003)

        result = video.director
        self.assertEqual(result, 'Quentin Tarantino')

        result = video.rating
        self.assertEqual(result, 8.2)

        result = video.genre
        self.assertEqual(result, 'Action')

        result = video.rentalStatus
        self.assertEqual(result, 'Unrented')

    def test_getName(self):
        video = Video("Kill Bill: Volume 1", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        result = video.getName()
        self.assertEqual(result, 'Kill Bill: Volume 1')

    def test_getYear(self):
        video = Video("Kill Bill: Volume 1", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        result = video.getYear()
        self.assertEqual(result, 2003)

    def test_getDirector(self):
        video = Video("Kill Bill: Volume 1", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        result = video.getDirector()
        self.assertEqual(result, 'Quentin Tarantino')

    def test_getRating(self):
        video = Video("Kill Bill: Volume 1", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        result = video.getRating()
        self.assertEqual(result, 8.2)

    def test_getGenre(self):
        video = Video("Kill Bill: Volume 1", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        result = video.getGenre()
        self.assertEqual(result, 'Action')

    def test_getRentalStatus(self):
        video = Video("Kill Bill: Volume 1", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        result = video.getRentalStatus()
        self.assertEqual(result, 'Unrented')

    def test_editName(self):
       video = Video("Kill Bill: Volume 1", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
       new_name = "Alien"
       video.editName(new_name)
       self.assertEqual(video.name, "Alien")

    def test_editYear(self):
        video = Video("Alien", 2003, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        new_year = 1979
        video.editYear(new_year)
        self.assertEqual(video.year, 1979)

    def test_editDirector(self):
        video = Video("Alien", 1979, "Quentin Tarantino",
                      8.2, "Action", "Unrented")
        new_director = "Ridley Scott"
        video.editDirector(new_director)
        self.assertEqual(video.director, "Ridley Scott")

    def test_editRating(self):
        video = Video("Alien", 1979, "Ridley Scott",
                      8.2, "Action", "Unrented")
        new_rating = 8.5
        video.editRating(new_rating)
        self.assertEqual(video.rating, 8.5)

    def test_editGenre(self):
        video = Video("Alien", 1979, "Ridley Scott",
                      8.5, "Action", "Unrented")
        new_genre = "Horror"
        video.editGenre(new_genre)
        self.assertEqual(video.genre, "Horror")

    def test_editRentalStatus(self):
        video = Video("Alien", 1979, "Ridley Scott",
                      8.5, "Horror", "Unrented")
        new_rentalStatus = "Rented"
        video.editRentalStatus(new_rentalStatus)
        self.assertEqual(video.rentalStatus, "Rented")



if __name__ == '__main__':
    unittest.main()
