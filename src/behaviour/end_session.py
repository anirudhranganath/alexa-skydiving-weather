import response_helper

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thanks! Blue Skies! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return response_helper.build_response({}, response_helper.build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        