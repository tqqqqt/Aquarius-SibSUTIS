import requests
import pytest
import ssl

@pytest.fixture
def openbmc_url():
	return "https://127.0.0.1:2443"

def test_corect_login(openbmc_url):
	payload={"UserName":"root", "Password":"0penBmc"}
	curent_code_result=-1
	curent_headers_result=' '
	need_code_result=201
	need_headers_result="X-Auth-Token"
	
	response=requests.post(f"{openbmc_url}/redfish/v1/SessionService/Sessions",json=payload,verify=False)
	curent_code_result=response.status_code
	curent_headers_result=response.headers

	assert curent_code_result==need_code_result
	assert need_headers_result in curent_headers_result

def test_incorect_login(openbmc_url):
	payload={"UserName":"abc", "Password":"abc"}
	curent_result=-1
	need_result=401
	
	response=requests.post(f"{openbmc_url}/redfish/v1/SessionService/Sessions",json=payload,verify=ssl.CERT_NONE)
	curent_result=response.status_code

	assert curent_result==need_result

def test_system_check(openbmc_url):
	login={"UserName":"root", "Password":"0penBmc"}
	headers={"X-Auth-Token":"", "Content-Type":"application/json"}
	curent_code_result=-1
	curent_json_result=' '
	need_code_result=200
	need_json_result_1="Status"
	need_json_result_2="PowerState"

	response=requests.post(f"{openbmc_url}/redfish/v1/SessionService/Sessions",json=login,verify=ssl.CERT_NONE)
	headers["X-Auth-Token"]=response.headers.get("X-Auth-Token")
	response=requests.get(f"{openbmc_url}/redfish/v1/Systems/system",headers=headers,verify=ssl.CERT_NONE)
	curent_code_result=response.status_code
	curent_json_result=response.json()

	assert curent_code_result==need_code_result
	assert need_json_result_1 in curent_json_result
	assert need_json_result_2 in curent_json_result

def test_power_control(openbmc_url):
	login={"UserName":"root", "Password":"0penBmc"}
	headers={"X-Auth-Token":"", "Content-Type":"application/json"}
	payload={"ResetType":"On"}
	curent_code_result_1=-1
	curent_code_result_2=-1
	curent_json_result=' '
	need_code_result_1=204
	need_code_result_2=200
	need_json_result="Off"

	response=requests.post(f"{openbmc_url}/redfish/v1/SessionService/Sessions",json=login,verify=ssl.CERT_NONE)
	headers["X-Auth-Token"]=response.headers.get("X-Auth-Token")
	response=requests.post(f"{openbmc_url}/redfish/v1/Systems/system/Actions/ComputerSystem.Reset",headers=headers,json=payload,verify=ssl.CERT_NONE)
	curent_code_result_1=response.status_code
	response=requests.get(f"{openbmc_url}/redfish/v1/Systems/system",headers=headers,verify=ssl.CERT_NONE)
	curent_code_result_2=response.status_code
	curent_json_result=response.json()['PowerState']

	assert curent_code_result_1==need_code_result_1
	assert curent_code_result_2==need_code_result_2
	assert curent_json_result==need_json_result