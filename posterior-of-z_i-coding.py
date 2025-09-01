OK_FORMAT = True

test = {   'name': 'posterior-of-z_i-coding',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> p0, p1, p2 = (0.5, 0.7, 0.4)\n>>> y = 1\n>>> expected = 0.636363\n>>> assert np.isclose(compute_posterior(y, p0, p1, p2), expected, atol=1e-06)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
