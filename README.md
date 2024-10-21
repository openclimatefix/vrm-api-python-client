Python client for interacting with the Victron VRM portal
(<http://vrm.victronenergy.com>)

This repo is being maintained by OCF because [the original](https://github.com/victronenergy/vrm-api-python-client) was not being maintained by Victron.

# Installation

``` bash
$ pip install vrmapi
```

# Examples

``` python
>> from vrmapi.vrm import VRM_API
>> api = VRM_API(username='vrm_username', password='vrm_password')
>> api.get_user_sites(api.user_id)

>>{u'records':
      [{u'accessLevel': 1,
      u'device_icon': u'solar',
      u'geofence': None,
      u'geofenceEnabled': False,
      u'idSite': 4470,
      u'idUser': 5155,
      u'identifier': u'6cecebc2d7de',
      u'name': u'Mukuyu HC',
      u'owner': True,
      u'pvMax': 1458,
      u'reports_enabled': True,
      u'timezone': u'Africa/Kigali'}],
  u'success': True}


>> api.get_consumption_stats(inst_id=4470) 

>>{u'records': {u'Bc': [[1473681210000, 0.018203735351562],
   [1473692010000, 0.018211364746094],
   [1473695610000, 0.036407470703125],
   [1473699210000, 0.054611206054688],
   [1473702810000, 0.054611206054688],
   [1473706410000, 0.054611206054688],
   [1473710010000, 0.054618835449219],
   [1473713610000, 0.054611206054688],
   [1473717210000, 0.036415100097656],
   [1473720810000, 0.054603576660156],
   [1473724410000, 0.054618835449219],
   [1473728010000, 0.054611206054688],
   [1473731610000, 0.054618835449219],
   [1473735210000, 0.018203735351562],
   [1473738810000, 0.018203735351562]],
  u'Gc': False,
  u'Pc': [[1473681210000, 0.018218994140625],
   [1473684810000, 0.018203735351562],
   [1473688410000, 0.036376953125],
   [1473692010000, 0.018218994140625],
   [1473742410000, 0.054641723632812],
   [1473746010000, 0.0181884765625]],
  u'gc': False},
 u'success': True,
 u'totals': {u'Bc': 0.63716125488281,
  u'Gc': False,
  u'Pc': 0.16384887695312,
  u'gc': False}}
```
