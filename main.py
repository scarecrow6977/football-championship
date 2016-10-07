import random
from prettytable import PrettyTable


def _play_championship(team_list):
    for i in range(len(team_list)):
        for j in range(i + 1, len(team_list)):
            score = (random.randint(0,6), random.randint(0,6))
            if score[0] == score[1]:
                team_list[i]['fullscore'] += 1
                team_list[i]['num of draws'] += 1
                team_list[i]['scored goals'] += score[0]
                team_list[i]['passed goals'] += score[1]
                team_list[i]['games'][team_list[j]['name']] = score

                team_list[j]['fullscore'] += 1
                team_list[j]['num of draws'] += 1
                team_list[j]['scored goals'] += score[1]
                team_list[j]['passed goals'] += score[0]
                team_list[j]['games'][team_list[i]['name']] = score[::-1]
            elif score[0] > score[1]:
                team_list[i]['fullscore'] += 3
                team_list[i]['num of wins'] += 1
                team_list[i]['scored goals'] += score[0]
                team_list[i]['passed goals'] += score[1]
                team_list[i]['games'][team_list[j]['name']] = score

                team_list[j]['fullscore'] += 0
                team_list[j]['num of loss'] += 1
                team_list[j]['scored goals'] += score[1]
                team_list[j]['passed goals'] += score[0]
                team_list[j]['games'][team_list[i]['name']] = score[::-1]
            else:
                team_list[i]['fullscore'] += 0
                team_list[i]['num of loss'] += 1
                team_list[i]['scored goals'] += score[0]
                team_list[i]['passed goals'] += score[1]
                team_list[i]['games'][team_list[j]['name']] = score

                team_list[j]['fullscore'] += 3
                team_list[j]['num of wins'] += 1
                team_list[j]['scored goals'] += score[1]
                team_list[j]['passed goals'] += score[0]
                team_list[j]['games'][team_list[i]['name']] = score[::-1]
    team_list.sort(key=lambda d: d['fullscore'], reverse=True)



def main():
    teams = ['AFC Bournemouth', 'Arsenal', 'Burnley', 'Chelsea',
             'Crystal Palace', 'Everton', 'Hull City', 'Leicester City',
             'Liverpool', 'Manchester City', 'Manchester United', 'Middlesbrough',
             'Southampton', 'Stoke City', 'Sunderland', 'Swansea City',
             'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United']

    team_list = [{'name': team,
                  'fullscore': 0,
                  'scored goals': 0,
                  'passed goals': 0,
                  'num of wins': 0,
                  'num of loss': 0,
                  'num of draws': 0,
                  'games': {},
                  } for team in teams]

    _play_championship(team_list)

    table = PrettyTable()
    table._set_field_names(['№', 'Team name', 'Wins', 'Loss\'', 'Draws', 'Scored goals', 'Passed goals','Fullscore'])
    for i in range(len(team_list)):
        table.add_row([i+1, team_list[i]['name'], team_list[i]['num of wins'], team_list[i]['num of loss'],
                       team_list[i]['num of draws'], team_list[i]['scored goals'], team_list[i]['passed goals'], team_list[i]['fullscore']])
    print(table)

    while 1:
        print()
        input_text = input('Enter NUMBERS of two teams FROM TABLE separated by space to see score of their game: \n(or print \'close\' to exit) ')
        if input_text == 'close':
            break
        teams = input_text.split(' ')
        if len(teams) != 2:
            print('\n\tERROR! You may see score only for two teams.')
        else:
            if teams[0].isdigit() and teams[1].isdigit():
                teams[0] = int(teams[0])
                teams[1] = int(teams[1])
                if teams[0] == teams[1]:
                    print('\n\tERROR! Same numbers! Team are not able to play with itself!')
                    continue
                try:
                    team1 = team_list[teams[0]-1]
                except IndexError:
                    print('\n\tERROR! The first number is out of range.')
                    continue
                try:
                    team2 = team_list[teams[1]-1]
                except IndexError:
                    print('\n\tERROR! The second number is out of range.')
                    continue
                score = team1['games'][team2['name']]
                print('\n\t{} and {} played with score {}:{}'.format(team1['name'], team2['name'], score[0], score[1]))
            else:
                print('\n\tERROR! You may only enter digits! Please try again!')


if __name__ == '__main__':
    main()


