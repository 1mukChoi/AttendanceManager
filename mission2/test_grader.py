import pytest

from grader import GraderNormal


@pytest.mark.parametrize("points, grade", [(0, "NORMAL"), (10, "NORMAL"), (20, "NORMAL"), (30, "SILVER"), (40, "SILVER"), (50, "GOLD"), (100, "GOLD")])
def test_grader_normal_set_grade(points, grade):
    grader = GraderNormal()
    grader.set_grade(points)
    assert grader.grade == grade

@pytest.mark.parametrize("grade, is_removed", [("NORMAL", True), ("SILVER", False), ("GOLD", False)])
def test_grader_normal_is_removed(grade, is_removed):
    grader = GraderNormal()
    grader._grade = grade
    assert grader.is_removed() == is_removed