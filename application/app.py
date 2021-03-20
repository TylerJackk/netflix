from chalice import Chalice

from chalicelib.scraper.constants import TV, MOVIE
from chalicelib.scraper.scraper import UnogsExplorer
from chalicelib.db_manager.constants import NF_ID_QUEUE

app = Chalice(app_name='application')
app.debug = True


# @app.on_sqs_message(queue=NF_ID_QUEUE, batch_size=1)
# def scrape_nf_detail(event):
#     for record in event:
#         app.log.debug("Received message with contents: %s", record.body)


@app.route('/explore', methods=['GET'])
def explore_all_nf_data():
    for resource_type in [TV, MOVIE]:
        u = UnogsExplorer(resource_type)
        u.explore()

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
