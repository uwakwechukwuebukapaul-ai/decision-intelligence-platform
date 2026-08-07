"""
Sentinel DNA Application Boot Test
"""


from app.factory import create_app



def test_application_creation():

    app = create_app()


    assert app is not None


    assert app.name is not None



def test_registered_blueprints():

    app = create_app()


    blueprints = list(
        app.blueprints.keys()
    )


    assert len(blueprints) > 0