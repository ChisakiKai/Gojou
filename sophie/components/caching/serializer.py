# Copyright (C) 2018 - 2020 MrYacha.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This file is part of Sophie.

from sophie.utils.config import config

conf = config.cache.serializer.lower()
if conf == 'pickle':
    from aiocache.serializers import PickleSerializer

    serializer = PickleSerializer
elif conf == 'json':
    from aiocache.serializers import JsonSerializer

    serializer = JsonSerializer
else:
    raise NotImplementedError
