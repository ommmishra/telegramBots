from flask import Flask, request
from gevent.pywsgi import WSGIServer
from random import randint
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get('TOKEN')
BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)
group_chat_id = int(os.environ.get('group_chat_id'))

@app.route("/update", methods = ["POST"])
def update():
	print("RunningBot.......")
	print(request.get_json())
	data = request.get_json()
	group_data = int(data['message']['chat']['id'])

	if group_data == group_chat_id:

		print("Working>>>>")

		if 'left_chat_member' in data['message']:
			print(data['message']['left_chat_member']['first_name'])
			Left_member_name = data['message']['left_chat_member']['first_name']
			r = requests.post(BASE_URL+ "sendMessage", data={'chat_id': group_chat_id, 'text': Left_member_name + " Left Codex" })

		if 'new_chat_member' in data['message']:
			print(data['message']['new_chat_member']['first_name'])
			New_member_name = data['message']['new_chat_member']['first_name']
			r = requests.post(BASE_URL+ "sendMessage", data={'chat_id': group_chat_id, 'text': "Welcome to Codex " + New_member_name})
			r = requests.post(BASE_URL + "sendMessage", data={'chat_id': group_chat_id, 'text': "To the new people joining:\n\nThere's a desktop and web client for Telegram so that you can stay updated everywhere. \n\nWe keep track of all members:\n\nhttp://codex.subhrajitpy.me\n\nAdd your names:\nhttps://github.com/SubhrajitPrusty/codex-github/issues/17\n\nSome channels and groups that you can utilise on telegram.\n\n@linux_group\n@thedevs\n@pythongroup\n@python\n@science\n@theprogrammingartgroup\n@TechGuide\n@fullstackbroadcast\n@linuxgram\n@techbinder\n@javaebooks\n@theprogrammingart\n@letstalkprogramming\n\nSome useful bots:\n@rextester_bot\n@gif\n@stickers\n@wiki\n@imdb\n\nBe respectful. Dont spam. Read the group rules.\n\nIn the @codexinit group \n\n* check someone's submission - ask them if they can make improvements \n\n* ask them what they're familiar with or working on\n\n* give them a suitable minor - but something that they have to learn in a short time period\nor if they seem weak with structuring code, then something that requires a good structure (a game would be one example)\n\nYou don't have to be an admin to review submissions."})
		
		if 'text' in data['message'] and (data['message']['text'] == '/xkcd') or (data['message']['text'] == '/xkcd@Alfredcodex_bot'):
			random = randint(1, 2100)
			i = requests.get("https://xkcd.com/"+str(random)+"/info.0.json")
			if i.status_code == 200:
				image = i.json()
				url = image.get("img")
				text = image.get("alt")
				r = requests.post(BASE_URL + "sendPhoto", data={'chat_id': group_chat_id, 'photo': url, 'caption': text })
		
		if 'text' in data['message'] and (data['message']['text'] =='/helpme') or (data['message']['text'] == '/helpme@Alfredcodex_bot'):
			r = requests.post(BASE_URL + "sendMessage", data={'chat_id': group_chat_id, 'text': "Hello I'm Alfred the official butler of Codex, here are somethings I can do:\n\n/helpme for Alfred's commands\n/xkcd for a bit of everthing\n/rules for Codexs' rules"})

		if 'text' in data['message'] and (data['message']['text'] == '/rules') or (data['message']['text'] == '/rules@Alfredcodex_bot'):
			r = requests.post(BASE_URL + "sendMessage", data={'chat_id': group_chat_id, 'text': "There's a desktop and web client for Telegram so that you can stay updated everywhere. \n\nWe keep track of all members:\n\nhttp://codex.subhrajitpy.me\n\nAdd your names:\nhttps://github.com/SubhrajitPrusty/codex-github/issues/17\n\nSome channels and groups that you can utilise on telegram.\n\n@linux_group\n@thedevs\n@pythongroup\n@python\n@science\n@theprogrammingartgroup\n@TechGuide\n@fullstackbroadcast\n@linuxgram\n@techbinder\n@javaebooks\n@theprogrammingart\n@letstalkprogramming\n\nSome useful bots:\n@rextester_bot\n@gif\n@stickers\n@wiki\n@imdb\n\nBe respectful. Dont spam. Read the group rules.\n\nIn the @codexinit group \n\n* check someone's submission - ask them if they can make improvements \n\n* ask them what they're familiar with or working on\n\n* give them a suitable minor - but something that they have to learn in a short time period\nor if they seem weak with structuring code, then something that requires a good structure (a game would be one example)\n\nYou don't have to be an admin to review submissions."})
	
	return "200, OK"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	http_server = WSGIServer(('', port),app)
	http_server.serve_forever() 
