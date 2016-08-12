import media
import fresh_tomatoes

# Creating instaces of the Movie class to hold information about each movie.
THE_MATRIX = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his"
                     " reality and his role in the war against its controllers.",
                     "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

MALLRATS = media.Movie("Mallrats",
                     "Both dumped by their girlfriends, two best friends seek refuge in the local mall.",
                     "http://ia.media-imdb.com/images/M/MV5BMTE5OTkxOTI1Ml5BMl5BanBnXkFtZTcwNjk2MTEzMQ@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=kwdBmG1VGZg")

CLERKS = media.Movie("Clerks",
                     "A day in the lives of two convenience clerks named Dante and Randal as they annoy"
                     " customers, discuss movies, and play hockey on the store roof.",
                     "http://ia.media-imdb.com/images/M/MV5BNzE1Njk0NmItNDhlMC00ZmFlLWI4ZTUtYTY4ZjgzNjkyMTU1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=Mlfn5n-E2WE")

BRAVEHEART = media.Movie("Braveheart",
                     "When his secret bride is executed for assaulting an English soldier who tried to"
                     " rape her, William Wallace begins a revolt against King Edward I of England.",
                     "http://ia.media-imdb.com/images/M/MV5BNjA4ODYxMDU3Nl5BMl5BanBnXkFtZTcwMzkzMTk3OA@@._V1_.jpg",
                     "hhttps://www.youtube.com/watch?v=1cnoM8EiGGU")

ALIEN = media.Movie("Alien",
                     "After a space merchant vessel perceives an unknown transmission as distress call,"
                     " their landing on the source planet finds one of the crew attacked by a"
                     " mysterious lifeform. Continuing their journey back to Earth with the"
                     " attacked crew having recovered and the critter deceased, they soon realize"
                     " that its life cycle has merely begun.",
                     "http://ia.media-imdb.com/images/M/MV5BNDNhN2IxZWItNGEwYS00ZDNhLThiM2UtODU3NWJlZjBkYjQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,681,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=LjLamj-b0I8")

PROMETHEUS = media.Movie("Prometheus",
                     "Following clues to the origin of mankind a team journey across the universe"
                     " and find a structure on a distant planet containing a monolithic statue of"
                     " a humanoid head and stone cylinders of alien blood but they soon find they"
                     " are not alone.",
                     "http://ia.media-imdb.com/images/M/MV5BMTY3NzIyNTA2NV5BMl5BanBnXkFtZTcwNzE2NjI4Nw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=sftuxbvGwiU")

WHAT_ABOUT_BOB = media.Movie("What About Bob",
                     "A successful psychotherapist loses his mind after one of his most dependent"
                     " patients, a manipulative, obsessively compulsive narcissist, tracks him down"
                     " during his family vacation.",
                     "http://ia.media-imdb.com/images/M/MV5BMTQxMjU2ODk4N15BMl5BanBnXkFtZTgwODQzNTcxMTE@._V1_.jpg",
                     "https://www.youtube.com/watch?v=ptmP1lziJw4")

FRIDAY = media.Movie("Friday",
                     "Two homies, Smokey and Craig, smoke a dope dealer's weed and try to figure a"
                     " way to get the $200 they owe to the dealer by 10pm that same night. In that"
                     " time, they smoke more weed and get jacked and shot at in a drive-by.",
                     "http://ia.media-imdb.com/images/M/MV5BMTQ1NzE3MzY0NV5BMl5BanBnXkFtZTYwNTM2MzE5._V1_.jpg",
                     "https://www.youtube.com/watch?v=umvFBoLOOgo")

THE_WATERBOY = media.Movie("Waterboy",
                     "A waterboy for a college football team discovers he has a unique tackling ability"
                     " and becomes a member of the team.",
                     "http://ia.media-imdb.com/images/M/MV5BMTcxODM0MzI5MF5BMl5BanBnXkFtZTcwNzE2MzQyMQ@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=z8yv9eq5s14")

# Adding movie instances to a list
movies = [
    THE_MATRIX,
    MALLRATS,
    CLERKS,
    BRAVEHEART,
    ALIEN,
    PROMETHEUS,
    WHAT_ABOUT_BOB,
    FRIDAY,
    THE_WATERBOY
]

# This magically generates a web page that will display all of the movies defined above
fresh_tomatoes.open_movies_page(movies)
