import argparse
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from pathlib import Path

'''Web-Scraper basilare implementato con BeautifulSoup per tracciare i risultati
dei sondaggi di StrawPoll.me'''

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="url for your new StrawPoll tracking")
parser.add_argument("--name", dest='name', help="Name of the csv file where to store results (will be created if not exists)" )

args = parser.parse_args()


client = uReq(args.url)
page_html = client.read()
client.close()
page_soup = BeautifulSoup(page_html, "html.parser")


if args.name is not None:
	fname = args.name + '.csv'
else:
	fname = "poll.csv"

fname_path = "./" + fname
Path(fname).touch(mode=0o777, exist_ok=True)
fp = open(fname, 'w')

headers = "Answer, Votes\n"

fp.write(headers)




poll_ans_list = page_soup.findAll("div", {"class":"sp-option"})
total_votes = page_soup.find("p", {"class":"total-votes"})

total_votes_text = "Total Votes:\t" + total_votes.text
print(total_votes_text)
print('\n')

for poll_ans in poll_ans_list:

	ans_name = poll_ans.p.span.text.strip()

	data_count = poll_ans.find("span", {"class":"option-count"})
	data_text = data_count.text

	percentage = poll_ans.find("span", {"class":"option-percent"})
	percentage_text = percentage.text + '%'

	print("Genre: " + ans_name)
	print("Votes: " + data_text)

	# PROBLEMI NELL'OTTENERE LA PERCENTUALE
	#print("Percentage: " + percentage_text)
	print('\n')

	fp.write(ans_name.replace(',', '|') + ',' + data_text.replace(',', '|') + '' + '\n')

# fp.write('\n' + total_votes_text + '\n')
fp.close()

