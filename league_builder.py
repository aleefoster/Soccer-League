import csv
import sys


def create_league():
    soccer_league = list()
    with open("soccer_players.csv", newline = "\n") as csvfile:
        playerreader = csv.reader(csvfile, delimiter = ",")
        rows = list(playerreader)
        for row in rows[1:]:
            soccer_league.append(", ".join(row))
    return soccer_league


def write_team_file(sharks_team, dragons_team, raptors_team):
    with open("teams.txt", "w") as file:
        file.write("Sharks\n")
        for player in sharks_team:
            file.write(player + "\n")
        file.write("\nDragons\n")
        for player in dragons_team:
            file.write(player + "\n")
        file.write("\nRaptors\n")
        for player in raptors_team:
            file.write(player + "\n")
                       
    
def write_welcome_letter(team_name, first_practice, player_name, guardians, file_name):
    with open(file_name, "w") as file:
        file.write("Dear {},\n\n".format(guardians))
        file.write("We are pleased inform you that {} will be joining ".format(player_name)) 
        file.write("the {} team for the 2018 season.\n\n".format(team_name))
        file.write("Please plan to attend the first practice session with your child on {}.\n\n".format(first_practice))
        file.write("We are looking forward to another exciting season!\n\n")
        file.write("Thank you,\n")
        file.write("Ashton Watt\n")


def prepare_player_data(team_name, first_practice, team_roster):
    location = 0
    for player in team_roster:
        player_details = player.split(", ")
        player_name = str(player_details[0])
        guardians = str(player_details[3])
        split_player_name = player_name.split(" ")
        first_name = split_player_name[0]
        last_name = split_player_name[1]
        file_name = first_name.lower() + "_" + last_name.lower() + ".txt"
        write_welcome_letter(team_name, first_practice, player_name, guardians, file_name)
        location += 1


if __name__ == "__main__":
    # Create soccer league from CSV file
    soccer_league = create_league()
    # Separate players by experience
    experienced_players = list()
    inexperienced_players = list()
    for player in soccer_league:    
        if "YES" in player:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)

    # Create teams
    sharks_team = list()
    dragons_team = list()
    raptors_team = list()
    
    # Add three experienced and three inexperienced players    
    sharks_team.extend(experienced_players[0:3])
    sharks_team.extend(inexperienced_players[0:3])
    dragons_team.extend(experienced_players[3:6])
    dragons_team.extend(inexperienced_players[3:6])
    raptors_team.extend(experienced_players[6:])
    raptors_team.extend(inexperienced_players[6:])
    
    # Output the teams to a text file
    write_team_file(sharks_team, dragons_team, raptors_team)
    
    # Create letters for Sharks
    team_name = "Sharks"
    first_practice = "October 17th at 5:30 PM"
    prepare_player_data(team_name, first_practice, sharks_team)
    print("\n\n")
     # Create letters for Dragons
    team_name = "Dragons"
    first_practice = "October 17th at 7:00 PM"
    prepare_player_data(team_name, first_practice, dragons_team)
    print("\n\n")
     # Create letters for Raptors
    team_name = "Raptors"
    first_practice = "October 18th at 6:00 PM"
    prepare_player_data(team_name, first_practice, raptors_team)
