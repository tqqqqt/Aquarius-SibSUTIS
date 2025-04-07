from locust import HttpUser, task, tag
from requests.packages import urllib3

class UserBehavior(HttpUser):

	def on_start(self):
		self.client.verify=False
		self.login={"UserName":"root", "Password":"0penBmc"}
		self.headers={"X-Auth-Token":"", "Content-Type":"application/json"}
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		response=self.client.post("https://127.0.0.1:2443/redfish/v1/SessionService/Sessions",json=self.login)
		self.headers["X-Auth-Token"]=response.headers.get("X-Auth-Token")
		pass

	def on_stop(self):
		pass

	@tag("openbmc_system")
	@task(1)
	def openbmc_system_info(self):
		response=self.client.get("https://127.0.0.1:2443/redfish/v1/Systems/system",headers=self.headers)
		assert response.status_code==200

	@tag("openbmc_power")
	@task(2)
	def openbmc_redfish_sys(self):
		response=self.client.get("https://127.0.0.1:2443/redfish/v1/Systems/system",headers=self.headers)
		assert response.status_code==200
		curent_state=response.json()
		assert "PowerState" in curent_state

	@tag("json_posts")
	@task(3)
	def json_posts(self):
		response=self.client.get("https://jsonplaceholder.typicode.com/posts")
		assert response.status_code==200