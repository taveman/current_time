from web.views import CurrentTime


def add_routes(app):
    """
    adding routes to API instance
    :param app:
    :type app: API
    :return:
    """
    current_time = CurrentTime()

    app.add_route('/api/time', current_time)

    return app
