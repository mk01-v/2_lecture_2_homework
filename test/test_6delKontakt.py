from model.kontakt import kontakt

def test_delete_kontakt(app):
    app.kontakt.delete_kontakt()