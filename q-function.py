OK_FORMAT = True

test = {   'name': 'q-function',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> Y = [1, 0, 1]\n'
                                               '>>> p0, p1, p2 = (0.5, 0.7, 0.4)\n'
                                               '>>> p0_t, p1_t, p2_t = (0.6, 0.8, 0.2)\n'
                                               '>>> expected = -3.652547418589841\n'
                                               '>>> assert np.isclose(Q_function(Y, p0, p1, p2, p0_t, p1_t, p2_t), expected, atol=1e-06)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.9}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
