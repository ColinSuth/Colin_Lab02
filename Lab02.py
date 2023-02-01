def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Colin Sutherland',
        'student_id' : 10261370,
        'toppings' : ['PEPPERS', 'ONIONS', 'SPINACH'],
        'movie_list' : [
            {
                'name' : 'the nice guys',
                'genre' : 'comedy'

            },
            {
                'name' : 'lord of the rings: the two towers',
                'genre' : 'fantasy'

            }
        ]
    }
        

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
        'name' : 'mulan',
        'genre' : 'animated'
    }
    about_me['movie_list'].append(new_movie)
    
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ('PEPPERONI', 'PESTO'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['movie_list'])
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print(f'My name is {about_me["full_name"]}, but you can call me Sir {about_me["full_name"].split()[0]}')
    print(f'My student ID is {about_me["student_id"]}')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    print('\nMy favourite pizza toppings are:')
    for p in about_me['toppings']:
        print(f'- {p}')
    about_me['toppings'].extend(toppings)
    about_me['toppings'].sort()
    about_me['toppings'] = [x.lower() for x in about_me['toppings']]
   
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy favourite pizza toppings are:')
    for p in about_me['toppings']:
        print(f'- {p}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    print('\nI like to watch ', end='')
    movie_genres = [g["genre"]for g in about_me['movie_list']]
    n = len(movie_genres)
    if n == 1:
        print(f'{movie_genres[0]} movies')
        return
    else:
        movie_csl = ', '.join(movie_genres[:-1])
        print(f'{movie_csl} and {movie_genres[-1]} movies.')
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print('\nSome of my favourite movies are ', end='')
    movie_title = [y['name'].title() for y in movie_list]
    n = len(movie_title)
    if n == 1:
        print(f'{movie_title[0]}!')
        return
    else:
        movie_csl = ', '.join(movie_title[:-1])
        print(f'{movie_csl} and {movie_title[-1]}!')
    return
    
if __name__ == '__main__':
    main()