from utils.dicts import get_val


def test_get_val():
    data_1 = {"vcs": "mercurial"}
    data_2 = {}
    assert get_val(data_1, "vcs") == "mercurial"
    assert get_val(data_1, "vcs", "git") == "mercurial"
    assert get_val(data_1, "git") == "git"
    assert get_val(data_1, "git", "remote") == "remote"

    assert get_val(data_2, "vcs") == "git"
    assert get_val(data_2, "vcs", "git") == "git"
    assert get_val(data_2, "git", "remote") == "remote"
    assert get_val(data_2, "vcs", "bazaar") == "bazaar"
