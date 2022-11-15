from requests import Response
from pytest_voluptuous import S
from schemas import schemas
from utils.base_session import reqres_session


def test_get_single_user_schema():
    result = reqres_session().get(
        url='/api/users/2'
    )

    assert result.status_code == 200
    assert result.json() == S(schemas.get_single_user_schema)


def test_single_user_not_found():
    result = reqres_session().get(
        url='/api/users/23'
    )

    assert result.status_code == 404


def test_create_user():
    name = "John"
    job = "Doe"

    result = reqres_session().post(
        url='/api/users',
        json={
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 201
    assert result.json() == S(schemas.create_user_schema)
    assert result.json()['name'] == name
    assert result.json()['job'] == job


def test_update_user():
    name = 'morbius'
    job = 'derp'

    result: Response = reqres_session().put(
        url='/api/users/2',
        json={
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(schemas.update_user_schema)


def test_register_successful():
    email = "eve.holt@reqres.in"
    password = "pistol"

    result: Response = reqres_session().post(
        url='/api/register',
        json={
            "email": email,
            "password": password
        }
    )

    print(result.json())
    assert result.status_code == 200
    assert result.json() == S(schemas.register_successful)


'''
def test_create_user_schema():
    name = 'morpheus_1'
    job = 'leader'

    result: Response = requests.post(
        url='https://reqres.in/api/users',
        json={
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user_schema)


def test_create_user_schema():
    name = 'morpheus_1'
    job = 'leader'

    result: Response = requests.post(
        url='https://reqres.in/api/users',
        json={
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user_schema)



def test_create_user_schema_external_base_url():
    name = 'morpheus_1'
    job = 'leader'

    result = reques_session().post(
        url='/api/users',
        json={
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user_schema)
'''