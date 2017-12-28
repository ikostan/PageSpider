from utilities.url_utilities import load_urls_from_file


def test_load_file():
    '''
    tests that list of retrieved urls is greater than one
    :return:
    '''
    test_urls = load_urls_from_file('input.txt')
    assert(len(test_urls) > 1)
