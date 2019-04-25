import requests
from riotwatcher import RiotWatcher
from classes import userwatcher


wat = RiotWatcher("RGAPI-7755cba1-3ad5-4ae1-9409-7815c284a46c")
sumoner = userwatcher.json_to_summoner(wat.summoner.by_name("br1","Jukes"))
print(userwatcher.SummonertoString(sumoner))

