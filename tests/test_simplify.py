from src.simplify import simplify_path

def test_examples():
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/a/./b/../../c/") == "/c"
    assert simplify_path("/a//b////c/d//././/..") == "/a/b/c"

def test_root_and_up_moves():
    assert simplify_path("/") == "/"
    assert simplify_path("/../") == "/"


# --- Edge Cases ---
def test_edge_many_slashes_and_trailing():
    assert simplify_path("/a///b////c///") == "/a/b/c"

def test_edge_many_parent_ups_beyond_root():
    assert simplify_path("/../../../../") == "/"

# --- Longer Scenario ---
def test_long_nested_path_with_mixed_segments():
    p = "/home//user/./projects/../projects/python/./.././ds///week4/../../notes/././../"
    # Walkthrough:
    # /home/user/projects -> /home/user
    # /home/user/projects/python -> /home/user/projects/python
    # then up -> /home/user/projects
    # then ds -> /home/user/projects/ds
    # then week4 -> /home/user/projects/ds/week4
    # then ../../ -> /home/user/projects
    # then notes -> /home/user/projects/notes
    # then ../ -> /home/user/projects
    assert simplify_path(p) == "/home/user/projects"
