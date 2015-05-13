##Installation and Setup
Install MovieMan through pip:
```bash
pip install git+https://github.com/simon-andrews/movieman2
```
Edit to your `INSTALLED_APPS` setting in settings.py like this:
```python
INSTALLED_APPS = (
    ...
    'django.contrib.humanize',
    'movieman2',
)
```
Edit your root URLconf to include MovieMan:
```python
urlpatterns = [
    ...
    url(r'^movieman/', include('movieman2.urls')),
]
```