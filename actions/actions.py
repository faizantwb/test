# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union

import json
import requests

class ActionGetIssueDetails(Action):

    def name(self) -> Text:
        return "action_get_issue_details"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["issue_type","issue_detail"]


    def submit(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_submit")

class ContactDetailsForm(FormAction):

    def name(self) -> Text:
        return "contact_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["name"]

    def slot_mappings(self) -> Text:
        return {
        "name": self.from_text(intent=None)
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_greet_with_name")
        return[]


class FirstTimeForm(FormAction):

    def name(self) -> Text:
        return "first_time_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        if tracker.get_slot("first_time") == True:
            return["first_time", "given_name", "location"]
        else:
            return["first_time"]

    def slot_mappings(self) -> Dict[str, Union[Dict[str, Any], List[Dict[str, Any]]]]:

        return {
            "first_time": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False)
            ],
            "given_name": [
                self.from_entity(entity="entity_given_name", intent="name_entry"),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="ask_again", value="ask again")
                #self.from_text(intent="name_entry")
            ],
            "location": self.from_text()
        }

    def validate_given_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate value."""
        if value == False:
            dispatcher.utter_message(template="utter_thats_fine")
            return {"given_name": ""}

        elif value =="ask again":
            dispatcher.utter_message(template="utter_your_first_name")
            return {"given_name": None}

        else:
            dispatcher.utter_message(template="utter_we_have_what_we_need")
            return {"given_name": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot("first_time") == False:
            dispatcher.utter_message(template="utter_welcome_back")
        else:
            dispatcher.utter_message(template="utter_greet_with_name")
        return[]


class FeedbackForm(FormAction):

    def name(self) -> Text:
        return "feedback_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if the answer to "Did we do OK?" is no...
        if tracker.get_slot("feedback") == False:
            return["feedback", "feedback_reason"]
        else:
            return["feedback"]

    def slot_mappings(self) -> Text:
        return {
        "feedback": [
            self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)
            ],
        "feedback_reason": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback")
        return[]

class LanguageQuestionsForm(FormAction):

    def name(self) -> Text:
        return "language_questions_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        # if the answer to "Did we do OK?" is no...
        if tracker.get_slot("willing_to_do_language_survey") == True:
            return[
                    "willing_to_do_language_survey",
                    "language_at_home",
                    "language_for_written_comms",
                    "language_for_verbal_comms",
                    "preferred_channel"
                    ]
        else:
            return["willing_to_do_language_survey"]

#        return["willing_to_do_survey","language_at_home","language_for_written_comms","language_for_verbal_comms","preferred_channel"]

    def slot_mappings(self) -> Text:
        return {
        "willing_to_do_language_survey": [
            self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)
        ],
        "language_at_home": self.from_text(),
        "language_for_written_comms": self.from_text(),
        "language_for_verbal_comms": self.from_text(),
        "preferred_channel": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot("willing_to_do_language_survey") == True:
            dispatcher.utter_message(template="utter_thanks_for_your_feedback")
        else:
            dispatcher.utter_message(text="OK, that's fine! How can I help you?")
        return[]


class MythSourceForm(FormAction):

    def name(self) -> Text:
        return "myth_source_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:

        return["myth_source"]

    def slot_mappings(self) -> Text:
        return {
        "myth_source": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_thanks_for_your_feedback")
        return[]


class ActionGetInfectionStats(Action):

    def name(self) -> Text:
        return "action_get_infection_stats"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # this is where to paste the call to API
        country = "DRC"
        url = "https://covid-193.p.rapidapi.com/statistics"
        headers = { 'x-rapidapi-host': "covid-193.p.rapidapi.com", 'x-rapidapi-key': "c41cd0c62dmshb99d2fb0a63207dp1775a0jsna4f33aea1040"}
        query_string = {"country":country}

        # get the response
        response = requests.request("GET", url, headers=headers, params=query_string)
        response_JSON = response.json()

        #get the bits of the response we want
        active = response_JSON['response'][0]['cases']['active']
        new = response_JSON['response'][0]['cases']['new']

        dispatcher.utter_message(template="utter_infection_stats", active = active, new = new, country = country)
#        dispatcher.utter_message(text=f'There are {active} people infected in {country}, a change of {new} on yesterday.')

        return []

class ActionGetPandemicVideo(Action):

    def name(self) -> Text:
        return "action_link_to_pandemic_video"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = "DRC"

        # dispatcher.utter_message(attachment={
        #     "type": "video",
        #     "payload": {
        #         "title": "Watch Below Video",
        #         "src": "https://www.youtube.com/watch?v=nMelwUuGqpA"
        #     }
        # })

        return []
