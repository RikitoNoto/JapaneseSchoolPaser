import os
from typing import Any
import pytest
from japanese_school_parser import parse_schools_to_dict, parse_schools_to_model
from models.faculty import Department, Faculty
from models.graduate_school import GraduateSchool, Major
from models.school import School


def major_equal(major1: Major, major2: Major) -> bool:
    if major1.name != major2.name:
        return False
    return True


def department_equal(department1: Department, department2: Department) -> bool:
    if department1.name != department2.name:
        return False
    return True


def faculty_equal(faculty1: Faculty, faculty2: Faculty) -> bool:
    if faculty1.name != faculty2.name:
        return False

    if len(faculty1.departments) != len(faculty2.departments):
        return False

    department1_progress = faculty1.departments.copy()
    department2_progress = faculty2.departments.copy()

    for department1 in faculty1.departments:
        for department2 in faculty2.departments:
            if department_equal(department1, department2):
                department1_progress.remove(department1)
                department2_progress.remove(department2)
                break

    if len(department1_progress) != 0 or len(department2_progress) != 0:
        return False

    return True


def graduate_school_equal(
    graduate_school1: GraduateSchool, graduate_school2: GraduateSchool
) -> bool:
    if graduate_school1.name != graduate_school2.name:
        return False

    if len(graduate_school1.majors) != len(graduate_school2.majors):
        return False

    major1_progress = graduate_school1.majors.copy()
    major2_progress = graduate_school2.majors.copy()

    for majors1 in graduate_school1.majors:
        for majors2 in graduate_school2.majors:
            if major_equal(majors1, majors2):
                major1_progress.remove(majors1)
                major2_progress.remove(majors2)
                break

    if len(major1_progress) != 0 or len(major2_progress) != 0:
        return False

    return True


def school_equal(school1: School, school2: School) -> bool:
    if school1.president != school2.president:
        return False

    if school1.school_code != school2.school_code:
        return False

    if school1.name != school2.name:
        return False

    if len(school1.faculties) != len(school2.faculties):
        return False

    faculty1_progress = school1.faculties.copy()
    faculty2_progress = school2.faculties.copy()

    for faculty1 in school1.faculties:
        for faculty2 in school2.faculties:
            if faculty_equal(faculty1, faculty2):
                faculty1_progress.remove(faculty1)
                faculty2_progress.remove(faculty2)
                break

    if len(faculty1_progress) != 0 or len(faculty2_progress) != 0:
        return False

    if len(school1.graduate_schools) != len(school2.graduate_schools):
        return False

    graduate_schools1_progress = school1.graduate_schools.copy()
    graduate_schools2_progress = school2.graduate_schools.copy()

    for graduate_schools1 in school1.graduate_schools:
        for graduate_schools2 in school2.graduate_schools:
            if graduate_school_equal(graduate_schools1, graduate_schools2):
                graduate_schools1_progress.remove(graduate_schools1)
                graduate_schools2_progress.remove(graduate_schools2)
                break

    if len(graduate_schools1_progress) != 0 or len(graduate_schools2_progress) != 0:
        return False

    return True


def school_list_equal(school_list1: list[School], school_list2: list[School]) -> bool:
    if len(school_list1) != len(school_list2):
        return False

    schools1_progress = school_list1.copy()
    schools2_progress = school_list2.copy()

    for school1 in school_list1:
        for school2 in school_list2:
            if school_equal(school1, school2):
                schools1_progress.remove(school1)
                schools2_progress.remove(school2)
                break

    if len(schools1_progress) != 0 or len(schools2_progress) != 0:
        return False

    return True


