from app import make_app
from errors import HttpError, error_handler
from my_views import UserView, AdvertisementView


app = make_app()

app.add_url_rule(
    rule='/users/<int:user_id>',
    view_func=UserView.as_view('current_user'),
    methods=['GET', 'PATCH', 'DELETE']
)


app.add_url_rule(  # прописывает роуты для метода
    rule='/users/',
    view_func=UserView.as_view('new_user'),
    methods=['POST']
)


app.add_url_rule(
    rule='/adv/<int:advertisement_id>',
    view_func=AdvertisementView.as_view('current_advertisement'),
    methods=['GET', 'PATCH', 'DELETE']
)


app.add_url_rule(  # прописывает роуты для метода
    '/adv/',
    view_func=AdvertisementView.as_view('new_advertisement'),
    methods=['POST']
)
app.errorhandler(HttpError)(error_handler)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
