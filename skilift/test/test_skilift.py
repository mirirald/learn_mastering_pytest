from skilift import Line,Quad,Lift
import pytest

def test_line_take(line):
    res = line.take(7)
    assert res == 5
    assert line.num_people == 0

def test_lift_one_bench(line, lift):
    res = lift.one_bench(line)
    assert res == {'loaded': 4, 'num_benches': 1, 'unloaded': 0}

@pytest.mark.parametrize('num_people',
                         [(''),([]),(None),('10')])
def test_line_bad(num_people):
    line = Line(num_people)
    with pytest.raises(TypeError):
        line.take(1)

@pytest.mark.parametrize('line_size, take_count, num_people',
                         [(0,5,0),(5,2,3),(10,0,10)])
def test_line_sizes(line_size, take_count, num_people):
    line = Line(line_size)
    res = line.take(take_count)
    assert line.num_people == num_people

@pytest.fixture
def line():
    return Line(5)

@pytest.fixture
def lift():
    return Lift(10, Quad)

@pytest.fixture
def line_n(request):
    size = request.node.get_closest_marker('line_size').args[0]
    line = Line(size)
    return line

@pytest.mark.line_size(6)
def test_line6(line_n):
    res = line_n.take(6)
    assert res == 6

@pytest.fixture
def BenchN(request):
    size = request.node.get_closest_marker('bench_size').args[0]

    class BSize(_Bench):
        size = size
    return BSize

