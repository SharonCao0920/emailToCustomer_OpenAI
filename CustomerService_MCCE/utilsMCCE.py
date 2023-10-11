import openai

def test_Moderation(comment):
    response = openai.Moderation.create(comment)
    moderation_output = response["results"][0]
    if moderation_output["flagged"] != False:
        return "The response is not appropriate!"
    else:
        return "The response is appropriate!"
    