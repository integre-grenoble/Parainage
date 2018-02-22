from collections import deque

def courtship(boys_prefs, girls_prefs):
    """Return a stable matching of list of list of index."""

    boys_prefs = [deque(pref) for pref in boys_prefs]

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

    boys_partner = [None for _ in range(len(boys_prefs))]
    for girl, boy in enumerate(strings):
        if not boy is None:
            boys_partner[boy] = girl
    return boys_partner, strings


def stable_matching(boys_prefs, girls_prefs):
    """Return a stable matching of dict of list of object."""

    boys = [boy for boy in boys_prefs.keys()]
    mat_boys = [[] for _ in boys_prefs]
    girls = [girl for girl in girls_prefs.keys()]
    mat_girls = [[] for _ in girls_prefs]

    for boy, prefs in enumerate(boys_prefs.values()):
        for girl in prefs:
            mat_boys[boy].append(girls.index(girl))
    for girl, prefs in enumerate(girls_prefs.values()):
        for boy in prefs:
            mat_girls[girl].append(boys.index(boy))

    res_boys, res_girls = courtship(mat_boys, mat_girls)

    for boy, girl in enumerate(res_boys):
        boys_prefs[boys[boy]] = girls[girl] if not girl is None else None
    for girl, boy in enumerate(res_girls):
        girls_prefs[girls[girl]] = boys[boy] if not boy is None else None

    return boys_prefs, girls_prefs


if __name__ == '__main__':
    guyprefers = {
        'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
        'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
        'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
        'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
        'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
        'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
        'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
        'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
        'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
        'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}
    girlprefers = {
        'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
        'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
        'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
        'dee':  ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
        'eve':  ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
        'fay':  ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
        'gay':  ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
        'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
        'ivy':  ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
        'jan':  ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']}

    print(stable_matching(guyprefers, girlprefers))
