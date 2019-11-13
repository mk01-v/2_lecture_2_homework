



def test_modifgroup(app):
    app.session.login(username="admin", password="secret")
    app.group.modif_group()
    app.session.logout()