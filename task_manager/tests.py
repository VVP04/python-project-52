import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200

    templates = [t.name for t in response.templates if t.name]
    assert "index.html" in templates
