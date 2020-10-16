NONE = 0
GAMES = 1
TV = 2
MOVIES = 3
ALL = 4

TITLE = 0
TIME_SPENT = 1
EPISODES_SEEN = 1
MOVIE_RUNTIME = 1
MOVIE_CONSENSUS = 2
TV_SHOW_EPISODE_COUNT = 2
AVG_TIME_TO_COMPLETE = 2
CONSENSUS_BY_OTHERS = 3

def build_database():
    f = open("gameinput.txt", "r")
    done = False
    games = []
    tv = []
    movies = []
    current_type = NONE
    while(not done):
        s = f.readline()
        s = s.rstrip()
        if(s == ""):
           done = True
        else:
            if(s == "Games"):
                current_type = GAMES
            elif(s == "TV"):
                current_type = TV
            elif(s == "Movies"):
                current_type = MOVIES
            else:
                attribute_list = s.split(':')
                if(current_type == GAMES):
                    attributes = (
                        attribute_list[TITLE], 
                        attribute_list[TIME_SPENT], 
                        attribute_list[AVG_TIME_TO_COMPLETE],
                        attribute_list[CONSENSUS_BY_OTHERS]
                        )
                    games.append(attributes)
                elif(current_type == TV):
                    attributes = (
                        attribute_list[TITLE], 
                        attribute_list[EPISODES_SEEN], 
                        attribute_list[TV_SHOW_EPISODE_COUNT],
                        attribute_list[CONSENSUS_BY_OTHERS]
                        )
                    tv.append(attributes)
                elif(current_type == MOVIES):
                    attributes = (
                        attribute_list[TITLE], 
                        attribute_list[MOVIE_RUNTIME], 
                        attribute_list[MOVIE_CONSENSUS]
                        )
                    movies.append(attributes)
    f.close()
    return games, tv, movies         

def write_data_to_file(games, tv, movies):
    f = open("gameinput.txt", "w")
    f.write("Games" + "\n")
    for i in range(0, len(games)):
        tupleg = list(games[i])
        datastring = ""
        for j in range(0, len(tupleg)):
            datastring += tupleg[j]
            datastring += ':'
        f.write(datastring + '\n')
    f.write("TV" + "\n")
    for i in range(0, len(tv)):
        tuplet = list(tv[i])
        datastring = ""
        for j in range(0, len(tuplet)):
            datastring += tuplet[j]
            datastring += ':'
        f.write(datastring + '\n')
    f.write("Movies" + "\n")
    for i in range(0, len(movies)):
        tuplem = list(movies[i])
        datastring = ""
        for j in range(0, len(tuplem)):
            datastring += tuplem[j]
            datastring += ':'
        f.write(datastring + '\n')

def print_games(games):
    for i in range(0, len(games)):
        game_tuple = games[i]
        print("Game " + str(i + 1) + ":")
        print("\tTitle: " + str(game_tuple[TITLE]))
        print("\tTime Spent: " + str(game_tuple[TIME_SPENT]) + " Hours")
        print("\tAverage time until completion: " + str(game_tuple[AVG_TIME_TO_COMPLETE]) + " Hours")
        print("\tOverall Consensus: " + str(game_tuple[CONSENSUS_BY_OTHERS]))

def print_tv(tv):
    for i in range(0, len(tv)):
        tv_tuple = tv[i]
        print("TV Show " + str(i + 1) + ":")
        print("\tTitle: " + str(tv_tuple[TITLE]))
        print("\tEpisodes Seen: " + str(tv_tuple[EPISODES_SEEN]))
        print("\tTotal Episode Count: " + str(tv_tuple[TV_SHOW_EPISODE_COUNT]))
        print("\tOverall Consensus: " + str(tv_tuple[CONSENSUS_BY_OTHERS]))

def print_movies(movies):
    for i in range(0, len(movies)):
        movie_tuple = movies[i]
        print("Movie " + str(i + 1) + ":")
        print("\tTitle: " + str(movie_tuple[TITLE]))
        print("\tMovie Runtime " + str(movie_tuple[MOVIE_RUNTIME]) + " Hours")
        print("\tOverall Consensus: " + str(movie_tuple[MOVIE_CONSENSUS]))

