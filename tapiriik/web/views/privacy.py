from django.shortcuts import render
from tapiriik.services import Service
from tapiriik.settings import WITHDRAWN_SERVICES
def privacy(request):

	OPTIN = "<span class=\"optin policy\">Opt-in</span>"
	NO = "<span class=\"no policy\">No</span>"
	YES = "<span class=\"yes policy\">Yes</span>"
	CACHED = "<span class=\"cached policy\">Cached</span>"
	SEEBELOW = "See below"

	services = dict([[x.ID, {"DisplayName": x.DisplayName, "ID": x.ID}] for x in Service.List() if x.ID not in WITHDRAWN_SERVICES])

	services["garminconnect"].update({"email": OPTIN, "password": OPTIN, "tokens": NO, "metadata": YES, "data":NO})
	services["strava"].update({"email": NO, "password": NO, "tokens": YES, "metadata": YES, "data":NO})
	services["sporttracks"].update({"email": OPTIN, "password": OPTIN, "tokens": NO, "metadata": YES, "data":NO})
	services["dropbox"].update({"email": NO, "password": NO, "tokens": YES, "metadata": YES, "data":CACHED})
	services["runkeeper"].update({"email": NO, "password": NO, "tokens": YES, "metadata": YES, "data":NO})
	services["rwgps"].update({"email": OPTIN, "password": OPTIN, "tokens": NO, "metadata": YES, "data":NO})
	services["trainingpeaks"].update({"email": OPTIN, "password": OPTIN, "tokens": NO, "metadata": YES, "data":NO})

	services_list = [x for key, x in services.items()]
	return render(request, "privacy.html", {"services": services_list})