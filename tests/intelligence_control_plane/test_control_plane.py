from app.factory import create_app



app = create_app()



def test_control_plane_status():


    client = app.test_client()


    response = client.get(
        "/control-plane/status"
    )


    assert response.status_code == 200



def test_control_plane_health():


    client = app.test_client()


    response = client.get(
        "/control-plane/health"
    )


    assert response.status_code == 200