#requirement 1
movies = Movie.objects.all()
for movie in movies:
    movie.delete()

users = User.objects.all()
for user in users:
    user.delete()

#requirement 2
Movie.objects.create(
    title="LA Confidential",
    description="lorem ipsum",
    director="Curtis Hanson",
    release_year="1997",
    budget="$50m",
    runtime="2 hours",
    rating="R",
    genre="Mystery, Thriller" "Crime",
)

Movie.objects.create(
    title="The Shawshank Redemption",
    description="lorem ipsum",
    director="Frank Darabont",
    release_year="1994",
    budget="$85m",
    runtime="2 hours, 22 minutes",
    rating="R",
    genre="Drama, Crime",
)

Movie.objects.create(
    title="The Godfather",
    description="lorem ipsum",
    director="Francis Ford Coppola",
    release_year="1972",
    budget="$6.8m",
    runtime="2 hours, 55 minutes",
    rating="R",
    genre="Crime, Drama",
)

Movie.objects.create(
    title="The Dark Knight",
    description="lorem ipsum",
    director="Christopher Nolan",
    release_year="2008",
    budget="$185m",
    runtime="2 hours, 32 minutes",
    rating="PG-13",
    genre="Action, Crime, Thriller",
)

Movie.objects.create(
    title="Schindler's List",
    description="lorem ipsum",
    director="Steven Spielberg",
    release_year="1993",
    budget="$75m",
    runtime="3 hours, 15 minutes",
    rating="R",
    genre="Historical Drama, War",
)

Movie.objects.create(
    title="12 Angry Men",
    description="lorem ipsum",
    director="Sidney Lumet",
    release_year="1957",
    budget="$350,000",
    runtime="1 hour, 36 minutes",
    rating="NR",
    genre="Drama, Crime",
)

Movie.objects.create(
    title="Pulp Fiction",
    description="lorem ipsum",
    director="Quentin Tarantino",
    release_year="1994",
    budget="$8 million",
    runtime="2 hours, 34 minutes",
    rating="R",
    genre="Crime, Comedy",
)

Movie.objects.create(
    title="The Lord of the Rings: The Return of the King",
    description="lorem ipsum",
    director="Peter Jackson",
    release_year="2003",
    budget="$200 million",
    runtime="3 hours, 21 minutes",
    rating="PG-13",
    genre="Adventure, Fantasy, Drama",
)

Movie.objects.create(
    title="Fight Club",
    description="lorem ipsum",
    director="David Fincher",
    release_year="1999",
    budget="$63 million",
    runtime="2 hours, 11 minutes",
    rating="R",
    genre="Drama, Thriller",
)

Movie.objects.create(
    title="Inception",
    description="lorem ipsum",
    director="Christopher Nolan",
    release_year="2010",
    budget="$160 million",
    runtime="2 hours, 28 minutes",
    rating="PG-13",
    genre="Action, Thriller, Sci-Fi",
)



#requirement 3
User.objects.create(username='dtaylor', password='nmbh1234', first_name='David', last_name='Taylor', email='david@mail.com')
User.objects.create(username='sgomez', password='mnbvc1234', first_name='Sarah', last_name='Gomez', email='sarah@mail.com')
User.objects.create(username='anielsen', password='cvbnm1234', first_name='Anna', last_name='Nielsen', email='anna@mail.com')


#requirement 4
#1
qs_all = Movie.objects.all()
for movie in qs_all:
    print(movie.title)
#2
qs_the = Movie.objects.filter(title__startswith="The")
for movie in qs_the:
    print(movie.title)
#3
single_movie_get = Movie.objects.get(pk = 3)
print(single_movie_get.title)
#4
update_movie = Movie.objects.get(pk = 7)
update_movie.genre = "Crime, Comedy, Legend"
print(update_movie.genre)
#5
movie_delete = Movie.objects.get(title = "Inception")
movie_delete.delete()


#Requirement 5

user_model = User.objects.get(username = "sgomez")
print(f"Username: {user_model.username}")
print(f"First name: {user_model.first_name}")
print(f"Last name: {user_model.last_name}")
print(f"Email: {user_model.email}")