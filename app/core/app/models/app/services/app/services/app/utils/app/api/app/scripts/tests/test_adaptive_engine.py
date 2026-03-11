from app.services.adaptive_engine import update_ability

def test_ability_increase():
    ability = update_ability(0.5, 0.4, True)
    assert ability > 0.5


def test_ability_decrease():
    ability = update_ability(0.5, 0.6, False)
    assert ability < 0.5
