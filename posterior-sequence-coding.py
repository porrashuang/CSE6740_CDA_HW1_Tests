OK_FORMAT = True

test = {   'name': 'posterior-sequence-coding',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> y_seq = [1, 1, 0, 1, 0]\n'
                                               '>>> p0, p1, p2 = (0.5, 0.7, 0.3)\n'
                                               '>>> expected = 0.699999999968254\n'
                                               '>>> assert np.isclose(compute_posterior_sequence(y_seq, p0, p1, p2), expected, atol=1e-06)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.3}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