@pytest.mark.parametrize(
    "source_path, expect_schools",
    [
        (
            f"{os.path.dirname(__file__)}/files/multi_sheets1.xlsx",
            [
                School(
                    name="京都精華大学",
                    school_code="F126310107644",
                    president="ウスビ・サコ",
                    faculties=[
                        Faculty(
                            name="芸術学部",
                            departments=[
                                Department(
                                    name="造形学科",
                                ),
                            ],
                        ),
                        Faculty(
                            name="デザイン学部",
                            departments=[
                                Department(
                                    name="ビジュアルデザイン学科",
                                ),
                                Department(
                                    name="イラスト学科",
                                ),
                                Department(
                                    name="プロダクトデザイン学科",
                                ),
                                Department(
                                    name="建築学科",
                                ),
                            ],
                        ),
                        Faculty(
                            name="マンガ学部",
                            departments=[
                                Department(
                                    name="マンガ学科",
                                ),
                                Department(
                                    name="アニメーション学科",
                                ),
                            ],
                        ),
                        Faculty(
                            name="人文学部",
                            departments=[
                                Department(
                                    name="総合人文学科",
                                ),
                            ],
                        ),
                        Faculty(
                            name="ポピュラーカルチャー学部",
                            departments=[
                                Department(
                                    name="ポピュラーカルチャー学科",
                                ),
                            ],
                        ),
                        Faculty(
                            name="メディア表現学部",
                            departments=[
                                Department(
                                    name="メディア表現学科",
                                ),
                            ],
                        ),
                        Faculty(
                            name="国際文化学部",
                            departments=[
                                Department(
                                    name="人文学科",
                                ),
                                Department(
                                    name="グローバルスタディーズ学科",
                                ),
                            ],
                        ),
                    ],
                    graduate_schools=[
                        GraduateSchool(
                            name="芸術研究科",
                            majors=[
                                Major(name="芸術専攻"),
                            ],
                        ),
                        GraduateSchool(
                            name="デザイン研究科",
                            majors=[
                                Major(name="デザイン専攻"),
                                Major(name="建築専攻"),
                            ],
                        ),
                        GraduateSchool(
                            name="マンガ研究科",
                            majors=[
                                Major(name="マンガ専攻"),
                            ],
                        ),
                        GraduateSchool(
                            name="人文学研究科",
                            majors=[
                                Major(name="人文学専攻"),
                            ],
                        ),
                    ],
                ),
                School(
                    name="明治国際医療大学",
                    school_code="F126310107653",
                    president="矢野　忠",
                    faculties=[
                        Faculty(
                            name="鍼灸学部",
                            departments=[
                                Department(
                                    name="鍼灸学科",
                                ),
                            ],
                        ),
                        Faculty(
                            name="保健医療学部",
                            departments=[
                                Department(
                                    name="柔道整復学科",
                                ),
                                Department(
                                    name="救急救命学科",
                                ),
                            ],
                        ),
                        Faculty(
                            name="看護学部",
                            departments=[
                                Department(
                                    name="看護学科",
                                ),
                            ],
                        ),
                    ],
                    graduate_schools=[
                        GraduateSchool(
                            name="鍼灸学研究科",
                            majors=[
                                Major(name="鍼灸学専攻"),
                                Major(name="臨床鍼灸学専攻"),
                            ],
                        ),
                        GraduateSchool(
                            name="保健医療学研究科",
                            majors=[
                                Major(name="柔道整復学専攻"),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)
def test_should_be_parse_model(source_path: str, expect_schools: list[School]):
    schools = parse_schools_to_model(source_path)
    assert school_list_equal(schools, expect_schools)


@pytest.mark.parametrize(
    "source_path, expect_schools",
    [
        (
            f"{os.path.dirname(__file__)}/files/multi_sheets1.xlsx",
            {
                "schools": [
                    {
                        "name": "京都精華大学",
                        "school_code": "F126310107644",
                        "president": "ウスビ・サコ",
                        "faculties": [
                            {
                                "name": "芸術学部",
                                "departments": [
                                    {
                                        "name": "造形学科",
                                    },
                                ],
                            },
                            {
                                "name": "デザイン学部",
                                "departments": [
                                    {
                                        "name": "ビジュアルデザイン学科",
                                    },
                                    {
                                        "name": "イラスト学科",
                                    },
                                    {
                                        "name": "プロダクトデザイン学科",
                                    },
                                    {
                                        "name": "建築学科",
                                    },
                                ],
                            },
                            {
                                "name": "マンガ学部",
                                "departments": [
                                    {
                                        "name": "マンガ学科",
                                    },
                                    {
                                        "name": "アニメーション学科",
                                    },
                                ],
                            },
                            {
                                "name": "人文学部",
                                "departments": [
                                    {
                                        "name": "総合人文学科",
                                    },
                                ],
                            },
                            {
                                "name": "ポピュラーカルチャー学部",
                                "departments": [
                                    {
                                        "name": "ポピュラーカルチャー学科",
                                    },
                                ],
                            },
                            {
                                "name": "メディア表現学部",
                                "departments": [
                                    {
                                        "name": "メディア表現学科",
                                    },
                                ],
                            },
                            {
                                "name": "国際文化学部",
                                "departments": [
                                    {
                                        "name": "人文学科",
                                    },
                                    {
                                        "name": "グローバルスタディーズ学科",
                                    },
                                ],
                            },
                        ],
                        "graduate_schools": [
                            {
                                "name": "芸術研究科",
                                "majors": [
                                    {"name": "芸術専攻"},
                                ],
                            },
                            {
                                "name": "デザイン研究科",
                                "majors": [
                                    {"name": "デザイン専攻"},
                                    {"name": "建築専攻"},
                                ],
                            },
                            {
                                "name": "マンガ研究科",
                                "majors": [
                                    {"name": "マンガ専攻"},
                                ],
                            },
                            {
                                "name": "人文学研究科",
                                "majors": [
                                    {"name": "人文学専攻"},
                                ],
                            },
                        ],
                    },
                    {
                        "name": "明治国際医療大学",
                        "school_code": "F126310107653",
                        "president": "矢野　忠",
                        "faculties": [
                            {
                                "name": "鍼灸学部",
                                "departments": [
                                    {
                                        "name": "鍼灸学科",
                                    },
                                ],
                            },
                            {
                                "name": "保健医療学部",
                                "departments": [
                                    {
                                        "name": "柔道整復学科",
                                    },
                                    {
                                        "name": "救急救命学科",
                                    },
                                ],
                            },
                            {
                                "name": "看護学部",
                                "departments": [
                                    {
                                        "name": "看護学科",
                                    },
                                ],
                            },
                        ],
                        "graduate_schools": [
                            {
                                "name": "鍼灸学研究科",
                                "majors": [
                                    {"name": "鍼灸学専攻"},
                                    {"name": "臨床鍼灸学専攻"},
                                ],
                            },
                            {
                                "name": "保健医療学研究科",
                                "majors": [
                                    {"name": "柔道整復学専攻"},
                                ],
                            },
                        ],
                    },
                ]
            },
        ),
    ],
)
def test_should_be_parse_dict(source_path: str, expect_schools: dict[str, Any]):
    schools = parse_schools_to_dict(source_path)
    assert schools == expect_schools
