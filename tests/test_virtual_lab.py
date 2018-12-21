from requests import get, post, put
from requests.auth import HTTPBasicAuth

from eNMS.base.helpers import fetch_all

from tests.test_base import check_blueprints


@check_blueprints('/inventory')
def test_rest_api_basic(user_client):
    # assert len(fetch_all('Device')) == 28
    # post(
    #     'http://192.168.105.2:5000/rest/instance/device',
    #     json={'name': 'new_router', 'model': 'Cisco'},
    #     auth=HTTPBasicAuth('admin', 'admin')
    # )
    # assert len(fetch_all('Device')) == 29
    # result = get(
    #     'http://192.168.105.2:5000/rest/instance/device/Washington',
    #     auth=HTTPBasicAuth('admin', 'admin')
    # ).json()
    # assert result['model'] == 'Arista' and len(result) == 14
    # post(
    #     'http://192.168.105.2:5000/rest/instance/device',
    #     json={'name': 'Washington', 'model': 'Cisco'},
    #     auth=HTTPBasicAuth('admin', 'admin')
    # )
    # result = get(
    #     'http://192.168.105.2:5000/rest/instance/device/Washington',
    #     auth=HTTPBasicAuth('admin', 'admin')
    # ).json()
    # assert result['model'] == 'Cisco' and len(result) == 14
    # result = get(
    #     'http://192.168.105.2:5000/rest/instance/service/get_facts',
    #     auth=HTTPBasicAuth('admin', 'admin')
    # ).json()
    # assert result['description'] == 'Getter: get_facts' and len(result) == 24
    # put(
    #     'http://192.168.105.2:5000/rest/instance/service',
    #     json={'name': 'get_facts', 'description': 'Get facts'},
    #     auth=HTTPBasicAuth('admin', 'admin')
    # )
    # result = get(
    #     'http://192.168.105.2:5000/rest/instance/service/get_facts',
    #     auth=HTTPBasicAuth('admin', 'admin')
    # ).json()
    # assert result['description'] == 'Get facts' and len(result) == 24
    assert len(fetch_all('Service')) == 21
    result = post(
        'http://192.168.105.2:5000/rest/instance/service',
        json={'name': 'new_service', 'vendor': 'Cisco'},
        auth=HTTPBasicAuth('admin', 'admin')
    ).json()
    assert result['vendor'] = 'Cisco'
    assert len(fetch_all('Service')) == 22
    assert len(fetch_all('Service')) == 4
    post(
        'http://192.168.105.2:5000/rest/instance/service',
        json={'name': 'new_service', 'model': 'Cisco'},
        auth=HTTPBasicAuth('admin', 'admin')
    )
    assert len(fetch_all('Service')) == 5


# @check_blueprints('/automation')
# def test_payload_transfer_workflow(user_client):
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'payload_transfer_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 3
#     post(
#         'http://192.168.105.2:5000/rest/instance/Workflow',
#         json={'name': 'payload_transfer_workflow', 'multiprocessing': True},
#         auth=HTTPBasicAuth('admin', 'admin')
#     )
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'payload_transfer_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 3
#     post(
#         'http://192.168.105.2:5000/rest/instance/Workflow',
#         json={'name': 'payload_transfer_workflow', 'devices': []},
#         auth=HTTPBasicAuth('admin', 'admin')
#     )
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'payload_transfer_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 10
# 
# 
# @check_blueprints('/automation')
# def test_netmiko_workflow(user_client):
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'Netmiko_VRF_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 3
#     post(
#         'http://192.168.105.2:5000/rest/instance/Workflow',
#         json={'name': 'Netmiko_VRF_workflow', 'multiprocessing': True},
#         auth=HTTPBasicAuth('admin', 'admin')
#     )
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'Netmiko_VRF_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 3
#     post(
#         'http://192.168.105.2:5000/rest/instance/Workflow',
#         json={'name': 'Netmiko_VRF_workflow', 'devices': []},
#         auth=HTTPBasicAuth('admin', 'admin')
#     )
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'Netmiko_VRF_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 8
# 
# 
# @check_blueprints('/automation')
# def test_napalm_workflow(user_client):
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'Napalm_VRF_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 3
#     post(
#         'http://192.168.105.2:5000/rest/instance/Workflow',
#         json={'name': 'Napalm_VRF_workflow', 'multiprocessing': True},
#         auth=HTTPBasicAuth('admin', 'admin')
#     )
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'Napalm_VRF_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 3
#     post(
#         'http://192.168.105.2:5000/rest/instance/Workflow',
#         json={'name': 'Napalm_VRF_workflow', 'devices': []},
#         auth=HTTPBasicAuth('admin', 'admin')
#     )
#     result = post(
#         'http://192.168.105.2:5000/rest/run_job',
#         json={'name': 'Napalm_VRF_workflow', 'async': 0},
#         auth=HTTPBasicAuth('admin', 'admin')
#     ).json()
#     assert result['success'] and len(result) == 8