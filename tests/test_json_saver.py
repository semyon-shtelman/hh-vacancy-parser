from src.storage.json_saver import JSONSaver


def test_add_and_get(tmp_path):
    file_path = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file_path))

    data = {"title": "Test", "description": "Python"}
    saver.add_vacancy(data)

    result = saver.get_vacancy()
    assert data in result


def test_no_duplicates(tmp_path):
    file_path = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file_path))

    data = {"title": "Test"}
    saver.add_vacancy(data)
    saver.add_vacancy(data)

    assert len(saver.get_vacancy()) == 1


def test_delete(tmp_path):
    file_path = tmp_path / "vacancies.json"
    saver = JSONSaver(str(file_path))

    data = {"title": "Test"}
    saver.add_vacancy(data)
    saver.delete_vacancy(data)

    assert data not in saver.get_vacancy()
