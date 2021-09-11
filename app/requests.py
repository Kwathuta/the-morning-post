import urllib.request, json
from .models import Sources

# Getting api key
api_key = None

# Getting sources base url
sources_base_url = None


def configure_request(app):
    global api_key, sources_base_url
    api_key = app.config["SOURCES_API_KEY"]
    sources_base_url = app.config["SOURCES_API_BASE_URL"]


def get_sources():
    """
    function to get json response from api
    """
    get_sources_url = sources_base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response["sources"]:
            sources_results_list = get_sources_response["sources"]
            sources_results = process_results(sources_results_list)
    return sources_results


def process_results(sources_list):
    """
    Function to process the sources result and turn them to a list of object
    Args:
        sources_list: A list of dictionaries to contain sources details
    Returns:
        sources_results: A list of sources objects
    """
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get("id")
        name = sources_item.get("name")
        description = sources_item.get("description")
        url = sources_item.get("url")

        sources_object = Sources(id, name, description, url)

        sources_results.append(sources_object)

    return sources_results
