import hasattr_safe


def test_returns_false_when_object_missing_attr():
    assert hasattr_safe(tuple(), 'its_not_there') is False


def test_returns_true_when_object_has_attr():
    class Car(object):
        NUM_WHEELS = 4

    assert hasattr_safe(Car(), 'NUM_WHEELS') is True
