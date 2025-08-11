import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Status

User = get_user_model()

@pytest.mark.django_db
class TestStatusCRUD:
    @pytest.fixture
    def logged_client(self, client):
        user = User.objects.create_user(username='user1', password='testpass123')
        client.login(username='user1', password='testpass123')
        return client

    def test_create_status(self, logged_client):
        url = reverse('status_create')
        response = logged_client.post(url, {'name': 'Новый'})
        assert response.status_code == 302
        assert Status.objects.filter(name='Новый').exists()

    def test_update_status(self, logged_client):
        status = Status.objects.create(name='Старый')
        url = reverse('status_update', args=[status.pk])
        logged_client.post(url, {'name': 'Обновленный'})
        status.refresh_from_db()
        assert status.name == 'Обновленный'

    def test_delete_status(self, logged_client):
        status = Status.objects.create(name='Удалить')
        url = reverse('status_delete', args=[status.pk])
        logged_client.post(url)
        assert not Status.objects.filter(pk=status.pk).exists()

    def test_status_list_requires_login(self, client):
        url = reverse('statuses_index')
        response = client.get(url)
        assert response.status_code == 302