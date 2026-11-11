from hello_jenkins.app import greet


def test_greet_with_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_defaults_to_jenkins():
    assert greet() == "Hello, Jenkins!"
