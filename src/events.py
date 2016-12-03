'''
This generally contains functions that route incoming messages from lambda_function to the correct handlers, and build responses
'''
from __future__ import print_function
import behaviour.get_weather
import behaviour.start_session
import behaviour.end_session

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return behaviour.start_session.get_welcome_response()
    

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetSkydivingWeather":
        return behaviour.get_weather.get_skydiving_weather(intent, session)
    #elif intent_name == "GetSkydivingWeatherAt":
    #    return get_skydiving_weather_at(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return behaviour.start_session.get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return behaviour.end_session.handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here