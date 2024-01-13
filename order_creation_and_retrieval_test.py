#Розалия Жарасова, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# Автотест по шагам
def test_order_creation_and_retrieval():
    track = {"t":sender_stand_request.get_order('track')}
    order_response = sender_stand_request.get_order(track)

    assert order_response.status_code == 200