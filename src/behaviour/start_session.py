import response_helper

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Skydiving weather. " \
                    "Please say get skydiving weather." 
                    #"or ask for get skydiving weather at a location"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please ask for the skydiving weather."
    should_end_session = False
    return response_helper.build_response(session_attributes, response_helper.build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
