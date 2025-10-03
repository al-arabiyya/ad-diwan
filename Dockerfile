# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Create new Django project and configure the settings
RUN python -m django startproject core
RUN cp -r ./ad_diwan ./core

# Settings
RUN echo "'ad_diwan'," >> core/settings.py
RUN echo "'ad_diwan.apps.home'," >> core/settings.py
RUN echo "'ad_diwan.cms'," >> core/settings.py
RUN echo "'ad_diwan.ui'," >> core/settings.py
RUN echo "'rest_wind'," >> core/settings.py
RUN echo "'rest_framework'," >> core/settings.py
RUN echo "'wagtail.contrib.forms'," >> core/settings.py
RUN echo "'wagtail.contrib.redirects'," >> core/settings.py
RUN echo "'wagtail.embeds'," >> core/settings.py
RUN echo "'wagtail.sites'," >> core/settings.py
RUN echo "'wagtail.users'," >> core/settings.py
RUN echo "'wagtail.snippets'," >> core/settings.py
RUN echo "'wagtail.documents'," >> core/settings.py
RUN echo "'wagtail.images'," >> core/settings.py
RUN echo "'wagtail.search'," >> core/settings.py
RUN echo "'wagtail.admin'," >> core/settings.py
RUN echo "'wagtail'," >> core/settings.py
RUN echo "'modelcluster'," >> core/settings.py
RUN echo "'taggit'," >> core/settings.py
RUN echo "]" >> core/settings.py

# URLConf
RUN echo "from django.urls import include" >> core/urls.py
RUN echo "urlpatterns += [path('', include('ad_diwan.ui.urls')), path('api/', include('ad_diwan.api.urls')),]" >> core/urls.py

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
