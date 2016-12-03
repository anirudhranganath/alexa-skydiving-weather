'''
This is the entry point of the code.
'''

import events

# --------------- Main handler ------------------

def lambda_function(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    #if (event['session']['application']['applicationId'] != ""):
    #    raise ValueError("Invalid Application ID")
    
    if event['request']['type'] == "LaunchRequest":
        return events.on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return events.on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return events.on_session_ended(event['request'], event['session'])
        
        