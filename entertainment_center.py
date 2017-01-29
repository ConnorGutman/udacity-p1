# Import necessary dependencies such as fresh_tomatoes and media
import fresh_tomatoes
import media

# create several objects of class Movie to start building a database of my
# favorite films
night_on_earth = media.Movie("Night On Earth",
                             "Night On Earth tells five stories each involving"
                             " a cab ride in different cities of the world.",
                             "https://t3.gstatic.com/images?q=tbn:ANd9GcRAqGir"
                             "U1EOol_i43FAuhZB5czgTrYSx7eEwWCeVOHQ7BtcA8eP",
                             "https://www.youtube.com/watch?v=F1m6GlPyOSU")
airplane = media.Movie("Airplane!",
                       "Airplane tells the story of a crazy flight where everyth\
                       ing goes wrong in all the best ways.",
                       "https://www.gstatic.com/tv/thumb/movieposters/1671/p16"
                       "71_p_v8_ae.jpg",
                       "https://www.youtube.com/watch?v=qaXvFT_UyI8")
nausicaa = media.Movie("Nausicaa of the valley of the wind",
                       "This film tells the story of a princess from a post-apo\
                       calyptic world where the Earth has been poisoned by man\
                       kind.",
                       "https://t3.gstatic.com/images?q=tbn:ANd9GcTNOE76eD9Y4y"
                       "U6154EgXTGpmvzIunHBv5l3fNG5yuALGJgP46c",
                       "https://www.youtube.com/watch?v=6zhLBe319KE")
do_the_right_thing = media.Movie("Do the Right Thing",
                                 "Do the Right Thing tells the story of racial \
                                 divides within a community located in Bed-Stu"
                                 "y.",
                                 "https://www.gstatic.com/tv/thumb/movieposter"
                                 "s/11644/p11644_p_v8_ab.jpg",
                                 "https://www.youtube.com/watch?v=muc7xqdHudI")
primer = media.Movie("Primer",
                     "Primer tells the story of a group of scientists that crea\
                     te a reality changing device.",
                     "https://www.gstatic.com/tv/thumb/movieposters/84960/p849"
                     "60_p_v8_aa.jpg",
                     "https://www.youtube.com/watch?v=3nj5MMURCm8")
adventureland = media.Movie("Adventureland",
                            "A college student gets a summer job at Adventurel"
                            "and.",
                            "https://www.gstatic.com/tv/thumb/movieposters/191"
                            "158/p191158_p_v8_aa.jpg",
                            "https://www.youtube.com/watch?v=gfPE_MEKipM")

# create an array containing all of the movie objects I created
movies = [night_on_earth, airplane, nausicaa,
          do_the_right_thing, primer, adventureland]

# call the method open_movies_page from fresh_tomatoes and pass the array
# movies to it. This will generate a website containing all of my favorite
# movies with trailers.
fresh_tomatoes.open_movies_page(movies)
