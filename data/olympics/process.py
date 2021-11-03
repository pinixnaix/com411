import tui


def list_years(data):
    tui.started("Listing years...")
    years = set()
    for year in data:
        years.add(year[9])
    tui.display_years()
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
    tui.display_medal_tally()
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying medals for each team.")
    team_medals = {}
    for team in data:
        if team[6] in team_medals:

        else:
            team_medals[team[6]] = {"Gold": 0, "Silver": 0, "Bronze": 0}

    tui.display_team_medal_tally()
    tui.completed()