def print_database(games, tv, movies):
    done = False
    selection = 0
    while(not done):
        print("Please select an option from the list to print:")
        print("[1]: GAMES")
        print("[2]: TV SHOWS")
        print("[3]: MOVIES")
        print("[4]: ALL")
        selection = int(input())
        if(selection == GAMES):
            print_games(games)
            done = True
        elif(selection == TV):
            print_tv(tv)
            done = True
        elif(selection == MOVIES):
            print_movies(movies)
            done = True
        elif(selection == ALL):
            print_games(games)
            print()
            print_tv(tv)
            print()
            print_movies(movies)
            done = True
        else:
            print("Invalid input")
    return selection

def print_main_options():
    print("[1]: Add a piece of media")
    print("[2]: Remove a piece of media")
    print("[3]: Update a piece of media")
    print("[4]: Print media")
    print("[5]: Quit")

def add_media(games, tv, movies):
    print("What type of media do you want to add?")
    print("Please select an option from the list to print:")
    print("[1]: Games")
    print("[2]: TV Shows")
    print("[3]: Movies")

    done = False
    while(not done):
        selection = int(input())
        if(selection == GAMES):
            done2 = False
            while(not done2):
                print("Please Enter The Game's Title:")
                title = input()
                print("Please Enter The Time Already Spent In The Game:")
                time_spent = input()
                print("Please Enter The Average Time To Complete The Game:")
                avg_time_to_complete = input()
                print("Please Enter The General Consensus On The Game:")
                consensus = input()
                print("The information you entered was: ")
                print("Title: " + title)
                print("Time Spent: " + time_spent)
                print("Average Time to Complete:" + avg_time_to_complete)
                print("General Consensus: " + consensus)
                print("Is this correct? If so type: YES")
                confirmation_input = input()
                if(confirmation_input == "YES"):
                    done2 = True
                    new_game = (title, time_spent, avg_time_to_complete, consensus)
                    games.append(new_game)
                    print("Would you like to enter another piece of media? If so type : YES")
                    confirmation_input = input()
                    if(confirmation_input != "YES"):
                        done = True
        elif(selection == TV):
            done2 = False
            while(not done2):
                print("Please Enter The TV Show's Title:")
                title = input()
                print("Please Enter The Number of Episodes You Have Seen:")
                episodes_seen = input()
                print("Please Enter The Total Number of Episodes:")
                episode_total = input()
                print("Please Enter The General Consensus On The TV Show:")
                consensus = input()
                print("The information you entered was: ")
                print("Title: " + title)
                print("Episodes Seen: " + episodes_seen)
                print("Number of Episodes:" + episode_total)
                print("General Consensus: " + consensus)
                print("Is this correct? If so type: YES")
                confirmation_input = input()
                if(confirmation_input == "YES"):
                    done2 = True
                    new_show = (title, episodes_seen, episode_total, consensus)
                    tv.append(new_show)
                    print("Would you like to enter another piece of media? If so type : YES")
                    confirmation_input = input()
                    if(confirmation_input != "YES"):
                        done = True
        elif(selection == MOVIES):
            done2 = False
            while(not done2):
                print("Please Enter The Movie's Title:")
                title = input()
                print("Please Enter The Runtime Of The Movie:")
                runtime = input()
                print("Please Enter The General Consensus On The Movie:")
                consensus = input()
                print("The information you entered was: ")
                print("Title: " + title)
                print("Runtime: " + runtime)
                print("General Consensus: " + consensus)
                print("Is this correct? If so type: YES")
                confirmation_input = input()
                if(confirmation_input == "YES"):
                    done2 = True
                    new_movie = (title, runtime, consensus)
                    movies.append(new_movie)
                    print("Would you like to enter another piece of media? If so type : YES")
                    confirmation_input = input()
                    if(confirmation_input != "YES"):
                        done = True

def remove_game(games):
    print_games(games)
    done = False
    while(not done):
        print("Please enter the number of the game you would like to delete")
        selection = int(input())
        if(selection < len(games) + 1 and selection != 0):
            print("Are you sure you want to remove Game " + str(selection) + "? If yes then type: YES")
            confirm = input()
            if(confirm == "YES"):
                games.pop(selection - 1)
            done = True
        else:
            print("Invalid input")
    return games

