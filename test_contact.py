from contact import Contact



def test_contact():
    contact = Contact('Zarif','Naxalov','+998 93 123 45 67')
    assert contact.first_name == 'Zarif'
    assert contact.last_name == 'Naxalov'
    assert contact.phone_number == '+998 93 123 45 67'

def test_check_phone_number():
    contact = Contact('Zarif','Naxalov','+998 93 123 45 67')
    assert contact.check_phone_number() == True
    contact = Contact('Zarif','Naxalov','+998 93 123 45 6')
    assert contact.check_phone_number() == False,'Phone number is not valid'
    contact = Contact('Zarif','Naxalov','1998 93 123 45 67')
    assert contact.check_phone_number() == False,'Phone number is not valid'
    



def test_check_name():
    contact = Contact('Zarif','Naxalov','+998 93 123 45 67')
    assert contact.check_name() == True
    contact = Contact('zarif','Naxalov','+998 93 123 45 67')
    assert contact.check_name() == False
