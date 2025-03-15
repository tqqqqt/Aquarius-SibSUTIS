import openbmc_main

def test_correct_login():
	user_name="root"
	user_pass="0penBmc"
	curent_res=""
	need_res="Overview"

	openbmc_main.startWork("https://127.0.0.1:2443/#/login")
	openbmc_main.loginServer(user_name,user_pass)
	curent_res=openbmc_main.getTitle()
	openbmc_main.endWork()

	assert curent_res==need_res


def test_incorect_login():
	user_name="abc"
	user_pass="abc"
	curent_res=""
	need_res="Login"

	openbmc_main.startWork("https://127.0.0.1:2443/#/login")
	openbmc_main.loginServer(user_name,user_pass)
	curent_res=openbmc_main.getTitle()
	openbmc_main.endWork()

	assert curent_res==need_res

def test_block_login():
	user_name="user"
	user_pass_incorect="abc"
	user_pass_correct="0penBmcc"
	curent_res=""
	need_res="Login"

	openbmc_main.startWork("https://127.0.0.1:2443/#/login")
	openbmc_main.loginServer(user_name,user_pass_incorect)
	openbmc_main.loginServer(user_name,user_pass_incorect)
	openbmc_main.loginServer(user_name,user_pass_incorect)
	openbmc_main.loginServer(user_name,user_pass_correct)
	curent_res=openbmc_main.getTitle()
	openbmc_main.endWork()

	assert curent_res==need_res