def remove_tv(tv):
    print_tv(tv)
    done = False
    while(not done):
        print("Please enter the number of the TV Show you would like to delete")
        selection = int(input())
        if(selection < len(tv) + 1 and selection != 0):
            print("Are you sure you want to remove TV Show " + str(selection) + "? If yes then type: YES")
            confirm = input()
            if(confirm == "YES"):
                tv.pop(selection - 1)
            done = True
        else:
            print("Invalid input")
    return tv

def remove_movie(movies):
    print_movies(movies)
    done = False
    while(not done):
        print("Please enter the number of the Movie you would like to delete")
        selection = int(input())
        if(selection < len(movies) + 1 and selection != 0):
            print("Are you sure you want to remove Movie " + str(selection) + "? If yes then type: YES")
            confirm = input()
            if(confirm == "YES"):
                movies.pop(selection - 1)
            done = True
        else:
            print("Invalid input")
    return movies

def remove_media(games, tv, movies):
    done = False
    while(not done):
        print("What type of media do you want to remove?")
        print("Please select an option from the list to print:")
        print("[1]: Games")
        print("[2]: TV Shows")
        print("[3]: Movies")
        selection = int(input())
        deletion_done = False
        if(selection == GAMES):
            games = remove_game(games)
            deletion_done = True
        elif(selection == TV):
            tv = remove_tv(tv)
            deletion_done = True
        elif(selection == MOVIES):
            movies = remove_movie(movies)
            deletion_done = True
        else:
            print("Invalid input")
        if(deletion_done):
            print("Would you like to delete another piece of media?")
            print("If so, type: YES")
            selection = input()
            if(input != "YES"):
                done = True

def update_game(games):
    print_games(games)
    done = False
    while(not done):
        print("Please enter the number of the game you would like to update")
        game_selection = int(input())
        if(game_selection < (len(games) + 1) and game_selection != 0):
            print("Are you sure you want to update Game " + str(game_selection) + "? If yes then type: YES")
            confirm = input()
            if(confirm == "YES"):
                update_field = False
                while(not update_field):
                    game_tuple = list(games[game_selection - 1])
                    print("What field would you like to update? Please select from the following list:")
                    print("[1]: Title")
                    print("[2]: Time Spent")
                    print("[3]: Average Time to Completion")
                    print("[4]: Overall Consensus")
                    selection = int(input()) - 1
                    if(selection == TITLE):
                        print("Please enter new Title:")
                        game_tuple[TITLE] = input()
                        update_field = True
                    elif(selection == TIME_SPENT):
                        print("Please enter any additional time spent(in hours):")
                        current_time = games[game_selection[TIME_SPENT]]
                        game_tuple[TIME_SPENT] = str(float(current_time) + float(input()))
                        update_field = True
                    elif(selection == AVG_TIME_TO_COMPLETE):
                        print("Please enter new average time to complete(in hours):")
                        game_tuple[AVG_TIME_TO_COMPLETE] = str(input())
                        update_field = True
                    elif(selection == CONSENSUS_BY_OTHERS):
                        print("Please enter new consensus:")
                        game_tuple[CONSENSUS_BY_OTHERS] = input()
                        update_field = True
                    else:
                        print("Invalid input")
                    if(update_field):
                        games[game_selection - 1] = tuple(game_tuple)
                        print("Would you like to update another field on this game?")
                        print("If so, please type: YES")
                        selection = input()
                        if(selection == "YES"):
                            update_field = False
            done = True
        else:
            print("Invalid input")
    return games

