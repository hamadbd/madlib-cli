import re
print('************************************')
print('Welcome to Madlib game ')
print('Madlib game its maybe funny game ')
print('please answer the questions')
print('************************************')
# path_2 = 'assets/make_me_a_video_game_template'



# path = 'assets/dark_and_stormy_night_template'
regex = r'\{(.*?)}'


def read_template(path_2):
    try:
        with open(path_2, 'r') as file:
            content_inside_file = file.read()
        return content_inside_file
    except FileNotFoundError as err:
        raise err

print('________________________________________________________________________________________________________________________________')

def parse_template(string):
    matches =tuple(re.findall(regex, string))
    new_string = re.sub(regex, '{}', string)
    return new_string,matches


def merge(string, tuple):
    new_string = parse_template(string)[0]
    # print(new_string.format(tuple))
    return new_string.format(*tuple)

def show_game (path_2):
    Adjective_one = input('Please Enter an Adjective_one : ')
    Adjective_two = input('Please Enter an Adjective_two: ')
    A_First_Name_one = input('Please Enter an A_First_Name_one: ')
    Past_tens_verb = input('Please Enter an Past_tens_verb:')
    A_First_Name_two = input('Please Enter an A_First_Name_two: ')
    Adjective_three = input('Please Enter an Adjective_three: ')
    Adjective_four = input('Please Enter an Adjective_four: ')
    Plural = input('Please Enter an Plural: ')
    Large_Animal = input('Please Enter an Large_Animal: ')
    Small_Animal = input('Please Enter an Small_Animal: ')
    A_girls_Name = input('Please Enter an A_girls_Name: ')
    Adjective_five = input('Please Enter an Adjective_five: ')
    Plural_two = input('Please Enter an Plural_two: ')
    Adjective_six = input('Please Enter an Adjective_six: ')
    Plural_three = input('Please Enter an Plural_three: ')
    Number_from_1_50 = input('Please Enter an Number_from_1_50: ')
    A_First_Name_three = input('Please Enter an A_First_Name_three: ')
    Number = input('Please Enter an Number: ')
    Plural_four = input('Please Enter an Plural_four: ')
    Number_two = input('Please Enter an Number_two: ')
    Plural_five = input('Please Enter an Plural_five: ')

    user_input = (Adjective_one, Adjective_two, A_First_Name_one, Past_tens_verb, A_First_Name_two, Adjective_three, Adjective_four, Plural, Large_Animal, Small_Animal, A_girls_Name,Adjective_five, Plural_two, Adjective_six, Plural_three, Number_from_1_50, A_First_Name_three, Number, Plural_four, Number_two, Plural_five)

    r = read_template(path_2)
    p = parse_template(r)[0]
    m = merge(p, user_input)
    return m



def copy_file():

    new_file = show_game('./assets/make_me_a_video_game_template')
    with open('./assets/copy_file', 'a') as f:
        f.write(new_file)
    print(new_file)


copy_file()

print('________________________________________________________________________________________________________________________________')

