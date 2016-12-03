'''
Function to handle retrieving the skydiving weather
'''

import response_helper

def get_skydiving_weather(intent, session):
    session_attributes = {}
    reprompt_text = None
    
    speech_output = "It's sunny blue skies! go jump!"
    should_end_session = True
   

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return response_helper.build_response(session_attributes, response_helper.build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))