def update_tv(tv):
    print_tv(tv)
    done = False
    while(not done):
        print("Please enter the number of the TV Show you would like to update")
        tv_selection = int(input())
        if(tv_selection < (len(tv) + 1) and tv_selection != 0):
            tv_tuple = list(tv[tv_selection - 1])
            print("Are you sure you want to update TV Show " + str(tv_selection) + "? If yes then type: YES")
            confirm = input()
            if(confirm == "YES"):
                update_field = False
                while(not update_field):
                    print("What field would you like to update? Please select from the following list:")
                    print("[1]: Title")
                    print("[2]: Episodes Seen")
                    print("[3]: Total Episodes")
                    print("[4]: Overall Consensus")
                    selection = int(input())
                    if(selection == TITLE):
                        print("Please enter new Title:")
                        tv_tuple[TITLE] = input()
                        update_field = True
                    elif(selection == EPISODES_SEEN):
                        print("Please enter the number of additional episodes watched:")
                        current_eps = int(tv[tv_selection[EPISODES_SEEN]])
                        tv_tuple[TIME_SPENT] = str(current_eps + int(input()))
                        update_field = True
                    elif(selection == TV_SHOW_EPISODE_COUNT):
                        print("Please enter the new total number of episodes:")
                        tv_tuple[TV_SHOW_EPISODE_COUNT] = str(input())
                        update_field = True
                    elif(selection == CONSENSUS_BY_OTHERS):
                        print("Please enter new consensus:")
                        tv_tuple[CONSENSUS_BY_OTHERS] = input()
                        update_field = True
                    else:
                        print("Invalid input")
                    if(update_field):
                        tv[tv_selection] = tuple(tv_tuple)
                        print("Would you like to update another field on this tv show?")
                        print("If so, please type: YES")
                        selection = input()
                        if(selection == "YES"):
                            update_field = False
            done = True
        else:
            print("Invalid input")
    return tv

def update_movies(movies):
    print_movies(movies)
    done = False
    while(not done):
        print("Please enter the number of the Movie you would like to update")
        movie_selection = int(input())
        if(movie_selection < (len(movies) + 1) and movie_selection != 0):
            movie_tuple = list(movies[movie_selection - 1])
            print("Are you sure you want to update Movie " + str(movie_selection) + "? If yes then type: YES")
            confirm = input()
            if(confirm == "YES"):
                update_field = False
                while(not update_field):
                    print("What field would you like to update? Please select from the following list:")
                    print("[1]: Title")
                    print("[2]: Runtime")
                    print("[3]: Consensus")
                    selection = int(input()) - 1
                    if(selection == TITLE):
                        print("Please enter new Title:")
                        movie_tuple[TITLE] = input()
                        update_field = True
                    elif(selection == MOVIE_RUNTIME):
                        print("Please enter the new runtime of the Movie(in hours):")
                        movie_tuple[MOVIE_RUNTIME] = str(input())
                        update_field = True
                    elif(selection == MOVIE_CONSENSUS):
                        print("Please enter new consensus:")
                        movie_tuple[MOVIE_CONSENSUS] = input()
                        update_field = True
                    else:
                        print("Invalid input")
                    if(update_field):
                        movies[movie_selection - 1] = tuple(movie_tuple)
                        print("Would you like to update another field on this movie?")
                        print("If so, please type: YES")
                        selection = input()
                        if(selection == "YES"):
                            update_field = False
            done = True
        else:
            print("Invalid input")
    return movies

def update_media(games, tv, movies):
    print("What type of media do you want to update?")
    print("Please select an option from the list to print:")
    print("[1]: Games")
    print("[2]: TV Shows")
    print("[3]: Movies")
    done = False
    while(not done):
        selection = int(input())
        update_done = False
        if(selection == GAMES):
            games = update_game(games)
            update_done = True
        elif(selection == TV):
            tv = update_tv(tv)
            update_done = True
        elif(selection == MOVIES):
            movies = update_movies(movies)
            update_done = True
        else:
            print("Invalid input")
        if(update_done):
            print("Would you like to update another piece of media?")
            print("If so, type: YES")
            selection = input()
            if(input != "YES"):
                done = True

def main():
    games = []
    tv = []
    movies = []
    games, tv, movies = build_database()
    done = False

    while(not done):
        print_main_options()
        print("Please select an option from the list:")
        selection = int(input())
        if(selection == 1):
            add_media(games, tv, movies)
        elif(selection == 2):
            remove_media(games, tv, movies)
        elif(selection == 3):
            update_media(games, tv, movies)
        elif(selection == 4):
            print_database(games, tv, movies)
        elif(selection == 5):
            write_data_to_file(games, tv, movies)
            done = True
        else:
            print("Invalid input")
        
main()