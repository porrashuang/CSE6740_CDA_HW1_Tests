OK_FORMAT = True

test = {   'name': 'posterior-of-z_i-coding-zero',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> p0, p1, p2 = (0.6, 0.5, 0.3)\n'
                                               '>>> y = 1\n'
                                               '>>> expected = 0.2857142857142857\n'
                                               '>>> assert np.isclose(compute_posterior_zero(y, p0, p1, p2), expected, atol=1e-06)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.6}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
