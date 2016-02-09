import mock

def exc():
    print 'here should raise'

def recursion():
    try:
        print 'here'
        return exc()
    except StandardError:
        print 'exc'
        return recursion()


def test_recursion():
    global exc
    exc = mock.Mock(side_effect = [StandardError, StandardError, mock.DEFAULT])
    recursion()

test_recursion()