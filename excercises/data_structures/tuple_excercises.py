
def filter_and_rank_teams(teams, min_score, restricted_teams, top_n):
    """
    Given a list of (int score, team name) tuples, and an integer min_score, 
    return a list consisting of only tuples where first score value is 
    greater than or equal to min_score AND if that team name is NOT in 
    the restricted_teams list.

    The final list must be sorted by score of the tuple, descending.

    Only return the top_n teams by score.

    @param: teams (list of tuples)
    @param: min_score (int)
    @param: restricted_teams (list of strings)

    HINT: List comprehensions, sorting, and slicing will be useful here!

    Test with:
    $ py.test tests/test_ds.py::DataStructureExcercises::test_filter_tuples
    """
    filtered = [(score, name) for score, name in teams
                if score >= min_score and
                    name not in restricted_teams]
    filtered.sort(reverse = True)

    return filtered[:top_n]