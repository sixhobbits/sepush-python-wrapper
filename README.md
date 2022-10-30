# SePush Python Wrapper

A very basic and dumb wrapper to the [SePush API](https://eskomsepush.gumroad.com/l/api) for tracking loadshedding schedules in South Africa.

## Usage

Set the ESP_TOKEN environment variable, e.g. 

```
export ESP_TOKEN=E8118DB2-FC475A06-BBF711B4-18852A4F
```

then import `sepush` and use the Python wrappers for any of the API endpoints. 


e.g. to get your remaining quota/API allowance:

```
import sepush
free_calls = sepush.get_api_allowance()
print(free_calls)
# >> {'allowance': {'count': 10, 'limit': 50, 'type': 'daily'}}
```

to get the current loadshedding status

```
import sepush
status = sepush.get_status()
print(status)
# >> {'status': {'capetown': {'name': 'Cape Town', 'next_stages': [{'stage': '2', 'stage_start_timestamp': '2022-10-31T16:00:00+02:00'}, {'stage': '3', 'stage_start_timestamp': '2022-10-31T22:00:00+02:00'}], 'stage': '0', 'stage_updated': '2022-10-29T00:00:06.153175+02:00'}, 'eskom': {'name': 'Eskom', 'next_stages': [{'stage': '2', 'stage_start_timestamp': '2022-10-31T05:00:00+02:00'}, {'stage': '3', 'stage_start_timestamp': '2022-10-31T16:00:00+02:00'}], 'stage': '0', 'stage_updated': '2022-10-29T00:00:06.153175+02:00'}}}
```
