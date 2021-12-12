TJEE Website
====
Custom-built website for the TJEE English conversation group

Table of Contents
------------------
- [API](#api)
------------------
##API
Status code explanations

|Method|Endpoint|Status -1|Status 0|Status 1|
|:---:|:---|:---:|:---:|:---:|
|POST|/api/members/create/|*|Creation Success|Member Exists|
|GET|/api/members/<member_id>/|*|Query Success|Member Doesn't Exist|
|GET|/api/members/|*|Query Success|No Members Exist|
|POST|/api/admins/login/|Bad Password|Login Success|Admin Doesn't Exist|
|POST|/api/admins/create/|*|Creation Success|Admin Exists|
|DELETE|/api/admins/delete/|Bad Password|Delete Success|Admin Doesn't Exist|
|POST|/api/admins/password/|Bad Password|Password Changed|Admin Doesn't Exist|
|POST|/api/line/messages/create/|*|Creation Successful|*|
|GET|/api/line/messages/|*|Query Success|No Messages Exist|
|GET|/api/line/messages/message/<message_id>/|*|Query Success|Message Doesn't Exist|
|POST|/api/line/messages/message/<message_id>/|*|Message Updated|Message Doesn't Exist|
|DELETE|/api/line/messages/message/<message_id>/|*|Message Deleted|Message Doesn't Exist|



