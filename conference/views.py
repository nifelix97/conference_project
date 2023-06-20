from django.shortcuts import render
from django.http import HttpResponse
import datetime

        {conferences =[

            "id": 1,
            "name": "ICT CHEMBER",
            "date": "2023-7-12",
            "location": "BK Arena"
        },
        {
            "id": 2,
            "name": "Data Management system",
            "date": "2023-12-12",
            "location": "BK ARENA"
        },
        {
            "id": 3,
            "name": "Impact of ICT on employment",
            "date": "2023-05-30",
            "location": " SELENA Hotel"
        },

        {
            "id": 4,
            "name": "Developing ICT in Africa",
            "date": "2023-12-21",
            "location": "Intare Conference Arena"
        },

        {
            "id": 5,
            "name": "KOICA Summit 2023",
            "date": "2023-11-01",
            "location": "Intare Arena"
        },
 ]
def conferences_view(request):
    return render(request, 'felix.html', context={"conferences": conferences})

def create_conference_view(request):
    return render(request, 'create_conferences.html')

def conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/conference.html", context={"conference": conference })

def update_conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/updateConference.html", context={"conference": conference})

def delete_conference_view(request,id):
    conference = None
    for conf in conferences:
        if conf["id"] == int(id):
            conference = conf
    return render(request, "conference/delete_conference.html", context={"conference" : conference})

def confirm_delete_view(request, id):
    return render(request, "conference/confirm_delete.html")
