from mean_sightings import get_sightings
filename = 'sightings_tab_sm.csv'
def test_owl_is_correct():
	owlrec, owlmean = get_sightings(filename, 'Owl')
	# assert test_statement message_if_test_is_false
	assert owlrec == 2, 'Number of records for owl is wrong'
	assert owlmean == 17#, 'Mean sightings for owl is wrong'

def test_muskox_is_correct():
	muskoxrec, muskoxmean = get_sightings(filename, 'Muskox')
	# assert test_statement message_if_test_is_false
	assert muskoxrec == 2, 'Number of records for muskox is wrong'
	assert muskoxmean == 25.5#, 'Mean sightings for muskox is wrong'

def test_animal_not_present():
    animrec, animmean = get_sightings(filename, 'NotPresent')
    assert animrec == 0, 'Animal missing should return zero records'
    assert animmean == 0, 'Animal missing should return zero mean'

def test_animal_case():
    animrec, animmean = get_sightings(filename, 'oWL')
    assert animrec == 2
    assert animmean == 17

