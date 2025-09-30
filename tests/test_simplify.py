# /tests/test_simplify.py

import pytest 
# --- Path Fix ---
import sys, os
# Add the project root to the path so 'src' can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 
# ----------------

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
    assert simplify_path(p) == "/home/user/projects"