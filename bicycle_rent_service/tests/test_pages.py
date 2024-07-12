import pytest


class TestTemplateView:

    @pytest.mark.django_db(transaction=True)
    def test_swagger(self, client):
        urls = ['/swagger/']
        for url in urls:
            try:
                response = client.get(url)
            except Exception as e:
                assert False, f'''Страница `{url}` работает неправильно. Ошибка: `{e}`'''
            assert response.status_code != 404, f'Страница `{url}` не найдена, проверьте этот адрес в *urls.py*'
            assert response.status_code == 200, (
                f'Ошибка {response.status_code} при открытиии `{url}`. Проверьте ее view-функцию'
            )

    @pytest.mark.django_db(transaction=True)
    def test_bicycles(self, client):
        urls = ['/api/v1/bicycles/']
        for url in urls:
            try:
                response = client.get(url)
            except Exception as e:
                assert False, f'''Страница `{url}` работает неправильно. Ошибка: `{e}`'''
            assert response.status_code != 404, f'Страница `{url}` не найдена, проверьте этот адрес в *urls.py*'
            assert response.status_code == 401, (
                f'Ошибка {response.status_code} при открытиии `{url}`. Проверьте разрещения'
            )
