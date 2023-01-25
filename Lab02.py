def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Colin Sutherland',
        'studnet_id' : 10261370,
        'toppings' : [
            {
            'TOPPINGS_1' : 'PEPPERS',
            'TOPPINGS_2' : 'ONIONS',
            'TOPPINGS_3' : 'SPINACH'
            }
        ],
        'movie_list' : [
            {
                'name' : 'the nice guys',
                'genre' : 'comedy'

            },
            {
                'name' : 'lord of the rings: the two towers',
                'genre' : ' fantasy'

            }
        ]
    }
        

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
        'name' : 'mulan',
        'genre' : 'fantasy'
    
    }
    about_me = ['movies'].append(new_movie)
    
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ('PEPPERONI', 'PESTO'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    print(f'My name is {about_me["full_name"]}, but you can call me Sir {about_me["full_name".split[0]]}')
    print(f'My student ID is {about_me["student_id"]}')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['toppings'].extend(toppings)
    about_me['toppings'].sort(toppings)
    about_me['toppings'].lower(toppings)

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy favourite pizza toppings are:')
    for p in about_me['toppings']:
        print(f'- {p}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    print('\nI like to watch', end='')
    movie_genres = [g["gnere"]for g in about_me['movie_list']]
    movie_csl = ', '.join(movie_genres)
    print(movie_csl)
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):

    return
    
if __name__ == '__main__':
    main()