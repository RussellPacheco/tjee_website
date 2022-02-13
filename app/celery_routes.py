from app import celery
from app.meetup_scraper import Meetup
import os, services, dao
from datetime import datetime
from app.models import db, NewMembers


@celery.task()
def update_new_members():
    print("inside new members")
    new_member_obj = NewMembers
    meetup = Meetup()
    meetup.login(email=os.getenv("MEETUP_EMAIL"), password=os.getenv("MEETUP_PASSWORD"))
    print("logged in")
    meetup_pending_members = meetup.get_pending_members()
    print("got pending members from meetup scraper")
    dao_pending_members = services.service_get_new_member_applications(new_member_obj)
    print("got service get new member applications")
    members_to_save = []

    if dao_pending_members["pending_members"] is None or len(dao_pending_members["pending_members"]) != 0:
        for meetup_member in meetup_pending_members:
            exists = False
            for dao_member in dao_pending_members["pending_members"]:
                if meetup_member["meetup_id"] == dao_member["meetup_id"]:
                    exists = True

            if not exists:
                meetup_member = meetup.get_pending_member_detail(meetup_member)
                members_to_save.append(meetup_member)

        for member in members_to_save:
            dao.dao_save_new_member(db, new_member_obj,
                                    meetup_id=member["meetup_id"],
                                    meetup_name=member["meetup_name"],
                                    created_at=member["created_at"],
                                    app_date=member["app_date"],
                                    link=member["link"],
                                    answer_one=member["answer_one"],
                                    answer_two=member["answer_two"],
                                    answer_three=member["answer_three"])
    else:
        for member in meetup_pending_members:
            member = meetup.get_pending_member_detail(member)

            dao.dao_save_new_member(db, new_member_obj,
                                    meetup_id=member["meetup_id"],
                                    meetup_name=member["meetup_name"],
                                    created_at=datetime.now(),
                                    app_date=member["app_date"],
                                    link=member["link"],
                                    answer_one=member["answers"]["answer_one"],
                                    answer_two=member["answers"]["answer_two"],
                                    answer_three=member["answers"]["answer_three"])

    meetup.quit()
    new_member_apps = services.service_get_new_member_applications(new_member_obj)
    return new_member_apps
