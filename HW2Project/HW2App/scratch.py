qs_movie = Movie.objects.all()
for movie in qs_movie:
    movie.delete

qs_user = User.objects.all()
for user in qs_user:
    user.delete

