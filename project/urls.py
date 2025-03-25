# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import include, path  # or re_path if you need regex support
from django.contrib import admin

import helloworld.views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', helloworld.views.index),
    path(r'health/', helloworld.views.healthcheck),
]
