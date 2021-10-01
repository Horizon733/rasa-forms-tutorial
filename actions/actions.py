# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Tuple
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
#
#
from database_utils.constants import EMAIL, REQUESTED_SLOT,OTP
from database_utils.database_utils import is_valid_user, is_valid_otp


class AuthenticatedAction(Action):
    def name(self) -> Text:
        return "action_authenticated"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
            email = tracker.get_slot("email")
            otp = tracker.get_slot("otp")
            if email is not None and otp is not None:
                dispatcher.utter_message(template="utter_authenticated_successfully")
            else:
                dispatcher.utter_message(text="utter_authentication_failure")
            return []


class ValidateAuthFormAction(FormValidationAction):
    def name(self) -> Text:
        return "validate_auth_form"

    def validate_email(
        self,
        value: Text,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[EventType]:
        returned_slots = {}
        if value is not None and is_valid_user(value):
            returned_slots = {EMAIL:value}
        else:
            returned_slots = {REQUESTED_SLOT: EMAIL}
            if value is None:
                dispatcher.utter_message(template="utter_email_not_valid")
            elif not is_valid_user(value):
                dispatcher.utter_message(template="utter_email_not_registered")
        return returned_slots

    def validate_otp(
        self,
        value: float,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[EventType]:
        email = tracker.get_slot(EMAIL)
        returned_slots = {}
        if value is not None and is_valid_otp(value,email):
            returned_slots = {OTP:value}
        else:
            returned_slots ={REQUESTED_SLOT:OTP}
            dispatcher.utter_message(template="utter_otp_not_valid")
        return returned_slots
