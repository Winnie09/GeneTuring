import json
import openai
import os
import re
import sys
import time
import urllib.request
import logging

def call_api(url):
	time.sleep(1)
	url = url.replace(' ', '+')
	print(url)

	req = urllib.request.Request(url) 
	with urllib.request.urlopen(req) as response:
		call = response.read()

	return call

def get_prompt_header(mask):
	'''
	mask: [1/0 x 6], denotes whether each prompt component is used

	output: prompt
	'''
	url_1 = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gene&retmax=5&retmode=json&sort=relevance&term=LMP10'
	call_1 = call_api(url_1)

	url_2 = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&retmax=5&retmode=json&id=19171,5699,8138'
	call_2 = call_api(url_2)

	url_3 = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=snp&retmax=10&retmode=json&id=1217074595' 
	call_3 = call_api(url_3)

	url_4 = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=omim&retmax=20&retmode=json&sort=relevance&term=Meesmann+corneal+dystrophy'
	call_4 = call_api(url_4)

	url_5 = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=omim&retmax=20&retmode=json&id=618767,601687,300778,148043,122100'
	call_5 = call_api(url_5)

	url_6 = 'https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=Put&PROGRAM=blastn&MEGABLAST=on&DATABASE=nt&FORMAT_TYPE=XML&QUERY=ATTCTGCCTTTAGTAATTTGATGACAGAGACTTCTTGGGAACCACAGCCAGGGAGCCACCCTTTACTCCACCAACAGGTGGCTTATATCCAATCTGAGAAAGAAAGAAAAAAAAAAAAGTATTTCTCT&HITLIST_SIZE=5'
	call_6 = call_api(url_6)
	rid = re.search('RID = (.*)\n', call_6.decode('utf-8')).group(1)

	url_7 = f'https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=Get&FORMAT_TYPE=Text&RID={rid}'
	time.sleep(30)
	call_7 = call_api(url_7)

	prompt = ''
	prompt += 'Hello. Your task is to use NCBI Web APIs to answer genomic questions.\n'
	#prompt += 'There are two types of Web APIs you can use: Eutils and BLAST.\n\n'

	if mask[0]:
		# Doc 0 is about Eutils
		prompt += 'You can call Eutils by: "[https://eutils.ncbi.nlm.nih.gov/entrez/eutils/{esearch|efetch|esummary}.fcgi?db={gene|snp|omim}&retmax={}&{term|id}={term|id}]".\n'
		prompt += 'esearch: input is a search term and output is database id(s).\n'
		prompt += 'efectch/esummary: input is database id(s) and output is full records or summaries that contain name, chromosome location, and other information.\n'
		prompt += 'Normally, you need to first call esearch to get the database id(s) of the search term, and then call efectch/esummary to get the information with the database id(s).\n'
		prompt += 'Database: gene is for genes, snp is for SNPs, and omim is for genetic diseases.\n\n'

	if mask[1]:
		# Doc 1 is about BLAST
		prompt += 'For DNA sequences, you can use BLAST by: "[https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD={Put|Get}&PROGRAM=blastn&MEGABLAST=on&DATABASE=nt&FORMAT_TYPE={XML|Text}&QUERY={sequence}&HITLIST_SIZE={max_hit_size}]".\n'
		prompt += 'BLAST maps a specific DNA {sequence} to its chromosome location among different specices.\n'
		prompt += 'You need to first PUT the BLAST request and then GET the results using the RID returned by PUT.\n\n'

	if any(mask[2:]):
		prompt += 'Here are some examples:\n\n'

	if mask[2]:
		# Example 1 is from gene alias task 
		prompt += f'Question: What is the official gene symbol of LMP10?\n'
		prompt += f'[{url_1}]->[{call_1}]\n' 
		prompt += f'[{url_2}]->[{call_2}]\n'
		prompt += f'Answer: PSMB10\n\n'

	if mask[3]:
		# Example 2 is from SNP gene task
		prompt += f'Question: Which gene is SNP rs1217074595 associated with?\n'
		prompt += f'[{url_3}]->[{call_3}]\n'
		prompt += f'Answer: LINC01270\n\n'

	if mask[4]:
		# Example 3 is from gene disease association
		prompt += f'Question: What are genes related to Meesmann corneal dystrophy?\n'
		prompt += f'[{url_4}]->[{call_4}]\n'
		prompt += f'[{url_5}]->[{call_5}]\n'
		prompt += f'Answer: KRT12, KRT3\n\n'

	if mask[5]:
		# Example 4 is for BLAST
		prompt += f'Question: Align the DNA sequence to the human genome:ATTCTGCCTTTAGTAATTTGATGACAGAGACTTCTTGGGAACCACAGCCAGGGAGCCACCCTTTACTCCACCAACAGGTGGCTTATATCCAATCTGAGAAAGAAAGAAAAAAAAAAAAGTATTTCTCT\n'
		prompt += f'[{url_6}]->[{rid}]\n'
		prompt += f'[{url_7}]->[{call_7}]\n'
		prompt += f'Answer: chr15:91950805-91950932\n\n'

	return prompt

def safe_api_call(url, max_retries=3):
    """Safely call external APIs with retry logic"""
    for attempt in range(max_retries):
        try:
            # Add delay for NCBI API calls
            if 'ncbi.nlm.nih.gov' in url:
                time.sleep(2)
            
            call = call_api(url)  # Your existing call_api function
            return call
            
        except Exception as e:
            # logger.warning(f"API call failed on attempt {attempt + 1}: {e}")
            if attempt == max_retries - 1:
                return f"API_ERROR: {str(e)}"
            time.sleep(5 * (attempt + 1))  # Increasing delay
            
def openai_request(q_prompt, logger, client, max_retries=3, base_timeout=60):
    """Make OpenAI API request with exponential backoff retry logic"""

    for attempt in range(max_retries):
        try:
            logger.info(f"Attempt {attempt + 1}/{max_retries}")
            
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",  # "gpt-4.1-nano"
                messages=[
                    {"role": "user", "content": q_prompt},
                ],
                temperature=0.0,
                stop=["->", "\n\nQuestion"],
                timeout=base_timeout * (2 ** attempt)  # Use timeout parameter correctly
            )
            
            return completion.choices[0].message.content  # Fixed: .content not ["content"]
            
        except openai.APITimeoutError as e:  # Updated exception handling
            logger.warning(f"Timeout on attempt {attempt + 1}: {e}")
            if attempt == max_retries - 1:
                return 'timeoutError'
            time.sleep(2 ** attempt)  # Exponential backoff
            
        except openai.RateLimitError as e:  # Updated exception handling
            logger.warning(f"Rate limit hit on attempt {attempt + 1}: {e}")
            if attempt == max_retries - 1:
                return 'rateLimitError'
            time.sleep(60)  # Wait longer for rate limits
            
        except openai.BadRequestError as e:  # Updated exception handling
            logger.error(f"Invalid request: {e}")
            return 'lengthError'
            
        except Exception as e:
            logger.error(f"Unexpected error on attempt {attempt + 1}: {e}")
            if attempt == max_retries - 1:
                return f'unexpectedError: {str(e)}'
            time.sleep(2 ** attempt)