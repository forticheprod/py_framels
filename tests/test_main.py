import py_framels


def test_listing():
    excepted = ["toto.****.tif@1-2"]
    result = py_framels.py_basic_listing(["toto.0001.tif", "toto.0002.tif"])
    assert excepted == result


def test_parse_dir():
    excepted = ["aaa.***.tif@1-5", "foo_bar.exr"]
    result = py_framels.py_parse_dir("./samples/small/")
    assert excepted == result


def test_recu_dir():
    excepted = [
        "./samples",
        "./samples/small",
        "./samples/small/aaa.***.tif@1-5",
        "./samples/small/foo_bar.exr",
    ]
    result = py_framels.py_recursive_dir("./samples/")
    assert excepted == result
