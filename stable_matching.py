from collections import deque

def courtship(boys_prefs, girls_prefs):
    """Return a stable matching according to Gale-Shapley algorithm."""

    boys_prefs = [deque(pref) for pref in boys_prefs]
    girls_prefs = [deque(pref) for pref in girls_prefs]

    proposals_list = [[] for _ in range(len(girls_prefs))]
    strings = [None for _ in range(len(girls_prefs))]
    rejected = set(range(len(boys_prefs)))

    while rejected:
        for boy in rejected:
            prefs = boys_prefs[boy]
            if len(prefs) > 0:
                proposals_list[prefs[0]].append(boy)

        rejected.clear()

        for girl, proposals in enumerate(proposals_list):
            if not strings[girl] is None:
                proposals.append(strings[girl])
            if len(proposals) > 0:
                strings[girl] = min(proposals,
                                    key=lambda x: girls_prefs[girl].index(x))
                for boy in proposals:
                    if boy != strings[girl]:
                        rejected.add(boy)

        proposals_list = [[] for _ in range(len(girls_prefs))]
        for boy in rejected:
            if len(boys_prefs[boy]) > 0:
                boys_prefs[boy].popleft()
                #boys_prefs[boy].pop(0)

    boys_partner = [None for _ in range(len(boys_prefs))]
    for girl, boy in enumerate(strings):
        if not boy is None:
            boys_partner[boy] = girl
    return boys_partner, strings


if __name__ == '__main__':
    boys_pref = [[0, 1, 2, 3],
                 [0, 3, 2, 1],
                 [1, 0, 2, 3],
                 [3, 1, 2, 0]]

    girls_pref = [[3, 2, 0, 1],
                  [1, 3, 0, 2],
                  [3, 0, 1, 2],
                  [2, 1, 0, 3]]

    boys_partner, girls_partner = courtship(boys_pref, girls_pref)

    for boy, girl in enumerate(boys_partner):
        print("boy {} with girl {}".format(boy, girl))
    for girl, boy in enumerate(girls_partner):
        print("girl {} with boy {}".format(girl, boy))
