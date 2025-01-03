from project.guardian import Guardian
from project.player import Player


def test_constructor():
    g = Guardian('Marry', 'Allen')
    assert g.first_name == 'Marry'
    assert g.last_name == 'Allen'


def test_add_guardian():
    g = Guardian('Marry', 'Allen')
    p = Player('Felicity', 'Smith', 16,[])


