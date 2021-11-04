import tui


def list_years(data):
    tui.started("Listing years...")
    years = set()
    for year in data:
        years.add(year[9])
    tui.display_years(years)
    tui.completed()


def tally_medals(data):
    tui.started("Tallying medals...")
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    gold = 0
    silver = 0
    bronze = 0
    for medal in data:
        if medal[14] == 'Gold':
            gold += 1
        elif medal[14] == 'Silver':
            silver += 1
        elif medal[14] == 'Bronze':
            bronze += 1
    medals['Gold'] = gold
    medals['Silver'] = silver
    medals['Bronze'] = bronze
    tui.display_medal_tally(medals)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying medals for each team.")
    team_medals = {}
    for team in data:
        if team[6] in team_medals:
            if team[14] == 'Gold':
                team_medals[team[6]]['Gold'] += 1
            elif team[14] == 'Silver':
                team_medals[team[6]]['Silver'] += 1
            elif team[14] == 'Bronze':
                team_medals[team[6]]['Bronze'] += 1
        else:
            team_medals[team[6]] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            if team[14] == 'Gold':
                team_medals[team[6]]['Gold'] += 1
            elif team[14] == 'Silver':
                team_medals[team[6]]['Silver'] += 1
            elif team[14] == 'Bronze':
                team_medals[team[6]]['Bronze'] += 1
    tui.display_team_medal_tally(team_medals)
    tui.completed()

    
def tally_athlete_medals(data):
    tui.started("Tallying medals for each athlete.")
    athlete_medals = {}
    for athlete in data:
        if athlete[2] in team_medals:
            if athlete[14] == 'Gold':
                athlete_medals[athlete[2]]['Gold'] += 1
            elif athlete[14] == 'Silver':
                athlete_medals[athlete[2]]['Silver'] += 1
            elif athlete[14] == 'Bronze':
                athlete_medals[athlete[2]]['Bronze'] += 1
        else:
            athlete_medals[athlete[2]] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            if athlete[14] == 'Gold':
                athlete_medals[athlete[2]]['Gold'] += 1
            elif athlete[14] == 'Silver':
                athlete_medals[athlete[2]]['Silver'] += 1
            elif athlete[14] == 'Bronze':
                athlete_medals[athlete[2]]['Bronze'] += 1
    tui.display_athlete_medal_tally(athlete_medals)
    tui.completed()
